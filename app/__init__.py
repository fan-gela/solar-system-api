from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
# load_dotenv()

def create_app(test_config = None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    from app.models.planet import Planet
    if not test_config:
        app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "solar_system_development")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "solar_system_test")

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app



# from flask import Flask

# def create_app(test_config=None):
#     app = Flask(__name__)

#     from .routes import planets_bp
#     app.register_blueprint(planets_bp)

#     return app