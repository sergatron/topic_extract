# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 20:28:44 2019

@author: smouz

"""

import sys
from collections import Counter

import numpy as np
import pandas as pd

from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import make_pipeline, make_union

#%%
# read-in article from file
def read_article(file):
    article = ''
    with open(file, 'r') as txt:
        article = txt.read()
    return article

#%%
def process_text(text_doc):
    """
    Convert to lowercase.
    Retain only alphabetical characters.
    Remove stop words.
    Lemmatize tokens into a new list.

    Returns:
    --------
        Lemmatized list
    """
    english_stops = stopwords.words('english')
    lower_tokens = [t.lower() for t in word_tokenize(text_doc)]

    alpha_only = [t for t in lower_tokens if t.isalpha()]

    no_stops = [t for t in alpha_only if t not in english_stops]

    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]
    return lemmatized

#%%

# print('Arguments:', sys.argv)
# filename = sys.argv[1]

filename = 'scrape-article/identify-topic/investing_article.txt'

# read-in article
article = read_article(filename)

# process article, returns bag-of-words
bow = process_text(article)

# split into sentences
sentences = sent_tokenize(article)

# process senteces into bag-of-words
sent_bow = list(map(process_text, sentences))

#%%

print('\n\n')
print('Most common words'.center(50, '-'))
Counter(bow).most_common(15)

top_words = []
for item in Counter(bow).most_common(15):
    top_words.append(item[0])

top_words
#%%

for item in sent_bow:
    print(" ".join(item))
    print('---')


#%%

cvect = CountVectorizer(ngram_range=(2, 2),
                        max_df=0.99,
                        min_df=2,
                        stop_words='english')

cvect.fit(sentences)

cvect.get_feature_names()

#%%
tfidf = TfidfVectorizer(ngram_range=(2, 2),
                        max_df=0.99,
                        min_df=2,
                        stop_words='english'
                        )
tfidf.fit(sentences)

tfidf.get_feature_names()


#%%

# COUNTVECTORIZER VOCABULARY
# create dataframe with results
df = pd.DataFrame({'words': list(cvect.vocabulary_.keys()),
                   'count': list(cvect.vocabulary_.values())})

df.sort_values('count', ascending=False)

# compute percent of appearance in documents
#df['percent'] = df['count'] / df['count'].sum()

df['percent'] = df['count'] / len(sentences)

print('\n\n')
print('Most frequent appearances'.center(50, '-'))
print(df.sort_values('percent', ascending=False)[:30])
print('\n\n')


#%%

# # TFIDF VOCABULARY
# # create dataframe with results
# tfidf_df = pd.DataFrame({'words': list(tfidf.vocabulary_.keys()),
#                         'count': list(tfidf.vocabulary_.values())})

# tfidf_df.sort_values('count', ascending=False)

# # compute percent of appearance in documents
# #df['percent'] = df['count'] / df['count'].sum()

# tfidf_df['percent'] = tfidf_df['count'] / len(sentences)

# print('\n\n')
# print('(TFIDF) Most frequent appearances'.center(50, '-'))
# print(tfidf_df.sort_values('percent', ascending=False)[:30])
# print('\n\n')

# NOTE:
    # results (word counts) are identical between TFIDF and CountVectorizer

#%%
# word count
Counter(tfidf.vocabulary_).most_common(10)

