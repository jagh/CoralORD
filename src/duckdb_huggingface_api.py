
import duckdb
import pandas as pd
import os
import glob
import json

########################################
## Uncomment the following lines to debug the DuckDB server
########################################
## Checking that duckdb is running
pandas_df = pd.DataFrame({"a": [42]})
duckdb.sql("SELECT * FROM pandas_df")
print(duckdb.sql("SELECT * FROM pandas_df").fetchall())

# ########################################
# ## Checking that the data descriptor JSON files can be read using the
# if os.path.exists("/coralord/src/data/descriptorExample1.json"):
#     duckdb.read_json("/coralord/src/data/descriptorExample1.json")
#     ## Directly read a JSON file from within SQL:
#     print(duckdb.sql("SELECT * FROM '/coralord/src/data/descriptorExample1.json'").fetchall())
#     ## Call read_json from within SQL:
#     print(duckdb.sql("SELECT * FROM read_json_auto('/coralord/src/data/descriptorExample1.json')").fetchall())
# else:
#     print("File not found")
# ########################################


########################################
########################################
## httpfs Extension for HTTP and S3 Support
## Tutorial -> Access 150k+ Datasets from Hugging Face with DuckDB

## Create a connection to DuckDB and install and load the httpfs extension to allow reading and writing remote files:

url = "https://huggingface.co/datasets/blog_authorship_corpus/resolve/refs%2Fconvert%2Fparquet/blog_authorship_corpus/blog_authorship_corpus-train-00000-of-00002.parquet"

con = duckdb.connect()
con.execute("INSTALL httpfs;")
con.execute("LOAD httpfs;")


## For example, to read a CSV file, you can use the following query:
print(duckdb.sql("SELECT * FROM 'hf://datasets/datasets-examples/doc-formats-csv-1/data.csv';").fetchall())

## To read a JSONL file, you can run
print(duckdb.sql("SELECT * FROM 'hf://datasets/datasets-examples/doc-formats-jsonl-1/data.jsonl';").fetchall())

## Finally, for reading a Parquet file, use the following query:
print(duckdb.sql("SELECT * FROM 'hf://datasets/datasets-examples/doc-formats-parquet-1/data/train-00000-of-00001.parquet';").fetchall())


## Real dataset

print(duckdb.sql("SELECT * FROM 'hf://huggingface.co/datasets/deepsynthbody/deepfake_ecg_full_train_validation_test/train/0';").fetchall())
