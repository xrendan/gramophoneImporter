from importers.GenericImporter import GenericImporter


class NaxosDeleter(GenericImporter):
    def __init__(self, db):
        super().__init__(db)

