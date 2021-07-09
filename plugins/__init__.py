from airflow.plugins_manager import AirflowPlugin

from operators import *


class DataLabPlugin(AirflowPlugin):
    name = "datalab_plugin"
    operators = [
        HelloOperator
    ]
