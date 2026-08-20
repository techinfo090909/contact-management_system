from contact_manager import ContactManager


APP_TITLE = "CONTACT MANAGEMENT SYSTEM"


def print_header(title: str) -> None:
    """Display a formatted section header."""
    print("\n" + "=" * 60)
    print(f"{title:^60}")
    print("=" * 60)


def display_contact(contact) -> None:
    """Display a single contact in a readable format."""
    print(
        f"ID: {contact.contact_id}\n"
        f"Name: {contact.name}\n"
        f"Phone: {contact.phone}\n"
        f"Email: {contact.email}\n"
        f"Group: {contact.group}\n"
        f"Created: {contact.created_at}\n"
        f"Updated: {contact.updated_at}"
    )
    print("-" * 60)


def display_contacts(contacts) -> None:
    """Display a list of contacts."""
    if not contacts:
        print("\nNo contacts found.")
        return

    print(f"\nFound {len(contacts)} contact(s):\n")

    for contact in contacts:
        display_contact(contact)


def add_contact(manager: ContactManager) -> None:
    """Handle contact creation."""
    print_header("ADD CONTACT")

    try:
        name = input("Name  : ")
        phone = input("Phone : ")
        email = input("Email : ")
        group = input("Group : ")

        contact = manager.add_contact(
            name=name,
            phone=phone,
            email=email,
            group=group,
        )

        print("\n✓ Contact added successfully.")
        print(f"Contact ID: {contact.contact_id}")

    except ValueError as error:
        print(f"\n✗ {error}")


def view_contacts(manager: ContactManager) -> None:
    """Display all contacts."""
    print_header("ALL CONTACTS")

    contacts = manager.get_all_contacts()
    display_contacts(contacts)


def search_contacts(manager: ContactManager) -> None:
    """Search contacts."""
    print_header("SEARCH CONTACT")

    query = input("Enter name, phone, email, or group: ").strip()

    if not query:
        print("\n✗ Search query cannot be empty.")
        return

    contacts = manager.search_contacts(query)
    display_contacts(contacts)


def update_contact(manager: ContactManager) -> None:
    """Handle contact updates."""
    print_header("UPDATE CONTACT")

    contact_id = input("Enter Contact ID: ").strip()

    if not contact_id:
        print("\n✗ Contact ID cannot be empty.")
        return

    try:
        existing = next(
            (
                contact
                for contact in manager.get_all_contacts()
                if contact.contact_id.lower() == contact_id.lower()
            ),
            None,
        )

        if existing is None:
            print(f"\n✗ Contact '{contact_id}' was not found.")
            return

        print("\nPress Enter to keep the existing value.\n")

        name = input(f"Name [{existing.name}]: ").strip()
        phone = input(f"Phone [{existing.phone}]: ").strip()
        email = input(f"Email [{existing.email}]: ").strip()
        group = input(f"Group [{existing.group}]: ").strip()

        updated = manager.update_contact(
            contact_id=contact_id,
            name=name if name else None,
            phone=phone if phone else None,
            email=email if email else None,
            group=group if group else None,
        )

        print("\n✓ Contact updated successfully.")
        display_contact(updated)

    except ValueError as error:
        print(f"\n✗ {error}")


def delete_contact(manager: ContactManager) -> None:
    """Handle contact deletion with confirmation."""
    print_header("DELETE CONTACT")

    contact_id = input("Enter Contact ID: ").strip()

    if not contact_id:
        print("\n✗ Contact ID cannot be empty.")
        return

    try:
        contact = next(
            (
                item
                for item in manager.get_all_contacts()
                if item.contact_id.lower() == contact_id.lower()
            ),
            None,
        )

        if contact is None:
            print(f"\n✗ Contact '{contact_id}' was not found.")
            return

        display_contact(contact)
        confirmation = input(
            "Are you sure you want to delete this contact? (y/n): "
        ).strip().lower()

        if confirmation != "y":
            print("\nDeletion cancelled.")
            return

        manager.delete_contact(contact_id)

        print("\n✓ Contact deleted successfully.")

    except ValueError as error:
        print(f"\n✗ {error}")


def filter_by_group(manager: ContactManager) -> None:
    """Display contacts from a selected group."""
    print_header("FILTER BY GROUP")

    group = input("Enter group name: ").strip()

    if not group:
        print("\n✗ Group cannot be empty.")
        return

    try:
        contacts = manager.filter_by_group(group)
        display_contacts(contacts)

    except ValueError as error:
        print(f"\n✗ {error}")


def sort_contacts(manager: ContactManager) -> None:
    """Sort contacts by a selected field."""
    print_header("SORT CONTACTS")

    print("1. Name")
    print("2. Group")
    print("3. Email")

    choice = input("\nSelect sorting option: ").strip()

    sort_options = {
        "1": "name",
        "2": "group",
        "3": "email",
    }

    sort_by = sort_options.get(choice)

    if sort_by is None:
        print("\n✗ Invalid sorting option.")
        return

    try:
        contacts = manager.sort_contacts(sort_by)
        display_contacts(contacts)

    except ValueError as error:
        print(f"\n✗ {error}")


def show_statistics(manager: ContactManager) -> None:
    """Display contact statistics."""
    print_header("CONTACT STATISTICS")

    statistics = manager.get_statistics()

    print(f"Total Contacts : {statistics['total_contacts']}")
    print(f"Total Groups   : {statistics['total_groups']}")

    print("\nContacts by Group:")

    if not statistics["contacts_by_group"]:
        print("No group data available.")
        return

    for group, count in sorted(
        statistics["contacts_by_group"].items()
    ):
        print(f"  • {group}: {count}")


def display_menu() -> None:
    """Display the main application menu."""
    print("\n" + "=" * 60)
    print(f"{APP_TITLE:^60}")
    print("=" * 60)

    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Filter by Group")
    print("7. Sort Contacts")
    print("8. Contact Statistics")
    print("9. Exit")

    print("=" * 60)


def main() -> None:
    """Start and run the Contact Management System."""

    try:
        manager = ContactManager()

    except RuntimeError as error:
        print(f"\n✗ Application startup failed: {error}")
        return

    print_header(APP_TITLE)
    print("Welcome! Manage your contacts efficiently and securely.")

    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            add_contact(manager)

        elif choice == "2":
            view_contacts(manager)

        elif choice == "3":
            search_contacts(manager)

        elif choice == "4":
            update_contact(manager)

        elif choice == "5":
            delete_contact(manager)

        elif choice == "6":
            filter_by_group(manager)

        elif choice == "7":
            sort_contacts(manager)

        elif choice == "8":
            show_statistics(manager)

        elif choice == "9":
            print("\nThank you for using Contact Management System.")
            print("Goodbye!")
            break

        else:
            print("\n✗ Invalid choice. Please select an option from 1 to 9.")


if __name__ == "__main__":
    main()