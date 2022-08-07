#! /usr/bin/bash

mkdir .airflow_home
virtualenv .env
source .env/bin/activate
export AIRFLOW_HOME=$(pwd)/.airflow_home
pip install -r requirements.txt
airflow db init
read -p "Username (e.g. admin): " uname
read -p  "First name (e.g. John): " fname
read -p  "Last name (e.g. Doe): " lname
read -p  "Role (e.g. Admin): " userrole
read -p  "Email (e.g. johndoe@email.com): " useremail

while true; do
  read -s -p "Password: " password1
  echo
  read -s -p "Confirm password: " password2
  echo
  [ "$password1" = "$password2" ] && break
  echo "Please try again"
done

airflow users create --username $uname --firstname $fname --lastname $lname --role $userrole --email $useremail --password $password1
mkdir $AIRFLOW_HOME/dags
cp src/ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags
deactivate