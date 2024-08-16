from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
wind1= driver.get("https://www.nseindia.com/")
driver.find_element(By.XPATH,'//*[@id="link_2"]').click()
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a').click()
time.sleep(2)
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("lehengas for women")
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
print("Page Title is: ",driver.title)
print("Current page URL is:", driver.current_url)
time.sleep(3)
# elementh1= driver.find_element(By.XPATH,'//*[@id="search"]/span[2]/div/h1')
el2=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]')
print(el2.text)
print("new windows inner html is: ",el2.get_attribute('innerHTML'))
el2.click()
print("h2 window id  is: ", driver.current_window_handle)
ListOfWindowHandl =driver.window_handles
print("all window ID/Handls are: ", ListOfWindowHandl)

# driver.switch_to.window(ListOfWindowHandl[1])
# time.sleep(3)
# driver.switch_to.window(ListOfWindowHandl[0])
# time.sleep(2)
# el3=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]')
# el3.click()
# driver.switch_to.window(ListOfWindowHandl[1])
# time.sleep(3)
# tiTleOfproduct=driver.find_element(By.XPATH,"//span[@id='productTitle']")
# print("ProductTitle: ", driver.title)
# time.sleep(3)
# driver.switch_to.window(ListOfWindowHandl[0])
# ## after
# # element1=driver.find_element(By.XPATH,'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div[2]/div[2]/h2/a')
# # # print("ye chk:", element1.)
# # element1.click()
# # options result='//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]'
# # result search = //*[@id="search"]
# driver.get("https://seleniumbase.io/demo_page")
# driver.get("https://the-internet.herokuapp.com/")
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#


# driver=webdriver.Chrome()
# wind1= driver.get("https://www.nseindia.com/")
# driver.find_element(By.XPATH,'//*[@id="link_2"]').click()
# time.sleep(4)
# driver.find_element(By.XPATH,'//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a').click()
# time.sleep(2)             # //span[normalize-space()='in Clothing']
# //span[normalize-space()='HETRANG']
# //img[@alt="HETRANG Women's Embroidered Georgette Lehenga Choli for Women I Designer I New I Bridal I Navratri I Bollywood I Letest I ..."]
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //div[@id='ppd']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //span[@id='productTitle']
# //div[@id='ppd']
# //div[@class='a-cardui _p13n-desktop-sims-fbt_fbt-desktop_flex-fbt-container__3fI_9']
# //div[@class='a-cardui _p13n-desktop-sims-fbt_fbt-desktop_flex-fbt-container__3fI_9']
# //div[@id='magnifierLens']
# //i[@class='a-icon a-icon-close']
# //span[@id='a-autoid-3']//input[@type='submit']
# //span[@id='a-autoid-3']//input[@type='submit']
# //img[@alt='ZAVERI PEARLS Gold Tone Kundan Choker Necklace Earring Maangtikka & Ring Set For Women-ZPFK10799']
# //span[@id='a-autoid-3']//input[@type='submit']
# //span[@id='a-autoid-4']//input[@type='submit']
# //span[@id='a-autoid-5']//input[@type='submit']
# //span[@id='a-autoid-5']//input[@type='submit']
# //span[@id='a-autoid-6']//input[@type='submit']
# //span[@id='a-autoid-7']//input[@type='submit']
# //span[@id='a-autoid-8']//input[@type='submit']
# //button[@title='Play Video']//span[@class='vjs-icon-placeholder']
# //button[@title='Play Video']//span[@class='vjs-icon-placeholder']
# //video[@id='mbsoftlines-player-443c2ba4-c8fc-4459-9ee2-2146ddac11bb-container-element_html5_api']
#
#
#
#
#
#
# body > div:nth-child(1) > header:nth-child(20) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)
# body > div:nth-child(1) > div:nth-child(27) > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > span:nth-child(1)
# img[alt="HETRANG Women's Embroidered Georgette Lehenga Choli for Women I Designer I New I Bridal I Navratri I Bollywood I Letest I ..."]
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# #ppd
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1) > span:nth-child(1)
#
# #ppd
# .a-cardui._p13n-desktop-sims-fbt_fbt-desktop_flex-fbt-container__3fI_9
#
# #magnifierLens
# body > div:nth-child(21) > div:nth-child(1) > div:nth-child(2) > header:nth-child(1) > button:nth-child(1) > i:nth-child(1)
# body > div:nth-child(5) > div:nth-child(78) > div:nth-child(7) > div:nth-child(7) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
#
# img[alt='ZAVERI PEARLS Gold Tone Kundan Choker Necklace Earring Maangtikka & Ring Set For Women-ZPFK10799']
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(5) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(6) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(7) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(8) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(9) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1) > input:nth-child(1)
# body > div:nth-child(5) > div:nth-child(72) > div:nth-child(7) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(5) > span:nth-child(1)

#mbsoftlines-player-443c2ba4-c8fc-4459-9ee2-2146ddac11bb-container-element_html5_api








# //*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a
# //*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]
# //li[contains(@class,'nav-item dropdown active')]//div[contains(@class,'row mrow')]//div[1]//ul[1]//li[1]
# driver.find_element(By.CSS_SELECTOR,'document.querySelector("body > header:nth-child(5) > nav:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1)")').click()
#
# driver.find_element(By.XPATH,"//li[contains(@class,'nav-item dropdown active')]//a[contains(@class,'nav-link')][normalize-space()='Pre-Open Market']").click()

# driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[3]/div/div[1]/div/div[1]/ul/li[1]/a').click()
# time.sleep(2)
# # # rows=len(driver.find_elements(By.XPATH,'//*[@id="livePreTable"]/thead/tr'))
# # # print(rows)
# # # print(driver.find_element(By.XPATH,"//td[normalize-space()='2,07,805']").text)
# # print(len(driver.find_elements((By.XPATH,'//*[@id="livePreTable"]/tbody/tr')))
# # # /html/body/header
# # driver.find_element(By.XPATH,'//*[@id="preopen-market"]/div/div[3]')
# # time.sleep(2)

