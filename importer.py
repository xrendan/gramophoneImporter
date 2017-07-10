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

def add_to_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id):
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
                    updated)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW()""",
                    (title, medium_id, cd_number, upc, artist, composer, year, label_id, distributor_id))
    if not cursor.rowcount:
        print(f"failed insert on upc {upc}")

def update_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label, distributor):
    cursor.execute("""UPDATE inventory SET
                cd_title = %s,
                medium_id = %s,
                distributor_cd_number = %s
                artist = %s,
                composer = %s,
                catalogue_listing_year = %s,
                label_id = %s,
                distributor_id = %s
                updated = NOW()
                WHERE upc = %s""", 
                (title, medium_id, cd_number, artist, composer, year, label_id, distributor_id, upc))
    
    if not cursor.rowcount:
        print(f"failed update on upc {upc}")

def import_naxos(cursor, row):
    title, upc, medium, cd_number, composer, artist, year, label = row
    distributor = "Naxos"

    distributor_id = get_distributor_id(cursor, distributor)
    label_id = get_label_id(cursor, label, distributor_id)
    medium_id = get_medium_id(cursor, medium)

    if check_upc(cursor, upc):
        update_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label, distributor)
    else:
        add_to_db(cursor, title, upc, medium_id, cd_number, composer, artist, year, label, distributor)



if __name__ == "__main__":
    import csv
    from sys import argv

    filename = argv[1]
    with open(argv[1], 'r', encoding='latin_1') as tsvfile:
        tsvin = csv.reader(tsvfile, delimiter='\t')

        if filename == "naxos.txt":
            for row in tsvin:
                import_naxos(c, row)
