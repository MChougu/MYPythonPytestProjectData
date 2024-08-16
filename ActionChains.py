import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

action = ActionChains(driver)
dropElem = driver.find_element(By.ID, 'myDropdown')
option2 = driver.find_element(By.ID, 'dropOption2')
time.sleep(4)
action.move_to_element(dropElem).move_to_element(option2).click().perform()
time.sleep(2)
## double click
# btn = driver.find_element(By.ID, 'myButton')
# action.double_click(btn).perform()
##Right Click
# time.sleep(2)
# action.context_click().perform()

## Drag and drop
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

action = ActionChains(driver)
#
dropCapital = driver.find_element(By.ID, 'box5')
dropBox = driver.find_element(By.ID, 'box105')
time.sleep(3)
action.drag_and_drop(dropCapital, dropBox).perform()
time.sleep(3)

