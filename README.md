# airflow_example

This project sets up an Apache Airflow environment, configures the server and implements a simple ETL (Extract, Transform, Load) process using bash operators for demonstration and practice purposes. In order to reproduce results, one must follow the process describe in "Usage" Section.
The ETL process consists in a few steps as follows:

- Set up the staging area;
- Download relevant data to be processed;
- Extract fields of interest;
- Transform data to make it more convenient;
- Load and compress the processed data; and
- Delete the staging area.

These steps are implemented in the source code found in this repository. This project was developed according to and following recommendations of IBM Data Engineer course (available at https://www.coursera.org/professional-certificates/ibm-data-engineer).

## Usage

The setup.sh script automates the process of setting up the airflow environment and can be executed as follows (only do this if no airflow server is already configured in the virtual environment):

```bash
./setup.sh
```

The script will ask for credentials to create a user after relevant software is installed. Run the server as shown:

```bash
./run-server.sh
```

Do not close the terminal running the server unless shutting it down is desired: open a new one to keep working on other tasks. Once both of these steps are completed, continue to run the Directed Acyclic Graph (DAG) on the webserver shown by the terminal (http://your_ip:8080/).