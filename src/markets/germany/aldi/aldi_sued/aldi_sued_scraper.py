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

def scrapeStarter(cheapie_scraper):
    scrapeBreadStuff(cheapie_scraper)