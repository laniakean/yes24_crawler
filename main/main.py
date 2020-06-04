# -*- coding: utf-8 -*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import subprocess, sys, requests, json

from configs.chrome_session import chrome_init
from selenium_command.yes24_best import url_builder, best_book_list, best_book_detail

from datetime import datetime
from pytz import timezone





def json_export(export_type, json_obj, limit):

    current_time = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    filename = current_time + '_yes24_best_{}'.format(limit)
    fileloc  = './results/' + filename

    if export_type=='txt':
        with open(fileloc+".txt", 'w', encoding='utf-8') as filewrite:
            for json in json_obj:
                    main_title, sub_title = json['main_title'], json['sub_title']
                    authors, published_at = json['authors'], json['published_at']
                    rate, price,url = json['rate'], json['price'], json['url']
                    txt_out = " | ".join([main_title,sub_title,authors,published_at,rate,price,url])
                    filewrite.write(txt_out + "\n")

    elif export_type=='csv':
        return None
        #jsons = json.load(json_obj)
        #df = json_normalize(jsons)
        #return df.to_csv(fileloc, index=False, set=',', encoding='utf-8')

    elif export_type=='json':
        return None
        #with open(fileloc, 'w', encoding='utf-8') as filewrite:
        #    for json in json_obj:
        #        filewrite.write(json + "\n")

def main(argv):

    # 001, 40
    best_category, limit = argv[1], argv[2]
    
    req_url         = url_builder(fetch_size = limit, category_number=best_category)
    target_urls     = best_book_list(req_url) 
    json_objects    = best_book_detail(target_urls)
    json_export('txt', json_objects, limit)    





if __name__ == "__main__":

    main(sys.argv)

