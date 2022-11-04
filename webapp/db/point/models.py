from webapp.db.common import db, Directory


class Point(db.Model, Directory):
    short = db.Column(db.String(10), default="")
    latitude = db.Column(db.Float, default=.0)
    longitude = db.Column(db.Float, default=.0)

    def __repr__(self) -> str:
        return f"<Point {self.title}, {self.id}>"

    def __str__(self) -> str:
        return f"{self.title}, {self.short}"

    @property
    def location(self):
        return (self.latitude, self.longitude)
