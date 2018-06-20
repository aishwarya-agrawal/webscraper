import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
import csv 
browser = webdriver.Firefox(executable_path=r'C:\Users\Lenovo\Desktop\geckodriver-v0.21.0-win64\geckodriver.exe')
#enter the link you want to scrape in inverted commas below
browser.get("")
city = []
'''
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
'''
for i in range(1,51):
	el = []
	titles_element=browser.find_elements_by_xpath("/html/body/section/div/div/div/div[2]/div[3]/div/div/div["+str(i)+"]/div[1]/div[2]/h2")
	title = [x.text for x in titles_element]
	t = title[0]
	link = browser.find_elements_by_link_text(t)
	link[0].click()
	browser.implicitly_wait(10)
	am = []
	p = browser.find_elements_by_class_name("mor-a")
	p[0].click()
	for i in range(1,11):
		try:
			if browser.find_elements_by_xpath('/html/body/form/div[6]/article[2]/div[3]/div/div/div[2]/ul/li['+str(i)+']'):
				amenities = browser.find_elements_by_xpath('/html/body/form/div[6]/article[2]/div[3]/div/div/div[2]/ul/li['+str(i)+']')
				amenity = [x.text for x in amenities]
				am.append(amenity)
			else:
				break
		except selenium.common.exceptions.NoSuchElementException:
			break
	for k in range(11,31):
		try:
			if browser.find_element_by_xpath('/html/body/form/div[6]/article[2]/div[3]/div/div/div[3]/ul/li['+str(k)+']'):
				y = browser.find_element_by_xpath("/html/body/form/div[6]/article[2]/div[3]/div/div/div[3]/ul/li["+str(k)+"]")
				am.append(y.text)
			else:
				break
		except selenium.common.exceptions.NoSuchElementException:
			break
	browser.back()
	browser.implicitly_wait(10)
	address_element = browser.find_elements_by_xpath("/html/body/section/div/div/div/div[2]/div[3]/div/div/div["+str(i)+"]/div[1]/div[2]/div[3]/div[2]")
	address = [x.text for x in address_element]
	el.append(title)
	el.append(address)
	el.append(am)
	print(el)
	city.append(el)
	
with open("easemytripdelhi.csv","w") as file1:
	writes = csv.writer(file1)
	writes.writerows(city)
print("complete")
