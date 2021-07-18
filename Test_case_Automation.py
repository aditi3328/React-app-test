# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:04:54 2021

Automation of Test case from TCF1 - TCF4
"""
from time import sleep
from selenium import webdriver

#Call Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

#To wait applicable for chrome browser
driver.implicitly_wait(30)

#To open the link
driver.get("http://skunkworks.ignitesol.com:3000/")

#To maximize the window
driver.maximize_window()

#TCF1 - Click on Fiction option
print ("TCF1:")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/a/button/span[1]/span').click()
print('Clicked on Fiction books option')


#TCF1 - Check if we are on Fiction page, check the page header
status = driver.find_element_by_xpath('//*[@id="root"]/div/div/h1').text
print("The Fiction books page loaded")

if  status == 'FICTION':
    print("The Test Case TCF1 passed")
else:
    print("The Test case TCF1 failed")
    
print()

#TCF2 - Check the Name of Placeholder in search box
print("TCF2:")
search_value = driver.find_element_by_xpath('//*[@id="outlined-full-width"]').get_attribute('placeholder')
print("The Value of Palceholder on screen is",search_value)

if search_value == "Placeholder":
    print("The Test case TCF2 has failed")
else:
    print("The Test case TCF2 Passed")
    
print()

#TCF3 - Check if the user can enter the book name in search box
print("TCF3:")
driver.find_element_by_xpath('//*[@id="outlined-full-width"]').send_keys('Dracula')
print('The book name Dracula entered in search bar')
print ('The Test case TCF3 Passed')
print()

#TCF4 - Search for the book by clicking on search button
print("TCF4:")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/button/span[1]').click()
print('Search for the book name Dracula')

sleep(10)

# Check the name of the first book name and compare it with the book name in searchbox
ele = driver.find_element_by_tag_name("h5").text
print("The name of first book name after search is:",ele)

if ele == "Dracula":
    print ("The Test case TFC4 Passed")
else:
    print("The Test case TFC4 Failed")


driver.close()