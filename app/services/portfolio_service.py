import json

from app.core.config import settings


class PortfolioService:
    def __init__(self) -> None:
        self._data_path = settings.DATA_DIR / "portfolio.json"

    def get_portfolio_context(self) -> dict:
        with open(self._data_path, encoding="utf-8") as file:
            return json.load(file)
