from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1'

    # Import Blueprints
    from .views import views
    from .auth import auth

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

#Blueprints are used to organize your code into distinct components that can be registered within the application.
# This is especially useful in larger applications or when working in a team,
# as it allows you to compartmentalize different parts of your app, such as authentication, main app logic, and feature-specific route















# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

# # Create a Flask application instance
# app = Flask(__name__)

# # Configure the SQLAlchemy database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

# # Create a SQLAlchemy database instance
# db = SQLAlchemy(app)

# # Create a LoginManager instance
# login_manager = LoginManager(app)
