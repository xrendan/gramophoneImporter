import MySQLdb

db = MySQLdb.connect("localhost", "root", "76trombones", "weberp")
c = db.cursor()


def check_upc(cursor, upc):
    cursor.execute("""SELECT upc from inventory WHERE upc = %s""", upc)
    return cursor.rowcount

def get_medium_id(cursor, medium):
    "SELECT medium_id from medium where name = {medium}"

def get_label_id(cursor, label):
    pass

def import_naxos():
    title, upc, medium, cd_number, composer, artist, year, label = row




if __name__ == "__main__":
    import csv
    from sys import argv
    filename = argv[1]
    with open(argv[1], 'r', encoding='latin_1') as tsvfile:
        tsvin = csv.reader(tsvfile, delimiter='\t')

        if filename = "naxos.txt":
            for row in tsvin:
                import_naxos(db, row)
