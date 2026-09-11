from dataclasses import dataclass


@dataclass
class ChatRequest:
    message: str

    @classmethod
    def from_dict(cls, data: dict) -> "ChatRequest":
        return cls(message=(data.get("message") or "").strip())


@dataclass
class ChatResponse:
    response: str

    def to_dict(self) -> dict:
        return {"response": self.response}
