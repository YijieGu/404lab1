import requests
print(requests.__version__)
homepage=requests.get("http://www.google.com")
print(homepage.text)
new_version= requests.get("https://raw.githubusercontent.com/YijieGu/404lab1/main/script.py")
print(new_version.text)