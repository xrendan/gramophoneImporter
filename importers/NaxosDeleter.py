from importers.GenericImporter import GenericImporter


class NaxosDeleter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        _, _, _, upc, *_ = row

        if self.check_upc(upc):
            self.discontinue(upc)
            print("deleted")
        else:
            print("Item to delete not in database")


