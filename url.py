from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import logging

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d, %H: %M: %S")
def arxiv_connect(author):
    base_url = 'https://arxiv.org/search/cond-mat?searchtype=author&query='

    # author_name = 'Eugene A. Eliseev'
    author_name = author
    author_input = author_name.replace(',', ' ').replace('.', ' ').split()
    author_input = author_input[-1] +'%2C+'+'+'.join(author_input[:-1])
    max_results = 25
    p_num = 0
    flag = True
    author_name_paper_number = 0
    author_search_paper_number = 0

    logging.info("Start Checking new material")

    while flag:
        url = base_url+author_input+f'&size={max_results}'+f'&start={p_num}'
        
        logging.info(f"Now Checking : {url}")
        req = requests.get(url)
        html = req.text

        soup = BeautifulSoup(html,'html.parser')

        cnt = 1

        while cnt<=max_results:
            a = soup.select(f'#main-container > div.content > ol > li:nth-child({cnt}) > p.authors')

            if not a:
                flag=False
                break

            if author_name in str(a[0]):
                author_name_paper_number+=1
            cnt+=1
            author_search_paper_number+=1
        
        p_num+=max_results
    return author_name_paper_number, author_search_paper_number


