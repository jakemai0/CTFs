import requests as req

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"
url = "http://natas22.natas.labs.overthewire.org?revelio"

session = req.Session()

response = session.get(url, auth=(username, password), allow_redirects=False)
print(response.text)