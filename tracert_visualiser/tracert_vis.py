from ipwhois import IPWhois
import os
import urllib.parse
import requests
import sys
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import geopandas
import geoplot
import matplotlib.pyplot as plt
import pandas as pd


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

def geopanda_vis(latlong):
    lats= []
    longs = []

    for i in latlong:
        lats.append(float(i['lat']))
        longs.append(float(i['lon']))
        
    
    geometry = [Point(x, y) for x, y in zip(longs, lats)]
    gdf = GeoDataFrame(df, geometry=geometry)   

    #this is a simple map that goes with geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)
    plt.savefig('w.jpg')

def geopandas_map():
    world = geopandas.read_file(
        geopandas.datasets.get_path('naturalearth_lowres')
    )
    boroughs = geopandas.read_file(
        geoplot.datasets.get_path('nyc_boroughs')
    )
    collisions = geopandas.read_file(
        geoplot.datasets.get_path('nyc_injurious_collisions')
    )
    geoplot.polyplot(world, figsize=(8, 4))
    plt.savefig('world.jpg')


ip_add_dict = enum_whois(get_ip(text))

latlong =  get_lat_long(ip_add_dict)
print(latlong)

geopanda_vis(get_lat_long(ip_add_dict))

#geopandas_map()
