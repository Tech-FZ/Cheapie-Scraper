import requests
import bs4
import core.data_includer as dataincl
import json

cookies = {
    '_rdfa': 's%3A6fbe6e4f-b105-41e1-b706-6ceb05000f59.kg9sN4xIYpIRcilnxLgJZ7yqzO2ABojmSm1Gzy3HMrc',
    'optimizelyEndUserId': 'oeu1571411829743r0.8517103064407519',
    'AMCVS_65BE20B35350E8DE0A490D45%40AdobeOrg': '1',
    'ecid': 'sea_google_ls_nonbr_milka-[mar-0002|bm|lm]_milka-kaufen-[mar-0002|eco-0012|1|bm|lm]_text-ad_833898230_43028178719',
    'trbo_usr': '1c0854b37e993a19cf919e3cead78156',
    'mf_2d859e38-92a3-4080-8117-c7e82466e45a': '-1',
    '_fbp': 'fb.1.1571411834470.1081952992',
    'icVarSave': 'TC%2042%20Treatment%20Random%2CTC45%20Treatment',
    's_cc': 'true',
    'ken_gclid': 'CjwKCAjwxaXtBRBbEiwAPqPxcNgeH3ccV9kjh8idQDoCSc3xwLjG0ReGjCnbBeQyQkHz2h1pVbx6VRoCXDsQAvD_BwE',
    'cto_lwid': 'abc4dd35-f42e-44fd-9d3d-8ee2b4f01c8c',
    'sto__vuid': '317fa2090832e63c6a88f410d2437c09',
    'myReweCookie': '%7B%22customerZip%22%3A%2210247%22%2C%22customerLocation%22%3A%2252.51604592808167%2C13.465546337768295%22%2C%22deliveryMarketId%22%3A%22231006%22%2C%22serviceType%22%3A%22DELIVERY%22%7D',
    'marketsCookie': '%7B%22online%22%3A%7B%22wwIdent%22%3A%22231006%22%2C%22marketZipCode%22%3A%2213089%22%2C%22serviceTypes%22%3A%5B%22PARCEL%22%2C%22DELIVERY%22%5D%2C%22customerZipCode%22%3A%2210247%22%7D%2C%22stationary%22%3A%7B%7D%7D',
    '_gcl_aw': 'GCL.1571411845.CjwKCAjwxaXtBRBbEiwAPqPxcNgeH3ccV9kjh8idQDoCSc3xwLjG0ReGjCnbBeQyQkHz2h1pVbx6VRoCXDsQAvD_BwE',
    'mfCookie': '-1',
    'cookie-consent': '1',
    'MRefererUrl': 'https%3A%2F%2Fwww.google.com%2F',
    'AMCV_65BE20B35350E8DE0A490D45%40AdobeOrg': '1075005958%7CMCIDTS%7C18199%7CMCMID%7C68984298103318409563185344066719227243%7CMCAAMLH-1572985682%7C6%7CMCAAMB-1572985682%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1572388082s%7CNONE%7CvVersion%7C4.4.1',
    'c_dslv_s': '11',
    's_vnum': '1572562800740%26vn%3D2',
    's_invisit': 'true',
    'sto__session': '1572380885541',
    'c_dslv': '1572380922284',
    's_ppn': 'rewe-de%3Asuche',
    'trbo_sess_3723808811': '%7B%22firstClickTime%22%3A1572380883%2C%22lastClickTime%22%3A1572380923%2C%22pageViewCount%22%3A2%2C%22sessionDuration%22%3A40%7D',
    'perfTimings': 'event180=0.04%2Cevent181=0.00%2Cevent182=0.00%2Cevent183=0.00%2Cevent184=0.50%2Cevent185=0.03%2Cevent186=3.79%2Cevent187=0.06%2Cevent188=5.13%2Cevent189%3Brewe-de:suche',
    'perfLoad': '5.13',
    '_derived_epik': 'dj0yJnU9ZHdKbEtVdFJ5dVBEZ08yUEJQMDVHczdMVlh0bzFhNzMmbj04WjRqU1ZOQVIzVEF4MVFFZWMzcDN3Jm09NyZ0PUFBQUFBRjI0b1Bz',
    'mtc': 's%3AIJzxk40H3Y8CGzgfvZKF8gJMVy8iMTMxMjdkLWVKZ2t2ckNmTW5wVFlkdmNqY3BKME05QnhwNCIi6gKKBsIE7AG6BMADWJwFtgRcngK%2BAuYFnAakBqwGqgYABsgD4gKoBAA%3D.RJNwL9jE5BtuIUnIZQlX701ZkcSswAW9scvTCJBbrOE',
    '_afid': '4502757903888691750',
    'trbo_session': '3723810860',
    'trbo_us_1c0854b37e993a19cf919e3cead78156': '%7B%22saleCount%22%3A0%2C%22sessionCount%22%3A2%2C%22brandSessionCount%22%3A1%2C%22pageViewCountTotal%22%3A3%2C%22sessionDurationTotal%22%3A10%2C%22externalUserId%22%3A%22%22%2C%22userCreateTime%22%3A1571411834%7D',
    'trbo_sess_3723810860': '%7B%22firstClickTime%22%3A1572381080%2C%22lastClickTime%22%3A1572381080%2C%22pageViewCount%22%3A1%2C%22sessionDuration%22%3A0%7D',
    'c_lpv_a': '1572381081513|seo_google_nn_nn_nn_nn_nn_nn_nn',
    'rstp': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhZXMxOTIiOiIyYjkwYWQ3MDdlMmQ5MGUyYTljNzJiZTAzNjgwZTdkMDczMzc3OTNjMmEyNTI2NzkzODc5Y2I5ZGMwYzM4MWI4YzMzNzA0NWE0ODZmMWYyZTczY2IwZjJjM2IxODRmYTE0MjU1YjQxYmVmM2M5M2Y4YzI2MDQzODllZWRjNGE3ZjgyYWQwZWNhMjY3ZjAzOTBjZmJiMDE1ZGY1ZTQ2ZmJhZjQ3ZDg3YzdkMDEyMzM1OWJjOWQxNGVlNjZkOTc5NjIwZjJiMzJlMjQ0NzkzOTk1MTIzMzU2MjEzZmNlZDZlMWNmMGFmZTUxOTAzYjkwNmY1MjFhMjY3ODNmYjBlODNhMTk3OWMxMWQ4Y2JjZDc3Yzc3ZTAxNjM2ZjcwNjg1NGM3ZDk5NzVhNDZkOWVjZjdiYjBhOTJlZWVhNzk0NjUzNGI5NTE3ZDVkZmU2Mjg0ZTRmOTkxOTI0NWU2NjYyMjk1MmY0MTgwOWE1ZjgxZWI5ZWE3ZjdiYmEzZWNiZWE4NjA3NDU0OTY3MzkwM2U1MmJmOTg3ZDI4ZmY0MTBlYTA1OGNmMjIzODNjZDZiZjM4OGIwYTZkNjg3YzFjY2JlNzBjZDNlOWI2OGE5ZjVhZjNlM2YzNGYwYTQzODA4YjYzYTJkNmQ2YWYwM2Q3ZjlhNTdjOWNlMDgyZWE0MmExYTk2NCIsImlhdCI6MTU3MjM4MTA4MSwiZXhwIjoxNTcyMzgxNjgxfQ.9Pwhf0LU7rCkV6IgqUjyLfRiez8SWMEvisficIifvHRmB9QHRfe7SdH3zTMqxOxtZc8Io9ITshCo2Si6owRwgw',
    'sto__count': '1',
    's_nr': '1572381123119-Repeat',
    's_sq': 'rewrewededev%3D%2526c.%2526a.%2526activitymap.%2526page%253Dproduktliste%2526link%253D2%2526region%253Dsearch-service-content%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
}

header = {
    'sec-fetch-mode': 'cors',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'accept': 'application/vnd.rewe.productlist+json',
    'referer': 'https://shop.rewe.de/productList?search=k%C3%A4se',
    'authority': 'shop.rewe.de',
    'sec-fetch-site': 'same-origin',
}

params = (
    ('market', '231006'),
    ('objectsPerPage', '100'),
    ('page', '0'),
    ('serviceTypes', 'DELIVERY,PARCEL'),
    ('sorting', 'RELEVANCE_DESC'),
    ('source', ''),
)

def scraper(cheapie_scraper, params):
    product_names = []
    product_prices = []
    product_pics = []
    page = requests.get("https://shop.rewe.de/api/products", headers=header, cookies=cookies, params=params)

    json_response = json.loads(page.content)

    #print(json_response)

    for product in json_response['_embedded']['products']:
        print(product)

    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    results1 = soup.find_all()

    for result in results1:
        print(result.prettify())

def scrapeMarkets(cheapie_scraper):
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    db_cursor.execute("SELECT CompanyID FROM Company WHERE CompanyName = 'REWE Markt GmbH'")
    exec_res1 = db_cursor.fetchall()

    for x in exec_res1:
        print(x)
        
    db_cursor.execute(f"SELECT CompanyInternalID FROM Branch WHERE Company = {exec_res1[0][0]}")
    exec_res2 = db_cursor.fetchall()

    for x in exec_res2:
        scrapeStarter(cheapie_scraper, x[0])

def scrapeStarter(cheapie_scraper, marketID):
    i = 1

    while i < 20:
        params = (
            ('market', f'{marketID}'),
            ('objectsPerPage', '100'),
            ('page', f'{i}'),
            ('serviceTypes', 'DELIVERY,PICKUP'),
            ('sorting', 'RELEVANCE_DESC'),
            ('source', ''),
        )

        scraper(cheapie_scraper, params)
        i += 1