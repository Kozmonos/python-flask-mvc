from flask import Flask
from app.views.test import bp as test

def create_app():
    app = Flask(__name__)
    app.register_blueprint(test,url_prefix='/test')
    
    return app