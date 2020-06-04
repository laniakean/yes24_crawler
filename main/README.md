# 예스24의 베스트셀러 Crawler


## Introduction


The purpose of this project is to collect and gather the list of best-selling books from the website called "Yes24". It is sort of scraper or crawler, letting you collect data of top-n best-selling books.


---


## Environment


- OS : Ubuntu:18.04

- Python Version : python3.6

- Environment : virtualenv


---


## Installation


### Prerequisit : Virtualenv, Python Library installation through pip (requirements.txt)

### 1. In case where you do not have chrome, ChromeDriver on your local machine

- Initiate the project by running the shell file "chrome_download.sh" by using the command "sh chrome_download.sh"

- Next, Run command "python3 chrome_driver_download.py" on your virtual environment



### 2. In case where you have chrome on the local machine, but not 


- Simply run command "python3 chrome_driver_download.py" on your virtual environment


---


## Using Guide


- Main Command : "python3 [Category argument] [Retrieve argument]"

> if you are looking for top-40 best selling books on the category number of "001",

> you can simply command as "python3 001 40" (Virtualenv must be on)


---


## Result


- Result file will be located at "./results"

- Filename follows certain rule something like "[current_date]_yes24_best_[row_count].txt".

- Delimiter inbetween data will be set as " | ". The reason why we do not use "," as delimiter, is becasue it already taken within data (Meant to be reducing confusion)

- Only the text file is supported at the moment.
