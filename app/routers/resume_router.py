import os

from flask import Blueprint, send_from_directory

from app.core.config import settings

resume_bp = Blueprint("resume", __name__)


@resume_bp.route("/resume")
def download_resume():
    resume_dir = os.path.join(settings.STATIC_DIR, "resume")
    return send_from_directory(resume_dir, "CV.pdf", as_attachment=True)
