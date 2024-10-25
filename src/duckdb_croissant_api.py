import duckdb
import mlcroissant as mlc


##############################################################
## Testing croissant 
##############################################################
# from mlcroissant import Dataset
# # The Croissant metadata exposes the first 5GB of this dataset
# ds = Dataset(jsonld="https://huggingface.co/api/datasets/deepsynthbody/deepfake_ecg_full_train_validation_test/croissant")
# records = ds.records("default")

# print(records)

# # Create a DuckDB in-memory connection
# con = duckdb.connect()

# # Register the records as a DuckDB table
# con.register("dataset_table", records)

# # Query the metadata from the dataset
# metadata_query = """
# SELECT * FROM dataset_table LIMIT 10;
# """

# # Run the query
# result = con.execute(metadata_query).fetchdf()

# print(result)


###############################################
# # The Croissant metadata exposes the first 5GB of this dataset
# ds = Dataset(jsonld="https://huggingface.co/api/datasets/deepsynthbody/deepfake_ecg_full_train_validation_test/croissant")
# records = ds.records("default")


###############################################
## Loading an example dataset:
# ds = mlc.Dataset("https://raw.githubusercontent.com/mlcommons/croissant/main/datasets/1.0/gpt-3/metadata.json")
# metadata = ds.metadata.to_json()

# print(f"{metadata['name']}: {metadata['description']}")
# # for x in ds.records(record_set="default"):
# #     print(x)


###############################################
## Use it in your ML workflow:
import mlcroissant as mlc
import tensorflow_datasets as tfds

## 1. Point to the Croissant file
url = "https://huggingface.co/api/datasets/fashion_mnist/croissant"
ds = mlc.Dataset(url)
metadata = ds.metadata.to_json()

## 2. Print basic information
print(f"{metadata['name']}: {metadata['description']}")

## 3. Inspect the distribution
print("Distribution inspect", metadata['distribution'])
for item in metadata['distribution']:
    if 'contentUrl' in item:
        print(f"{item['@type']} -> contentUrl: {item['contentUrl']}, encodingFormat: {item['encodingFormat']}")

## 4. Get the correct record set ID from metadata
record_set_id = metadata['recordSet'][0]['@id']  # Should be "fashion_mnist"
print(f"Using record set ID: {record_set_id}")


## 5. Print all available record sets to make sure we're using the correct ID
for record_set in metadata['recordSet']:
    print(f"Available record set: {record_set['@id']}")


####################################################################
## Read the records from the dataset using DuckDB

# 1. Setup DuckDB
con = duckdb.connect()
con.execute("INSTALL httpfs;")
con.execute("LOAD httpfs;")

# 2. Define the working URLs for train and test sets
train_url = "https://huggingface.co/datasets/zalando-datasets/fashion_mnist/resolve/refs%2Fconvert%2Fparquet/fashion_mnist/train/0000.parquet"
test_url = "https://huggingface.co/datasets/zalando-datasets/fashion_mnist/resolve/refs%2Fconvert%2Fparquet/fashion_mnist/test/0000.parquet"

# 3. Query the data
try:
    # Count records in training set
    train_count_query = f"""
    SELECT COUNT(*) AS train_count
    FROM read_parquet('{train_url}');
    """
    print("Training set count:", duckdb.sql(train_count_query).fetchall())

    # Count records in test set
    test_count_query = f"""
    SELECT COUNT(*) AS test_count
    FROM read_parquet('{test_url}');
    """
    print("Test set count:", duckdb.sql(test_count_query).fetchall())

    # # Get sample of data with all columns
    # sample_query = f"""
    # SELECT *
    # FROM read_parquet('{train_url}')
    # LIMIT 5;
    # """
    # print("\nSample data:")
    # print(duckdb.sql(sample_query).fetchall())

    # Get label distribution
    label_dist_query = f"""
    SELECT 
        label,
        COUNT(*) as count,
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM read_parquet('{train_url}')) as percentage
    FROM read_parquet('{train_url}')
    GROUP BY label
    ORDER BY label;
    """
    print("\nLabel distribution:")
    print(duckdb.sql(label_dist_query).fetchall())

except Exception as e:
    print(f"Error: {e}")

# try:
#     # Image statistics query
#     image_stats_query = f"""
#     SELECT 
#         MIN(image) as min_pixel_value,
#         MAX(image) as max_pixel_value,
#         AVG(image) as avg_pixel_value
#     FROM read_parquet('{train_url}')
#     LIMIT 1000;  -- Limiting to 1000 images for faster computation
#     """
#     print("\nImage statistics:")
#     print(duckdb.sql(image_stats_query).fetchall())
# except Exception as e:
#     print(f"Error: {e}")

    
# # Then use the correct ID in the builder
# builder = tfds.core.dataset_builders.CroissantBuilder(
#     jsonld=url,
#     record_set_ids=['fashion_mnist'],  # Use the correct ID
#     file_format='array_record',
# )

# ## 5. Create the builder with correct record set ID
# builder = tfds.core.dataset_builders.CroissantBuilder(
#     jsonld=url,
#     record_set_ids=[record_set_id],  # Use "fashion_mnist" instead of "record_set_fashion_mnist"
#     file_format='array_record',
# )

# # 6. Download and prepare the dataset
# builder.download_and_prepare()

# # 7. Split for training/testing
# train, test = builder.as_data_source(split=['default[:80%]', 'default[80%:]'])







###########################################
## Todo:
## 1. Read the records from the dataset
## 2. Use duckdb to read the records from the dataset
## 3. Use duckdb to query and downloading a subset of the dataset

# # Create a DuckDB in-memory connection
# con = duckdb.connect()
# con.execute("INSTALL httpfs;")
# con.execute("LOAD httpfs;")

## 2. Use duckdb to read the Parquet file from the dataset
# print(duckdb.sql("SELECT * FROM 'hf://datasets/datasets-examples/doc-formats-parquet-1/data/train-00000-of-00001.parquet';").fetchall())
# print(duckdb.sql("SELECT * FROM 'hf://datasets/zalando-datasets/fashion_mnist/train/*.parquet'';").fetchall())




# # Register the records as a DuckDB table
# con.register("dataset_table", records)

# # Query the metadata from the dataset
# metadata_query = """
# SELECT * FROM dataset_table LIMIT 10;
# """






# # for x in ds.records(record_set="default"):
# for x in ds.records(record_set='"record_set_fashion_mnist"'):
#     print(x)

# # 3. Use Croissant dataset in your ML workload
# import tensorflow_datasets as tfds
# builder = tfds.core.dataset_builders.CroissantBuilder(
#     jsonld=url,
#     record_set_ids=["record_set_fashion_mnist"],
#     file_format='array_record',
# )
# builder.download_and_prepare()
# # 4. Split for training/testing
# train, test = builder.as_data_source(split=['default[:80%]', 'default[80%:]'])