from app import ParserHTML, kathimeriniScraper
import pandas as pd

kathimerini = ParserHTML.readRawHTML('../data/raw/kathimerini/polemos-stin-oukrania.txt')
articles = kathimerini.find_all('article')
kathimerini_df = pd.DataFrame()
count = 0
path = '../data/raw/kathimerini/'

for article in articles:
    data = kathimeriniScraper.constructData(article)
    kathimerini_df = pd.concat([kathimerini_df, pd.DataFrame([data])], axis=0, ignore_index=True)
    print(kathimerini_df.shape)

kathimerini_df.to_csv(f'{path}kathimerini-polemos-stin-oukrania.csv')
print('FINISHED!!!')


