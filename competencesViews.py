from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import CompetencesUtilisateurs, db

competences_bp = Blueprint('competences', __name__)

@competences_bp.route('/competences', methods=['GET'])
@jwt_required()
def get_competences():
    # Récupérer l'identifiant de l'utilisateur à partir du token JWT
    user_id = get_jwt_identity()

    # Récupérer les compétences de l'utilisateur à partir de la table competencesutilisateurs
    competences = CompetencesUtilisateurs.query.filter_by(idUtilisateur=user_id).all()

    # Convertir les compétences en une liste de dictionnaires
    competences_dict = [{'id': c.idCompetence, 'nom': c.competence.nomCompetence, 'avancement': c.avancementCompetences} for c in competences]

    # Renvoyer les compétences dans la réponse JSON
    return jsonify(competences=competences_dict)
