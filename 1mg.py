import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
import csv 
browser = webdriver.Firefox(executable_path=r'C:\Users\Lenovo\Desktop\geckodriver-v0.21.0-win64\geckodriver.exe')
browser.get("https://www.1mg.com/manufacturers")
link = []
browser.implicitly_wait(5)
#extract links of companies 
for i in range(1,64):
	names = browser.find_element_by_id('srchRslt').find_elements_by_tag_name('a')
	for x in names :
		try:
			link.append(x.get_attribute('href'))
			print(x.get_attribute('href'))
		except:
			continue	
	browser.implicitly_wait(10)
	#click on the arrow for next page 
	el = browser.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/div/div[2]/div[2]/div[2]/nav/div/ul/li[5]/a')
	el.click()
med_name = []
#extract link of medicines 
for lnk in link:
	browser.get(lnk)
	medicine = browser.find_element_by_id('srchRslt').find_elements_by_tag_name('a')
	for x in medicine:
		try:
			med_name.append(x.get_attribute('href'))
			print(x.get_attribute('href'))
		except:
			continue
med = []
#extract data from medicine link 
for medcn in med_name:
	browser.get(medcn)
	browser.implicitly_wait(5)
	try:
		name = browser.find_element_by_css_selector('.DrugInfo__drug-name-heading___adCs-')
		symp = browser.find_element_by_css_selector('.DrugInfo__uses___381Re')
		comp = browser.find_element_by_css_selector('.DrugInfo__company-name___39Abk')
		drug = browser.find_element_by_css_selector('.saltInfo > a:nth-child(1)')
		new = []
		new.append(name.text)
		new.append(symp.text)
		new.append(comp.text)
		new.append(drug.text)
		med.append(new)
	except:
		continue
	print(new)
with open("1mg_medicines.csv","w") as file1:
		writes = csv.writer(file1)
		writes.writerows(med)
print('complete')