# 📝 FastAPI ToDo App with Docker, Kubernetes & Argo CD

This is a simple and scalable ToDo API built with Python FastAPI and PostgreSQL for storage, containerized using Docker, deployed on Kubernetes.

## 🔧 Tech Stack
- 🐍 Python FastAPI – Lightweight, high-performance REST API

- 🐘 PostgreSQL – Relational database for persistent ToDo storage

- 🐳 Docker – Containerization for easy deployment

- ☸️ Kubernetes – Container orchestration

## 📂 Project Structure

```bash
.
├── src/
│   ├── main.py              # App code starting point
│   ├── Dockerfile           # Docker setup for the app
│   └── requirements.txt
├── kustomization/           # Kubernetes deployment and service YAMLs
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

## 🔁 Argo CD
```
argocd app create fast-api-rest-prod \
--repo https://github.com/soumiknandi/fast-api-rest.git \
--path kustomization/overlays/prod \
--dest-server https://kubernetes.default.svc \
--dest-namespace fast-api-rest-prod \
--sync-option CreateNamespace=true \
--sync-policy automated
```

## 📄 API Documentation
FastAPI auto-generates:

- Swagger UI: http://\<host\>:\<port\>/docs

## ✅ Todo 
- [X] ARGO CD
- [ ] GitHub Actions for CI
- [ ] Helm
