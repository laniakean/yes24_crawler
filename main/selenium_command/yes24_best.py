
from selenium import webdriver
from bs4 import BeautifulSoup
from configs.chrome_session import chrome_init



# Webdriver Control

# -> http://www.yes24.com/24/Category/BestSeller -> Convert a link as URI with parameters as below
# -> Security breach may occur on query parameters -> No Limitation
def url_builder(fetch_size='40', category_number='001', page_number='1'):
    url = ("http://www.yes24.com/24/category/bestseller"
                + "?CategoryNumber={}".format(category_number)
                + "&sumgb=06"
                + "&fetchSize={}".format(fetch_size)
                + "&PageNumber={}".format(page_number)
            )
    return url



def best_book_list(list_page_url):

    chromedriver = chrome_init()
    
    try:
        chromedriver.get(list_page_url)
        html = chromedriver.page_source
        
        soup    = BeautifulSoup(html, 'lxml')
        divs    = soup.find("table",{"id":"category_layout"}).find_all("div",{"class":"goodsImgW"}) # chaining
        params  = [div.find("a",{"href": lambda x:x.startswith("/Product/Goods/")})['href'] for div in divs]
        urls    = list(map(lambda x: "http://www.yes24.com" + x, params)) 
    
    except:
        print("Something went wrong on the function called 'best_book_list'")
        urls = None
    
    finally:
        chromedriver.quit()

    return urls







def best_book_detail(url_list):
    
    json_objects = list()
    chromedriver = chrome_init()
    
    try:
        for detail_page_url in url_list:
            chromedriver.get(detail_page_url)
            html = chromedriver.page_source

            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find("div",{"class":"topColRgt"})

            authors_obj = divs.find("span",{"class":"gd_auth"}).find_all("a",{"target":"_blank"})
            author_list = [author.getText().strip() for author in authors_obj]
            authors     = ", ".join(author_list)

            main_title_obj = divs.find("h2", {"class": "gd_name"})
            main_title = main_title_obj.getText() if main_title_obj else "-"

            sub_title_obj = divs.find("h3", {"class": "gd_nameE"})
            sub_title = sub_title_obj.getText() if sub_title_obj else "-"

            published_at_obj = divs.find("span", {"class":"gd_date"})
            published_at = published_at_obj.getText() if published_at_obj else "-"

            rate_obj = divs.find("em", {"class":"yes_b"})
            rate = rate_obj.getText() if rate_obj else "-"

            price_obj = divs.find("em", {"class":"yes_m"})
            price = price_obj.getText() if price_obj else "-"

            jobject = {
                "main_title"    : main_title,
                "sub_title"     : sub_title,
                "authors"       : authors,
                "published_at"  : published_at,
                "rate"          : rate,
                "price"         : price,
                "url"           : detail_page_url
                }
            json_objects.append(jobject)
    except:
        print("Something went wrong on the function called 'best_book_detail'.")

    finally:
        chromedriver.quit()

    return json_objects
