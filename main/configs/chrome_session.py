from selenium import webdriver
import subprocess, os


# create a new Chrome session with a little configurations..
def chrome_init(
                    window_size     = '1920x1080',
                    user_agent      = ("Mozilla/5.0"
                                        + "(Macintosh; Intel Mac OS X 10_12_6)"
                                        + "AppleWebKit/537.36 (KHTML, like Gecko)"
                                        + "Chrome/61.0.3163.100 Safari/537.36"),
                    browser_head    = '--headless',
                    pkill_chrome    = True
    ):



    current_path = '/crawler/main/configs'


    # Kill all chrome-related processes beforehand
    # Warning! Multi-Threading is not considered! Be aware of using it because it will wipe out all existing chrome processes.

    if pkill_chrome:
        subprocess.run(['pkill', 'chrome'],stdout=subprocess.PIPE,universal_newlines=True)

    options = webdriver.ChromeOptions()
    options.add_argument(browser_head)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size={}'.format(window_size))
    options.add_argument("--disable-gpu")
    options.add_argument("user-gent={}".format(user_agent))
    options.add_argument('--lang=UTF-8')
    driver = webdriver.Chrome(options=options, executable_path=current_path+"/chromedriver")
    driver.maximize_window()
    return driver
