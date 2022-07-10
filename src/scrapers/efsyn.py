import pandas as pd
from app import efsynScraper
from prototypes.endpoints import Endpoints

base_url = Endpoints.EFSYN_OUKRANIA.value
efsyn_df = pd.DataFrame()
articles = []
currentPage = 0
totalPages = 200


while True:
    url = f'{base_url}?page={currentPage}'
    print(f'URL: {url}')
    data = efsynScraper.getArticles(url)
    efsyn_df = pd.concat([efsyn_df, pd.DataFrame(data)], axis=0, ignore_index=True)
    articles.extend(data)
    print(f'Articles: {len(articles)} so far ==============================================================')
    currentPage += 1
    if currentPage == totalPages:
        break

efsyn_df.to_csv('../data/raw/efsyn/efsyn-oukrania.csv')
print('FINISHED!!!')
# print(efsyn_df.shape)
