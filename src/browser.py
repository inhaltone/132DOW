# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
from selenium.webdriver.common.by import By

from endpoints import Endpoints
#
# driver = webdriver.Firefox()
#
#
# # driver.get(Endpoints.KATHIMERINI_TAGS_POLEMOS_STIN_OUKRANIA.value)
# # ajax = driver.find_element(By.CLASS_NAME, "nx_loadmore")
# # ajax.click()
#
# def document_initialised(driver):
#     return driver.execute_script("return initialised")
#
#
# driver.get(Endpoints.KATHIMERINI_TAGS_POLEMOS_STIN_OUKRANIA.value)
# WebDriverWait(driver, timeout=10).until(document_initialised)
# ajax = driver.find_element(By.CLASS_NAME, "nx_loadmore")
# assert ajax.text == "Hello from JavaScript!"

# from webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

raw_html = None
count = 0
driver = webdriver.Firefox()
driver.get(Endpoints.KATHIMERINI_TAGS_POLEMOS_STIN_OUKRANIA.value)
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME, "nx_loadmore"))
time.sleep(10)
while True:
    try:
        # time.sleep(5)
        ajax = WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME, "nx_loadmore"))
        ajax.click()
        print('is clicked')
        count += 1
        print(f'Page: {count}')
    except TimeoutException:
        break
    if not ajax:
        break

raw_html = driver.page_source
print(raw_html)
with open("../data/raw/kathimerini/polemos-stin-oukrania.txt", "w") as file:
    file.write(raw_html)
print('finished')

