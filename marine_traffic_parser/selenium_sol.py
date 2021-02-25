from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

client = webbrowser.get('firefox')
browser = webdriver.Chrome('./chromedriver')

url = "www.example.com"
browser.get(url)
###### Wait until you see some element that signals the page is completely loaded
WebDriverWait(browser, timeout=10).until(lambda x: x.find_element_by_class_name('Even'))

############## do your things with the first page
content =  browser.page_source.encode('ascii','ignore').decode("utf-8")


#### Now if you are sure there is next page
next_button_class = 'icon-arrowright-thin--pagination' ###here insert the class of 'next button'
browser.find_element_by_class_name(next_button_class).click()
time.sleep(3)

###### Wait until you see some element that signals the page is completely loaded
WebDriverWait(browser, timeout=10).until(lambda x: x.find_element_by_class_name('Even'))

content =  browser.page_source.encode('ascii','ignore').decode("utf-8")