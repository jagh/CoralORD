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
# 1. Point to a local or remote Croissant file
import mlcroissant as mlc
url = "https://huggingface.co/api/datasets/fashion_mnist/croissant"

# 2. Inspect metadata
print(mlc.Dataset(url).metadata.to_json())


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