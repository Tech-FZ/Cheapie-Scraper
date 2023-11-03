def insertStock(cheapie_scraper, product_id, product_price, branch_id, currency):
    db_cursor = cheapie_scraper.cheapie_db.cursor()

    if product_price.__contains__(","):
        product_price = product_price.replace(",", ".")

    db_cursor.execute(f"SELECT Product, Branch FROM Stock WHERE Product = {product_id} AND Branch = {branch_id}")
    exec_res2 = db_cursor.fetchall()

    try:
        if len(exec_res2) > 0:
            db_cursor.execute(f"DELETE FROM Stock WHERE Product = {product_id} AND Branch = {branch_id}")

    except:
        print("Can progress")

    stock_id = 0

    while True:
        db_cursor.execute(f"SELECT StockID FROM Stock WHERE StockID = {stock_id}")
        exec_res1 = db_cursor.fetchall()

        try:
            if len(exec_res1) > 0:
                stock_id += 1

            else:
                break

        except:
            break

    sql = "INSERT INTO Stock (StockID, Product, Branch, Price, Currency) VALUES (%s, %s, %s, %s, %s)"
    val = (stock_id, product_id, branch_id, product_price, currency)
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    db_cursor.execute(sql, val)
    cheapie_scraper.cheapie_db.commit()

def productIntoDb(cheapie_scraper, product_id, product_name, product_pic_url, type_id):
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    sql = "INSERT INTO Product (ProductID, ProductName, ProductType, PictureURL) VALUES (%s, %s, %s, %s)"
    val = (product_id, product_name, type_id, product_pic_url)
    db_cursor.execute(sql, val)
    cheapie_scraper.cheapie_db.commit()

def addProduct(cheapie_scraper, product_name, product_price, product_pic_url, branch_id, currency):
    db_cursor = cheapie_scraper.cheapie_db.cursor()
    product_id = 0

    while True:
        db_cursor.execute(f"SELECT ProductID FROM Product WHERE ProductID = {product_id}")
        exec_res2 = db_cursor.fetchall()

        try:
            if len(exec_res2) > 0:
                product_id += 1

            else:
                break

        except:
            break

    
    db_cursor.execute(f"SELECT * FROM ProductType")
    exec_res1 = db_cursor.fetchall()
    print(f"The product \"{product_name}\" is not included in the product database yet.")
    print("The following types are available: \n")

    if len(exec_res1) > 0:
        for x in exec_res1:
            print(str(x[0]) + ") " + str(x[1]))

    while True:
        need_to_repeat = True
        asking = input("Type in one of the listed type IDs to assign the product to that type or A to create a new type: ")

        if asking == "A" or asking == "a":
            type_id = 0

            while True:
                db_cursor.execute(f"SELECT TypeID FROM ProductType WHERE TypeID = {type_id}")
                exec_res3 = db_cursor.fetchall()

                try:
                    if len(exec_res3) > 0:
                        type_id += 1

                    else:
                        break

                except:
                    break

            type_name = input("Type in the name of the desired type: ")

            if type_name != "":
                db_cursor.execute(f"SELECT TypeName FROM ProductType WHERE TypeName = \"{type_name}\"")
                exec_res4 = db_cursor.fetchall()

                if len(exec_res4) <= 0:
                    sql = "INSERT INTO ProductType (TypeID, TypeName) VALUES (%s, %s)"
                    val = (type_id, type_name)
                    db_cursor.execute(sql, val)
                    cheapie_scraper.cheapie_db.commit()
                    productIntoDb(cheapie_scraper, product_id, product_name, product_pic_url, type_id)
                    need_to_repeat = False

        else:
            for x in exec_res1:
                if int(asking) == x[0]:
                    type_id = int(asking)
                    productIntoDb(cheapie_scraper, product_id, product_name, product_pic_url, type_id)
                    need_to_repeat = False

        if need_to_repeat == False:
            break

    insertStock(cheapie_scraper, product_id, product_price, branch_id, currency)