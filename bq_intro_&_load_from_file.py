### After that you enabled API for your project,
### Created a service account and grant it a role,
### created a key and downloaded the json file,
### all you need to do now is

### 1, export the GOOGLE_APPLICATION_CREDENTIALS variable to the path where the key is living.
import os
key_path = '/Users/saryashawa/Downloads/sarya-sandbox-0586faea03aa.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

### 2. import the library
from google.cloud import bigquery


### 3. Initialize a client to authenticate and connect to the BigQuery API.
client = bigquery.Client()

### From here, you can basically start sending different commands.
### --------------------------------------------------------------- ###
### --------------------------------------------------------------- ###

### The following is a couple of examples about commands you can do.

### how to run a query and store results!
query = """
SELECT
  CONCAT(
    'https://stackoverflow.com/questions/',
    CAST(id as STRING)) as url,
  view_count
FROM `bigquery-public-data.stackoverflow.posts_questions`
WHERE tags like '%google-bigquery%'
ORDER BY view_count DESC
LIMIT 10
"""
query_job = client.query(query)
results = query_job.result()


### How to load data
### Start with initiating some important variables
table_id =  'sarya-sandbox.dataset_test.loaded_via_py'
job_config = bigquery.LoadJobConfig(
    ### Use the line below if you want to overwrite an existing table
    #write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    autodetect = True,
    skip_leading_rows = 1,
    source_format = bigquery.SourceFormat.CSV,
    )
csv_file_path = '/Users/saryashawa/Documents/sandbox/bigquery/export_order_2022_01_30_16_05_45.csv'

### The loading command is here
with open(csv_file_path,'rb') as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config = job_config)
    job.result()

### To retrieve information about a table
loaded_table = client.get_table(table_id)
print(
    "Loaded {} rows and {} columns to {}".format(
        loaded_table.num_rows, len(loaded_table.schema), table_id
    )
)
