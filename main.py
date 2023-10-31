from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/projetisfec'

db = SQLAlchemy(app)

metadata = MetaData()

with app.app_context():
    metadata.reflect(bind=db.engine)

Utilisateur = metadata.tables['utilisateurs']

@app.route('/')
def index():
    with app.app_context():
        utilisateurs_data = db.session.query(Utilisateur).all()
    result = ""
    for utilisateur in utilisateurs_data:
        result += f"{utilisateur}"
    print(result)
    return result

@app.route('/user/<int:user_id>')
def user(user_id):
    with app.app_context():
        utilisateur = db.session.query(Utilisateur).filter_by(id=user_id).first()
    if utilisateur is None:
        return "Utilisateur non trouvé"
    else:
        return str(utilisateur)


if __name__ == '__main__':
    app.run()
