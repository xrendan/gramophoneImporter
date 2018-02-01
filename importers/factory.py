from importers.NaxosMonthlyImporter import NaxosMonthlyImporter
from importers.NaxosFullImporter import *
from importers.NaxosMonthlyUpcAdder import NaxosMonthlyUpcAdder
from importers.NaxosFullUpcAdder import NaxosFullUpcAdder
from importers.OutsideImporter import OutsideImporter
from importers.NaxosDeleter import NaxosDeleter
from importers.SonyPriceChanger import SonyPriceChanger
from importers.WarnerDistributorChanger import WarnerDistributorChanger
from importers.NaxosGuildImporter import NaxosGuildImporter
from importers.UniversalImporter import *


def factory(import_type, db):
    if import_type == "Naxos_Monthly": return NaxosMonthlyImporter(db)
    if import_type == "Naxos_Full": return NaxosFullImporter(db)
    if import_type == "Naxos_Vendor": return NaxosVendorCodingImporter(db)
    if import_type == "Naxos_Monthly_UPC": return NaxosMonthlyUpcAdder(db)
    if import_type == "Naxos_Full_UPC": return NaxosFullUpcAdder(db)
    if import_type == "Naxos_Deleter": return NaxosDeleter(db)
    if import_type == "Outside": return OutsideImporter(db)
    if import_type == "Sony_Price_Changer": return SonyPriceChanger(db)
    if import_type == "Warner_Distributor_Changer": return WarnerDistributorChanger(db)
    if import_type == "Naxos_Guild_Importer": return NaxosGuildImporter(db)
    if import_type == "Universal_Full": return UniversalFullImporter(db)
    if import_type == "Universal_Discontinue": return UniversalDiscontinuer(db)
    if import_type == "Universal_Price_Code": return UniversalPriceCodeUpdater(db)
    if import_type == "Naxos_Monthly_Catalogue": return NaxosMonthlyCatalogueUpdater(db)
    if import_type == "New_Naxos_Vendor": return NaxosVendorNewCodingImporter(db)


    else:
        raise SyntaxError
