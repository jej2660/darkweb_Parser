import requests
from bs4 import BeautifulSoup

site = "http://ekbgzchl6x2ias37.onion/elandretail-com-kmall24-com"

r = requests.session()
r.proxies = {'http':'socks5h://localhost:9050',
            'https':'socks5h://localhost:9050'}
res = r.get(site)

bs = BeautifulSoup(res.content, "html.parser")

html = bs.find_all('strong')
for i in html:
    print(i)