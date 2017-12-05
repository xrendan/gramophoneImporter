class GenericImporter():
    def __init__(self, db):
        self.db = db
        self.c = db.cursor()

    def check_upc(self, upc):
        self.c.execute("""SELECT upc from inventory WHERE upc = %s""", (upc,))
        return self.c.rowcount

    def get_medium_id(self, medium):
        self.c.execute("""SELECT medium_id from medium where name = %s""", (medium,))
        if not self.c.rowcount:
            self.c.execute("""INSERT INTO medium (name) VALUES (%s)""", (medium,))
            self.c.execute("""SELECT LAST_INSERT_ID()""")

        return self.c.fetchone()[0]

    def get_label_id(self, label, distributor_id):
        self.c.execute("""SELECT label_id from label where label_name = %s""", (label,))
        if not self.c.rowcount:
            self.c.execute("""INSERT INTO label (label_name, distributor_id) VALUES (%s, %s)""",
                           (label, distributor_id))
            self.c.execute("""SELECT LAST_INSERT_ID()""")
        else:
            return self.c.fetchone()[0]

    def get_distributor_id(self, distributor):
        self.c.execute("""SELECT distributor_id from distributor where distributor_name = %s""", (distributor,))
        if not self.c.rowcount:
            raise ValueError(f"Could not find distributor: {distributor} in database")
        else:
            return self.c.fetchone()[0]

    def get_inventory_id(self, upc):
        self.c.execute("""SELECT inventory_id from inventory WHERE upc = %s""", (upc,))
        if not self.c.rowcount:
            raise ValueError(f"Could not find item with upc: {upc} in database")
        else:
            return self.c.fetchone()[0]

    def get_title(self, upc):
        self.c.execute("""SELECT cd_title from inventory WHERE upc = %s""", (upc,))
        if not self.c.rowcount:
            raise ValueError(f"Could not find item with upc: {upc} in database")
        else:
            return self.c.fetchone()[0]

    def add_pricing(self, cost, price):
        self.c.execute("""INSERT INTO inventory_pricing 
            (inventory_id, unit_cost, unit_sell, store_id) 
            VALUES (LAST_INSERT_ID(), %s, %s, 1) """,
                       (cost, price))

    def update_pricing(self, cost, price, upc):
        inventory_id = self.get_inventory_id(upc)
        self.c.execute(f"""UPDATE inventory_pricing SET
                    unit_cost = %s,
                    unit_sell = %s
                    WHERE inventory_id = %s""",
                       (cost, price, inventory_id))

    def add_row(self, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                price, blurb="NULL"):
        self.c.execute("""INSERT INTO inventory 
                       (cd_title,
                        medium_id,
                        distributor_cd_number,
                        upc,
                        artist,
                        composer,
                        catalogue_listing_year,
                        label_id,
                        distributor_id,
                        entered_on, 
                        updated, 
                        distributor_sales_blurb,
                        distributor_stocklevel,
                        distributor_last_updated,
                        category_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW(), %s, 0, NOW(), 133)""",
                       (title, medium_id, cd_number, upc, artist, composer, year, label_id, distributor_id, blurb))
        if not self.c.rowcount:
            print(f"failed insert on upc {upc}")
        else:
            self.add_pricing(cost, price)

    def discontinue(self, upc):
        try:
            old_title = self.get_title(upc)
            new_title = "DISC" + old_title
            self.c.execute("""UPDATE inventory SET
                                cd_title = %s,
                                updated = NOW()
                                WHERE upc = %s """,
                           (new_title, upc))
        except ValueError:
            pass

    def update_row(self, title, upc, medium_id, cd_number, composer, artist, year, label_id, distributor_id, cost,
                   price):
        self.c.execute("""UPDATE inventory SET
                    cd_title = %s,
                    medium_id = %s,
                    distributor_cd_number = %s,
                    artist = %s,
                    composer = %s,
                    catalogue_listing_year = %s,
                    label_id = %s,
                    distributor_id = %s,
                    updated = NOW()
                    WHERE upc = %s """,
                       (title, medium_id, cd_number, artist, composer, year, label_id, distributor_id, upc))

        if not self.c.rowcount:
            print(f"failed update on upc {upc}")
        elif cost != 0:
            self.update_pricing(cost, price, upc)

    def delete_row(self):
        pass

    def get_sales_price(self, cost):
        return int(float(cost) * 1.67 + 0.05) - 0.01

    def execute_row(self, row):
        pass

    def commit(self):
        self.db.commit()
