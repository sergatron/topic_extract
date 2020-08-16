# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:12:49 2019

@author: smouz

"""
import sys
import os
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

# import encodings to iterate over
from encodings.aliases import aliases
alias_values = set(aliases.values())

print('Current working dir:', os.getcwd())

#%%

# if flag is provided then scrape from URL
if sys.argv[1] == '-r':
    print('Argument passed:', sys.argv[1])
    print('Connecting to URL')
    r = requests.get('https://examine.com/supplements/royal-jelly')
    r.status_code
    


#%%
# if NO FLAG, then open existing file



#%%
# try various encodings
for enc in list(alias_values):
    try:
#         print("Encoding:", enc)
        df_enc = []
        with open('invst.txt', 'r', encoding=enc) as file:
            df_enc.append(file.read())
        print("Encoding:", enc)
        if df_enc:
            print("Success:", enc)
            break
    except Exception as e:
#         print(e)
        pass


#%%
# open article
file_name = sys.argv[1]
article = ''
with open(file_name, 'r', encoding='utf-8') as file:
    article = file.read()

#%%
# use BS4 to find tags of paragraphs
soup = bs(article, 'lxml')

soup = bs(r.text, 'lxml')

#%%
# find all paragraph tags and put together into one article
par = ''
soup.find_all('p')
for item in soup.find_all('p'):
    par = par + item.text

#%%
# write content to file
def to_text(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as new_f:
        print(f'Writing {file_name} ... ')
        new_f.write(content)
        print('Finished!')

#%%
to_text('royal-jelly-summary.txt', par)


