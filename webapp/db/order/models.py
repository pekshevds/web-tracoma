from webapp.db.common import db, Directory


class Order(db.Model, Directory):
    carrier_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    consignee_address = db.Column(db.String(255))
    consignee_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    consignee_phone = db.Column(db.String(255))
    declared = db.Column(db.Float)
    desc = db.Column(db.Text)
    point_from_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    point_to_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    shipper_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)
    shipper_address = db.Column(db.String(255))
    shipper_contact_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    shipper_phone = db.Column(db.String(255))
    weight = db.Column(db.Float)
    volume = db.Column(db.Float)

    def __repr__(self) -> str:
        return f"<Cargo {self.title}, {self.id}>"
