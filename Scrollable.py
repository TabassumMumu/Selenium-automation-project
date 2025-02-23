from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/Scrollable/")
driver.maximize_window()

time.sleep(2)

# Scroll down the page
scrollable_div = driver.find_element(By.CLASS_NAME, "scrollable-area")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)

time.sleep(2)  # Allow time to observe scrolling

# Scroll back to top
driver.execute_script("arguments[0].scrollTop = 0", scrollable_div)

time.sleep(2)

# Close the browser
driver.quit()
