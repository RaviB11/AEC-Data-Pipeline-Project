# AEC Project Data Pipeline (Conceptual Project)

## Objective
This project is a self-study initiative to demonstrate the fundamental principles of data engineering by building a simple, automated ETL (Extract, Transform, Load) pipeline for a sample Architecture, Engineering, and Construction (AEC) dataset.
## The Process: ETL

This pipeline follows a standard ETL workflow:

### 1. Extract
The process begins by extracting raw project data from a source system, simulated here by a `projects.csv` file. This raw data contains information about project tasks, timelines, and costs.

### 2. Transform
A Python script (`pipeline.py`) using the Pandas library performs the necessary transformations to clean the data and make it ready for analysis. The key transformation steps include:
* Reading the raw CSV data into a DataFrame.
* Validating data quality by checking for null values.
* Converting date strings into proper datetime objects.
* Engineering a new feature by calculating the `Duration` of each task.
* Saving the cleaned, enriched data into a new CSV file.

### 3. Load
The final step is to load the cleaned data into a target system, such as a data warehouse like Azure Synapse or a SQL database, where it can be used by data analysts and scientists for reporting and modeling.

## Technologies & Concepts Demonstrated
* **Languages:** Python (Pandas), SQL (conceptual)
* **Data Engineering:** ETL/ELT Pipeline Development, Data Modeling Concepts, Data Quality & Validation, Workflow Automation
* **Methodologies:** SDLC, Agile Concepts
* **Cloud Familiarity:** The principles used here are directly applicable to cloud ETL tools like Azure Data Factory and Azure Databricks.

## How to Run
1.  Ensure you have Python and the Pandas library installed.
2.  Clone this repository.
3.  Run the script from your terminal: `python pipeline.py`
4.  A new file named `cleaned_projects.csv` will be created in the directory.
