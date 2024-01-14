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

    driver = webdriver.Firefox()
    print("Webdriver: Firefox")

    try:
        print("Trying markt")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-markt-{str(market_data[1]).lower().replace(' ', '-')}")

    except:
        print("Trying center")
        driver.get(f"https://www.rewe.de/angebote/{str(market_data[2]).lower()}/{str(market_data[3])}/rewe-center-{str(market_data[1]).lower().replace(' ', '-')}")

    time.sleep(5)
    print("Trying to navigate")

    try:
        acceptframe = driver.find_element_by_xpath("/html/body/div[3]/div[0]/div[0]/div[1]/div[0]/div[1]/div[0]/div[1]/div[0]/div[0]/div[0]/div[0]/button[1]").click()
        print("Had to accept cookies")

    except:
        print("Cookies accepted")

def scrapeStarter(cheapie_scraper):
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    db_cursor.execute("SELECT CompanyID FROM Company WHERE CompanyName = 'REWE Markt GmbH'")
    exec_res1 = db_cursor.fetchall()

    for x in exec_res1:
        print(x)

    j = 0

    while j < len(exec_res1):
        db_cursor.execute(f"SELECT BranchID, BranchAddress, BranchCity, CompanyInternalID FROM Branch WHERE Company = {exec_res1[j][0]}")
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