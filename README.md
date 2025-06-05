# Docker Playground: Automated API Testing with Docker Compose

This project demonstrates how to use Docker and Docker Compose to automate the testing of a REST API using Python scripts. It is designed for educational and practical purposes, showing how to structure, run, and log API tests in a containerized environment.

## Project Structure

- `Dockerfile` — Builds a Python image with all dependencies for running the test scripts.
- `docker-compose.yml` — Defines multiple services for different test scripts, each running in its own container.
- `setup.sh` — Helper script to build images, run tests, and manage logs.
- `test_authentication.py` — Tests user authentication against the API.
- `test_authorization.py` — Tests user authorization for different API endpoints and versions.
- `test_content.py` — Tests the sentiment analysis content of the API.
- `log.txt` — Aggregated log file for test results (mounted from containers).
- `compose_log.txt` — Output from Docker Compose runs.

## How the Testing Works

All tests are executed using a single Docker image, which is built from the provided `Dockerfile`. This image contains all the required Python scripts for the three different tests:

- `test_authentication.py`
- `test_authorization.py`
- `test_content.py`

In the `docker-compose.yml`, three separate containers are created from this one image. Each container runs a different test script by specifying the appropriate command (`CMD`) for that container. This approach ensures consistency, reduces image build time, and makes it easy to add or modify tests in the future—just update the scripts in the image and adjust the service commands as needed.

## Usage

1. **Build and Run Tests**
   ```bash
   ./setup.sh
   ```
   This script will:
   - Build the Docker image for tests
   - Remove any old logs
   - Run all test services and the API via Docker Compose
   - Save test results to `log.txt`
   - Automatically stop all containers (including the API) when tests finish

   Alternatively, you can run Docker Compose directly:
   ```bash
   docker-compose up --abort-on-container-exit --exit-code-from test_content
   ```
   This will stop all services when the last test finishes.

2. **View Results**
   - Check `log.txt` for a summary of all test results.
   - Check `compose_log.txt` for full container output and troubleshooting.

## Customization

- To add new tests, create a new Python script and add a service in `docker-compose.yml` using the same image but a different command.
- To change the API address, update the `api_address` variable in the test scripts to use `http://api:8000` (the Docker Compose service name and port).

## Notes & Best Practices
- Test scripts use environment variables and mounted volumes to report results back to the host system.
- The test containers communicate with the API using the service name `api` (the name given to the service in the docker-compose.yaml).

## License

The Unlicense. See `LICENSE` for details.
