# 132 War Days Dataset
This dataset created by scraping from various journal web domains based on Europe.  
### Origin
| Publisher    | Number of articles | Comments | Lang |
|:-------------|:-------------------|----------|------|
| NAFTEMPORIKI | 4628               | `NaN`    | `el` |
| KATHIMERINI  | 3230               | `NaN`    | `el` |
| EFSYN        | 2400               | `NaN`    | `el` |
| THE GUARDIAN | 3205               | 67478    | `en` |

### Number of articles
The dataset contains **13463** articles.
### Variables
There are **19** attributes in each case of the dataset
## Dataset

| Keys                 | Value                                                                                                                                                                                                |
|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Publisher**        | `THE GUARDIAN` `KATHIMERINI` `EFSYN` `NAFTEMPORIKI`                                                                                                                                                  |
| **Date Formatted**   | `2022-02-23`                                                                                                                                                                                         |
| **Lang**             | `en/el`                                                                                                                                                                                              |
| **Heading**          | `Russia-Ukraine war: what we...`                                                                                                                                                                     |
| **Tag**              | `WORLD` `POLITICS` `BOOKS` `...`                                                                                                                                                                     |
| **Text**             | `Not long ago, Brexit Britain was the bad boy of Europe. Then it was Poland’s turn, its rightwing leadership likewise excoriated for defying the Brussels establishment. Now, after the invasion...` |
| **Comments exist**   | `True` `False`                                                                                                                                                                                       |
| **Comments count**   | `7064`                                                                                                                                                                                               |
| **Comments api key** | `/p/kz3fp`                                                                                                                                                                                           |
| **Article url**      | `https://www.theguardian.com/politics/live/2022/feb/23/uk-politics...`                                                                                                                               |
| **Chars**            | `18673`                                                                                                                                                                                              |
| **Words**            | `3017`                                                                                                                                                                                               |
| **Year**             | `2022`                                                                                                                                                                                               |
| **Month**            | `2`                                                                                                                                                                                                  |
| **Day**              | `23`                                                                                                                                                                                                 |
| **Lemma**            | `long ago brexit britain bad boy europe poland turn rightwing leadership likewise excoriate defy brussels establishment invasion...`                                                                 |
| **Sentiments**       | `negative` `neutral` `positive`                                                                                                                                                                      |
| **Positivity**       | `0.219`                                                                                                                                                                                              |
| **Negativity**       | `0.089`                                                                                                                                                                                              |

## Import dataset
```python
import pandas as pd

war = pd.read_csv('../data/processed/war-ukraine-sentiment-zip.csv',
                  compression={'method': 'gzip',
                               'compresslevel': 1,
                               'mtime': 1},
                  index_col=[0])
```
## Plots
Scatter plot describes linear relations between negativity and positivity variables

![This is an image](reports/26-linear-relations.png)

Sentiments distribution along Publishers

![This is an image](reports/4-1-dist-sentiment-publisher.png)

![This is an image](reports/16-dist-bar-sentiments.png)

![This is an image](reports/17-dist-reverse.png)


## Project structure
````
├── data
│   └── final 
│       └── 132-war-days-zip.csv
│   ├── images
│   ├── intermediate
│   ├── nrc
│   ├── old
│   ├── processed
│   └── raw
│
├── docs
│   ├── src 
│   └── index.html
│   
├── notebooks
│   ├── dataAnalysisVisualization.ipynb
│   ├── dataImportTransform.ipynb
│   ├── dataMerge.ipynb
│   ├── dataOptCleaning.ipynb
│   ├── dataTesting.ipynb
│   ├── guardianComments.ipynb
│   └── sentimentAnalysis.ipynb
│
├── reports
│   └── ***.png
│   
├── src
│   ├── helpers
│   │   └── utilities.py
│   │ 
│   ├── plots
│   │   └── cloud.py
│   │  
│   ├── prototypes
│   │   ├── browser.py 
│   │   ├── datamodel.py 
│   │   ├── endpoints.py 
│   │   └── twitterapi.py
│   │ 
│   ├── scrapers
│   │   ├── comments.py 
│   │   ├── efsyn.py 
│   │   ├── guardian.py 
│   │   ├── guardian-old.py 
│   │   ├── images.py 
│   │   ├── kathimerini.py 
│   │   ├── naftemporiki.py 
│   │   ├── scrapeajax.py 
│   │   ├── scrapescroll.py 
│   │   └── tweets.py
│   │                    
│   └── app.py 
│             
├── .gitignore
├── .env
└── README.md
````

## Run the guardian scraper
````shell
$ cd src/scrapers
````
````shell
$ source /venv/bin/activate
````
````shell
$ python guardian.py
````