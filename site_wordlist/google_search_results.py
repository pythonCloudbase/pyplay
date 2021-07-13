from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get("http://www.google.com")
element = driver.find_element_by_name("q")

element.send_keys(input("Enter your search query? "))
element.submit()


results = driver.find_elements_by_xpath("//*[@id='rso']//*[@class='g']//div//div//div[1]//a")
# //*[@id="rso"]/div[2]/div/div/div[1]/a
# for x in dir(results[0]):
#     print(x)

top_results = []


for result in results: 
    link = result.get_attribute("href")
    
    top_results.append(link)


    # print(result.get_attribute("href"))

for link in top_results:
    driver.get(link)
    driver.save_screenshot("./image/" + str(link.split("/")[2]) + ".png")
    # driver.quit()


driver.close()