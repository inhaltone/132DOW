from app import ImageDownloader
from helpers.utilities import Utilities
import pandas as pd

guardian_df = pd.read_csv('../../data/raw/guardian/guard-articles-ukraine.csv')
guardian_images = guardian_df[~guardian_df['Image Url'].isnull()]

for index, row in guardian_images.iterrows():
    url = row['Image Url']
    caption = Utilities.convertToKebapCase(str(row['Image Alt']))
    indexId = str(index)
    filename = f'{indexId}-{caption[:12]}'
    ImageDownloader.getImage(url, filename)
    print(filename, index, url)
