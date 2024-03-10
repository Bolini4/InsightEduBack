from . import db
import datetime


class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    userType = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, nom, prenom, email, password, userType, token):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.userType = userType
        self.token = token

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,id,jti,created_at):
        self.id = id
        self.jti = jti
        self.created_at = created_at

class Competences(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nomCompetence = db.Column(db.String)
    idGroupeCompetences = db.Column(db.Integer)

    def __init__(self, id, nomCompetence, idGroupeCompetences):
        self.id = id
        self.nomCompetence = nomCompetence
        self.idGroupeCompetences = idGroupeCompetences
    
class CompetencesUtilisateurs(db.Model):
    __tablename__ = 'competencesutilisateurs'

    idUtilisateur = db.Column(db.Integer, db.ForeignKey('utilisateurs.id'), primary_key=True)
    idCompetence = db.Column(db.Integer, db.ForeignKey('competences.id'), primary_key=True)
    avancementCompetences = db.Column(db.Integer)
    edited_at = db.Column(db.DateTime, default=datetime.datetime, onupdate=datetime.datetime)

    def __init__(self, idUtilisateur, idCompetence, avancementCompetences):
        self.idUtilisateur = idUtilisateur
        self.idCompetence = idCompetence
        self.avancementCompetences = avancementCompetences
