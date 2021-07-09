from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from datalab.operators import HelloOperator

_DEFAULT_ARGS = {"owner": "datalab"}


@dag(dag_id="gyodag_dag_dag_dag", default_args=_DEFAULT_ARGS, schedule_interval=None, start_date=days_ago(2), tags=['datalab'])
def hello(name: str = "default name"):
    hi = HelloOperator(task_id='hi', greetings=name)

    @task(multiple_outputs=True)
    def message(name_task):
        return {
            'subject': f"Hi {name_task}",
            'message': f"Airflow operator is working!!!!",
        }

    message_task = message(name)

    hi_again = HelloOperator(task_id='hi_again', greetings=name)
    hi >> message_task >> hi_again


dag = hello("Jonh Malkovich")


