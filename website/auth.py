from flask import Blueprint, request, jsonify
from .models import Utilisateur
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from . import db

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        utilisateur = Utilisateur.query.filter_by(email=email).first()#Au moment de la création de compte il faudra faire attention au fait que l'on ai que 1 fois ce mail
        
        if utilisateur:
            if password == utilisateur.password:
                access_token = create_access_token(identity=email)
                response = {"access_token":access_token}
                print("Loggin success")
            else:
                response = "BAD"
                print("incorrect Password")

    return(response)

@auth.route('/logout',methods=['GET','POST'])
def logout():
    response = jsonify({"msg":"logout_success"})
    unset_jwt_cookies(response)
    print("coucou")
    return(response)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    return('signupPage')