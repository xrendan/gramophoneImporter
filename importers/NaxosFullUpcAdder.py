from importers.GenericImporter import GenericImporter


class NaxosFullUpcAdder(GenericImporter):
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
        _, label, _, cd_number, title, upc, _, _, year, artist, composer, medium, _ = row

        self.add_upc(upc)
