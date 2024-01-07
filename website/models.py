from . import db


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