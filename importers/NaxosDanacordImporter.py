from importers.GenericImporter import GenericImporter


class NaxosDanacordImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def get_row(self, row):
        _, label, cd_number, upc, composer, title, artist, _, medium, year, cost, _, price_code, *_ = row
        row_dict = dict()
        row_dict["year"] = year
        row_dict["label"] = label
        row_dict["cd_number"] = cd_number
        row_dict["upc"] = upc
        row_dict["composer"] = composer
        row_dict["title"] = title
        row_dict["artist"] = artist
        row_dict["medium"] = medium
        row_dict["cost"] = cost
        row_dict["price_code"] = price_code

        return row_dict

    def execute_row(self, row):
        super().execute_row(row)
        row_dict = self.get_row(row)
        year = row_dict["year"]
        label = row_dict["label"]
        cd_number = row_dict["cd_number"]
        upc = row_dict["upc"]
        composer = row_dict["composer"]
        title = row_dict["title"]
        artist = row_dict["artist"]
        medium = row_dict["medium"]
        cost = row_dict["cost"]
        price_code = row_dict["price_code"]

        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                            price)
            self.update_price_code(upc, price_code)
            print("update")
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                         price)
            self.update_price_code(upc, price_code)
            print("add")
