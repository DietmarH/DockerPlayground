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

## Prerequisites

- **The API server is running**
- The API server image `datascientest/fastapi:1.0.0` (or compatible) available. You can pull and run it with:
  ```bash
  docker pull datascientest/fastapi:1.0.0
  docker run -d -p 8000:8000 datascientest/fastapi:1.0.0
  ```

## Usage

1. **Build and Run Tests**
   ```bash
   ./setup.sh
   ```
   This script will:
   - Build the Docker image for tests
   - Remove any old logs
   - Run all test services via Docker Compose
   - Save test results to `log.txt`

2. **View Results**
   - Check `log.txt` for a summary of all test results.
   - Check `compose_log.txt` for full container output and troubleshooting.

## Customization

- To add new tests, create a new Python script and add a service in `docker-compose.yml` using the same image but a different command.
- To change the API address, update the `api_address` variable in the test scripts.

## Notes & Best Practices
- Test scripts use environment variables and mounted volumes to report results back to the host system.
- For enhanced security and portability, consider configuring Docker networking instead of relying on the host network.

## License

The Unlicense. See `LICENSE` for details.
