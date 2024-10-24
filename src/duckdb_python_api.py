import duckdb
import pandas as pd

pandas_df = pd.DataFrame({"a": [42]})
duckdb.sql("SELECT * FROM pandas_df")

print(duckdb.sql("SELECT * FROM pandas_df").fetchall())


duckdb.read_json("example.json")