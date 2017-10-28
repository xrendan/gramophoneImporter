from importers.GenericImporter import GenericImporter


class NaxosMonthlyUpcAdder(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def add_upc(self, upc):
        self.c.execute("""INSERT INTO upc 
                       (upc)
                        VALUES (%s)""",
                       (upc,))
        if not self.c.rowcount:
            print(f"failed insert on upc {upc}")

    def execute_row(self, row):
        super().execute_row(row)
        _, label, cd_number, upc, artist, composer, title, medium, _, cost, _, year, blurb = row

        self.add_upc(upc)
