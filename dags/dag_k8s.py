from datetime import date, timedelta

from airflow.models import DAG

from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'DataLab',
    'start_date': days_ago(2),
    'catchup': False,
    'queue': 'kubernetes'
}

DAG_PREFIX = "dagdagdag"
DAG_VERSION = "1.0"

with DAG(
        dag_id=DAG_PREFIX + "_" + DAG_VERSION,
        default_args=default_args,
        schedule_interval=None,
        tags=['exampleK8s']
) as dag:

    sleep_command = BashOperator(
        task_id='sleep_command',
        bash_command='sleep 5 ',
        dag=dag
    )

    sleep_again = BashOperator(
        task_id='sleep_again',
        bash_command='sleep 5 ',
        dag=dag,
    )

    sleep_command >> sleep_again
