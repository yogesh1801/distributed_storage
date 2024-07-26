
# Distributed Large Text Summarization with GKE and MinIO

This project implements a distributed system for summarizing large text files using Google Kubernetes Engine (GKE), a distributed MinIO setup for file storage, and a Large Language Model (LLM) for summarization.

## System Architecture

1. **File Storage**: Distributed MinIO cluster (4 instances) running on GKE
2. **Processing**: Distributed Python script running on GKE
3. **Summarization**: Large Language Model (BART)

## Workflow

1. Files are uploaded to the distributed MinIO storage.
2. Python scripts retrieve files from MinIO for processing.
3. The LLM summarizes the content.
4. Summarized content is uploaded back to MinIO.

## Setup Instructions

### Prerequisites

- Google Cloud Platform account with GKE enabled
- kubectl installed and configured
- Python 3.7+
- Helm (for MinIO deployment)

### GKE Cluster Setup

1. Create a GKE cluster: 
```sh
gcloud container clusters create minio-llm-cluster \
    --num-nodes=2 \
    --zone=us-central1-a \
    --machine-type=e2-standard-4
```

2. Pull the GKE credentials
```sh
gcloud container clusters get-credentials minio-llm-cluster --zone us-central1-a
```

3. Use helm to configure minio

```sh
helm repo add minio https://charts.min.io/
helm repo update
helm install minio minio/minio -f minio-values.yaml
```

4. Get the Access Key, Secret Key and Cluster IP
```sh
kubectl get secret minio -o jsonpath="{.data.rootUser}" | base64 --decode

kubectl get secret minio -o jsonpath="{.data.rootPassword}" | base64 --decode

export MINIO_ENDPOINT=$(kubectl get services minio -o jsonpath="{.status.loadBalancer.ingress[0].ip}")
```

### Project Setup

1. Create virtual environment
```sh
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

2. install the require packages

```sh
pip install -r requirements.txt
```

3. Run the App
```sh
## Place the content into "article.txt"
python app.py
```

## Future Improvements

- Implement auto-scaling based on workload
- Add data replication and backup strategies
- Implement a queue system for better task distribution