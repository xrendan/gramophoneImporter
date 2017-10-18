from importers.GenericImporter import GenericImporter


class OutsideImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        distributor = "Outside Distribution"
        distributor_id = self.get_distributor_id(distributor)

        cd_number, artist, title, label, _, _, upc, medium, cost, year = row
        composer = ''

        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
            print("update")
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
            print("add")
