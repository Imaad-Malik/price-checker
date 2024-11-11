import requests
from bs4 import BeautifulSoup
import re

l=[]
o={}

prod_details = {}

target_url = 'https://www.amazon.com/Xero-Shoes-Mens-Cross-Training/dp/B079XY48HQ?pd_rd_i=B09CN4SDPD&pd_rd_w=mg9B3&content-id=amzn1.sym.aea1191b-d0a0-48b0-b738-68a9d9512319&pf_rd_p=aea1191b-d0a0-48b0-b738-68a9d9512319&pf_rd_r=P9D1PESB1S6EQJN7ZB47&pd_rd_wg=phG9h&pd_rd_r=f81574d2-f357-41b7-a006-ddb5e6335a9b&th=1&psc=1'

headers={
    "accept-language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

resp = requests.get(target_url, headers = headers)
print(resp.status_code)

soup = BeautifulSoup(resp.text, 'html.parser')

product_facts = soup.find('div', id='productFactsDesktopExpander')

rows = product_facts.find_all('div', class_='a-fixed-left-grid product-facts-detail')

for row in rows:
    label = row.find('div', class_='a-fixed-left-grid-col a-col-left').get_text(strip=True)

    value = row.find('div', class_='a-fixed-left-grid-col a-col-right').get_text(strip=True)
    
    prod_details[label] = value


try:
    o["title"] = soup.find('h1',{'id':'title'}).text.strip()
    o["images"] = re.findall('"hiRes":"(.+?)"', resp.text)
    o["price"] = soup.find('span',{'class': 'aok-offscreen'}).text.strip()
    o["rating"] = soup.find('span',{'class': 'a-size-base'}).text.strip()
    o["product_details"] = prod_details

except:
    o["title"] = None
    o["images"] = None
    o["price"] = None
    o["rating"] = None
    o["product_details"] = None

print(o)