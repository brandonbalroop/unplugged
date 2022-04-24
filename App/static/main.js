
import json
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db, User, Pokemon, MyPokemon

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

''' Set up JWT here '''
def authenticate(username, password):
  user = User.query.filter_by(username=username).first()
  if(user and user.check_password(password)):
    return user

def identity(payload):
  return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)

''' End JWT Setup '''


@app.route('/')
def index():
  profile = profile.query.limit(50).all()
  return render_template('index.html')

@app.route('/app')
def client_app():
  return app.send_static_file('app.html')




#Sign up
@app.route('/signup', methods=['POST'])
def signup():
  data = request.get_json()
  newuser = User(username=data['username'], email=data['email'])
  newuser.set_password(data['password'])
  db.session.add(newuser)
  db.session.commit()
  return ("user created")

#Login
@app.route('/auth', methods=['POST'])
def login():
  data = request.get_json()
  user = authenticate(data['username'], data['password'])
  return JWT(app, user, identity)

#Save my profile
@app.route('/myprofile', methods=['POST'])
@jwt_required()
def save_my_profile():
  data = request.get_json()
  pokemon = MyProfile(pid=data['pid'], name=data['name'], id=current_identity.id)
  db.session.add(profile)
  db.session.commit()
  return (data['name'] + " captured")

#Get my account
@app.route('/myprofile', methods=['GET'])
@jwt_required()
def get_my_profile():
  my_profile = MyProfile.query.filter_by(id=current_identity.id).all()
  my_profile = [profile.toDict() 
  return json.dumps(my_profile)



#Delete my profile
@app.route('/myprofile/<nth>', methods=['DELETE'])
@jwt_required()
def delete_my_nth_profile(nth):
  nrows = MyProfile.query.filter_by(id=current_identity.id).count()
  if(nrows > 0):
    try:
      my_pokemon = MyProfile.query.filter_by(id=current_identity.id).limit(1)[int(nth) - 1]
      if(my_profile):
        db.session.delete(my_profile)
        db.session.commit()
        return ("Profile delieted!")
    except IndexError:
      return ("Invalid Index")
 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
