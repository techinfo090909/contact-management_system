import re


def validate_name(name: str) -> str:
    """Validate and return a properly formatted contact name."""
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if len(name) < 2:
        raise ValueError("Name must contain at least 2 characters.")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters.")

    if not re.fullmatch(r"[A-Za-z]+(?:[ '-][A-Za-z]+)*", name):
        raise ValueError(
            "Name can contain only letters, spaces, apostrophes, or hyphens."
        )

    return " ".join(word.capitalize() for word in name.split())


def validate_phone(phone: str) -> str:
    """Validate a 10-digit Indian mobile number."""
    phone = phone.strip()

    if not phone:
        raise ValueError("Phone number cannot be empty.")

    if not re.fullmatch(r"[6-9]\d{9}", phone):
        raise ValueError(
            "Phone number must contain exactly 10 digits and start with 6, 7, 8, or 9."
        )

    return phone


def validate_email(email: str) -> str:
    """Validate a standard email address."""
    email = email.strip().lower()

    if not email:
        raise ValueError("Email address cannot be empty.")

    if len(email) > 254:
        raise ValueError("Email address is too long.")

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, email):
        raise ValueError("Please enter a valid email address.")

    return email


def validate_group(group: str) -> str:
    """Validate and normalize a contact group."""
    group = group.strip()

    if not group:
        raise ValueError("Group cannot be empty.")

    if len(group) < 2:
        raise ValueError("Group must contain at least 2 characters.")

    if len(group) > 30:
        raise ValueError("Group cannot exceed 30 characters.")

    if not re.fullmatch(r"[A-Za-z0-9]+(?:[ '&_-][A-Za-z0-9]+)*", group):
        raise ValueError(
            "Group can contain letters, numbers, spaces, hyphens, "
            "underscores, apostrophes, and '&'."
        )

    return " ".join(word.capitalize() for word in group.split())