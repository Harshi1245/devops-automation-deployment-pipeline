# DevOps Automation and Deployment Pipeline

A containerized Python Flask application demonstrating automated testing, Docker containerization, health monitoring, and GitLab CI/CD configuration.

## Project Overview

This project demonstrates how to package a Python web application using Docker, run it with Docker Compose, verify its functionality with automated tests, and configure a GitLab CI/CD pipeline.

## Features

- REST API built with Python and Flask
- Automated unit tests using pytest
- Docker image creation using a Dockerfile
- Container orchestration using Docker Compose
- Docker health checks for application monitoring
- `.dockerignore` to exclude unnecessary files from the build context
- GitLab CI/CD pipeline configuration

## Tech Stack

- **Language:** Python
- **Web Framework:** Flask
- **Testing:** pytest
- **Containerization:** Docker
- **Container Orchestration:** Docker Compose
- **CI/CD Configuration:** GitLab CI/CD
- **Version Control:** Git and GitLab

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
├── .gitlab-ci.yml
└── README.md
```

## Prerequisites

Install the following tools:

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

The current test suite contains two tests covering the home endpoint and health endpoint. Both tests have passed locally.

### 4. Start the Docker application

```bash
docker compose up -d --build
```

### 5. Check container status

```bash
docker compose ps
```

### 6. Stop the application

```bash
docker compose down
```

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns project information and application status |
| `/health` | Returns the application health status |

When running through the supplied Docker Compose configuration, the application is available on port `8081`.

- Home endpoint: http://localhost:8081/
- Health endpoint: http://localhost:8081/health

Expected health response:

```json
{
  "status": "healthy"
}
```

## Docker Health Monitoring

The Dockerfile defines a health check that periodically sends a request to the application's `/health` endpoint. Docker reports the container as healthy when the check succeeds.

## GitLab CI/CD

The `.gitlab-ci.yml` file defines a test stage that installs the Python dependencies and runs pytest.

**Note:** A successful local test run does not guarantee that the GitLab pipeline has run. Pipeline execution requires GitLab to accept the configuration and provide an eligible runner.

## Future Improvements

- Enable a working CI/CD runner and verify pipeline execution
- Add code quality checks and linting
- Publish the Docker image to a container registry
- Add automated deployment to a hosting environment
- Add application logging and monitoring

## Author

**Devangam Harshitha**

GitLab: https://gitlab.com/devangamharshitha14

---

This project is developed for hands-on learning and demonstration of DevOps fundamentals.