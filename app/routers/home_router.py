from flask import Blueprint, render_template

from app.services.portfolio_service import PortfolioService

home_bp = Blueprint("home", __name__)
portfolio_service = PortfolioService()


@home_bp.route("/")
def home():
    portfolio = portfolio_service.get_portfolio_context()
    return render_template(
        "index.html",
        personal_info=portfolio["personal_info"],
        experience=portfolio["experience"],
        education=portfolio["education"],
        projects=portfolio["projects"],
        publications=portfolio["publications"],
        book_chapter=portfolio.get("book_chapter"),
        awards=portfolio["awards"],
    )
