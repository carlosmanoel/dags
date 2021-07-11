from typing import Any

from airflow.models import BaseOperator


class HelloOperator(BaseOperator):
    """

    NomadOperator allows the DAG submit a payload to run in a NomadCluster
    """

    def __init__(self, greetings="",
                 *args,
                 **kwarg):
        super(HelloOperator, self).__init__(*args, **kwarg)
        self._greetings = greetings

    def execute(self, context: Any):
        message = "Hello {}".format(self._greetings)
        print(message)
        return message
