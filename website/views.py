from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt, jwt_required, JWTManager
from .models import Utilisateur, TokenBlocklist
from . import db
from datetime import datetime, timedelta, timezone

views = Blueprint('views',__name__)

@views.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test success'})
# Récupérer tous les utilisateurs
@views.route('/utilisateurs', methods=['GET'])
@jwt_required()
def get_users():
    utilisateurs = Utilisateur.query.all()
    result = []
    for utilisateur in utilisateurs:
        result.append({
            'id': utilisateur.id,
            'nom': utilisateur.nom,
            'prenom': utilisateur.prenom,
            'email': utilisateur.email,
            'userType': utilisateur.userType
        })
    return jsonify(result)

# Récupérer un utilisateur par son ID
@views.route('/utilisateurs/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    utilisateur = Utilisateur.query.get_or_404(user_id)
    result = {
        'id': utilisateur.id,
        'nom': utilisateur.nom,
        'prenom': utilisateur.prenom,
        'email': utilisateur.email,
        'userType': utilisateur.userType
    }
    return jsonify(result)

# Ajouter un nouvel utilisateur
@views.route('/utilisateurs', methods=['POST'])
@jwt_required()
def add_user():
    data = request.get_json()
    new_user = Utilisateur(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        password=data['password'],
        userType=data['userType'],
        token=None
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Nouvel utilisateur ajouté'})

# Mettre à jour un utilisateur
@views.route('/utilisateurs/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    utilisateur = Utilisateur.query.get_or_404(user_id)
    utilisateur.nom = data['nom']
    utilisateur.prenom = data['prenom']
    utilisateur.email = data['email']
    utilisateur.password = data['password']
    utilisateur.userType = data['userType']
    db.session.commit()
    return jsonify({'message': 'Utilisateur mis à jour'})

# Supprimer un utilisateur
@views.route('/utilisateurs/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    utilisateur = Utilisateur.query.get_or_404(user_id)
    db.session.delete(utilisateur)
    db.session.commit()
    return jsonify({'message': 'Utilisateur supprimé'})
