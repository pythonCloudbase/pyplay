from ipwhois import IPWhois
import os
import urllib.parse
import requests
import sys

from flask import Flask, render_template, request
app = Flask(__name__)

f1 = open('google_com.txt', 'r+')
text  = f1.readlines()

@app.route('/input')
def display():
    print(request.args.get('filename'))
    if 'index'== request.args.get('filename'):
        myfilename = request.args.get('filename')
        return render_template('index.html')
    else :
        return "no input file specified"

def get_ip(text):
    ip_addresses = []
    for i, element in enumerate(text):
        if (i == 0):
            pass
        elif (element.split()[1] != '*'):
            ip_addresses.append(element.split()[1])
    return ip_addresses

def enum_whois(ips):
    p_addresses = {}
    for ip in ips:
        # print('for: ', ip)
        try:
            obj = IPWhois(ip)
            # object_methods = [method_name for method_name in dir(obj)
            #       if callable(getattr(obj, method_name))]
            # print(object_methods)


            # res = obj.lookup_whois()
            # print(res['asn_country_code'])

            res = obj.lookup_rdap()

            # print(res['asn_country_code'])
            p_addresses[ip] = res['asn_country_code']


            # for complete address
            # for i in res['objects']:
            #     # print(i)
            #     # print('*')
            #     # print(res['objects'][i])
            #     try:
            #         print(res['objects'])
            #         if(res['objects'][i]['contact']['address'][0]):
            #             # print(res['objects'][i]['contact']['address'][0]['value'])
            #             # print('\n')
            #             p_addresses[ip] = str(res['objects'][i]['contact']['address'][0]['value']).replace('\n', ' ')
                    
            #     except Exception as e:
            #         pass
                
        except Exception as e:
            print(e)
    return p_addresses

def get_lat_long(ip_add_dict):

    # print(ip_add_dict)
    unique_adds = []
    for i in ip_add_dict:
        unique_adds.append(ip_add_dict[i])

    
    unique_adds = list(set(unique_adds))

    
    latlong = []
    for i in unique_adds:
        ll = {}
        # print("For address: ", i)
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(i) +'?format=json'

        response = requests.get(url).json()
        #print(response)
        ll["lat"] =  response[0]["lat"]
        ll["lon"] = response[0]["lon"]
        # print(response[0]["lat"])
        # print(response[0]["lon"])
        latlong.append(ll)
    return latlong

if __name__=='__main__':

    ip_add_dict = enum_whois(get_ip(text))

    latlong =  get_lat_long(ip_add_dict)
    print(latlong)
    
    app.run(host='0.0.0.0', debug=True, port=3134)


