import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import pandas as pd
import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt
import markets.germany.rewe.rewe_scraper_citylist as citylist
import core.data_includer as dataincl
import core.usrfile_handler as usrfiles
import datetime

def cookieExpirationDateFinder(cheapie_scraper):
    todayDate = datetime.datetime.now()
    expiresAt = todayDate + datetime.timedelta(days=365 * 2)
    return expiresAt

def scraper(cheapie_scraper, market_data):
    print("Function could be run")
    product_names = []
    product_prices = []
    product_pics = []
    cookieExpire = cookieExpirationDateFinder(cheapie_scraper=cheapie_scraper)

    #options = webdriver.ChromeOptions()
    #options.add_argument(f"user-data-dir={usrfiles.chromeFileDir()}")
    driver = webdriver.Chrome()
    print("Webdriver: Chrome")

    try:
        print("Trying markt")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-markt-{str(market_data[1]).lower().replace(' ', '-')}")

    except:
        print("Trying center")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-center-{str(market_data[1]).lower().replace(' ', '-')}")

    """ driver.add_cookie({
        "name": "ar_debug",
        "value": "1",
        "domain": ".pinterest.com",
        "expires": f"{cookieExpire.year}-{cookieExpire.month}-{cookieExpire.day}T{cookieExpire.hour}:{cookieExpire.minute}:{cookieExpire.second}.000Z",
        "httpOnly": True,
        "path": "/",
        "sameSite": "None",
        "secure": True
        })

    driver.add_cookie({
        "name": "_pinterest_ct_ua",
        "value": "\"TWc9PSZPdlNrS0JkcXI3cFdDRTNVRXg0YTBNSFMzWkYxRU9McCtQQWlaRVBaSU5UVUwxYjNkZU9WZ2pXcGYydndCNW9jYjdhOHMzQ0xPdnVzd3JYcUM2c09uNVJ6ejl0dnFJQXVMZDZ6VzlsUVV6WT0mc0FoVEMwNDZNNEpQZVlYQW9vRlg5ODR1elA0PQ==\"",
        "domain": "ct.pinterest.com",
        "expires": f"{cookieExpire.year}-{cookieExpire.month}-{cookieExpire.day}T{cookieExpire.hour}:{cookieExpire.minute}:{cookieExpire.second}.000Z",
        "path": "/",
        "sameSite": "None",
        "secure": True
        }) """
    
    #time.sleep(10)
    print("Do the CAPTCHA and accept the cookies if required.")
    thing = input("When you're ready, press any key.")

    try:
        #acceptframe = driver.find_element_by_xpath("/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/button[2]").send_keys(Keys.ENTER)
        #acceptframe = driver.find_element(By.CLASS_NAME("cvYqei")).click()
        #cookiewin = driver.find_element(By.ID("uc-center-container"))
        #acceptbtn = cookiewin.find_element(By.CLASS_NAME("cvYqei")).click()
        #acceptframe = driver.find_elements(By.CSS_SELECTOR("button.sc-dcJsrY"))
        #acceptbtn = acceptframe.get(1)
        #acceptbtn.click()
        #cookiewin = driver.find_element(By.ID("uc-center-container"))
        #buttons = cookiewin.find_element(By.CSS_SELECTOR("div.sc-eeDRCY.iURToW"))
        #acceptbtn = buttons.get(1).click()
        #denybtn = driver.find_element(By.XPATH("/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[3]/div/div[2]/a[2]"))
        #driver.get(denybtn.get_attribute("href"))
        #denybtn.send_keys(Keys.ENTER)
        print("Had to accept cookies")

    except:
        print("Cookies accepted")

    time.sleep(3)
    #sales_path = "/html/body/main/div[1]/div[1]/div[0]/div[1]"
    sales_path = "/html/body/main/div[2]/div[2]/div/div[2]/"
    first_sector_path = sales_path + "div[2]/div[2]" #/div[1]

    try:
        info = driver.find_element(By.XPATH, first_sector_path + "/div[2]")
        sale_count = 0
        sale_count = len(info)
        print(sale_count)

        while True:
            try:
                show_more = driver.find_element(By.XPATH, first_sector_path + "/div[3]/button")

                if show_more.is_displayed():
                    show_more_info = show_more.text
                    show_more_info_split = show_more_info.split(" ")
                    sale_count += int(show_more_info_split[0])
                    show_more.click()
                    print(sale_count)

                else:
                    break

            except:
                break

    except:
        pass

def scrapeStarter(cheapie_scraper):
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    db_cursor.execute("SELECT CompanyID FROM Company WHERE CompanyName = 'REWE Markt GmbH'")
    exec_res1 = db_cursor.fetchall()

    for x in exec_res1:
        print(x)

    db_cursor.execute(f"SELECT BranchID, BranchAddress, BranchCity, CompanyInternalID FROM Branch WHERE Company = {exec_res1[0][0]}")
    exec_res2 = db_cursor.fetchall()

    for x in exec_res2:
        print(x)
        to_insert = list(x)
            
        for city in citylist.citylist:
            print(city)
            i = 0
                
            while i < len(city[1]):
                print(city[1][i])
                if city[1][i] == x[2]:
                    to_insert[2] = city[0]
                    break

                i += 1

            print("Scraping")
            scraper(cheapie_scraper, to_insert)
            break