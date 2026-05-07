import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print("Status Code:", response.status_code)
print("Response Data:")
print(response.json())