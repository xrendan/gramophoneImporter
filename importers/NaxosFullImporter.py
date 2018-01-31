from importers.GenericImporter import GenericImporter


class NaxosFullImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        cd_number, upc, composer, title, artist, _, cost, _, label, year, medium, _ = row

        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            # self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
            #           price)
            # print("update")
            pass
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                         price)
            print("add")


class NaxosVendorCodingImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        year, upc, cd_number, composer, title, artist, _, medium, _, label, cost, _, price_code, blurb, *_ = row

        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            # self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
            #           price)
            # print("update")
            pass
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                         price)
            self.update_price_code(upc, price_code)
            print("add")


class NaxosMonthlyCatalogueUpdater(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        cd_number, upc, composer, title, artist, _, cost, year, _, label, medium, *_ = row
        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            # self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
            #           price)
            # print("update")
            pass
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                         price)
            print("add")


class NaxosVendorNewCodingImporter(GenericImporter):
    # TODO DO NOT USE!!!!!!!!!!!!!!!!!!!!!!!!!
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row(row)
        year, upc, cd_number, composer, title, artist, _, medium, _, label, cost, _, price_code, blurb, *_ = row

        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = self.get_sales_price(cost)

        if self.check_upc(upc):
            # self.update_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
            #           price)
            # print("update")
            pass
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                         price)
            self.update_price_code(upc, price_code)
            print("add")
