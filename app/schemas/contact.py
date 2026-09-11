from dataclasses import dataclass


@dataclass
class ContactRequest:
    name: str
    email: str
    subject: str
    message: str

    @classmethod
    def from_dict(cls, data: dict) -> "ContactRequest":
        return cls(
            name=data["name"],
            email=data["email"],
            subject=data["subject"],
            message=data["message"],
        )


@dataclass
class ContactResponse:
    message: str
    status_code: int = 200

    def to_dict(self) -> dict:
        return {"message": self.message}
