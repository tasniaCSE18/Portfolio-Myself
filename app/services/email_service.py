import smtplib
from email.mime.text import MIMEText

from app.core.config import settings
from app.core.logger import get_logger
from app.schemas.contact import ContactRequest, ContactResponse

logger = get_logger(__name__)


class EmailService:
    def send_contact_message(self, contact: ContactRequest) -> ContactResponse:
        full_message = f"""
    Name: {contact.name}
    Email: {contact.email}

    Message:
    {contact.message}
    """

        msg = MIMEText(full_message)
        msg["Subject"] = contact.subject
        msg["From"] = settings.GMAIL_ADDRESS
        msg["To"] = settings.GMAIL_ADDRESS

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(settings.GMAIL_ADDRESS, settings.GMAIL_APP_PASSWORD)
            server.sendmail(
                settings.GMAIL_ADDRESS,
                settings.GMAIL_ADDRESS,
                msg.as_string(),
            )
            server.quit()
            return ContactResponse(message="Message sent successfully!", status_code=200)
        except Exception as exc:
            logger.error("Failed to send email: %s", exc)
            return ContactResponse(message="Failed to send message", status_code=500)
