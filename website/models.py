from . import db


class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    userType = db.Column(db.String)

    def __init__(self, nom, prenom, email, password, userType):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.userType = userType