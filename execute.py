from email_alert import alert_mail
import logging
import schedule
import getpass
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict


def arxiv_connect(authors : list = [], EMAIL_ADDR : str = None, EMAIL_PASSWORD : str = None):
    if not authors:
        logging.info('No authors input!!!')
        return 

    url = 'https://arxiv.org/list/cond-mat/new'

    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html,'html.parser')


    article_titles = OrderedDict()

    
    section_hash = {'New submissions':'10',
                    # , 'Cross-lists':'12', 
                    'Replacements':'14'
                    }
    
    for sector in section_hash.keys():
        num_of_article = 1
        while True:
            contents = soup.select(f'#dlpage > dl:nth-child({section_hash[sector]}) > dd:nth-child({int(num_of_article * 2)})')

            if not contents:
                break
            else:
                author_number = 1
                this_paper_authors = []
                article_title = 'None'
                while True:
                    ca = soup.select(f'#dlpage > dl:nth-child({section_hash[sector]}) > dd:nth-child({int(num_of_article * 2)}) > div > div.list-authors > a:nth-child({author_number+1})')

                    if not len(ca):
                        break
                    content_author = soup.select(f'#dlpage > dl:nth-child({section_hash[sector]}) > dd:nth-child({int(num_of_article * 2)}) > div > div.list-authors > a:nth-child({author_number+1})')[0].get_text()
                    real_name = content_author
                    content_author = content_author.replace(',', '').replace('.', '')
                    
                    this_paper_authors.append(real_name)
                    logging.info(f'Searching for {sector} content number : {num_of_article}  , author {content_author}, {author_number}')

                    if content_author in authors:
                        article_title = soup.select(f'#dlpage > dl:nth-child({section_hash[sector]}) > dd:nth-child({int(num_of_article * 2)}) > div > div.list-title.mathjax')[0].get_text()
                        if article_title not in article_titles:
                            article_titles[article_title] = None
                    
                     
                    author_number+=1
                    
                if article_title in article_titles:
                    article_titles[article_title] = this_paper_authors

                num_of_article+=1

    logging.info(f'Done for Searching today !!')

    if article_titles:
        alert_mail(EMAIL_ADDR=EMAIL_ADDR, EMAIL_PASSWORD=EMAIL_PASSWORD, articles =article_titles)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d, %H: %M: %S")

    req_author_names =['Vojtěch Chlan', 'Antti Penttilä',  'Mehraneh Tirandari', 'Jiabin Yu', 'Kunpeng Dou', 'Zhengyan Darius Shi', 'Xiulin Ruan', 'Philip Kim', 'Romain Danneau',
                       'Klaus Ensslin']

    req_authors = [req.replace(',', '').replace('.', '') for req in req_author_names ]
    EMAIL_ADDR = input("Please enter your gmail id : ")
    EMAIL_PASSWORD = getpass.getpass("please enter your gmail password : ")


    # arxiv_connect(req_authors, EMAIL_ADDR, EMAIL_PASSWORD)
    job = schedule.every().day.at("02:00").do(arxiv_connect, req_authors, EMAIL_ADDR, EMAIL_PASSWORD)

    # 테스트 해보고 싶으면 아래 job을 활성화 시키세요!
    # job = schedule.every(10).seconds.do(arxiv_connect, req_authors, EMAIL_ADDR, EMAIL_PASSWORD)
    
    while True:
        schedule.run_pending()
        
       

                