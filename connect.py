import webbrowser
import selenium                     
from selenium import webdriver
'''
pip3 install selenium      
install chromedriver 
rm chromedriver /usr/local/bin
allow in security and privary to open
'''

driver = webdriver.Chrome()
driver.get('http://geopig3.la.asu.edu:8080/GEOPIG/pigopt1.html')

#set Temperature (degCel), pressure (bars)

ind_var = driver.find_element_by_xpath("//input[@name='iopt_state_var' and @value='2']")
ind_var.click() 

uni_curve = driver.find_element_by_xpath("//input[@name='univar_curve_opt' and @value='N']")
uni_curve.click()

iso_bars_range = driver.find_element_by_id("iso_bars_range")
iso_bars_range.send_keys("0, 150, 15")

temp_range = driver.find_element_by_id("temp_range")
temp_range.send_keys("0, 200, 25")
