from mail_app import db


class User(db.Model):
    __tablename__ = 'mail_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    passwd = db.Column(db.String(10))

    def __init__(self, username, passwd):
        self.username = username
        self.passwd = passwd

    def __repr__(self):
        return f"Username:{self.username}, Passwd:{self.passwd}"


#db.create_all()


