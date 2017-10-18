from importers.GenericImporter import GenericImporter


class NaxosMonthlyImporter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

