from selenium.common.exceptions import TimeoutException
import time
from endpoints import Endpoints
from browser import Browser


def getKathimeriniAjaxButton():
    return driver.getElementByClassName("nx_loadmore")


raw_html = None
count = 0
driver = Browser()
driver.openBrowserWindow(Endpoints.KATHIMERINI_TAGS_POLEMOS_STIN_OUKRANIA.value)
getKathimeriniAjaxButton()
time.sleep(10)
while True:
    try:
        time.sleep(5)
        ajax = getKathimeriniAjaxButton()
        ajax.click()
        count += 1
        print('is clicked')
        print(f'Page: {count}')
    except TimeoutException:
        break
    if not ajax:
        break

raw_html = driver.page_source
print(raw_html)
with open("../data/raw/kathimerini/polemos-stin-oukrania-sample.txt", "w") as file:
    file.write(raw_html)
print('finished')
