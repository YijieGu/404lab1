import requests
print(requests.__version__)
#homepage=requests.get("http://google.com")
homepage= requests.get("https://raw.githubusercontent.com/YijieGu/404lab1/main/script.py")
print(homepage.text)