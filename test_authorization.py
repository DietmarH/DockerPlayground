import os
import requests

# API address and port (use 'localhost' for host networking, or service name in Docker Compose networks)
api_address = 'localhost'
api_port = 8000


def test_authorization(user, version):
    """
    Sends a GET request to the /<version>/sentiment endpoint with the given user's credentials.
    Returns a formatted string with the test result and prints it.
    """
    r = requests.get(
        url=f'http://{api_address}:{api_port}/{version}/sentiment',
        params={
            'username': user['username'],
            'password': user['password'],
            'sentence': '',  # Empty sentence to test permissions
        }
    )

    # Prepare output for this test case
    expected_status = user[f'expected_status_code_{version}']
    output = f'''
request done at "/{version}/sentiment"
| username="{user['username']}"
| password="{user['password']}"
| sentence=""
expected result = {expected_status}
actual result = {r.status_code}
==>  {'PASSED' if r.status_code == expected_status else 'FAILED'}
'''
    print(output)
    return output



# Summary header for the test log
summary = '''
============================
    Authorization test
============================
'''

# List of users to test, with expected status codes for each API version
users = [
    {
        'username': 'alice',
        'password': 'wonderland',
        'expected_status_code_v1': 200,
        'expected_status_code_v2': 200,
    },
    {
        'username': 'bob',
        'password': 'builder',
        'expected_status_code_v1': 200,
        'expected_status_code_v2': 403,
    },
]

# List of API versions to test
versions = ['v1', 'v2']

# Run the authorization test for each user and version, append the result to the summary
for version in versions:
    for user in users:
        summary += test_authorization(user, version)

# If the LOG environment variable is set to "1", write the summary to a log file
if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)