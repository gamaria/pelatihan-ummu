from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask('__name__', template_folder='katalog/templates', static_folder='katalog/static')
app.config['SECRET_KEY']="gamariamandar"

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///katalogbuku.db'
db=SQLAlchemy(app)


#registari bluprint
from katalog.admin.routes import radmin
app.register_blueprint(radmin)