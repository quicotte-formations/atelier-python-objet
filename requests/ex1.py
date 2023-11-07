import requests

rep = requests.get('http://127.0.0.1/api.php')
data = rep.json()
