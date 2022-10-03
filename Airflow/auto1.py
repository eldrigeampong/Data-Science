# %%
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_arguments = {
  'depends_on_past': False,
  'email': ['eldrigeampong@gmail.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=5),
  # 'queue': 'bash_queue',
  # 'pool': 'backfill',
  # 'priority_weight': 10,
  # 'end_date': datetime(2016, 1, 1),
  # 'wait_for_downstream': False,
  # 'sla': timedelta(hours=2),
  # 'execution_timeout': timedelta(seconds=300),
  # 'on_failure_callback': some_function,
  # 'on_success_callback': some_other_function,
  # 'on_retry_callback': another_function,
  # 'sla_miss_callback': yet_another_function,
  # 'trigger_rule': 'all_success'
}

with DAG(
  dag_id='northwind_database',
  description='extract data from northwind database',
  schedule_interval=timedelta(days=1),
  start_date=datetime(2022, 10, 3),
  end_date=datetime(2022, 10, 10),
  catchup=False
  ) as dag:

    task1 = PostgresOperator(
      task_id = 'extract_customers_data',
      postgres_conn_id = 'postgres_localhost',
      sql='''
          select * from customers c;
         '''
    )

    task2 = PostgresOperator(
      task_id = 'extract_orders_data',
      postgres_conn_id='postgres_localhost',
      sql='''
            select * from orders o;
          '''
    ),

    task3 = PostgresOperator(
      task_id = 'extract_categories_data',
      postgres_conn_id='postgres_localhost',
      sql='''
            select * from categories c;
          '''
    ),

    task4 = PostgresOperator(
      task_id = 'extract_products_data',
      postgres_conn_id = 'postgres_localhost',
      sql='''
            select * from products p;
          '''
    )

    [task1, task2, task3, task4]
# %%
