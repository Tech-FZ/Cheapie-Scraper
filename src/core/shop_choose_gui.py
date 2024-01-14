import markets.germany.aldi.aldi_sued.aldi_sued_scraper as aldi_sued_de
import markets.germany.rewe.rewe_scraper as rewe_de
import sys
import PySimpleGUI as psg

german_markets = ["ALDI SÜD", "REWE"]

def shop_choose(cheapie_scraper):
    applayout = [
        [psg.Text(f"Cheapie Scraper {cheapie_scraper.cheapie_version}", key="-HEADING-", justification="center")],
        [psg.Text("Please choose a shop.", key="-REQUESTLBL-", justification="center")],
        [psg.Text("Chain", key="-CHAINLBL-"), psg.Combo(german_markets, key="-CHAINCOMBO-")],
        [psg.Button("OK"), psg.Button("Exit")]
    ]

    appwindow = psg.Window("Cheapie Scraper", applayout)

    while True:
        event, values = appwindow.read()

        if event == psg.WIN_CLOSED or event == "Exit":
            break

        elif event == "OK":
            if values["-CHAINCOMBO-"] == "ALDI SÜD":
                aldi_sued_de.scrapeStarter(cheapie_scraper)
                break

            elif values["-CHAINCOMBO-"] == "REWE":
                rewe_de.scrapeStarter(cheapie_scraper)
                break

        appwindow.close()