# CoralORD: Self-updating software-defined datasets for reproducible ML applications

CoralORD framework ensures that datasets for ML applications are consistently up-to-date and reproducible by automatically managing changes and processing steps.

## CoralORD Data Stack
The `CoralORD` data stack uses Docker to containerize the ML environment, `Croissant` to define dataset metadata and subset descriptors, `DuckDB` for remote file and file-set I/O and managing the dataset metadata catalog, `Python` for scripting and data manipulation, and use `Git` to build a software-defined datasets manager `SDDM` for asynchronous collaboration, integration, and version control. 

The image below shows one-slide overview of the CoralORD project, which was presented at the [SDSC Hackathon 2024](https://sdsc-hackathons.ch/projectPage?projectRef=vUt8BfDJXaAs0UfOesXI|6kJdtOIKKczmbD7QfTSt) at EPFL in Lausanne.
![image](https://github.com/user-attachments/assets/70a7b264-7587-4ca9-8c35-990f0acb7fb8)
 
## CoralORD Characteristics and Associated Technologies:
### 1. Remote Dataset Management
- **Efficient Remote Access**: CoralORD handles large software-defined datasets with remote access capabilities, leveraging `DuckDB` for remote file and file-set I/O and metadata catalog management.
- **Dataset Metadata & Subset Descriptions**: CoralORD uses `Croissant` to define dataset metadata and subset descriptors for structured and scalable data management.

### 2. Automated Ingestion and Environment Setup
- **Automated Data Ingestion**: CoralORD automates the ingestion process using `DuckDB` in `Python` scripts, simplifying data loading and preparation.
- **Environment Deployment**: It automates ML environment setup using `Docker`, ensuring reproducibility by deploying consistent environments for all users.

### 3. Asynchronous Collaboration
- **Collaborative Dataset Management**: CoralORD supports asynchronous collaboration by using `Git` and `SDDM` to enable real-time dataset creation, download, and version control.
- **Version Control**: Datasets and subsets are versioned with `GitHub`, ensuring traceability and synchronization across multiple collaborators.



## Use Cases
sodeda-era4:
huggingface-fmnist: 
