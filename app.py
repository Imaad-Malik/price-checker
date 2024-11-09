import requests
from bs4 import BeautifulSoup

target_url = 'https://www.amazon.com/Xero-Shoes-Mens-Cross-Training/dp/B09CN4SDPD?pd_rd_i=B09CN4SDPD&pd_rd_w=mg9B3&content-id=amzn1.sym.aea1191b-d0a0-48b0-b738-68a9d9512319&pf_rd_p=aea1191b-d0a0-48b0-b738-68a9d9512319&pf_rd_r=P9D1PESB1S6EQJN7ZB47&pd_rd_wg=phG9h&pd_rd_r=f81574d2-f357-41b7-a006-ddb5e6335a9b'

headerstuff={
    "accept-language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

resp = requests.get(target_url, headers = headerstuff)

print(resp.text)