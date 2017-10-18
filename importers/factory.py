from importers.NaxosMonthlyImporter import NaxosMonthlyImporter
from importers.NaxosFullImporter import NaxosFullImporter
from importers.OutsideImporter import OutsideImporter
from importers.NaxosDeleter import NaxosDeleter
from importers.SonyPriceChanger import SonyPriceChanger
from importers.WarnerDistributorChanger import WarnerDistributorChanger
from importers.NaxosGuildImporter import NaxosGuildImporter


def factory(import_type, db):
    if import_type == "Naxos_Monthly": return NaxosMonthlyImporter(db)
    if import_type == "Naxos_Full": return NaxosFullImporter(db)
    if import_type == "Naxos_Deleter": return NaxosDeleter(db)
    if import_type == "Outside": return OutsideImporter(db)
    if import_type == "Sony_Price_Changer": return SonyPriceChanger(db)
    if import_type == "Warner_Distributor_Changer": return WarnerDistributorChanger(db)
    if import_type == "Naxos_Guild_Importer": return NaxosGuildImporter(db)
    else:
        raise SyntaxError
