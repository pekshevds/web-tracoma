from datetime import datetime
from webapp.db.common import db, Directory
from webapp.db.point.fetchers import get_point_by_id


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    point_a_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    point_b_id = db.Column(db.Integer, db.ForeignKey('point.id'), nullable=False)
    distance = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        return f"<Route {get_point_by_id(id=self.point_a_id)}, {get_point_by_id(id=self.point_b_id)}>"

    def __str__(self) -> str:
        return f"<Route {self.point_a}, {self.point_b}>"

    @property
    def point_a(self):
        return get_point_by_id(self.point_a_id)

    @property
    def point_b(self):
        return get_point_by_id(self.point_b_id)
