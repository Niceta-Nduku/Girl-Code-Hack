from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Student(db.Model):
    "Create students table"

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(60),index=True)
    username = db.Column(db.String(60),index=True, unique=True)
    # level = db.Column(db.String(60))
    mentorship = db.Column(db.Boolean, default=False)
    # mentor = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # mentor_type = db.Column(db.Integer, db.ForeignKey('roles.id'))


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Student: {}>'.format(self.username)

# class professional:

#     __tablename__ = 'professionals'

#     def __repr__(self):
#         return '<Professional: {}>'.format(self.username)

# class interersts:

#     __tablename__ = "Interests"

#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.(db.String(60))

# class organisation:

#     __tablename__ = 'organisations'

#     def __repr__(self):
#         return '<Student: {}>'.format(self.username)

# class Opportunity:

#     __tablename__ = 'opportunities'

#     def __repr__(self):
#         return '<Student: {}>'.format(self.username)



