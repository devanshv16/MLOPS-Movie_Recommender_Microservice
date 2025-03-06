# MLOPS-Movie_Recommender_Microservice

### CI/CD Pipeline Status

#### ✅ CI (Testing & Linting)
[![CI Status](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml/badge.svg?job=build-and-test)](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml)

#### 🚀 CD (Docker Deployment)
[![CD Status](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml/badge.svg?job=deploy)](https://github.com/devanshv16/MLOPS-Movie_Recommender_Microservice/actions/workflows/main.yml)

## Overview
This is a **containerized machine learning microservice** that provides movie recommendations using the **MovieLens 100k dataset**. The service is built with **FastAPI** and designed to be deployed as a Docker container.

## Tech Stack
### **Machine Learning & Data Processing**
- **scikit-learn** – Collaborative filtering, SVD for recommendations
- **pandas** – Data handling and preprocessing
- **numpy** – Numerical computations

### **API & Backend**
- **FastAPI** – Lightweight and fast web framework
- **Uvicorn** – ASGI server for running FastAPI

### **Testing & Code Quality**
- **pytest** – Unit testing
- **pytest-cov** – Code coverage
- **pylint** – Code linting
- **black** – Code formatting
- **flake8** – Linting support
- **mypy** – Static type checking

### **CLI Tool**
- **Click** – Command-line interface for interacting with the model

### **Deployment & Containerization**
- **Docker** – Containerizing the application
- **GitHub Actions** – Automating testing in CI/CD pipeline

## Workflow
1. **Develop & Test Locally**
   - Implement the movie recommender system.
   - Write unit tests with `pytest`.
   - Use `pylint` and `black` to maintain code quality.

2. **Version Control & CI/CD**
   - Push code to GitHub.
   - GitHub Actions automatically runs tests on push.

3. **Containerization**
   - Build a Docker image manually.
   - Run and test the container locally.

4. **Future Deployment (Not Implemented Yet)**
   - Push the Docker image to a container registry.
   - Deploy on AWS/GCP/Azure.

## Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-microservice.git
   cd movie-recommendation-microservice
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   pytest
   ```

4. **Run FastAPI application locally:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Future Enhancements
- Automate Docker build in GitHub Actions
- Deploy using AWS Lambda or Kubernetes
- Implement user-based and item-based collaborative filtering

