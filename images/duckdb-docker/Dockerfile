# Base image for both architectures
FROM ubuntu:24.10 AS base
ARG DUCKDB_VERSION=v1.0.0

# Install dependencies and download the DuckDB CLI
RUN apt-get update \
    && apt-get install -y curl unzip python3 python3-pip \
    && curl -L -o duckdb_cli.zip "https://github.com/duckdb/duckdb/releases/download/${DUCKDB_VERSION}/duckdb_cli-linux-amd64.zip" \
    && unzip duckdb_cli.zip \
    && rm duckdb_cli.zip

# Install Python dependencies with --break-system-packages flag
RUN pip3 install duckdb pandas --break-system-packages

# Remove or comment out the entry point for DuckDB CLI
# ENTRYPOINT [ "/duckdb" ]
