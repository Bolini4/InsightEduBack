from flask import Blueprint, request
from flask_jwt_extended import jwt_required
import json
from .models import Utilisateur
from . import db

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
    


