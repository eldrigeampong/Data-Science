# %% - Abstract

# import modules
import os
import spacy
from spacy import displacy

# %% - Read Text Document

# get current working directory
cwd = os.getcwd()

# get file path
fullpath = os.path.join(cwd, 'files', 'abstract.txt')

with open(fullpath, 'r') as f:
    text = f.readline()
    print(text)

# %%
print('Python Text length: {0}'.format(len(text)))

# text exploration from python
for idx, token in enumerate(text):
    print('\n', idx, token)

# %%

# load spacy model
nlp = spacy.load('en_core_web_md')

# %% 
doc = nlp(text)
print(doc)

# %%

# get the number of tokens in the document
print(f'Spacy Document Length: {len(doc)}')

# %%
for idx, token in enumerate(doc):
    print(idx, token)
