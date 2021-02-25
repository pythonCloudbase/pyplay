try:
    import requests
    from bs4 import BeautifulSoup
    import os
    import time
    import csv
    import pandas as pd
    import numpy as np
except ImportError  as e:
    print(e)
    raise SystemExit("Please install modules and try again.")

#Setting paths to where the scrape.csv files are located
file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(file_path)


scrape_folder = os.path.join(project_directory + "\scrape_data")

print("The current project directory is ", scrape_folder)

print(os.chdir(project_directory))

def scrape_info():
    
    url = input("Enter url: ")
    new_scrape_name = input("Enter text file name: ")
    target_tag = input("What HTML tag are you looking for? : ")
    return url, new_scrape_name, target_tag


def basicscraper(url, new_scrape_name, target_tag):
    
    page_data = requests.get(url)
    print(page_data)

    soup = BeautifulSoup(page_data.text, "lxml")
    print(soup)

    for something in soup.find_all(target_tag):
        tag_text = something.text.strip()
        if not os.path.exists(scrape_folder):
            os.makedirs(project_directory + "\scrape_data")
            with open(os.path.join(scrape_folder, new_scrape_name + ".csv"), "a") as output:
                output.write(url + "|" + target_tag + "|" + time.strftime("%d%m%Y") + "|" + tag_text + "\n")
        os.chdir(scrape_folder)
        with open(new_scrape_name + ".csv", "a") as output:
            output.write(url + "|" + target_tag + "|" + time.strftime("%d%m%Y") + "|" + tag_text + "\n")
        os.chdir(project_directory)

def simplescrapper(url):

    page_data = requests.get(url)
    soup = BeautifulSoup(page_data.text, "lxml")
    
    counter = 0
    some_list = []
    for something in soup.find_all('tr'):
        # print(something)
        # print("\n")
        counter += 1
        for some in something.find_all('td'):
            some_list.append(str(some))
        some_list.append("> "+str(counter)+"\n")
        
    
    f = open('output.txt', 'w+', encoding="utf-8")
    
    f.write("\n".join(some_list))
        


def scrape_away(url=None, new_scrape_name=None, target_tag=None):
    
    url = 'https://www.fleetmon.com/vessels/'

    simplescrapper(url)

    
    # if url is None and new_scrape_name is None and target_tag is None:
    #     # url, new_scrape_name, target_tag = scrape_info()
    #     basicscraper(url, new_scrape_name, target_tag)
    # else:
    #     basicscraper(url, new_scrape_name, target_tag)


scrape_away()