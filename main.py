from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table,select

import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/projetisfec'

db = SQLAlchemy(app)

metadata = MetaData()

with app.app_context():
    metadata.reflect(bind=db.engine)

#Init Objet <-> Tables mapping
Utilisateur = metadata.tables['utilisateurs']
Competences = metadata.tables['competences']
CompetencesUtilisateurs = metadata.tables['competencesutilisateurs']


def return_users():
    with app.app_context():
        utilisateurs_data = db.session.query(Utilisateur).all()
    result = ""
    for utilisateur in utilisateurs_data:
        result += f"{utilisateur}"
    print(result)
    return result

def generateNoneJson():
    result ={
        "statut":0,
        "resultat":None
    }
    return(json.dumps(result))

@app.route('/')
def index():
    return(return_users())

@app.route('/user/<int:user_id>')
def user(user_id):
    with app.app_context():
        utilisateur = db.session.query(Utilisateur).filter_by(id=user_id).first()
    if utilisateur is None:
        return "Utilisateur non trouvé"
    else:
        return str(utilisateur)
    
@app.route("/login", methods=['POST'])
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

if __name__ == '__main__':
    app.run()
