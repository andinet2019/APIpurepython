import requests
response=requests.get("http://placegoat.com/200/200")
print(response.request.headers)
response.headers.get("Content-type")