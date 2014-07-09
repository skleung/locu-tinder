from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    locu_id = db.Column(db.String(20))
    username = db.Column(db.String(64))
    categories = db.relationship('Category', backref = 'user', lazy = 'dynamic')
    needs = db.relationship('Need', backref = 'user', lazy = 'dynamic')
    matches = db.relationship('Matches', backref = 'user', lazy = 'dynamic')

    def __repr__(self):
        return '<User %r>' % (self.username)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    locu_str_id = db.Column(db.String(64))
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Category %r>' % (self.name)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    messages = db.relationship('Message', backref = 'match', lazy = 'dynamic')

    def __repr__(self):
        return '<Match %r>' % (self.body)

class Message(db.Model):
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<Message %r>' % (self.body)
