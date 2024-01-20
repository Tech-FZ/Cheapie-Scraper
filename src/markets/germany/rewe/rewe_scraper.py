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

def scraper(cheapie_scraper, market_data):
    print("Function could be run")
    product_names = []
    product_prices = []
    product_pics = []

    driver = webdriver.Chrome()
    print("Webdriver: Chrome")

    try:
        print("Trying markt")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-markt-{str(market_data[1]).lower().replace(' ', '-')}")

    except:
        print("Trying center")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-center-{str(market_data[1]).lower().replace(' ', '-')}")

    time.sleep(10)
    print("Trying to navigate")

    try:
        #acceptframe = driver.find_elements_by_xpath("/html/body/div[3]/div[0]/div[0]/div[1]/div[0]/div[1]/div[0]/div[1]/div[0]/div[0]/div[0]/div[0]/button[1]").get(0).click()
        #acceptframe = driver.find_element(By.CLASS_NAME("cvYqei")).click()
        #cookiewin = driver.find_element(By.ID("uc-center-container"))
        #acceptbtn = cookiewin.find_element(By.CLASS_NAME("cvYqei")).click()
        acceptframe = driver.find_elements(By.CSS_SELECTOR("button.sc-dcJsrY"))
        acceptbtn = acceptframe.get(1)
        acceptbtn.click()
        print("Had to accept cookies")

    except:
        print("Cookies accepted")

    time.sleep(3)
    sales_path = "/html/body/main/div[1]/div[1]/div[0]/div[1]"
    first_sector_path = sales_path + "/div[1]/div[1]" #/div[1]

    try:
        info = driver.find_elements_by_xpath(first_sector_path + "/div[1]")
        sale_count = 0
        sale_count = len(info)

        while True:
            try:
                show_more = driver.find_element_by_xpath(first_sector_path + "/div[2]/button")
                show_more_info = show_more.text
                show_more_info_split = show_more_info.split(" ")
                sale_count += int(show_more_info_split[0])
                show_more.click()

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