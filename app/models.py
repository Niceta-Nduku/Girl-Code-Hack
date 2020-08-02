from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

db.metadata.clear()

class Student(UserMixin,db.Model):
    "Create students table"

    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(60),index=True,nullable=False)
    surname = db.Column(db.String(60),index=True, unique=True,nullable=False) 
    level = db.Column(db.String(60), nullable=False) #has only one level
    mentorship = db.Column(db.Boolean, default=False) #wants a mentor or not
    interests = db.relationship("Interests", backref = "student", lazy="dynamic", viewonly=False, order_by = "Interests.id")
    mentor = db.Column(db.Integer, db.ForeignKey('professionals.id'))
    mentor_type = db.Column(db.Integer, db.ForeignKey('profession_type.id'))
    location = db.Column(db.Integer, db.ForeignKey('locations.id'))
    about = db.Column(db.Text)

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

@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))



class Professional(UserMixin,db.Model):

    __tablename__ = 'professionals'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(60),index=True,nullable=False)
    username = db.Column(db.String(60),index=True, unique=True,nullable=False) 
    mentor = db.Column(db.Boolean, default=False) #wants a mentor or not
    profession_type = db.Column(db.Integer, db.ForeignKey('profession_type.id'))
    location = db.Column(db.Integer, db.ForeignKey('locations.id'))
    company = db.Column(db.Integer, db.ForeignKey('organisations.id'))
    linkedIn = db.Column(db.String(120), index=True, unique=True)
    about = db.Column(db.Text)
    interests = db.relationship("Interests", backref = "professional", viewonly=False, order_by = "Interests.id")

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
    
    #add login_manager

    def __repr__(self):
        return '<Professional: {}>'.format(self.username)

class Interests(db.Model):

    __tablename__ = "Interests"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), unique=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    professional_id = db.Column(db.Integer, db.ForeignKey('professionals.id'))

    def __repr__(self):
        return '<Interests: {}>'.format(self.id)

class organisation(UserMixin, db.Model):

    __tablename__ = 'organisations'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable= False, unique=True)
    website = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.Text)
    email = db.Column(db.String(120), index=True, unique=True)
    opportunities = db.relationship('opportunity', backref='Organisation', lazy=True)
    location = db.Column(db.Integer, db.ForeignKey('locations.id'))
    employees = db.relationship('Professional', backref='Organisation', lazy=True)
    

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
        return '<Student: {}>'.format(self.id)

class opportunity(db.Model):
    __table_args__ = {'extend_existing': True} 
    __tablename__ = 'opportunities'

    id = db.Column(db.Integer, primary_key=True)
    opp_type = db.Column(db.String(120),nullable= False)
    duration = db.Column(db.Integer)
    dpplication_deadline = db.Column(db.DateTime)
    description = db.Column(db.Text)
    paying = db.Column(db.Boolean, default=False) 
    location =  db.Column(db.Integer, db.ForeignKey('locations.id'))
    organisation =  db.Column(db.Integer, db.ForeignKey('organisations.id'))

    def __repr__(self):
        return '<Student: {}>'.format(self.id)

class locations(db.Model):

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80),unique=True)
    country = db.Column(db.String(80))

    def __repr__(self):
        return '<Student: {}>'.format(self.id)

class Levels(db.Model):

    __tablename__ = 'student_level'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), unique=True)

    def __repr__(self):
        return '<student_level: {}>'.format(self.id)

class Profession_type(db.Model):

    __tablename__= 'profession_type'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(60), unique=True)

    def __repr__(self):
        return '<profession_type: {}>'.format(self.id)


