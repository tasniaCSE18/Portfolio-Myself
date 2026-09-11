from flask import Blueprint, jsonify, request

from app.core.logger import get_logger
from app.schemas.contact import ContactRequest
from app.services.email_service import EmailService

logger = get_logger(__name__)
contact_bp = Blueprint("contact", __name__)
email_service = EmailService()


@contact_bp.route("/send-email", methods=["POST"])
def send_email():
    try:
        contact_request = ContactRequest.from_dict(request.get_json())
        response = email_service.send_contact_message(contact_request)
        return jsonify(response.to_dict()), response.status_code
    except (KeyError, TypeError) as exc:
        logger.error("Invalid contact form payload: %s", exc)
        return jsonify({"message": "Invalid form data"}), 400
    except Exception as exc:
        logger.error("Contact form error: %s", exc)
        return jsonify({"message": "Failed to send message"}), 500
