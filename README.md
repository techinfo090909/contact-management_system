Contact Management System

A simple Python-based Contact Management System that allows users to manage their contacts from the command line.

The project was built with a focus on clean code, basic validation, file handling, and a simple modular structure. Contact data is stored in a JSON file so that it remains available when the application is run again.

Features

- Add a new contact
- View all saved contacts
- Search for a contact
- Update contact details
- Delete a contact
- Validate user input
- Handle invalid inputs and errors
- Store contact data in JSON format
- Run unit tests for core functionality
- Simple command-line interface

Technologies Used

- Python 3
- JSON
- Object-Oriented Programming
- File Handling
- Exception Handling
- "unittest"

Project Structure

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

Project Architecture

The project follows a simple modular structure where each component has a specific responsibility.

                    main.py
                       │
                       ▼
              contact_manager.py
                ↙        ↓        ↘
          models.py  validators.py  storage.py
                                      │
                                      ▼
                              data/contacts.json

Architecture Flow

main.py starts the application and handles user interaction.

contact_manager.py contains the main contact management operations.

models.py defines the structure of a contact.

validators.py handles input validation.

storage.py manages reading and writing contact data.

data/contacts.json stores the contact information permanently.

This separation keeps the project organized and makes individual parts easier to understand and maintain.

File Overview

"main.py"

The main file of the application. It starts the program and provides the menu through which the user can perform different contact management operations.

"contact_manager.py"

Contains the main logic for managing contacts, including adding, viewing, searching, updating, and deleting contacts.

"models.py"

Contains the "Contact" model used to represent contact information in the application.

"validators.py"

Contains functions used to validate contact details and user input.

"storage.py"

Handles saving and loading contact data from the JSON file.

"data/contacts.json"

Stores the contact information so that data is not lost when the application is closed.

"tests/test_contact_manager.py"

Contains unit tests for checking the main contact management functionality.

"screenshots/"

Contains screenshots of the application while it is running.

"PROJECT_REPORT.md"

Contains the detailed project report, including the project objective, implementation details, testing, and other information.

How to Run

1. Open the Project

Open the project folder in VS Code.

2. Open the Terminal

Make sure the terminal is opened in the project directory.

3. Run the Application

python main.py

If the above command does not work, try:

py main.py

Application Menu

When the application starts, the user can select different options from the menu:

1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Filter by Group
7. Sort Contacts
8. Contact Statistics
9. Exit

The available options may vary depending on the final implementation of the application.

How the Application Works

The application follows a simple flow:

Start Application
       │
       ▼
Display Menu
       │
       ├── Add Contact
       │
       ├── View Contacts
       │
       ├── Search Contact
       │
       ├── Update Contact
       │
       ├── Delete Contact
       |
       |__ Filter by Group
       |
       |__ Sort Contacts
       |
       |__ Contact Statistics
       │
       └── Exit

When a contact is added or updated, the information is stored in "data/contacts.json".

When the application starts again, the saved contacts are loaded from the same file.

Validation and Error Handling

Basic validation and error handling are included to make the application more reliable.

The application handles situations such as:

- Invalid menu choices
- Invalid contact information
- Missing contact records
- Incorrect user input
- File-related errors
- JSON data handling errors

This helps prevent the application from terminating unexpectedly because of normal user mistakes.

Testing

Unit tests are included in the project to check important parts of the contact management functionality.

Run All Tests

From the project directory, run:

python -m unittest discover -s tests

Run the Test File Directly

python -m unittest tests/test_contact_manager.py

The test file is located at:

tests/test_contact_manager.py

Screenshots

Screenshots of the working application are stored in the:

screenshots/

folder.

They show the application running through the command-line interface and demonstrate some of its main operations.

Data Storage

The project uses a JSON file for storing contact information.

data/contacts.json

Using a separate storage module keeps the data-handling code independent from the main application logic.

Learning Outcomes

While working on this project, I practiced:

- Python programming
- Functions and modules
- Lists and dictionaries
- Classes and objects
- File handling
- JSON data handling
- Input validation
- Exception handling
- Modular code organization
- Unit testing

Future Improvements

Some features that could be added in the future are:

- Graphical User Interface
- SQLite database support
- Import and export of contacts
- Better search and filtering
- Contact sorting
- More detailed input validation
- User authentication
- Web-based version of the application

Author

[MOHAMMED YAROOQUE AHMED]

B.Tech Computer Science Engineering(AI/ML) Student

Project Purpose

This project was developed as part of a ML project/internship learning activity to practice building a small, functional application using Python and to understand how different parts of a project can be organized into separate modules.

License

This project is created for educational and internship purposes.