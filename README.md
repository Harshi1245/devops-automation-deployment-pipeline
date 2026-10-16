# DevOps Automation and Deployment Pipeline

A containerized Python Flask application demonstrating Docker image versioning, production-style application serving with Gunicorn, automated testing, code quality checks, health monitoring, and GitLab CI/CD configuration.

## Project Overview

This project demonstrates how to package a Python web application using Docker, run it with Docker Compose, validate it using automated tests and Flake8, and publish versioned images to Docker Hub.

## Features

- REST API built with Python and Flask
- Automated tests using pytest
- Test coverage measurement using pytest-cov
- Code quality checks using Flake8
- Docker image creation using a Dockerfile
- Application serving with Gunicorn inside the Docker container
- Container orchestration using Docker Compose
- Docker health checks
- Docker image versioning and rollback preparation
- Published Docker images on Docker Hub
- GitLab CI/CD pipeline configuration

## Tech Stack

- **Language:** Python
- **Web Framework:** Flask
- **Production WSGI Server:** Gunicorn
- **Testing:** pytest, pytest-cov
- **Code Quality:** Flake8
- **Containerization:** Docker
- **Container Orchestration:** Docker Compose
- **CI/CD:** GitLab CI/CD
- **Version Control:** Git and GitLab
- **Container Registry:** Docker Hub

## Project Structure

```text
devops-automation-deployment-pipeline/
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── .flake8
├── .gitlab-ci.yml
├── validate.bat
└── README.md
```

## Prerequisites

- Python 3.12 or a compatible Python version
- Git
- Docker Desktop with Docker Compose

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://gitlab.com/devangamharshitha14/devops-automation-deployment-pipeline.git
cd devops-automation-deployment-pipeline
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run automated tests

```bash
python -m pytest -v
```

### 4. Run code quality checks

```bash
python -m flake8 app.py test_app.py
```

### 5. Start the application using Docker Compose

```bash
docker compose up -d --build
```

### 6. Check container status

```bash
docker compose ps
```

### 7. Stop the application

```bash
docker compose down
```

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns project information and application status |
| `/health` | Returns the application health status and version |

When running through the supplied Docker Compose configuration, the application is available on port `8081`.

- Home endpoint: http://localhost:8081/
- Health endpoint: http://localhost:8081/health

For version 1.2, the expected health response is:

```json
{
  "status": "healthy",
  "version": "1.2"
}
```

## Docker Hub

Docker images are published to:

**Repository:** https://hub.docker.com/r/harshitha1245/devops-automation

Published tags include:

- `harshitha1245/devops-automation:1.1`
- `harshitha1245/devops-automation:1.2`

Pull version 1.2:

```bash
docker pull harshitha1245/devops-automation:1.2
```

Run the published image:

```bash
docker run -d --name devops-hub-v1-2 -p 8086:5000 harshitha1245/devops-automation:1.2
```

Test the application:

```bash
curl http://localhost:8086/health
curl http://localhost:8086/
```

## Docker Health Monitoring

The Dockerfile defines a health check that periodically sends a request to the application's `/health` endpoint. Docker reports the container as healthy when the check succeeds.

## Docker Image Versioning and Rollback

The project maintains versioned Docker images so earlier releases can remain available if a newer version has problems.

Build version 1.1:

```bash
docker build -t devops-automation:1.1 .
```

Build version 1.2:

```bash
docker build -t devops-automation:1.2 .
```

Version 1.2 uses Gunicorn to serve the Flask application inside the container.

Previously tested images can be run alongside newer versions on different host ports for comparison and verification.

## GitLab CI/CD

The `.gitlab-ci.yml` file configures linting and automated test stages, including a test coverage threshold.

The pipeline configuration is committed to the GitLab repository. Successful execution on GitLab has not yet been confirmed because pipeline execution previously encountered an identity-verification restriction.

## Validation

The local validation script is:

```bat
validate.bat
```

It runs Flake8 and pytest on Windows.

## Future Improvements

- Verify successful GitLab CI/CD pipeline execution
- Add automated deployment to a hosting environment
- Improve application logging and monitoring
- Add container image vulnerability scanning
- Configure automated releases for new image versions

## Author

**Devangam Harshitha**

GitLab: https://gitlab.com/devangamharshitha14

GitHub: https://github.com/Harshi1245

---

This project was developed for hands-on learning and demonstration of DevOps fundamentals.
