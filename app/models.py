import sqlalchemy

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    admin = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @property
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'admin': self.admin,
            'avatar': self.avatar,
            'active': self.active,
            'created_at': str(self.created_at) if self.created_at else None,
            'connections': [cxn.dict for cxn in self.user_1s] + [cxn.dict for cxn in self.user_2s]
        }


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)

    user_1_id = db.Column(db.BigInteger, db.ForeignKey('user.id', ondelete="CASCADE"))
    user_2_id = db.Column(db.BigInteger, db.ForeignKey('user.id', ondelete="CASCADE"))

    user_1 = db.relationship("User", foreign_keys=[user_1_id], backref=sqlalchemy.orm.backref('user_1s'))
    user_2 = db.relationship("User", foreign_keys=[user_2_id], backref=sqlalchemy.orm.backref('user_2s'))

    @property
    def dict(self):
        return {
            'user_1': {
                'id': self.user_1_id,
                'name': self.user_1.name
            },
            'user_2': {
                'id': self.user_2_id,
                'name': self.user_2.name
            },
            'id': self.id,
        }
