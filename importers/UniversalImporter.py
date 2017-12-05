from importers.GenericImporter import GenericImporter


class UniversalFullImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        label, _, year, artist, title, cd_number, upc, _, _, _, cost, medium, _ = row
        composer = ""
        distributor = "Universal"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            self.update_pricing(cost, price, upc)
            print("update")
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                      price)
            print("add")


class UniversalDiscontinuer(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        upc = row[0]

        self.discontinue(upc)