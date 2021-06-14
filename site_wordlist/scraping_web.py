from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.headless = True

driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

driver.get("https://econpy.pythonanywhere.com/ex/001.html")

max_page_length = 5

big_array = []

for j in range(1, max_page_length):

    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    num_page_items = len(buyers)

    # print(len(buyers), len(prices))
    for i in range(num_page_items):
        big_array.append(buyers[i].text + " : " + prices[i].text)

    url = f"//a[@href='http://econpy.pythonanywhere.com/ex/00{j+1}.html']"
    buttons = driver.find_elements_by_xpath(url)
    print(url)
    for button in buttons:
        button.click()

print("The entire list is : ")

for array in big_array:
    print(array)

driver.close()