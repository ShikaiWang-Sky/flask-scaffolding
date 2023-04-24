from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    # return a printable representation of the object
    def __repr__(self):
        return "<UserID {}>".format(self.id)
