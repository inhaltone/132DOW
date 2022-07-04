import pandas as pd
from app import GuardianScraper
from endpoints import Endpoints

url = Endpoints.THE_GUARDIAN_RUSSIA.value
guardian_df = pd.DataFrame()
data = []
count = 0


while True:
    raw_html = GuardianScraper.getRawHTML(url)
    print(f'Fetching data from URL: {url}')
    data = GuardianScraper.transformHTMLtoObject(raw_html)
    url = GuardianScraper.getNextUrl(raw_html, url)
    guardian_df = pd.concat([guardian_df, pd.DataFrame(data)], axis=0, ignore_index=True)
    count += 1
    print(f'===================================== page: {count} =======================================')
    if not url:
        break

guardian_df.to_csv('data/guard-articles-russia.csv')
print('FINISHED!!!')
print(guardian_df.shape)
