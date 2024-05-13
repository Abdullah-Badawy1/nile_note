from flask import Flask
from generation_Q import generation_Q  # Import the blueprint
from __future__ import absolute_import
from Questgen.encoding import encoding
from Questgen.mcq import mcq
from Questgen.main import QGen, BoolQGen, AnswerPredictor


def create_app():
    app = Flask(__name__)
    app.config ['SECRET_KEY'] = 'your_secret_key'

    # Import Blueprints
    from .views import views
    from .auth import auth

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Register the question_gen blueprint
    app.register_blueprint(generation_Q, url_prefix='/api')


    return app


