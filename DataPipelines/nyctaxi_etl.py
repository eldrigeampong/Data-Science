import os
import sys
import glob
import pandas as pd
from credentials import *
sys.path.append(sys_path_ds)
from sqlalchemy import create_engine, text



def read_data()->pd.DataFrame:
    '''
    Load parquet objects from the file path, returning a DataFrame

    '''
    files_directory = os.path.join('Datasets', 'NYC Taxi', 'Yellow Taxi Trip Records', '*.parquet')
    files = glob.glob(files_directory)

    frame = []
    [frame.append(pd.read_parquet(files)) for _ in files]
  
    return pd.concat(frame)



def load():
    '''
    Write Transformed Records Stored In A DataFrame to PostgreSQL database
     
    '''
    df = read_data()

    engine = create_engine(f'{driver_postgres}://{user_postgres}:{password_postgres}@{hostname_postgres}/{database_postgres}')

    table_name, conn, schema_name, replace = 'yellow_taxi', engine, 'public', 'replace'  

    return df.to_sql(name=table_name, con=conn, schema=schema_name, if_exists=replace, index=False)


if __name__ == '__main__':
    load()