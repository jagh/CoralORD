# CoralORD: Self-updating software-defined datasets for reproducible ML applications

CoralORD framework ensures that datasets for ML applications are consistently up-to-date and reproducible by automatically managing changes and processing steps

1. **Software-Defined Configuration**
    - **Dataset metadata & subset description**: The system maintains detailed metadata and descriptor information about datasets and subsets, defining the content and structure.
    - **Data processing pipeline**: A flexible and adaptable data processing pipeline is part of the system configuration.
2. **Self-Updating Mechanism**
    - **Metadata descriptor & catalog of datasets/subsets**: Metadata and catalog define and track available datasets and their subsets.
    - **Automatic updates**: The system is designed to automatically update itself when new subsets of datasets are added or when changes occur in the processing pipeline.
    - **Dataset version control:**
    - Github
        - **Dataset & Subset publishing**: The system enables the publication of dataset subsets based on these metadata descriptions.
3. **On-Demand Data Access**
    - **Efficient data fetching**: The system fetches and processes data only when it is needed, optimizing resource use.
    - **Subset downloading**: Only specific files or subsets that are described in the subset descriptor are downloaded, reducing unnecessary data transfer.
4. **Collaboration & Synchronization**
    - **Docker-based environment selection**: Users have the option to select their Docker images to synchronize the execution environment across collaborators.
