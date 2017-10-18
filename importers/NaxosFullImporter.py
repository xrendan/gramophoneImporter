from importers.GenericImporter import GenericImporter


class NaxosFullImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

    def execute_row(self, row):
        super().execute_row()
        _, label, _, cd_number, title, upc, _, _, year, artist, composer, medium, _ = row
        cost = 0
        distributor = "Naxos"

        distributor_id = self.get_distributor_id(distributor)
        label_id = self.get_label_id(label, distributor_id)
        medium_id = self.get_medium_id(medium)
        price = 0

        if self.check_upc(upc):
            pass
        else:
            self.add_row(title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost, price)
            print("add")
