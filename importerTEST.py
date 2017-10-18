import MySQLdb

db = MySQLdb.connect("localhost", "root", "76trombones", "weberp")
c = db.cursor()


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


def import_outside(cursor, row):

    distributor = "Outside Distribution"
    distributor_id = get_distributor_id(cursor, distributor)

    cd_number, artist, title, label, _, _, upc, medium, cost, year = row
    composer = ''

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

    try:
        if argv[2] == "commit":
            commit = True
    except:
        commit = False

    if filename == "naxos.txt":
        with open(argv[1], 'r', encoding='latin_1') as tsvfile:
            tsvin = csv.reader(tsvfile, delimiter='\t')
            for idx, row in enumerate(tsvin):
                print(idx, "\n")
                import_naxos(c, row)

    elif filename == "new_naxos.csv":
        with open(argv[1], 'r', encoding='latin_1') as csvfile:
            csvin = csv.reader(csvfile)
            for row in csvin:
                import_new_naxos(c, row)

    elif filename[:7] == "outside":
        with open(argv[1], 'r', encoding='latin_1') as tsvfile:
            tsvin = csv.reader(tsvfile, delimiter='\t')
            for idx, row in enumerate(tsvin):
                print(idx, "\n", row)
                import_outside(c, row)
    else:
        pass
        # for row in tsvin:
        #     import_general(c, row)
    
    if commit:
        db.commit()
