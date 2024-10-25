# CoralORD: Self-updating software-defined datasets for reproducible ML applications

CoralORD framework ensures that datasets for ML applications are consistently up-to-date and reproducible by automatically managing changes and processing steps.

## CoralORD Data Stack
The `CoralORD` data stack uses Docker to containerize the ML environment, `Croissant` to define dataset metadata and subset descriptors, `DuckDB` for remote file and file-set I/O and managing the dataset metadata catalog, `Python` for scripting and data manipulation, and use `Git` to build a software-defined datasets manager `SDDM` for asynchronous collaboration, integration, and version control. The image below shows one-slide overview of the CoralORD project presented at the SDSC Hackathon on October 24–25, 2024, at EPFL, Lausanne.
![image](https://github.com/user-attachments/assets/4807fe38-080b-4587-8864-550fc10f6ece)
 
## CoralORD Characteristics and Associated Technologies:
1. **Software-Defined Configuration**
- **Dataset Metadata & Subset Descriptions:** CoralORD uses the `Croissant` metadata format to define dataset descriptors, extended to include `Dockerfile` environment configurations and the ML pipeline.
- **Flexible Data Pipeline:** CoralORD’s data pipeline is defined using `Python` and integrated with `DuckDB` to support flexible data transformations and processing.

2. **Self-Updating Mechanism**
- **Metadata Catalog:** CoralORD manages the metadata catalog using `DuckDB` and `SDDM`, enabling fast querying and tracking of datasets and subsets.
- **Automatic Updates:** The system leverages Croissant to automatically detect and update the metadata when new datasets, subsets, or changes in the pipeline are introduced.

3. Software-Defined Dataset Version Control
- **GitHub Integration:** CoralORD uses `Git` and `GitHub` for version control of datasets, ensuring metadata and dataset subsets are tracked and versioned.
- **On-Demand Data Access:** CoralORD uses `DuckDB` for efficient querying and `Python` for fetching and processing data on-demand. Subsets are downloaded based on Croissant-defined descriptors, reducing unnecessary data transfer.

4. Collaboration & Synchronization
- **Docker-Based Environments:** CoralORD utilizes `Docker` to allow users to select pre-configured images, ensuring consistency across collaborators’ environments and synchronizing execution for reproducibility.


sddm
duckdb conector
docker


## Use Cases
sodeda-era4:
huggingface-fmnist: 
