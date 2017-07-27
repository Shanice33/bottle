from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:jhy123@119.29.205.205/WEB'
db = SQLAlchemy(app)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# eng = create_engine('mysql+mysqlconnector://shanice:ss123@119.29.205.205/WEB')
# DBSession = sessionmaker(bind=eng)
# session = DBSession()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(320),unique=True)
    phone = db.Column(db.String(32), nullable=False)

    def __init__(self,
                 username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone


if __name__ == '__main__':
    db.create_all()