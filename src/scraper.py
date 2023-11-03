import mysql.connector
from getpass import getpass
import markets.germany.aldi.aldi_sued.aldi_sued_scraper as aldi_sued_de

class CheapieScraper():
    def __init__(self):
        self.cheapie_db = None
        self.cheapie_version = "2023.11.0.1"

    def connectToDb(self):
        pwd = getpass("Please type in the password for cheapie-scraper: ")

        self.cheapie_db = mysql.connector.connect(
            host = "localhost",
            user = "cheapie-scraper",
            password = pwd,
            database = "cheapie_db"
        )

        print(self.cheapie_db)

        aldi_sued_de.scrapeStarter(self)

cheapie_scraper = CheapieScraper()

print(f"""
    Cheapie Scraper {cheapie_scraper.cheapie_version} Copyright (C) 2023 Nicolas Lucien and Cheapie contributors
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See the LICENSE file for details.
""")

cheapie_scraper.connectToDb()