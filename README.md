# 📝 FastAPI ToDo App with Docker, Kubernetes & Argo CD

This is a simple and scalable ToDo API built with Python FastAPI, containerized using Docker, deployed on Kubernetes.

## 🔧 Tech Stack
- 🐍 Python FastAPI – Lightweight, high-performance REST API

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
- Create, read, update, delete ToDo items

- RESTful API endpoints

- Dockerized for easy container - deployment

- Kubernetes manifests for scalable deployment

## 📦 Setup (Locally with Docker)
```bash
docker compose up
```

Access the app at: http://localhost:8000

## ☸️ Deploy on Kubernetes (Minikube / Cluster)
```bash
kubectl apply -k kustomization/
```

## 📄 API Documentation
FastAPI auto-generates:

- Swagger UI: http://\<host\>:\<port\>/docs

## ✅ Todo 
- [ ] ARGO CD
- [ ] GitHub Actions for CI
- [ ] Helm
