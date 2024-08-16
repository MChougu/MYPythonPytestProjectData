import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
#driver.get("https://www.google.com/search?q=grace+hopper&sca_esv=463472b0d30e7bda&sca_upv=1&rlz=1C1PNBB_enIN1030IN1030&sxsrf=ADLYWIJ5_PnXCvqsreIQ_xqV7jwHYh9VQw%3A1723621175462&ei=N1-8Zpr8G4Sf4-EPoM6GgA8&oq=&gs_lp=Egxnd3Mtd2l6LXNlcnAiACoCCAMyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyBxAjGCcY6gIyHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQEyHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQEyHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQEyHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQEyHBAuGIAEGNEDGEMYtAIYxwEYyAMYigUY6gLYAQFIzmhQ1QZYmBpwAngBkAEBmAG-AqABuwuqAQcwLjcuMS4xuAEByAEA-AEBmAIIoALBB6gCD8ICChAAGLADGNYEGEfCAg0QABiABBiwAxhDGIoFwgIZEC4YgAQYsAMY0QMYQxjHARjIAxiKBdgBAcICChAjGIAEGCcYigXCAhYQLhiABBixAxjRAxhDGIMBGMcBGIoFwgILEAAYgAQYsQMYgwHCAgUQABiABMICCBAAGIAEGLEDwgIKEAAYgAQYQxiKBcICJRAuGIAEGLEDGNEDGEMYgwEYxwEYigUYlwUY3AQY3gQY4ATYAQLCAhYQLhiABBixAxjRAxiDARgUGIcCGMcBwgIQEAAYgAQYsQMYgwEYFBiHAsICJRAuGIAEGLEDGNEDGIMBGBQYhwIYxwEYlwUY3AQY3gQY4ATYAQLCAhEQLhiABBixAxjRAxiDARjHAcICBBAjGCfCAhMQLhiABBjHARgnGIoFGI4FGK8BwgIQEC4YgAQY0QMYQxjHARiKBcICEBAAGIAEGLEDGEMYgwEYigWYAwWIBgGQBhS6BgYIARABGAi6BgYIAhABGBSSBwUyLjUuMaAHl2Q&sclient=gws-wiz-serp")

time.sleep(3)
# Page scroll by pixel
driver.execute_script('window.scrollBy(0,3000)', "")

time.sleep(3)
# Scroll by or upto specific element
ele = driver.find_element(By.ID, 'Programming_examples')
driver.execute_script("arguments[0].scrollIntoView()", ele)

time.sleep(3)
## scroll till the end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")

time.sleep(3)
## scroll upside
driver.execute_script("window.scrollBy(0, -3000)", "")      ## how to reach top of page

time.sleep(3)
## scroll upside
driver.execute_script("window.scrollTo(0,0)", "")
time.sleep(3)

