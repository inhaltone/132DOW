## 132 days of war
#### Import dataset as dataframe

#### Dataset

| Keys             | `Value`                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Publisher**    | `THE GUARDIAN`                                                                                                          |
| Date Formatted   | `2022-02-23`                                                                                                            |
| Lang             | `en/el`                                                                                                                 |
| Heading          | `Russia-Ukraine war: what we...`                                                                                        |
| Tag              | `WORLD`                                                                                                                 |
| Text             | `snap verdictPMQs has never been a forum that handles nuance...`                                                        |
| Comments exist   | `True` `False`                                                                                                          |
| Comments count   | `7064`                                                                                                                  |
| Comments api key | `/p/kz3fp`                                                                                                              |
| Article url      | https://www.theguardian.com/politics/live/2022/feb/23/uk-politics-live-boris-johnson-ukraine-russia-pmqs-latest-updates |
| Chars            | `18673`                                                                                                                 |
| Words            | `3017`                                                                                                                  |
| Year             | `2022`                                                                                                                  |
| Month            | `2`                                                                                                                     |
| Day              | `23`                                                                                                                    |
| Lemma            | `snap verdictpmqs forum handle nuance...`                                                                               |
| Sentiments       | `negative` `neutral` `positive`                                                                                         |
| Positivity       | `0.219`                                                                                                                 |
| Negativity       | `0.089`                                                                                                                 |


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
