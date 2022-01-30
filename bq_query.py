import os
from google.cloud import bigquery

key_path = 'PATH TO THE KEY FILE YOU DOWNLOADED'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path


client = bigquery.Client()
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
