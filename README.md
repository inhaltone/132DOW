## 132 days of war
#### Import dataset as dataframe

````python
import pandas as pd

war = pd.read_csv('../data/processed/war-ukraine-sentiment-zip.csv',
                  compression={'method': 'gzip',
                               'compresslevel': 1,
                               'mtime': 1},
                  index_col=[0])
````
#### Run the guardian scraper
````shell
python main.py
````
