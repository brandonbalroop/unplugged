from werkzeug.security import check_password_hash, generate_password_hash
from App.database import 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    routeslist = db.relationship('Routeslist', backref='user_routeslist')

     def toDict(self):
      return {
        "id": self.id,
        "username": self.username,
        "password": self.password
      }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Routeslist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    route = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)

class Route(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    startlocation = db.Column(db.String(120), nullable=False)
    endlocation = db.Column(db.String(120), nullable=False)
    lastupdate= db.Column(db.String(120), nullable=False)
    distance= db.Column(db.Float, nullable=False)
    maxifare= db.Column(db.Integer, nullable=False)
    taxifare= db.Column(db.Integer, nullable=False)
    routeslist = db.relationship('Routeslist', backref='route_routeslist')
    

    def toDict(self):
        return {
            "id":self.id,
            "startlocation":self.startlocation,
            "endlocation":self.endlocation,
            "lastupdate":self.lastupdate,
            "distance":self.distance,
            "maxifare":self.maxifare,
            "taxifare":self.taxifare
        }


