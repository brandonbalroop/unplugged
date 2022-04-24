from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()


class MyProfile(db.Model):
  bid = db.Column('Bid', db.Integer, primary_key=True)
  id = db.Column('Id', db.Integer, db.ForeignKey('user.id'))
  pid = db.Column('Pid', db.Integer, db.ForeignKey('profile.pid'))
  name = db.Column(db.String(50))
  pokemon = db.relationship('Profile')


  def toDict(self):
    return{
      'Name':self.username,
      'Account':self.profile.toDict()
    }


## Create a User Model
## must have set_password, check_password and to Dict


class User(db.Model):
  id = db.Column('Id', db.Integer, primary_key=True)
  username = db.Column(db.String(50))
  email = db.Column(db.String(50))
  password = db.Column(db.String(255))


  def toDict(self):
    return{
      "Id": self.id,
      "Username": self.username,
      "Email": self.email,
      "Password":self.password
    }


  def set_password(self, password):
    self.password = generate_password_hash(password, method='sha256')


  def check_password(self, password):
    return check_password_hash(self.password, password)

  //Create a new profile


class Profile(db.Model):
  pid = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(80), nullable=False)
  password = db.Column(db.String(80), nullable=False)
 

  def toDict(self):
    return{
      'Pid':self.pid,
      'Name':self.username,
      'Emaile':self.email,
      'Password':self.password,
      
    }
