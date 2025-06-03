#!/bin/bash
set -e

echo "Expecting that the api server is running and listening on port 8000"
echo " If not, wou can get the image and run the server with the following commands:"
echo "docker image pull datascientest/fastapi:1.0.0"
echo "docker container run -p 8000:8000 datascientest/fastapi:1.0.0"


echo "Building Docker image..."
docker build -t tests_image .

# Clear logfile
rm -f log.txt
touch log.txt

echo "Running tests with docker-compose..."

docker-compose up > compose_log.txt 2>&1

echo "View the test results in log.txt"
