import requests
from bs4 import BeautifulSoup
import fake_useragent

session = requests.Session()  # для сохранения прогресса, куки

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = 'https://coursehunter.net/sign-in'
datas = {
    "e_mail": "vladimir.inves@gmail.com",
    "password": "kbjytkm10"
}

res = session.post(link, data=datas, headers=header)

print(res.status_code)
if res.ok:
    print('Ok!')
else:
    print('Ошибка запроса')

profile_info_link = 'https://coursehunter.net/cabinet'
res2 = session.get(profile_info_link, headers=header).text
soup = BeautifulSoup(res2, 'lxml')
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(res2)
    file.close()
my_id = soup.find('div', class_='user-block-title')
print(my_id)
