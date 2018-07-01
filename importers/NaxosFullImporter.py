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

    def get_row(self, row):
        year, upc, cd_number, composer, title, artist, _, medium, _, label, cost, _, price_code, blurb, *_ = row
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

        return row_dict

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
    def __init__(self, db):
        super().__init__(db)

    def get_row(self, row):
        year, _, label, cd_number, upc, composer, title, artist, _, medium, cost, blurb, *_ = row
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
            # self.update_price_code(upc, price_code)
            print("add")


class NaxosVendorNewJulyCodingImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def get_row(self, row):
        year, label, cd_number, upc, composer, title, artist, _, medium, cost, _, blurb, *_ = row
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
            # self.update_price_code(upc, price_code)
            print("add")
