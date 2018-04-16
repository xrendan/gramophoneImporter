from importers.GenericImporter import GenericImporter


class NaxosDeleter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def get_row(self, row):
        _, _, _, upc, *_ = row
        row_dict = dict()
        row_dict["upc"] = upc
        return row_dict

    def execute_row(self, row):
        super().execute_row(row)
        row_dict = self.get_row(row)

        if self.check_upc(row_dict["upc"]):
            self.discontinue(row_dict["upc"])
            print("deleted")
        else:
            print("Item to delete not in database")


