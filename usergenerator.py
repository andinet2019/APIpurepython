import requests
response = requests.get("https://api.thedogapi.com/v1/breeds")
request=response.request
print(request.url)
print(request.headers)
print(request.path_url)
