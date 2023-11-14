# CLI Project - Phase 3

This project is a Command Line Interface (CLI) application developed as part of Phase 3 in the Moringa School curriculum. The CLI application utilizes Python, SQLAlchemy, and Click to implement a simple task management system.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This CLI application is designed to demonstrate knowledge acquired during Phase 3 of the Moringa School curriculum. It incorporates Python fundamentals, SQLAlchemy for database management, and Click for building a command-line interface. The application provides a basic task management system with user and task entities.

## Features

- **User Management:** Add and list users.
- **Task Management:** Add and list tasks associated with users.
- **SQLite Database:** Utilizes SQLAlchemy to interact with an SQLite database.
- **Virtual Environment:** Recommends the use of virtual environments (Pipenv or venv).
- **Package Structure:** Follows a proper package structure for maintainability.

## Prerequisites

Ensure that you have the following installed on your machine:

- Python 3.x
- Pipenv (optional but recommended)
- SQLite (optional)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/samakpan-sp/CLI-Phase-3.git
   cd CLI-Phase-3
   
## Set Up Virtual Environment
  * Using Pipenv (recommended)
    pipenv install --dev
    pipenv shell

## Using venv (alternative)
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux

## Install Dependencies
  pipenv install  # If using Pipenv
  pip install -r requirements.txt  # If using venv

##Usage
  python cli.py add_user <username>
  python cli.py list_users

## Contributing
  Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
  This project is licensed under the MIT License.





