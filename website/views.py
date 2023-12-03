from flask import Blueprint, request
from flask_jwt_extended import jwt_required
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

#TO CLEAR
@views.route('/test')
def test():
    value = "tokenExample"
    time = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(id=None,jti=value,created_at=time))
    db.session.commit()
    return("added to db")

    


