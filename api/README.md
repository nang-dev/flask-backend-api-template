# [🛒.ai]: Backend API

### 🛠️ Directory Structure

```
   api                      # API related code
    ├── Dockerfile           # Dockerfile for the API
    ├── README.md            # README for the API
    ├── __init__.py          # API package initialization
    ├── app                  # Main application package
    │   ├── __init__.py      # App package initialization
    │   ├── ai               # AI-related services
    │   │   ├── ai_service.py
    │   │   ├── image
    │   │   │   └── image_service.py
    │   │   ├── shopping
    │   │   │   └── shopping_service.py
    │   │   └── video
    │   │       └── video_service.py
    │   ├── config.py        # Configuration file
    │   ├── data
    │   │   └── database_service.py # Database service
    │   ├── entry
    │   │   ├── __init__.py
    │   │   └── entry_service.py # All endpoints will enter here to be triaged to the appropriate path
    │   ├── health
    │   │   ├── __init__.py
    │   │   └── health_service.py # Health check service
    │   ├── routes.py        # Route definitions
    │   └── utils            # Utility functions and classes
    ├── main.py              # Main entry for running the API
    ├── requirements.txt     # Required Python packages
    ├── swagger.json         # Swagger specification
    └── tests                # Test package
        ├── __init__.py      # Test package initialization
        ├── conftest.py      # Pytest configuration
        └── test_routes.py   # Tests for the routes
```

## 🧭 How To Run (Containerized - RECOMMENDED)

1. ```sh
   docker image build -t flask_docker .
   ```

2. ```sh
   docker run -d -p 8000:8000 flask_docker
   ```

3. Trigger endpoints with:
   ```sh
   curl -X 'GET' \
   'http://127.0.0.1:8000/health'
   -H 'accept: application/json'
   ```

4. Run tests with:
   ```sh
   docker exec <container_id> pytest -p no:warnings
   ```

## 🧭 How To Run (Local)

1. ```sh
   cd api
   ```

2. ```sh
   pip install -r requirements.txt
   ```

3. ```sh
   python main.py
   ```

4. Trigger endpoints with:
   ```sh
   curl -X 'GET' \
   'http://127.0.0.1:8000/health'
   -H 'accept: application/json'
   ```

5. Run tests with:
   ```sh
   python -m pytest -p no:warnings
   ```

## CI/CD + Dev Notes

### Python Version and Code Style
- Using **Python 3.7** for development.
- Code formatting is handled by [**black**](https://black.readthedocs.io/en/stable/), a code formatter that enforces PEP 8 style guide.
- Linting is done with [**flake8**](https://flake8.pycqa.org/en/latest/), which helps to identify coding errors and maintain code quality.

### Pre-commit Hooks
- The project uses [**pre-commit**](https://pre-commit.com/) to manage and maintain pre-commit hooks.
- Run `pre-commit install` to install pre-commit formatting and linting. This ensures that every commit adheres to the code style guide and passes linting checks.
- You can manually run all pre-commit hooks on a repository with `pre-commit run --all-files`.
