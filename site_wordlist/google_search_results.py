from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get("http://www.google.com")
element = driver.find_element_by_name("q")
element.send_keys("Spring MVC Login form Example")
element.submit()

results = driver.find_elements_by_xpath("//div[@class='g']//div[@class='r']//a[not(@class)]")

for result in results:
    print(result)
    # print(result.get_attribute("href"))
