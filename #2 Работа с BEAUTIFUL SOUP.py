import requests
from bs4 import BeautifulSoup
import fake_useragent

link = 'https://browser-info.ru/'
user = fake_useragent.UserAgent().random
header = {'user-agent': user}
res = requests.get(link, headers = header)
print(res.status_code)
soup = BeautifulSoup(res.text, 'lxml')
info_js = soup.find('div', id = 'javascript_check').find('span').find_next().text
info_cookie = soup.find('div', id = 'cookie_check').find_all('span')[1].text
info_user_agent = soup.find('div', id = 'user_agent').text
print(f'Javascript: {info_js}')
print(f'Cookie: {info_cookie}')
print(info_user_agent)

