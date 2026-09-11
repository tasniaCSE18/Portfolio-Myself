from flask import Blueprint, jsonify, request

from app.ai_services.chatbot_service import ChatbotService
from app.core.logger import get_logger
from app.schemas.chat import ChatRequest, ChatResponse

logger = get_logger(__name__)
chat_bp = Blueprint("chat", __name__)
chatbot_service = ChatbotService()


@chat_bp.route("/chat", methods=["POST"])
def chat():
    try:
        chat_request = ChatRequest.from_dict(request.get_json() or {})

        if not chat_request.message:
            return jsonify(ChatResponse(
                response="Please ask me something about Tasnia!"
            ).to_dict())

        bot_response = chatbot_service.get_response(chat_request.message)
        return jsonify(ChatResponse(response=bot_response).to_dict())

    except Exception as exc:
        logger.error("Chatbot error: %s", exc)
        return jsonify(ChatResponse(
            response="Sorry, I encountered an error. Please try again!"
        ).to_dict())
