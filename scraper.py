import sys
from termcolor import colored, cprint
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/TCL-43S425-Inch-Ultra-Smart/dp/B07DK5PZFY/ref=sxin_3_osp21-049d1d07_cov?ascsubtag=049d1d07-a18e-41f6-8148-52b097396088&creativeASIN=B07DK5PZFY&cv_ct_id=amzn1.osp.049d1d07-a18e-41f6-8148-52b097396088&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=tv&linkCode=oas&pd_rd_i=B07DK5PZFY&pd_rd_r=85fc62ca-37fe-41e2-8690-fb4d4cb8e20a&pd_rd_w=y8PZB&pd_rd_wg=ZHiuK&pf_rd_p=71f1c6c5-d697-4844-8fde-6c0e8c1923da&pf_rd_r=YW901NQP99DATFVMPYKC&qid=1567827340&s=gateway&tag=onsitertings-20'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id= "productTitle").get_text()
price = soup2.find(id = "priceblock_ourprice").get_text()
converted_price = price[0:7]

print('')
print(title.strip())
print(colored(converted_price, 'green'))
print('')
