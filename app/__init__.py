from flask import Flask

from app.core.config import settings
from app.routers import chat_bp, contact_bp, home_bp, resume_bp


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(settings.TEMPLATES_DIR),
        static_folder=str(settings.STATIC_DIR),
    )

    app.register_blueprint(home_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(resume_bp)

    return app
