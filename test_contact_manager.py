import unittest
from unittest.mock import patch

from contact_manager import ContactManager


class TestContactManager(unittest.TestCase):
    """Test cases for the Contact Management System."""

    def setUp(self):
        """Create a fresh ContactManager for each test."""
        self.contacts = []

        self.load_patch = patch(
            "contact_manager.load_contacts",
            return_value=self.contacts,
        )
        self.save_patch = patch(
            "contact_manager.save_contacts"
        )

        self.load_patch.start()
        self.mock_save = self.save_patch.start()

        self.manager = ContactManager()

    def tearDown(self):
        """Stop mocked dependencies after each test."""
        self.save_patch.stop()
        self.load_patch.stop()

    def test_add_contact(self):
        """Test adding a valid contact."""
        contact = self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        self.assertEqual(len(self.manager.contacts), 1)
        self.assertEqual(contact.contact_id, "C001")
        self.assertEqual(contact.name, "Rahul Sharma")
        self.assertEqual(contact.phone, "9087865432")
        self.assertEqual(contact.group, "Friends")

    def test_duplicate_contact_is_rejected(self):
        """Test that duplicate phone numbers are rejected."""
        self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        with self.assertRaises(ValueError):
            self.manager.add_contact(
                name="Amit Kumar",
                phone="9087865432",
                email="amit@example.com",
                group="College",
            )

    def test_search_contact(self):
        """Test searching contacts by name."""
        self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        results = self.manager.search_contacts("Rahul")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Rahul Sharma")

    def test_update_contact(self):
        """Test updating an existing contact."""
        contact = self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        updated = self.manager.update_contact(
            contact_id=contact.contact_id,
            name="Rahul Sharma Khan",
            group="College",
        )

        self.assertEqual(updated.name, "Rahul Sharma Khan")
        self.assertEqual(updated.group, "College")
        self.assertEqual(updated.phone, "9087865432")

    def test_delete_contact(self):
        """Test deleting an existing contact."""
        contact = self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        self.manager.delete_contact(contact.contact_id)

        self.assertEqual(len(self.manager.contacts), 0)

    def test_filter_by_group(self):
        """Test filtering contacts by group."""
        self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        self.manager.add_contact(
            name="Amit Kumar",
            phone="9876543210",
            email="amit@example.com",
            group="College",
        )

        results = self.manager.filter_by_group("Friends")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].name, "Rahul Sharma")
        def test_invalid_phone_is_rejected(self):
            """Test that an invalid phone number is rejected."""
        with self.assertRaises(ValueError):
            self.manager.add_contact(
                name="Rahul Sharma",
                phone="12345",
                email="rahul@example.com",
                group="Friends",
            )

    def test_statistics(self):
        """Test contact statistics."""
        self.manager.add_contact(
            name="Rahul Sharma",
            phone="9087865432",
            email="rahul@example.com",
            group="Friends",
        )

        self.manager.add_contact(
            name="Amit Kumar",
            phone="9876543210",
            email="amit@example.com",
            group="Friends",
        )

        statistics = self.manager.get_statistics()

        self.assertEqual(statistics["total_contacts"], 2)
        self.assertEqual(statistics["total_groups"], 1)
        self.assertEqual(
            statistics["contacts_by_group"]["Friends"],
            2,
        )


if __name__ == "__main__":
    unittest.main()