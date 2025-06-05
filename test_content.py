import os
import requests

# API address and port (use 'localhost' for host networking, or service name in Docker Compose networks)
api_address = 'api'
api_port = 8000

def test_content(data, version):
    """
    Sends a GET request to the /<version>/sentiment endpoint with a test sentence.
    Checks if the sentiment score matches the expected sign (positive/negative).
    Returns a formatted string with the test result and prints it.
    """
    r = requests.get(
        url=f'http://{api_address}:{api_port}/{version}/sentiment',
        params={
            'username': 'alice',  # Using a fixed user for testing
            'password': 'wonderland',  # Using a fixed password for testing
            'sentence': data['sentence'],
        }
    )

    # Get the score from the response if available
    try:
        score = r.json().get('score', None)
    except Exception:
        score = None

    # Determine the actual sign of the score
    if score is not None:
        if score > 0:
            actual_sign = 'positive'
        elif score < 0:
            actual_sign = 'negative'
        else:
            actual_sign = 'neutral'
    else:
        actual_sign = 'none'

    # Determine if the test passed based on expected and actual sign
    test_status = 'PASSED' if (score is not None and ((score > 0 and data['expected_sign'] == 'positive') or (score < 0 and data['expected_sign'] == 'negative'))) else 'FAILED'

    # Prepare output for this test case
    output = f'''
request done at "/{version}/sentiment"
| username="alice"
| password="wonderland"
| sentence="{data['sentence']}"
expected sign = {data['expected_sign']}
actual sign = {actual_sign}
actual result = {score}
==>  {test_status}
'''
    print(output)
    return output

# Summary header for the test log
summary = '''
============================
    Content test
============================
'''

# List of test sentences and their expected sentiment sign
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

# List of API versions to test
versions = ['v1', 'v2']

# Run the content test for each sentence and version, append the result to the summary
for version in versions:
    for data in test_data:
        summary += test_content(data, version)

# If the LOG environment variable is set to "1", write the summary to a log file
if os.environ.get('LOG') == "1":
    with open('api_log.txt', 'a') as file:
        file.write(summary)