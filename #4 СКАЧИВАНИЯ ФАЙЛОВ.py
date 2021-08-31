import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = 'https://zastavok.net'

for page in range(1,3):
    dop_page = f'/{page}/'
    req = requests.get(link+dop_page, headers = header)
    soup = BeautifulSoup(req.text, 'lxml')
    img_href_list = soup.find('div', class_ = 'block-photo').find_all('div', class_ = 'short_full')
    image_number = 1
    for item in img_href_list:
        image_link = item.find('a').get('href')
        req2 = requests.get(link+image_link, headers = header)
        soup2 = BeautifulSoup(req2.text, 'lxml')
        result_link = link+soup2.find('div', class_ = 'block_down').find('a').get('href')
        image_bytes = requests.get(result_link, headers = header).content
        with open(f'img_les4/image_p{page}number{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)
            file.close()
        image_number+=1