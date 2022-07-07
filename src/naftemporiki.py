from app import ParserHTML
from app import naftemporikiScraper
import pandas as pd

naftemporiki = ParserHTML.readRawHTML('../data/raw/naftemporiki/polemos-stin-oukrania-naftemporiki-raw-html.txt')
articles = naftemporiki.find_all('div', attrs={'class': 'stream-item'})
naftemporiki_df = pd.DataFrame()
path = '../data/raw/naftemporiki/'

for article in articles:
    data = naftemporikiScraper.constructData(article)
    naftemporiki_df = pd.concat([naftemporiki_df, pd.DataFrame([data])], axis=0, ignore_index=True)
    print(naftemporiki_df.shape)

naftemporiki_df.to_csv(f'{path}naftemporiki-polemos-stin-oukrania.csv')
print('FINISHED!!!')


