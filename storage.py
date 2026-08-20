import json
from pathlib import Path
from typing import List

from models import Contact


DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "contacts.json"


def ensure_data_file() -> None:
    """Create the data directory and JSON file if they do not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_contacts() -> List[Contact]:
    """Load contacts from the JSON file."""
    ensure_data_file()
    print("READING FILE:", DATA_FILE.resolve())

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Contact data must be stored as a list.")

        return [Contact.from_dict(item) for item in data]

    except json.JSONDecodeError as error:
        raise RuntimeError(
            "The contacts data file is corrupted or contains invalid JSON."
        ) from error

    except (KeyError, TypeError) as error:
        raise RuntimeError(
            "The contacts data contains an invalid record."
        ) from error


def save_contacts(contacts: List[Contact]) -> None:
    """Save all contacts to the JSON file."""
    ensure_data_file()

    data = [contact.to_dict() for contact in contacts]

    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except OSError as error:
        raise RuntimeError(
            "Unable to save contacts. Please check file permissions."
        ) from error