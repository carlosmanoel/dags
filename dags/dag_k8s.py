from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from hellooperator_0 import HelloOperator0

default_args = {
    'owner': 'DataLab',
    'start_date': days_ago(2),
    'catchup': False,
    'queue': 'kubernetes'
}

DAG_PREFIX = "hello"
DAG_VERSION = "1.0"

with DAG(
        dag_id=DAG_PREFIX + "_" + DAG_VERSION,
        default_args=default_args,
        schedule_interval=None,
        tags=['exampleK8s']
) as dag:

    sleep_command = HelloOperator0(
        task_id='sleep_command',
        greetings="joao",
        dag=dag
    )

    sleep_again = BashOperator(
        task_id='sleep_again',
        bash_command='sleep 5 ',
        dag=dag,
    )

    sleep_command >> sleep_again
