from typing import Dict

from airflow.decorators import dag, task
from airflow.utils.dates import days_ago

from datalab.operators import HelloOperator

_DEFAULT_ARGS = {"owner": "datalab"}


@dag(dag_id="gyodag_dag_dag_dag", default_args=_DEFAULT_ARGS, schedule_interval=None, start_date=days_ago(2), tags=['datalab'])
def hello(name: str = "default name"):
    hi = HelloOperator(task_id='hi', greetings=name)

    @task(multiple_outputs=True)
    def message(name_task) -> Dict[str, str]:
        return {
            'subject': f"Hi {name_task}",
            'message': f"Airflow operator is working!!!!",
        }


    message_returned = message(name)

    hi = HelloOperator(task_id='hi_again', greetings=name)


dag = hello("Jonh Malkovich")
