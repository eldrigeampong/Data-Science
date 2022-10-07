# %%
import pandas as pd
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


def transformer(df: pd.DataFrame):
  '''
  
  Parameters
  ----------

  df: pd.Dataframe
      pandas dataframe
  
  Returns
      pandas dataframe

  '''
  # rename dataframe columns
  df.rename(columns={'0': 'A', '1': 'B'}, inplace=True)

  # convert all column names to lower case
  df.columns = [col.lower() for col in df.columns]
  return df




args = {
  'depends_on_past': False,
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 1,
  'retry_delay': timedelta(minutes=5)
}


with DAG(dag_id='project_1',
  description='data_wrangling',
  schedule_interval='@once',
  start_date=datetime(2022, 10, 7),
  end_date=datetime(2022, 10, 8),
  default_args=args
) as dag:

  task_1 = PostgresOperator(
    task_id='postgres_connection',
    sql='''select * from employees;''',
    postgres_conn_id='postgres_localhost'
  )

  task2 = PythonOperator(
    task_id='transform_data',
    python_callable=transformer
  )

# %%
