from flask import Blueprint, request
from flask_jwt_extended import get_jwt,jwt_required,JWTManager
import json
from .models import Utilisateur
from .models import TokenBlocklist
from . import db

from datetime import datetime
from datetime import timedelta
from datetime import timezone


views = Blueprint('views',__name__)


@views.route('/', methods=["POST","GET"])
@jwt_required()
def index():
    return("coucouLogged")

@views.route('/user/<int:user_id>')
def user(user_id):
    print("there")
    utilisateur = db.session.query(Utilisateur).filter_by(id=user_id).first()
    print(utilisateur.nom)
    print(utilisateur.password)
    if utilisateur is None:
        return "Utilisateur non trouvé"
    else:
        return str(utilisateur.nom)


@views.route('/getIdUser', methods=["GET"])
@jwt_required()
def getIdUser():
    jti = get_jwt()["jti"]
    token = request.headers.get("Authorization")
    now = datetime.now(timezone.utc)
    parts = token.split(' ')
    if len(parts) == 2 and parts[0].lower() == 'bearer':
        jwt_token = parts[1]
        print(jwt_token)
    else:
        print("La chaîne ne commence pas par 'Bearer'")
    user = Utilisateur.query.filter_by(token=jwt_token).first()
    print(user.id)
    return(str(user.id))
#TO CLEAR
@views.route('/test')
def test():
    value = "tokenExample"
    time = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(id=None,jti=value,created_at=time))
    db.session.commit()
    return("added to db")

    


