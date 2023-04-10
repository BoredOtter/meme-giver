# Import the requests module
import requests

# Send a GET request to the desired API URL
response = requests.get('https://meme-api.com/gimme')

# Parse the response and print it
data = response.json()
print(data)