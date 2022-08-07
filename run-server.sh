#! /usr/bin/bash
# script to run airflow webserver and scheduler in background using a virtual environment

source .env/bin/activate
airflow webserver -p 8080 & airflow scheduler