import os
import requests

# definition of the API address
api_address = 'localhost'  # Use the docker-compose service name
# API port
api_port = 8000


def test_authorization(data, version):
    r = requests.get(
        url='http://{address}:{port}/{version}/sentiment'.format(address=api_address, port=api_port, version=version),
        params={
            'username': 'alice',  # Using a fixed user for testing
            'password': 'wonderland',  # Using a fixed password for testing
            'sentence': data['sentence'],  # Using the sentence from the test data
        }
    )

    # Get the score from the response if available
    try:
        score = r.json().get('score', None)
    except Exception:
        score = None

    test_status = 'PASSED' if (score is not None and ((score > 0 and data['expected_sign'] == 'positive') or (score < 0 and data['expected_sign'] == 'negative'))) else 'FAILED'

    output = '''
request done at "/{version}/sentiment"
| username="alice"
| password="wonderland"
| sentence="{sentence}"
expected sign = {expected_sign}
actual result = {score}
==>  {test_status}
'''.format(
        version=version,
        sentence=data['sentence'],
        expected_sign=data['expected_sign'],
        score=score,
        test_status=test_status
    )
    print(output)
    return output



summary = '''
============================
    Content test
============================
'''

test_data = [
    {
        'sentence': 'life is beautiful',
        'expected_sign': 'positive',
    },
    {
        'sentence': 'that sucks',
        'expected_sign': 'negative',
    },
]
versions = ['v1', 'v2']
for version in versions:
    for data in test_data:
        summary += test_authorization(data, version)

if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)