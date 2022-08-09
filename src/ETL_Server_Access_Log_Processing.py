from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# defining DAG arguments

default_args = {
    'owner': 'Your Name Here',
    'start_date': days_ago(0),
    'email': ['your@email.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

# defining the DAG

dag = DAG(
    dag_id='ETL_Server_Access_Log_Processing',
    default_args=default_args,
    description='Sample ETL DAG using Bash',
    schedule_interval=timedelta(days=1),
)

# defining the tasks

create_staging_area = BashOperator(
    task_id='create_staging_area',
    bash_command='echo creating staging area; \
    mkdir ~/staging',
    dag=dag,
)

download = BashOperator(
    task_id='download',
    bash_command='echo download phase started; \
    wget -O ~/staging/web-server-access-log.txt https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt',
    dag=dag,
)

extract = BashOperator(
    task_id='extract',
    bash_command='echo extract phase started; \
    cut -d"#" -f1,4 ~/staging/web-server-access-log.txt > ~/staging/extracted_fields.txt',
    dag=dag,
)

transform = BashOperator(
    task_id='transform',
    bash_command='echo transform phase started; \
    tr "[:upper:]" "[:lower:]" < ~/staging/extracted_fields.txt > ~/staging/extracted_fields_lower.txt',
    dag=dag,
)

load = BashOperator(
    task_id='load',
    bash_command='echo load phase started; \
    zip ~/compressed.zip ~/staging/extracted_fields_lower.txt;',
    dag=dag,
)

del_staging_area = BashOperator(
    task_id='delete_staging_area',
    bash_command='echo removing staging area; \
    rm -r ~/staging/',
    dag=dag,
)

create_staging_area >> download >> extract >> transform >> load >> del_staging_area
