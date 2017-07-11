import MySQLdb

db = MySQLdb.connect("localhost", "root", "76trombones", "weberp")
c = db.cursor()

def check_upc(cursor, upc):
    cursor.execute("""SELECT upc from inventory WHERE upc = %s""", (upc,))
    return cursor.rowcount

def get_medium_id(cursor, medium):
    cursor.execute("""SELECT medium_id from medium where name = %s""", (medium,))
    if not cursor.rowcount:
        cursor.execute("""INSERT INTO medium (name) VALUES (%s)""", (medium,))
        cursor.execute("""SELECT LAST_INSERT_ID()""")
    
    return cursor.fetchone()[0]

def get_label_id(cursor, label, distributor_id):
    cursor.execute("""SELECT label_id from label where label_name = %s""", (label,))
    if not cursor.rowcount:
        cursor.execute("""INSERT INTO label (label_name, distributor_id) VALUES (%s, %s)""", (label, distributor_id))
        cursor.execute("""SELECT LAST_INSERT_ID()""")
    else:
        return cursor.fetchone()[0]

def get_distributor_id(cursor, distributor):
    cursor.execute("""SELECT distributor_id from distributor where distributor_name = %s""", (distributor,))
    if not cursor.rowcount:
        raise ValueError(f"Could not find distributor: {distributor} in database")
    else:
        return cursor.fetchone()[0]

def add_to_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price, blurb="NULL"):
    cursor.execute("""INSERT INTO inventory 
                   (cd_title,
                    medium_id,
                    distributor_cd_number,
                    upc,
                    artist,
                    composer,
                    catalogue_listing_year,
                    label_id,
                    distributor_id,
                    entered_on, 
                    updated, distributor_sales_blurb)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW(), %s)""",
                    (title, medium_id, cd_number, upc, artist, composer, year, label_id, distributor_id, blurb))
    if not cursor.rowcount:
        print(f"failed insert on upc {upc}")
    else:
        add_pricing(cursor, cost, price)

def update_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price):
    cursor.execute("""UPDATE inventory SET
                cd_title = %s,
                medium_id = %s,
                distributor_cd_number = %s,
                artist = %s,
                composer = %s,
                catalogue_listing_year = %s,
                label_id = %s,
                distributor_id = %s,
                updated = NOW()
                WHERE upc = %s """, 
                (title, medium_id, cd_number, artist, composer, year, label_id, distributor_id, upc))
    
    if not cursor.rowcount:
        print(f"failed update on upc {upc}")
    else:
        update_pricing(cursor, cost, price, upc)

def import_naxos(cursor, row):
    title, upc, medium, cd_number, composer, artist, year, cost, label = row
    distributor = "Naxos"

    distributor_id = get_distributor_id(cursor, distributor)
    label_id = get_label_id(cursor, label, distributor_id)
    medium_id = get_medium_id(cursor, medium)
    price = get_sales_price(cost)

    if check_upc(cursor, upc):
        update_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
        print("update")
    else:
        add_to_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
        print("add")

def get_sales_price(cost):
    return int(float(cost) * 1.67 + 0.05) - 0.01

def get_inventory_id(cursor, upc):
    cursor.execute("""SELECT inventory_id from inventory WHERE upc = %s""", (upc,))
    if not cursor.rowcount:
        raise ValueError(f"Could not find item with upc: {upc} in database")
    else:
        return cursor.fetchone()[0]

def update_pricing(cursor, cost, price, upc):
    inventory_id = get_inventory_id(cursor, upc)
    cursor.execute(f"""UPDATE inventory_pricing SET
                unit_cost = %s,
                unit_sell = %s
                WHERE inventory_id = %s""",
                (cost, price, inventory_id))

def add_pricing(cursor, cost, price):
    cursor.execute("""INSERT INTO inventory_pricing 
        (inventory_id, unit_cost, unit_sell, store_id) 
        VALUES (LAST_INSERT_ID(), %s, %s, 1) """,
        (cost, price))

def import_new_naxos(cursor, row):
    _, label, cd_number, upc, artist, composer, title, medium, _, cost, _, year, blurb = row
    
    distributor = "Naxos"

    distributor_id = get_distributor_id(cursor, distributor)
    label_id = get_label_id(cursor, label, distributor_id)
    medium_id = get_medium_id(cursor, medium)
    price = get_sales_price(cost)

    if check_upc(cursor, upc):
        update_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
        print("update")
    else:
        add_to_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
        print("add")
def import_general(cursor, row):
    pass

if __name__ == "__main__":
    import csv
    from sys import argv

    filename = argv[1]
    

    if filename == "naxos.txt":
        with open(argv[1], 'r', encoding='latin_1') as tsvfile:
            tsvin = csv.reader(tsvfile, delimiter='\t')
            for idx, row in enumerate(tsvin):
                print(idx, "\n")
                import_naxos(c, row)
            db.commit()
                    
        
    elif filename == "new_naxos.csv":
        with open(argv[1], 'r', encoding='latin_1') as csvfile:
            csvin = csv.reader(csvfile)
            for row in csvin:
                import_new_naxos(c, row)
    else:
        for row in tsvin:
            import_general(c, row)

