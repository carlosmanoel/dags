from airflow.plugins_manager import AirflowPlugin

from operators.hellooperator import HelloOperator

class DataLabPlugin(AirflowPlugin):
    name = "datalab_plugin"
    operators = [
        HelloOperator
    ]
