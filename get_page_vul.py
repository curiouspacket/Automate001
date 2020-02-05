#!/usr/bin/env python

from selenium import webdriver
from bs4 import BeautifulSoup



driver = webdriver.Chrome(r'C:\Users\shapaar1\drivers\chromedriver.exe')

CVE =[] 
description = []
link = []
driver.maximize_window()
version =  input('What version of code would you like to look up? [NX-OS, IOS XR, IOS XE, IOS] ')
webAddress = ('https://tools.cisco.com/security/center/publicationListing.x?product=Cisco&title=%s&sort=-day_sir#~Vulnerabilities' % version)
print(webAddress)

driver.get(webAddress)
cve_list = driver.find_element_by_xpath("//*[@id="tab-1"]/div[2]/table/tbody[2]/tr[1]/td/table/tbody/tr[2]/td/div/div[2]/p[1]")
links = cve_list.find_element_by_class_name("np-scope")
for i in range(len(links)):
    print(links[i].txt)
    




#vul_element = driver.find_elements_by_class_name("ng-scope")
#for item in vul_element:
#    cveid = item.find_elements_by_class_name('ng-binding')
#    for item in cveid:
#        print(str(item))

