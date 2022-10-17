from webapp.db.common import db, Directory
        

class Point(db.Model, Directory):
    
    short = db.Column(db.String(10))

    def __repr__(self) -> str:
        return f"<Point {self.title}, {self.id}>"
