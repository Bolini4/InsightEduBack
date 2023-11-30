from flask import Blueprint, request, redirect,url_for
from .models import Utilisateur
from flask_login import login_user, login_required, logout_user, current_user 
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
                print("Loggin success")
                login_user(utilisateur, remember=True)
            else:
                print("incorrect Password")

    return('loginpage')

@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()#logout the current user
    return('logoutPage')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    return('signupPage')