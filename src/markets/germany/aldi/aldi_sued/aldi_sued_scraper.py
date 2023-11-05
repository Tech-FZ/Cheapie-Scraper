import requests
import bs4
import core.data_includer as dataincl

header = {
    'authority': 'www.aldi-sued.de',
    'accept': '*/*',
    'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://www.aldi-sued.de/de/produkte/produktsortiment/brot-aufstrich-und-cerealien.html',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

def scraper(cheapie_scraper, endpoint, header):
    product_names = []
    product_prices = []
    product_pics = []
    page = requests.get(endpoint, headers=header)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    results1 = soup.find_all(class_="product-title")
    #print(results1)

    for result in results1:
        print(result.prettify())
        product_names.append(result.text.strip())

    results2 = soup.find_all(class_="at-product-price_lbl")
    #print(results2)

    for result in results2:
        print(result.prettify())
        product_prices.append(result.text.strip().replace('€ ', ''))

    results3 = soup.find_all(class_="at-product-images_img")
    #print(results2)

    for result in results3:
        print(result.prettify())
        product_pics.append(result['data-src'])

    print(product_names)
    print(product_prices)
    print(product_pics)

    db_cursor = cheapie_scraper.cheapie_db.cursor()
    db_cursor.execute("SELECT CompanyID FROM Company WHERE CompanyName = 'ALDI SÜD Dienstleistungs-SE & Co. oHG'")
    exec_res1 = db_cursor.fetchall()

    for x in exec_res1:
        print(x)

    j = 0

    while j < len(exec_res1):
        db_cursor.execute(f"SELECT BranchID FROM Branch WHERE Company = {exec_res1[j][0]}")
        exec_res2 = db_cursor.fetchall()

        for x in exec_res2:
            print(x)
            i = 0

            while i < len(product_names):
                db_cursor = cheapie_scraper.cheapie_db.cursor()
                db_cursor.execute(f"SELECT ProductID, ProductName FROM Product WHERE ProductName = '{product_names[i]}'")
                exec_res3 = db_cursor.fetchall()

                if len(exec_res3) > 0:
                    for y in exec_res3:
                        print(y)

                        dataincl.insertStock(cheapie_scraper, y[0], product_prices[i], x[0], "€")

                else:
                    dataincl.addProduct(cheapie_scraper, product_names[i], product_prices[i], product_pics[i], x[0], "€")
            
                print(exec_res3)

                i += 1

        j += 1

def scrapeBreadStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/brot-aufstrich-und-cerealien.html"

    while i < 20:
        endpoint = "https://www.aldi-sued.de/de/produkte/produktsortiment/brot-aufstrich-und-cerealien.onlyProduct.html?pageNumber=" + str(i) + "&_1698492075964"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeCooledFrozenStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/kuehlung-und-tiefkuehlkost.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/kuehlung-und-tiefkuehlkost.onlyProduct.html?pageNumber={str(i)}&_1699180107923"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeNutrients(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/nahrungsmittel.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/nahrungsmittel.onlyProduct.html?pageNumber={str(i)}&_1699180251054"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeCoffeeTea(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/kaffee-und-tee.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/kaffee-und-tee.onlyProduct.html?pageNumber={str(i)}&_1699180370726"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeDrinks(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/getraenke.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/getraenke.onlyProduct.html?pageNumber={str(i)}&_1699180532588"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeSweetsSnacks(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/suessigkeiten-und-snacks.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/suessigkeiten-und-snacks.onlyProduct.html?pageNumber={str(i)}&_1699180617805"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeDrugstoreCosmetics(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/drogerie-und-kosmetik.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/drogerie-und-kosmetik.onlyProduct.html?pageNumber={str(i)}&_1699180796850"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeBabyChildStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/baby-und-kind.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/baby-und-kind.onlyProduct.html?pageNumber={str(i)}&_1699180897291"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeHouseholdStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/haushalt.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/haushalt.onlyProduct.html?pageNumber={str(i)}&_1699181427160"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapePetStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/tierbedarf.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/tierbedarf.onlyProduct.html?pageNumber={str(i)}&_1699181484213"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapePrepaidCards(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/aldi-guthaben-und-geschenkkarten.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/aldi-guthaben-und-geschenkkarten.onlyProduct.html?pageNumber={str(i)}&_1699181616856"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeGrillingStuff(cheapie_scraper):
    i = 0
    header['referer'] = "https://www.aldi-sued.de/de/produkte/produktsortiment/grillen.html"

    while i < 20:
        endpoint = f"https://www.aldi-sued.de/de/produkte/produktsortiment/grillen.onlyProduct.html?pageNumber={str(i)}&_1699181818370"
        scraper(cheapie_scraper, endpoint, header)
        i += 1

def scrapeStarter(cheapie_scraper):
    scrapeBreadStuff(cheapie_scraper)
    scrapeCooledFrozenStuff(cheapie_scraper)
    scrapeNutrients(cheapie_scraper)
    scrapeCoffeeTea(cheapie_scraper)
    scrapeDrinks(cheapie_scraper)
    scrapeSweetsSnacks(cheapie_scraper)
    scrapeDrugstoreCosmetics(cheapie_scraper)
    scrapeBabyChildStuff(cheapie_scraper)
    scrapeHouseholdStuff(cheapie_scraper)
    scrapePetStuff(cheapie_scraper)
    scrapePrepaidCards(cheapie_scraper)
    scrapeGrillingStuff(cheapie_scraper)