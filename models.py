from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Dict


@dataclass
class Contact:
    contact_id: str
    name: str
    phone: str
    email: str
    group: str
    created_at: str
    updated_at: str

    @classmethod
    def create(
        cls,
        contact_id: str,
        name: str,
        phone: str,
        email: str,
        group: str
    ):
        current_time = datetime.now().isoformat(timespec="seconds")

        return cls(
            contact_id=contact_id,
            name=name,
            phone=phone,
            email=email,
            group=group,
            created_at=current_time,
            updated_at=current_time
        )

    def to_dict(self) -> Dict:
        """Convert contact object into a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict):
        """Create a Contact object from dictionary data."""
        return cls(
            contact_id=data["contact_id"],
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            group=data["group"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )