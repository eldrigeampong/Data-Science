import json
import pandas as pd
import datetime as dt
from credentials import *
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


def extract()->json:
  '''
  Returns a paginated list of all active cryptocurrencies with latest market data

  https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest

  '''
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

  parameters = {
                 'start':'1',
                 'limit':'5000',
                 'convert':'USD'
               }

  headers = {
              'Accepts': 'application/json',
              'X-CMC_PRO_API_KEY': f'{coinmkt_API_Key}',
            }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  return data


def transform()->pd.DataFrame:
  '''
  Transform Json data to pandas dataframe

  '''
  json_data = extract()['data']
  df_pd = pd.DataFrame(json_data)

  cols_to_use = ['name', 'symbol', 'num_market_pairs', 'max_supply', 'circulating_supply', 'total_supply', 'cmc_rank', 'date_added', 'last_updated']
  df_pd = df_pd[cols_to_use]

  df_pd['date_added'] = pd.to_datetime(df_pd['date_added']).dt.date
  df_pd['last_updated'] = pd.to_datetime(df_pd['last_updated']).dt.date

  df_pd['date_added'] = pd.to_datetime(df_pd['date_added'])
  df_pd['last_updated'] = pd.to_datetime(df_pd['last_updated'])
  
  return df_pd

if __name__ == '__main__':
  transform()