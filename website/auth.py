import json

from flask import Blueprint, request, jsonify
from .models import Utilisateur
from .models import TokenBlocklist
from flask_jwt_extended import create_access_token, unset_jwt_cookies, get_jwt_identity, get_jwt,jwt_required,JWTManager
from datetime import datetime, timedelta, timezone
from . import db
from . import jwt

blacklist = set()
auth = Blueprint('auth',__name__)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        utilisateur = Utilisateur.query.filter_by(email=email).first()#Au moment de la création de compte il faudra faire attention au fait que l'on ai que 1 fois ce mail
        
        if utilisateur:
            if password == utilisateur.password:
                access_token = create_access_token(identity=email)
                userToLog = Utilisateur.query.filter_by(email=email).first()
                print(userToLog)
                userToLog.token = access_token
                db.session.commit()
                response = {"access_token":access_token}
                print("Loggin success")
            else:
                response = "BAD"
                print("incorrect Password")

    return(response)

@auth.route("/logout", methods=["POST"])
@jwt_required()
def logout():
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
    print(user)
    user.token = None
    db.session.add(TokenBlocklist(id=None,jti=jti, created_at=now))
    db.session.commit()
    return jsonify(msg="Access token revoked")

@auth.route('/signup',methods=['GET','POST'])
def signup():
    return('signupPage')


@auth.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response