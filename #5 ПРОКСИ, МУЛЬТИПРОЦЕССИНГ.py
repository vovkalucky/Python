import requests
from bs4 import BeautifulSoup
import fake_useragent
import multiprocessing

def handler(proxy):
    for proxy in proxy_base:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

        link = 'http://icanhazip.com/'
        try:
            req = requests.get(link, proxies=proxies, timeout=2).text
            print(f'IP: {req.strip()}')
        except:
            print('Proxy not valid!')

with open('proxy') as file:
    proxy_base = ''.join(file.readlines()).strip().split('\n')

def main():
    with multiprocessing.Pool(multiprocessing.cpu_count()) as process:
        process.map(handler, proxy_base)
if __name__ == '__main__':
    main()
#print(proxy_base)

