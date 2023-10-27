import requests


url = "https://projektejwkk.de/_____mailGen/send.php"

params = {
    "author": "Janne",
    "receiver": "jabbekeipert@gmail.com",
    "message": "hallo, test",
    "subject": "test"
}

requests.post(url, data=params)
