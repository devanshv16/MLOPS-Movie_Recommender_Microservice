# MLOps Movie Recommender Microservice

## CI/CD Pipeline Status

### ✅ Continuous Integration (CI) - Testing & Linting
[![CI Status](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml/badge.svg?job=build-and-test)](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml)

### 🚀 Continuous Deployment (CD) - Docker Image Build & Push
[![CD Status](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml/badge.svg?job=deploy)](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml)

---

## Overview
This is a **containerized machine learning microservice** that provides movie recommendations using the **MovieLens 100k dataset**. The service is built with **FastAPI** and designed for seamless deployment using **Docker** and **GitHub Actions**. The Docker image is publicly available on **Docker Hub**, allowing others to easily pull and run the service.

---

## Tech Stack

### **Machine Learning & Data Processing**
- **scikit-learn** - SVD-based collaborative filtering
- **pandas** - Data preprocessing & manipulation
- **numpy** - Numerical computations

### **API & Backend**
- **FastAPI** - High-performance web framework
- **Uvicorn** - ASGI server for running FastAPI

### **Testing & Code Quality**
- **pytest** - Unit testing framework
- **pytest-cov** - Code coverage
- **black** - Code formatter
- **pylint** - Linter for static code analysis

### **CLI Tool**
- **Fire** - Command-line interface for interacting with the model

### **Deployment & Containerization**
- **Docker** - Containerized application
- **GitHub Actions** - Automated testing & deployment

---

## CI/CD Workflow

### 1️⃣ Code Development & Testing
- Implement the recommender system
- Run tests using `pytest`
- Maintain code quality with `black` and `pylint`

### 2️⃣ CI/CD Automation
- Push code to GitHub
- GitHub Actions runs automated tests
- Build & push the Docker image to Docker Hub

### 3️⃣ Containerization & Deployment
- The Docker image is created and stored in **Docker Hub**
- Future deployment plans: **AWS/GCP/Kubernetes**

---

## Getting Started

### Clone the repository
```bash
git clone https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice.git
cd MLOPS-Movie_Recommender_Microservice
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run tests
```bash
pytest
```

### Start the FastAPI server
```bash
uvicorn app.main:app --reload
```

---

## Running with Docker

The Docker image for this service is publicly available on **Docker Hub**. You can pull and run the container using the following commands:

### Pull the image from Docker Hub
```bash
docker pull devanshv16/mlops-movie-recommender:latest
```

### Run the container
```bash
docker run -p 8000:8000 devanshv16/mlops-movie-recommender
```

This will start the FastAPI server on `http://localhost:8000`.

---

## Future Enhancements
- Automate Docker builds in GitHub Actions
- Improve hyperparameter tuning for better recommendations
- Deploy using AWS Lambda or Kubernetes
- Implement hybrid collaborative + content-based filtering

