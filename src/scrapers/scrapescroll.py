from selenium.common.exceptions import TimeoutException
import time
from prototypes.endpoints import Endpoints
from prototypes.browser import Browser

raw_html = None
count = 0
driver = Browser()
driver.openBrowserWindow(Endpoints.NAFTEMPORIKI_POLEMOS_STIN_OUKRANIA.value)
time.sleep(5)
while True:
    try:
        driver.scrollDown()
        count += 1
        print(f'Page: {count}')
    except TimeoutException:
        break
    if count > 8000:
        break

raw_html = driver.driver.page_source
with open("../../data/raw/naftemporiki/polemos-stin-oukrania-naftemporiki-raw-html.txt", "w") as file:
    file.write(raw_html)
print('finished')
