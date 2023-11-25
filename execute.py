from url import arxiv_connect
from email_alert import alert_mail
import json
import os
import logging
import schedule, keyboard
import getpass


def main(*args):
    # print(args)
    author_name, g_mail_id, g_mail_pwd = args

    author_name_paper_number, author_search_paper_number = arxiv_connect(author=author_name)
    logging.info(f'Searching for author {author_name}')

    if not os.path.isfile('author_material.json'):
        author_info = dict()
        author_info[author_name] = {'num_of_paper':author_name_paper_number, 'num_of_search_res_paper': author_search_paper_number}
        json_data = json.dumps(author_info, indent=4)

        with open('author_material.json', 'w') as f:
            f.write(json_data)
            logging.info(f"Add Material Info of author : {author_name}")

    else:
        with open('author_material.json', 'r') as file:
            author_info = json.load(file)

            if author_name not in author_info:
                author_info[author_name] = {'num_of_paper':author_name_paper_number, 'num_of_search_res_paper': author_search_paper_number}
                json_data = json.dumps(author_info, indent=4)
                with open('author_material.json', 'w') as f:
                    f.write(json_data)
                    logging.info(f"Add Material Info of author : {author_name}")
            
            else:
                if author_info[author_name]['num_of_paper'] != author_name_paper_number:

                    alert_mail(EMAIL_ADDR=g_mail_id, EMAIL_PASSWORD=g_mail_pwd,author=author_name)
                    logging.info(f"Detect New Material from author : {author_name}")

                    author_info[author_name] = {'num_of_paper':author_name_paper_number, 'num_of_search_res_paper': author_search_paper_number}
                    json_data = json.dumps(author_info, indent=4)
                    with open('author_material.json', 'w') as f:
                        f.write(json_data)
    return 


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d, %H: %M: %S")

    author_name ='Eugene A. Eliseev'
    EMAIL_ADDR = input("Please enter your gmail id : ")
    EMAIL_PASSWORD = getpass.getpass("please enter your gmail password : ")


    job = schedule.every(30).seconds.do(main, author_name, EMAIL_ADDR, EMAIL_PASSWORD)

    # job = schedule.every().day.at("00:00").do(main, author_name)
    
    while True:
        schedule.run_pending()
        
       

                