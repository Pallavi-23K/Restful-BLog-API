from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from blog_api.config import Config
from blog_api.models import db
from blog_api.routes import init_routes

def create_app(test_config=None):
    app = Flask(__name__)

    # Default config (production/dev)
    app.config.from_object(Config)

    # Override with test config (for pytest)
    if test_config:
        app.config.update(test_config)

    # Initialize extensions
    db.init_app(app)
    jwt = JWTManager(app)

    # Swagger configuration
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Blog REST API",
            "description": "RESTful API for managing blog posts, comments, likes, followers, and notifications",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "bearerAuth": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        },
        "security": [{"bearerAuth": []}]
    }
    Swagger(app, template=swagger_template)

    # Register routes
    init_routes(app)

    # Create tables (only when running normally, not for tests)
    if not test_config:
        with app.app_context():
            db.create_all()

    return app

# This is the app used by flask run
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
