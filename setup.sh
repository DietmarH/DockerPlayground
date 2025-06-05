#!/bin/bash
set -e

# Clear logfile
rm -f log.txt
touch log.txt

echo "Running tests with docker-compose..."

docker-compose up --abort-on-container-exit --exit-code-from test_content > compose_log.txt 2>&1

echo "View the test results in log.txt"
