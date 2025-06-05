import os
import requests

# API address and port (use 'localhost' for host networking, or service name in Docker Compose networks)
api_address = 'api'
api_port = 8000


def test_authentication(user):
    """
    Sends a GET request to the /permissions endpoint with the given user's credentials.
    Returns a formatted string with the test result and prints it.
    """
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': user['username'],
            'password': user['password']
        }
    )

    # Prepare output for this test case
    output = f'''
request done at "/permissions"
| username="{user['username']}"
| password="{user['password']}"
expected result = {user['expected_status_code']}
actual result = {r.status_code}
==>  {'PASSED' if r.status_code == user['expected_status_code'] else 'FAILED'}
'''
    print(output)
    return output



# Summary header for the test log
summary = '''
============================
    Authentication test
============================
'''

# List of users to test, with expected status codes
users = [
    {
        'username': 'alice',
        'password': 'wonderland',
        'expected_status_code': 200,
    },
    {
        'username': 'bob',
        'password': 'builder',
        'expected_status_code': 200,
    },
    {
        'username': 'clementine',
        'password': 'mandarine',
        'expected_status_code': 403,
    },
]

# Run the authentication test for each user and append the result to the summary
for user in users:
    summary += test_authentication(user)

# If the LOG environment variable is set to "1", write the summary to a log file
if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)