import requests
link = 'https://2ip.ru/'
res = requests.get(link)
print(res.status_code)
print(res.text)