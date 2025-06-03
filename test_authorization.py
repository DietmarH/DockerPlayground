import os
import requests

# definition of the API address
api_address = 'localhost'  # Use the docker-compose service name
# API port
api_port = 8000


def test_authorization(user, version):
    r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
        params={
            'username': user['username'],
            'password': user['password'],
            'sentence': '',  # Empty sentence to test permissions
        }
    )

    status_code = r.status_code

    output = '''
request done at "/{version}/sentiment"
| username="{username}"
| password="{password}"
| sentence=""
expected result = {expected_status_code}
actual restult = {status_code}
==>  {test_status}
'''.format(
        version=version,
        username=user['username'],
        password=user['password'],
        expected_status_code=user[f'expected_status_code_{version}'],
        status_code=r.status_code,
        test_status='PASSED' if r.status_code == user[f'expected_status_code_{version}'] else 'FAILED'
    )
    print(output)
    return output



summary = '''
============================
    Authentication test
============================
'''

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

versions = ['v1', 'v2'] 
for version in versions:
    for user in users:
        summary += test_authorization(user, version)

if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)