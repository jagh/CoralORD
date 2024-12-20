  "descriptor": {
    "metadata": {
      "name": "zalando-datasets/fashion_mnist/Pullover",
      "train_url": "https://huggingface.co/datasets/coralord/fashion_mnist/resolve/refs%2Fconvert%2Fparquet/fashion_mnist/train/Pullover/0000.parquet",,
			"test_url": "https://huggingface.co/datasets/coralord/fashion_mnist/resolve/refs%2Fconvert%2Fparquet/fashion_mnist/test/Pullover/0000.parquet",
      "files": {
      "distribution": [
		    {
		      "@type": "cr:FileObject",
		      "@id": "repo",
		      "name": "repo",
		      "description": "The Hugging Face git repository.",
		      "contentUrl": "https://huggingface.co/datasets/coral/fashion_mnist/tree/refs%2Fconvert%2Fparquet",
		      "encodingFormat": "git+https",
		      "sha256": "https://github.com/mlcommons/croissant/issues/80"
		    },
		    {
		      "@type": "cr:FileSet",
		      "@id": "parquet-files-for-config-fashion_mnist",
		      "name": "parquet-files-for-config-fashion_mnist",
		      "description": "The underlying Parquet files as converted by Hugging Face",
		      "containedIn": {
		        "@id": "repo"
		      },
		      "encodingFormat": "application/x-parquet",
		      "includes": "fashion_mnist/Pullover/*.parquet"
		    }
		  ],
		  }
      "pipeline": "hf_descriptor_fashion_mnist.py",
      "docker": "duckdb-docker"
    }
  }
}
