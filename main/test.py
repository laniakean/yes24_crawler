from selenium import webdriver
from bs4 import BeautifulSoup
from configs.chrome_session import chrome_init

def best_book_detail(url_list):
    chromedriver = chrome_init()
    
    for detail_page_url in url_list:
        chromedriver.get(detail_page_url)
        html = chromedriver.page_source

        soup = BeautifulSoup(html, 'lxml')
        divs = soup.find("div",{"class":"topColRgt"})

        authors_obj = divs.find("span",{"class":"gd_auth"}).find_all("a",{"target":"_blank"})
        author_list = [author.getText().strip() for author in authors_obj]
        authors     = ", ".join(author_list)

        main_title_obj = divs.find("h2", {"class": "gd_name"})
        main_title = main_title_obj.getText() if main_title_obj else None

        sub_title_obj = divs.find("h3", {"class": "gd_nameE"})
        sub_title = sub_title_obj.getText() if sub_title_obj else None

        published_at_obj = divs.find("span", {"class":"gd_date"})
        published_at = published_at_obj.getText() if published_at_obj else None

        rate_obj = divs.find("em", {"class":"yes_b"})
        rate = rate_obj.getText() if rate_obj else None

        price_obj = divs.find("em", {"class":"yes_m"})
        price = price_obj.getText() if price_obj else None



if __name__ == "__main__":
    
    

    dummy_url = [
            'http://www.yes24.com/Product/Goods/89309569',
            'http://www.yes24.com/Product/Goods/90266627',
            'http://www.yes24.com/Product/Goods/90233128',
            'http://www.yes24.com/Product/Goods/90248119'
            ]
    best_book_detail(dummy_url)
