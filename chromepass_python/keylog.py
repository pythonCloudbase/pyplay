import os
import sys
import sqlite3
import csv
import json
import argparse
import win32crypt

# try:
#     import win32crypt
# except Exception as e:
#     print("Cannot run win32crypt.")
#     print(e)


def main():
    info_list = []
    path = getpath()

    try:
        connection = sqlite3.connect(path + "Login Data")

        with connection:

            cursor = connection.cursor()
            v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()

        if (os.name == "posix") and (sys.platform == "darwin"):
            print("Mac OSX not supported.")
            sys.exit(0)
        
        # print("\nThe value fetched: ", value)

        for origin_url, username, password in value:

            print('origin url: ', origin_url)
            print('useraname: ', username)
            print('password: ', password)

            if os.name == 'nt':
                
                try:
                    password = win32crypt.CryptUnprotectData(
                        password, None, None, None, 0)[1]
                except Exception as e:
                    print(e)
            
            if password:
                info_list.append({
                    'origin_url': origin_url,
                    'username': username,
                    'password': str(password)
                })

    except sqlite3.OperationalError as e:

        print("\nEncountered operational error: ", e)
        e = str(e)
        if (e == 'database is locked'):
            print('[!] Make sure Google Chrome is not running in the background')
        elif (e == 'no such table: logins'):
            print('[!] Something wrong with the database name')
        elif (e == 'unable to open database file'):
            print('[!] Something wrong with the database path')
        else:
            print(e)
        sys.exit(0)

    print("\nInfo list: ")

    for i in info_list:
        print(i)
        print()

    return info_list


def getpath():
    print("\nThe operating system detected: ", os.name)

    if os.name == "nt":
        # This is the Windows Path
        PathName = os.getenv('localappdata') + \
            '\\Google\\Chrome\\User Data\\Default\\'
    elif os.name == "posix":
        PathName = os.getenv('HOME')
        if (sys.platform == "darwin"):
            # This is the OS X Path
            PathName += '/Library/Application Support/Google/Chrome/Default/'
        else:
            # This is the Linux Path
            PathName += '/.config/google-chrome/Default/'
   
    if not os.path.isdir(PathName):
        print('[!] Chrome Doesn\'t exists')
        sys.exit(0)
    
    print("\nThe pathname chosen: ", PathName)

    return PathName


def output_csv(info):
    try:
        with open('chromepass-passwords.csv', 'wb') as csv_file:
            csv_file.write('origin_url,username,password \n'.encode('utf-8'))
            for data in info:
                csv_file.write(('%s, %s, %s \n' % (data['origin_url'], data[
                    'username'], data['password'])).encode('utf-8'))
        print("Data written to chromepass-passwords.csv")
    except EnvironmentError:
        print('EnvironmentError: cannot write data')


def output_json(info):
	try:
		with open('chromepass-passwords.json', 'w') as json_file:
			json.dump({'password_items':info},json_file)
			print("Data written to chromepass-passwords.json")
	except EnvironmentError:
		print('EnvironmentError: cannot write data')



if __name__ == '__main__':
    main()