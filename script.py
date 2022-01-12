import requests
print(requests.__version__)
homepage=requests.get("http://google.com")
print(homepage.text)