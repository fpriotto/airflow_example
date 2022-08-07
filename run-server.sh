#! /usr/bin/bash
# script to run airflow webserver and scheduler in background using a virtual environment

source .env/bin/activate
export AIRFLOW_HOME=$(pwd)/.airflow_home
airflow webserver -p 8080 & airflow scheduler