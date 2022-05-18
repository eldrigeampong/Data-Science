# %% - List of countries by GDP (nominal)

# import libraries
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

r = requests.get(url=url)

print(f'Status code: {r.status_code}')
print(f'Encoding: {r.encoding}')

# %% - HTML Document Exploration
soup = BeautifulSoup(r.text, 'html.parser')
print(f'Document title: {soup.title.string}')
print('\n', soup.prettify())
# %%
