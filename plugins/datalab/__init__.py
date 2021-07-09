from airflow.plugins_manager import AirflowPlugin

from datalab.operators import HelloOperator


class DataLabPlugin(AirflowPlugin):
    name = "datalab_plugin"
    operators = [
        HelloOperator
    ]
