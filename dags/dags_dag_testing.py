# -------------------------------------------------------------------------------------------------#
# IMPORTS
# -------------------------------------------------------------------------------------------------#

from airflow import DAG
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

# -------------------------------------------------------------------------------------------------#
# DEFAULT ARGUMENTS AND CONSTANTS
# -------------------------------------------------------------------------------------------------#

LOCATION = Variable.get("DATASET_LOCATION")

TEMPLATE_SEARCHPATH = ["/home/airflow/gcs/data/sql/intermediaries"]

EXECUTION_TIME = "{{ ds }}"

EMAIL_RECIPIENT = [
    "dennis.kawa@ptgue.com"
]

default_args = {
    "owner": "Data Engineer",
    "email": EMAIL_RECIPIENT,
    "email_on_failure": True,
    "email_on_retry": False,
    "retry_exponential_backoff": True,
    "retry_delay": timedelta(seconds=5),
    "execution_timeout": timedelta(minutes=15),
    "retries": 4,
    "catchup_by_default": False
}

# -------------------------------------------------------------------------------------------------#
# DAG DEFINITION
# -------------------------------------------------------------------------------------------------#

with DAG(
        dag_id="d_data_testing",
        schedule_interval=None,
        start_date=datetime(year=2022, month=1, day=3, hour=2, minute=0, second=0),
        catchup=False,
        template_searchpath=TEMPLATE_SEARCHPATH,
        max_active_runs=1,
        default_args=default_args,
        tags=["TESTING", "SCHEDULED", "T_TEST"]
) as dag:

    load_data = BigQueryInsertJobOperator(
        task_id="t_data_testing",
        configuration={
            "query": {
                "query": "{% include 'intermediary_testing.sql' %}",
                "useLegacySql": False
            }
        },
        location=LOCATION
    )

# -------------------------------------------------------------------------------------------------#
# DAG FLOW
# -------------------------------------------------------------------------------------------------#

load_data
