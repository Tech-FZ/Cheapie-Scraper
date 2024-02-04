import mysql.connector
from getpass import getpass
import markets.germany.aldi.aldi_sued.aldi_sued_scraper as aldi_sued_de
import markets.germany.rewe.rewe_scraper as rewe_de
import core.shop_choose_gui as scgui
import sys

class CheapieScraper():
    def __init__(self):
        self.cheapie_db = None
        self.cheapie_version = "2024.2.0.0"

    def chooseShopDe(self):
        print("Market list")
        print("")
        print("1. ALDI SÜD (Germany)")
        print("2. REWE (Germany)")
        print("3. Exit")
        print("")

        try:
            chosen_market = int(input("Please type in a number: "))

            if chosen_market == 1:
                aldi_sued_de.scrapeStarter(self)

            elif chosen_market == 2:
                chosen_market = 2
                rewe_de.scrapeStarter(self)

            elif chosen_market == 3:
                print("Bye.")
                sys.exit()

            else:
                print("Not a valid option")

        except TypeError:
            print("Not a valid option")

    def connectToDb(self):
        tries = 3
        while True:
            pwd = getpass("Please type in the password for cheapie-scraper: ")

            try:
                self.cheapie_db = mysql.connector.connect(
                    host = "localhost",
                    user = "cheapie-scraper",
                    password = pwd,
                    database = "cheapie_db"
                )

                print(self.cheapie_db)
                break

            except:
                print("Wrong password.")

                tries -= 1

                if tries > 1:
                    print(f"{tries} tries left.")

                elif tries == 1:
                    print("1 try left.")

                else:
                    print("No more tries! Bye.")
                    exit()

        #self.chooseShopDe()
        scgui.shop_choose(self)

cheapie_scraper = CheapieScraper()

print(f"""
    Cheapie Scraper {cheapie_scraper.cheapie_version} Copyright (C) 2023 - 2024 Nicolas Lucien and Cheapie contributors
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the LICENSE file for details.
""")

cheapie_scraper.connectToDb()