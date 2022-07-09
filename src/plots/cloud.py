import pandas as pd
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt

war_df = pd.read_csv('../../data/processed/war-ukraine-extended-ordered.csv',
                     index_col=[0])

nlp_el = spacy.load("el_core_news_md")
nlp_en = spacy.load("en_core_web_md")

greek_text = war_df[war_df['Lang'] == 'el']['Text'].str.cat(sep=' ')
english_text = war_df[war_df['Lang'] == 'en']['Text'][:10].str.cat(sep='')

full_words_el = nlp_el(war_df['Text'][1])
lemma_words_el = ' '.join(token.lemma_ for token in full_words_el)

wordcloud = WordCloud(
    stopwords=nlp_el.Defaults.stop_words,
    width=2000,
    height=1000,
    background_color='black'
).generate(lemma_words_el)
fig = plt.figure(
    figsize=(40, 30),
    facecolor='k',
    edgecolor='k')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()

full_words_en = nlp_en(english_text)
lemma_words_en = ' '.join(token.lemma_ for token in full_words_en)

wordcloud = WordCloud(
    stopwords=nlp_en.Defaults.stop_words,
    width=2000,
    height=1000,
    background_color='black'
).generate(lemma_words_en)
fig = plt.figure(
    figsize=(40, 30),
    facecolor='k',
    edgecolor='k')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
