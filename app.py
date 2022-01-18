from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import flask_sqlalchemy

app = Flask(__name__)

# Definindo caminho do arquivo do banco de dados
# ----------------------------------------------
## sqlite:'///' --> indica que o caminho até o arquivo será relativo
## 'app.db'     --> nome do arquivo do banco sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Vinculando o banco de dados ao nosso app. Flask
# -----------------------------------------------
## SQLAlchemy() --> classe responsável por realizar o vínculo
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self) -> str:
        return self.name

@app.route('/')
def index():
    users = User.query.all() # SELECT * FROM USERS;
    return render_template('user.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
 