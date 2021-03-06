import MySQLdb
from importers.factory import factory

db = MySQLdb.connect("localhost", "root", "76trombones", "weberp")
if __name__ == "__main__":
    import csv
    from sys import argv

    # type must be in importers.factory
    import_type = argv[1]
    importer = factory(import_type, db)

    # Filename is second argument
    filename = argv[2]

    commit = True if (len(argv) > 3 and argv[3] == "commit") else False
    verify = True if (len(argv) > 3 and argv[3] == "verify") else False
    try:
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            csvin = csv.reader(csvfile)
            for idx, row in enumerate(csvin):
                importer.execute_row(row)
                print(idx)
                if verify:
                    importer.verify(row)
                    break
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as csvfile:
            csvin = csv.reader(csvfile)
            for idx, row in enumerate(csvin):
                importer.execute_row(row)
                print(idx)
                if verify:
                    importer.verify(row)
                    break

    if commit:
        importer.commit()
