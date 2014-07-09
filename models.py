from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    

    def __repr__(self):
        return '<User %r>' % (self.nickname)

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
