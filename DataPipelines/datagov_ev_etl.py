import requests
import numpy as np
import pandas as pd
from credentials import *
from sqlalchemy import text, create_engine




def extract():
    '''
    Extract Electric Vehicle Population Data From DataGov Website

    '''
    url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.json?accessType=DOWNLOAD'

    try:
        r = requests.get(f'{url}', timeout=(2, 10))

        if r.status_code == requests.codes.ok:
            print('request successful')
    except requests.exceptions.ConnectionError as error:
        print(f'Error Message: {error}')
    else:
        r.raise_for_status()
    return r.json()




def transform():
    '''
    Transform Json File to Pandas Dataframe

    '''
    response = extract()

    data = response[DATA]
    df_pd = pd.DataFrame(data)

    col_lists = np.arange(len(response[META][VIEW][COLUMNS]))

    column_names = [response[META][VIEW][COLUMNS][idx][NAME] for idx in col_lists]
    df_pd.columns = column_names
    df_pd.columns = [col.replace(' ', '_') for col in df_pd.columns]

    df = df_pd.iloc[:, [9, 10, 11, 12, 13, 14, 15, 16, 18]]

    return df




def load():
    '''
    Write Transformed Records Stored In A DataFrame to PostgreSQL database
     
    '''
    df_transformed = transform()

    engine = create_engine(f'{driver_postgres}://{user_postgres}:{password_postgres}@{hostname_postgres}/{database_postgres}')

    table_name, conn, schema_name, replace = 'electric_vehicles', engine, 'state', 'replace'  

    df_transformed.to_sql(name=table_name, con=conn, schema=schema_name, if_exists=replace, index=False)

    return df_transformed


if __name__ == '__main__':
    load()



    












