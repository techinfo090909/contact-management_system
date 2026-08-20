# Project Report

## Contact Management System

### Python Project

---

## 1. Project Overview

The **Contact Management System** is a modular Python-based application designed to manage contact information efficiently. It provides users with a simple interface to add, view, search, update, and delete contacts.

The application uses **JSON-based local storage**, allowing contact information to remain available between program executions. The project demonstrates practical use of Python fundamentals, modular programming, Object-Oriented Programming, file handling, input validation, and exception handling.

---

## 2. Project Objectives

The main objectives of this project are:

- To develop a functional contact management application using Python.
- To implement CRUD operations for contact records.
- To organize the application using a modular architecture.
- To validate user input and handle invalid data safely.
- To store contact information persistently using JSON.
- To apply Python programming concepts to a practical real-world problem.
- To develop a maintainable and easy-to-understand project structure.

---

## 3. Problem Statement

Managing contacts manually can become difficult as the number of contacts increases. Users need a simple way to store, find, modify, and remove contact information.

The Contact Management System solves this problem by providing a centralized application where users can manage their contact records through a simple Python interface.

---

## 4. Proposed Solution

The proposed system provides a menu-driven contact management application.

Users can perform operations such as:

1. Add a contact
2. View All contacts
3. Search contact
4. Update contact
5. Delete contact
6. Filter by Group
7. Sort contact
8. Contact Statistics
9. Exit the application

The contact data is stored in a JSON file so that the information can be reused when the application is opened again.

---

## 5. Technologies Used

| Technology        | Purpose                               |
|-------------------|---------------------------------------|
| Python 3          | Core programming language             |
| JSON              | Persistent data storage               |
| OOP               | Data modeling and code organization   |
| File Handling     | Reading and writing contact data      |
| Exception Handling| Managing runtime errors               |
| Pytest            | Automated testing                     |

---

## 6. System Requirements

### Hardware Requirements

- Basic computer or laptop
- Minimum 4 GB RAM recommended
- Basic storage space

### Software Requirements

- Python 3.x
- VS Code or any Python-compatible IDE
- Terminal / Command Prompt
- Pytest for running tests

---

## 7. Project Architecture

The project follows a modular architecture where each component has a specific responsibility.

```text
                    main.py
                       │
                       ▼
              contact_manager.py
                ↙        ↓        ↘
          models.py  validators.py  storage.py
                                      │
                                      ▼
                                 contacts.json
```

### Module Responsibilities

#### `main.py`

Handles the application's main menu, user interaction, and program flow.

#### `contact_manager.py`

Contains the main business logic for managing contacts, including adding, searching, updating, and deleting contacts.

#### `models.py`

Defines the Contact data model and represents the structure of a contact.

#### `validators.py`

Validates user-provided information and helps prevent invalid contact data.

#### `storage.py`

Handles persistent storage by reading contact records from and writing contact records to the JSON file.

#### `contacts.json`

Stores contact records locally in JSON format.

---

## 8. Project Structure


Contact Management System/
│
├── main.py
├── contact_manager.py
├── models.py
├── validators.py
├── storage.py
│
├── data/
│   └── contacts.json
│
├── tests/
│   └── test_contact_manager.py
│
├── screenshots/
│
├── README.md
└── PROJECT_REPORT.md




## 9. Key Features

### 9.1 Add Contact

Users can create a new contact by entering relevant information such as:

- Name
- Phone number
- Email
- Group

### 9.2 View Contacts

The system displays the stored contacts so users can easily review their contact list.

### 9.3 Search Contact

Users can search for a contact using available identifying information.

### 9.4 Update Contact

Existing contact information can be modified when details change.

### 9.5 Delete Contact

Users can remove unwanted contact records from the system.

### 9.6 Contact Groups

Contacts can be organized into groups such as:

- Family
- Friends
- Work
- College
- Other

### 9.7 Input Validation

The system validates user input before processing it. This helps prevent invalid or incomplete data from being stored.

### 9.8 Exception Handling

Exception handling is used to manage unexpected situations without unnecessarily terminating the application.

### 9.9 Persistent Storage

Contact records are stored in a JSON file, allowing data to remain available after the application is closed.

---

## 10. CRUD Operations

The system implements the fundamental CRUD operations:

| Operation         | Description               |
|-------------------|---------------------------|
| Create            | Add a new contact         |
| Read              | View and search contacts  |
| Update            | Modify an existing contact|
| Delete            | Remove a contact          |

CRUD functionality is one of the core requirements of many real-world data management applications.

---

## 11. Data Storage

The application uses a JSON file for local data persistence.

Example structure:

```json
[
    {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "rahul@example.com",
        "group": "Friends"
    }
]
```

JSON was selected because it is lightweight, human-readable, and easy to process using Python's built-in `json` module.

---

## 12. Input Validation and Error Handling

Input validation is implemented to improve the reliability of the application.

Examples include:

- Checking required fields
- Validating phone number format
- Validating email input
- Handling invalid menu selections
- Handling missing records
- Handling invalid JSON data
- Handling file-related errors

Exception handling helps prevent unexpected application crashes and provides a better user experience.

---

## 13. Application Workflow

The general workflow of the application is:

```text
Start
  │
  ▼
Display Main Menu
  │
  ▼
User Selects Operation
  │
  ├── Add Contact ──────┐
  ├── View Contacts ────┤
  ├── Search Contact ───┤
  ├── Update Contact ───┤
  ├── Delete Contact ───┤
  └── Group Management ─┘
                         │
                         ▼
                  Validate Input
                         │
                         ▼
                  Process Request
                         │
                         ▼
                  Update JSON Data
                         │
                         ▼
                   Return to Menu
                         │
                         ▼
                       Exit
```

---

## 14. Testing

Testing is performed to verify that important application operations work as expected.

### Test Areas

- Adding a valid contact
- Searching for an existing contact
- Updating contact information
- Deleting a contact
- Handling invalid input
- Handling missing contacts
- Reading and writing JSON data

Tests can be executed using:


python -m pytest


---

## 15. Expected Output

When the application starts, the user is presented with a menu containing the available contact management operations.

Example:

```text
=================================
     CONTACT MANAGEMENT SYSTEM
=================================

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Manage Groups
7. Exit

Enter your choice:
```

The exact menu and output may vary depending on the final implementation.

---

## 16. Advantages of the System

- Simple and user-friendly
- Modular code structure
- Easy to maintain
- Uses persistent local storage
- Includes input validation
- Includes exception handling
- Demonstrates practical Python programming
- Can be extended with additional features

---

## 17. Challenges Faced

During development, common challenges include:

- Designing a clean modular structure
- Managing JSON data correctly
- Validating different types of user input
- Handling invalid user operations
- Maintaining data consistency during updates and deletions
- Separating business logic from user-interface code
- Testing different possible input scenarios

These challenges helped improve understanding of software design and practical Python development.

---

## 18. Learning Outcomes

Through this project, the following concepts were practiced:

- Python programming fundamentals
- Functions and modules
- Lists and dictionaries
- Object-Oriented Programming
- File handling
- JSON data processing
- Input validation
- Exception handling
- CRUD operations
- Modular architecture
- Basic automated testing
- Project documentation

---

## 19. Future Scope

The project can be further enhanced by adding:

- Graphical User Interface (GUI)
- SQLite or MySQL database integration
- Contact import and export
- CSV support
- Advanced search and filtering
- Contact statistics dashboard
- Profile pictures
- Authentication and user accounts
- Cloud synchronization
- REST API integration
- Web-based interface

---

## 20. Conclusion

The **Contact Management System** successfully demonstrates how Python can be used to develop a practical data management application.

The project combines modular programming, Object-Oriented Programming, CRUD operations, JSON-based persistent storage, input validation, exception handling, and testing into a single application.

The modular architecture makes the system easier to understand, maintain, test, and extend. The project also provides a strong foundation for future improvements such as database integration, GUI development, and web-based functionality.

---

## 21. Author

**MOHAMMED YAROOQUE AHMED**

### Project Type

Python Application / Contact Management System

### Purpose

Developed as a practical Python project to demonstrate programming fundamentals, software design, data handling, validation, testing, and documentation.
