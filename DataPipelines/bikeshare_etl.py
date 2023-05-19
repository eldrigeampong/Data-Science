import os
import sys
import glob
import pandas as pd
from credentials import *
sys.path.append(sys_path_ds)
from sqlalchemy import create_engine, text



def read_data()->pd.DataFrame:
    '''
    Load csv objects from the file path, returning a DataFrame

    '''
    directory = os.path.join(bike_share_folder, '*.csv')
    files = glob.glob(directory)

    frame = []
    [frame.append(pd.read_csv(files[_], low_memory=False)) for _ in range(len(files))]

    return pd.concat(frame)



def load():
    '''
    Write Transformed Records Stored In A DataFrame to PostgreSQL database
     
    '''
    df = read_data()

    # drop empty columns
    cols_to_drop = ['start_station', 'end_station', 'bike_type', 'start station name', 'end station name']
    df = df.drop(cols_to_drop, axis=1)

    engine = create_engine(f'{driver_postgres}://{user_postgres}:{password_postgres}@{hostname_postgres}/{pg_db_bs}')

    table_name, conn, schema_name, replace = 'bike_share', engine, 'public', 'replace'  

    return df.to_sql(name=table_name, con=conn, schema=schema_name, if_exists=replace, index=False)


if __name__ == '__main__':
    load()