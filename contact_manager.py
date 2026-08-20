from datetime import datetime
from typing import List, Optional

from models import Contact
from storage import load_contacts, save_contacts
from validators import (
    validate_name,
    validate_phone,
    validate_email,
    validate_group,
)


class ContactManager:
    """Manage contacts and their persistent storage."""

    def __init__(self):
        self.contacts = load_contacts()

    # ---------- Internal Helpers ----------

    def _save(self) -> None:
        """Persist current contacts to storage."""
        save_contacts(self.contacts)

    def _find_by_id(self, contact_id: str) -> Optional[Contact]:
        """Find a contact by its unique ID."""
        return next(
            (
                contact
                for contact in self.contacts
                if contact.contact_id.lower() == contact_id.lower()
            ),
            None,
        )

    def _generate_id(self) -> str:
        """Generate the next sequential contact ID."""
        if not self.contacts:
            return "C001"

        numbers = []

        for contact in self.contacts:
            try:
                numbers.append(int(contact.contact_id[1:]))
            except (ValueError, IndexError):
                continue

        next_number = max(numbers, default=0) + 1
        return f"C{next_number:03d}"

    # ---------- Duplicate Detection ----------

    def _is_duplicate(
        self,
        phone: str,
        email: str,
        exclude_id: Optional[str] = None,
    ) -> bool:
        """Check whether phone or email already belongs to another contact."""
        for contact in self.contacts:
            if exclude_id and contact.contact_id.lower() == exclude_id.lower():
                continue

            if contact.phone == phone or contact.email.lower() == email.lower():
                return True

        return False

    # ---------- Create ----------

    def add_contact(
        self,
        name: str,
        phone: str,
        email: str,
        group: str,
    ) -> Contact:
        """Validate and add a new contact."""

        name = validate_name(name)
        phone = validate_phone(phone)
        email = validate_email(email)
        group = validate_group(group)

        if self._is_duplicate(phone, email):
            raise ValueError(
                "A contact with this phone number or email already exists."
            )

        contact = Contact.create(
            contact_id=self._generate_id(),
            name=name,
            phone=phone,
            email=email,
            group=group,
        )

        self.contacts.append(contact)
        self._save()

        return contact

    # ---------- Read ----------

    def get_all_contacts(self) -> List[Contact]:
        """Return all contacts sorted alphabetically by name."""
        return sorted(
            self.contacts,
            key=lambda contact: contact.name.lower(),
        )

    # ---------- Search ----------

    def search_contacts(self, query: str) -> List[Contact]:
        """Search contacts by name, phone, email, or group."""
        query = query.strip().lower()

        if not query:
            return []

        return [
            contact
            for contact in self.contacts
            if (
                query in contact.name.lower()
                or query in contact.phone
                or query in contact.email.lower()
                or query in contact.group.lower()
            )
        ]

    # ---------- Group Filter ----------

    def filter_by_group(self, group: str) -> List[Contact]:
        """Return contacts belonging to a specific group."""
        group = validate_group(group)

        return [
            contact
            for contact in self.contacts
            if contact.group.lower() == group.lower()
        ]

    # ---------- Update ----------
    
    def update_contact(
        self,
        contact_id: str,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        group: Optional[str] = None,
    ) -> Contact:
        """Update one or more fields of an existing contact."""

        contact = self._find_by_id(contact_id)

        if contact is None:
            raise ValueError(f"Contact '{contact_id}' was not found.")

        new_name = validate_name(name) if name is not None else contact.name
        new_phone = validate_phone(phone) if phone is not None else contact.phone
        new_email = validate_email(email) if email is not None else contact.email
        new_group = validate_group(group) if group is not None else contact.group

        if self._is_duplicate(
            phone=new_phone,
            email=new_email,
            exclude_id=contact.contact_id,
        ):
            raise ValueError(
                "Another contact already uses this phone number or email."
            )

        contact.name = new_name
        contact.phone = new_phone
        contact.email = new_email
        contact.group = new_group
        contact.updated_at = datetime.now().isoformat(timespec="seconds")

        self._save()

        return contact

    # ---------- Delete ----------

    def delete_contact(self, contact_id: str) -> Contact:
        """Delete a contact by ID."""
        contact = self._find_by_id(contact_id)

        if contact is None:
            raise ValueError(f"Contact '{contact_id}' was not found.")

        self.contacts.remove(contact)
        self._save()

        return contact

    # ---------- Sorting ----------

    def sort_contacts(self, sort_by: str = "name") -> List[Contact]:
        """Return contacts sorted by name, group, or email."""

        allowed_fields = {
            "name": lambda contact: contact.name.lower(),
            "group": lambda contact: contact.group.lower(),
            "email": lambda contact: contact.email.lower(),
        }

        if sort_by.lower() not in allowed_fields:
            raise ValueError(
                "Invalid sort option. Choose name, group, or email."
            )

        return sorted(
            self.contacts,
            key=allowed_fields[sort_by.lower()],
        )

    # ---------- Statistics ----------

    def get_statistics(self) -> dict:
        """Return basic contact statistics."""

        groups = {}

        for contact in self.contacts:
            groups[contact.group] = groups.get(contact.group, 0) + 1

        return {
            "total_contacts": len(self.contacts),
            "total_groups": len(groups),
            "contacts_by_group": groups,
        }