import os
import requests

# definition of the API address
api_address = 'localhost'  # Use the docker-compose service name
# API port
api_port = 8000


def test_authentication(user):
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=api_address, port=api_port),
        params={
            'username': user['username'],
            'password': user['password']
        }
    )

    status_code = r.status_code

    output = '''
request done at "/permissions"
| username="{username}"
| password="{password}"
expected result = {expected_status_code}
actual restult = {status_code}
==>  {test_status}
'''.format(
        username=user['username'],
        password=user['password'],
        expected_status_code=user['expected_status_code'],
        status_code=r.status_code,
        test_status='PASSED' if r.status_code == user['expected_status_code'] else 'FAILED'
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

for user in users:
    summary += test_authentication(user)

if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)