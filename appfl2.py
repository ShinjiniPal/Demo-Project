import requests

# URL of the Flask server
url = 'http://127.0.0.1:5000/calculate'

# JSON payload containing the operation to be calculated
payload = {'operation': '5 ADD 9'}

# Sending a POST request to the server
response = requests.post(url, json=payload)

# Printing the response
print(response.json())
