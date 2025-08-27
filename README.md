# 📝 FastAPI ToDo App with Docker, Kubernetes & Argo CD

This is a simple and scalable ToDo API built with Python FastAPI and PostgreSQL for storage, containerized using Docker, deployed on Kubernetes.

## 🔧 Tech Stack
- 🐍 Python FastAPI – Lightweight, high-performance REST API

- 🐘 PostgreSQL – Relational database for persistent ToDo storage

- 🐳 Docker – Containerization for easy deployment

- ☸️ Kubernetes – Container orchestration

- 🚀 Argo CD – GitOps-based continuous delivery

- 🛠️ Helm – Kubernetes manifest templating

## 📂 Project Structure

```bash
.
├── src/
│   ├── main.py              # App code starting point
│   ├── Dockerfile           # Docker setup for the app
│   └── requirements.txt
├── .github/                 # GitHub Actions folder
├── kustomization/           # Kubernetes deployment and service YAMLs
├── helm/                    # Helm charts
├── docker-compose/          # Docker compose file for the app
├── README.md
```

## 🚀 Features
- RESTful API endpoints for create, read, update, delete ToDo items

- Persistent storage using PostgreSQL

- Dockerized for easy local and cloud deployment

- Kubernetes manifests for both API and DB

- Auto-generated Swagger UI documentation

## 📦 Setup (Locally with Docker)
```bash
docker compose up
```

Access the app at: http://localhost:8000

## ☸️ Deploy on Kubernetes (Minikube / Cluster)
```bash
kubectl apply -k kustomization/overlays/dev
```

## 🚀 Argo CD

Use below command to run using ARGO CD or via GUI.

```
argocd app create fast-api-rest-prod \
--repo https://github.com/soumiknandi/fast-api-rest.git \
--path kustomization/overlays/prod \
--dest-server https://kubernetes.default.svc \
--dest-namespace fast-api-rest-prod \
--sync-option CreateNamespace=true \
--sync-policy automated
```

## 🛠️ Helm

Steps to follow

- Run helm package command

    ```bash
    cd helm
    helm dependency update fastapi-postgres
    ```

- Run below command from project root based on the environment

    - Base

        ```bash
        helm install release-fast-api helm/ --values helm/values.yaml -n fast-api-rest --create-namespace
        ```

    - Dev

        ```bash
        helm install release-fast-api helm/ --values helm/values.yaml -f helm/values-dev.yaml -n fast-api-rest-dev --create-namespace
        ```

    - Prod

        ```bash
        helm install release-fast-api helm/ --values helm/values.yaml -f helm/values-prod.yaml -n fast-api-rest-prod --create-namespace
        ```

## 📄 API Documentation
FastAPI auto-generates:

- Swagger UI: http://\<host\>:\<port\>/docs

## ✅ Todo 
- [X] ARGO CD
- [X] GitHub Actions for CI
- [X] Helm
