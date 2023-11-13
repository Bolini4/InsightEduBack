from flask import Blueprint, request
import json
from .models import Utilisateur
from . import db

views = Blueprint('views',__name__)

def return_users():
    utilisateurs_data = db.session.query(Utilisateur).all()
    result = ""
    for utilisateur in utilisateurs_data:
        result += f"{utilisateur}"
    print(result)
    return result


@views.route('/')
def index():
    return(return_users())

@views.route('/user/<int:user_id>')
def user(user_id):
    print("there")
    utilisateur = db.session.query(Utilisateur).filter_by(id=user_id).first()
    print(utilisateur.nom)
    if utilisateur is None:
        return "Utilisateur non trouvé"
    else:
        return str(utilisateur.nom)
    
@views.route("/login", methods=['POST'])
def check_login():

    mail = request.form.get('email')
    password = request.form.get('password')
    with app.app_context():
        user = db.session.query(Utilisateur).filter_by(email=mail, password=password).first()
    
    if user is None:
        return(json.dumps({"statut":0,"resultat":None}))
    else:
        jsonresult =json.dumps( {
                "statut": 1,
                "resultat": {
                    "nom": user.nom,
                    "prenom":user.prenom,
                    "email":user.email,
                    "userType":user.userType   
                }
                })
        return(jsonresult)
    

    
@views.route("/addUser", methods=['POST'])
def addUser():
    print('addingUser')
    with app.app_context():
        new_user = Utilisateur(nom="tetsnom", prenom="tetsprenom", email="testemail", password="tetstpassword", userType="testUserType")
        db.session.add(new_user)
        db.session.commit()
    print('shouldbedone')
    return 'done'
