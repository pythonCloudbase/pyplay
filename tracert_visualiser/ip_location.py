from ipwhois import IPWhois
import os
import IP2Location
database = IP2Location.IP2Location("IP-COUNTRY.BIN")

f1 = open('google_com.txt', 'r+')
text  = f1.readlines()

def get_ip(text):
    ip_addresses = []
    for i, element in enumerate(text):
        if (i == 0):
            pass
        elif (element.split()[1] != '*'):
            ip_addresses.append(element.split()[1])
    return ip_addresses

def enum_whois(ips):
    for i in ips:
        print('for: ', i)
        try:
            obj = IPWhois(i)
            # object_methods = [method_name for method_name in dir(obj)
            #       if callable(getattr(obj, method_name))]
            # print(object_methods)


            # res = obj.lookup_whois()
            # print(res['asn_country_code'])

            res = obj.lookup_rdap()

            # for i in res['objects']:
            #     print(i)
            #     # print(res['objects'][i])
            #     for j in res['objects'][i]:
            #         print(j)
            #     print('\n')
                
            
            break
        except Exception as e:
            print(e)

def ip2loc(ip):
    rec = database.get_all(ip)

    print(rec.country_short)
    print(rec.country_long)
    print(rec.region)
    print(rec.city)
    print(rec.isp)  
    print(rec.latitude)
    print(rec.longitude)            
    print(rec.domain)
    print(rec.zipcode)
    print(rec.timezone)
    print(rec.netspeed)
    print(rec.idd_code)
    print(rec.area_code)
    print(rec.weather_code)
    print(rec.weather_name)
    print(rec.mcc)
    print(rec.mnc)
    print(rec.mobile_brand)
    print(rec.elevation)
    print(rec.usage_type)

ip2loc(get_ip(text)[1])