from ipwhois import IPWhois
import os
import urllib.parse
import requests
import sys

from subprocess import Popen, PIPE

from flask import Flask, render_template, request
app = Flask(__name__)

# if using text as tracert input

# f1 = open('google_com.txt', 'r+')
# text  = f1.readlines()

# print(text)
larr = []

@app.route('/input')
def display():

    # text  =  run_tracert('facebook.com')

    # ip_add_dict = enum_whois(get_ip(text))

    # latlong =  get_lat_long(ip_add_dict)
    # larr = []
    # for i in latlong:
    #     larr.append(i['lat'])
    #     larr.append(i['lon'])

    return render_template('sample_geojson.html', value=larr)

@app.route('/trace', methods=['POST'])
def traceDisplay():
    data = request.get_data().decode("utf-8")
    
    print(data)
    text  =  run_tracert(data.split("=")[1])

    ip_add_dict = enum_whois(get_ip(text))

    latlong =  get_lat_long(ip_add_dict)

    larr = []
    for i in latlong:
        larr.append(i['lat'])
        larr.append(i['lon'])
        larr.append(i['add'])
    
    print(larr)

    return {'data': larr}
    # return render_template('sample_geojson.html', value=larr)


def run_tracert(host):
    p = Popen(['traceroute', host], stdout=PIPE)
    
    #lines = p.stdout.readlines()
    lines = []
    while True:
        line = p.stdout.readline().decode("utf-8")
        if not line:
            break
        lines.append(str(line))
    
    f1 = open("tracert_result.txt", "w+")
    f1.write("\n".join(lines))
    f1.close()
    return lines

def get_ip(text):
    ip_addresses = []
    text = text[1:-1]
    for i, element in enumerate(text):
        i = str(i)
        if (i == 0):
            pass
        elif (element.split()[1] != '*'):
            ip_addresses.append(element.split()[2].strip("()"))
    return ip_addresses

def enum_whois(ips):
    # I assume we are in india
    #p_addresses = {'0.0.0.0':'IN'}
    p_addresses = {}
    for ip in ips:
        # print('for: ', ip)
        if (ip == "10.10.10.141"):
            print("vpn detected")
            p_addresses["10.10.10.141"] = ["PK", 'vpn']
        elif(ip == "10.10.10.1"):
            p_addresses["10.10.10.1"] = ["IN", 'internal']
        else:
            try:
                obj = IPWhois(ip)
                # object_methods = [method_name for method_name in dir(obj)
                #       if callable(getattr(obj, method_name))]
                # print(object_methods)


                # res = obj.lookup_whois()
                # print(res['asn_country_code'])

                res = obj.lookup_rdap()

                # print(res['asn_country_code'])
                p_addresses[ip] = [res['asn_country_code']]

                # for complete address
                for i in res['objects']:
                    # print(i)
                    # print('*')
                    # print(res['objects'][i])
                    try:
                        # print(res['objects'])
                        if(res['objects'][i]['contact']['address'][0]):
                            # print(res['objects'][i]['contact']['address'][0]['value'])
                            # print('\n')
                            p_addresses[ip].append(str(res['objects'][i]['contact']['address'][0]['value']).replace('\n', ' '))
                        
                    except Exception as e:
                        pass
                    
            except Exception as e:
                print(e)
    print(p_addresses)
    return p_addresses

def get_lat_long(ip_add_dict):

    
    # print(ip_add_dict)
    unique_adds = []
    unique_str = []
    for i in ip_add_dict:
        print(ip_add_dict[i][0])
        if (ip_add_dict[i][0] not in unique_adds):
            unique_adds.append(ip_add_dict[i][0])
            unique_str.append(ip_add_dict[i][1])

    
    unique_adds = list(dict.fromkeys(unique_adds))
    unique_str = list(dict.fromkeys(unique_str))
    
    # unique_adds = list(unique_adds)
    print("unique_addresses generated: ", unique_adds)

    latlong = []
    for index, i in enumerate(unique_adds):
        ll = {}
        # print("For address: ", i)
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(i) +'?format=json'

        response = requests.get(url).json()
        #print(response)
        ll["lat"] =  response[0]["lat"]
        ll["lon"] = response[0]["lon"]
        ll["add"] = unique_str[index]
        # print(response[0]["lat"])
        # print(response[0]["lon"])
        latlong.append(ll)
    return latlong

if __name__=='__main__':

    # text  =  run_tracert('facebook.com')

    # ip_add_dict = enum_whois(get_ip(text))

    # latlong =  get_lat_long(ip_add_dict)
    # print(latlong)
    
    app.run(host='0.0.0.0', debug=True, port=3134)


