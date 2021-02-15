from flask import Flask



app=Flask('__name__', template_folder='katalog/templates', static_folder='katalog/static')
app.config['SECRET_KEY']="gamariamandar"


#registari bluprint
from katalog.admin.routes import radmin
app.register_blueprint(radmin)