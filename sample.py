from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Chrome ('C:\Python39\chromedriver_win32\chromedriver.exe')
 
driver.get("https://www.wikipedia.org/")
time.sleep(5)
link = driver.find_element_by_xpath('//*[@id="js-link-box-en"]')
link.click()
time.sleep(5)
searchBox = driver.find_element_by_id("searchInput")
searchBox.send_keys("Software")
searchBox.send_keys(Keys.RETURN)
time.sleep(10)
driver.quit()
