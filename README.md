# My Bucket List CLI

A command-line interface application for managing your personal goals and dreams.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [CLI Script (cli.py)](#cli-script-(cli.py))
- [Helper Functions (helpers.py)](#helper-functions-(helpers.py))
- [Database Models (models.py)](#database-models-(models.py))
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)

## Overview

My Bucket List CLI is a Python-based application that allows users to create, manage, and track their personal bucket list items directly from the command line. Whether you're planning your next adventure, setting personal goals, or just keeping track of your dreams, this app provides an intuitive interface to help you stay organized and motivated.

## File Structure 
```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── __init__.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    |   └── dreams.db
    |   └── database.py
    ├── debug.py
    └── helpers.py
    ├── migrations
    │   ├── version
    │   └── env.py
    |   └── README
    |   └── __pycache__   
```

## Features

- 📝 Add new quests with titles, descriptions, and deadlines
- ✏️ Edit existing quests
- ✅ Mark quests as completed
- 🗑️ Delete quests
- 📋 View all quests with filtering options
- 🔍 Search quests by keywords
- 🏷️ Categorize quests for better organization
- ⏰ Set and track deadlines for time-sensitive goals
- 📊 Monitor your progress with completion statistics
- 💾 Export and import your bucket list data

## CLI Script (cli.py)
   The cli.py file is the heart of our application. It provides the main entry point and user interface for the My Bucket List CLI.
   Main Functions:

   clear_screen(): Clears the terminal screen for a clean interface.
   print_header(): Displays a stylized header for the application.
   print_menu(): Shows the main menu options to the user.
   main(): The core function that runs the CLI loop, handling user input and calling appropriate helper functions.

## Helper Functions (helpers.py)
   The helpers.py file contains the core functionality of my application. Each function corresponds to a specific user action:

   add_quest(): Prompts the user for quest details and adds it to the database.
   edit_quest(): Allows the user to modify an existing quest's details.
   complete_quest(): Marks a specified quest as completed.
   delete_quest(): Removes a quest from the database.
   list_quest(): Displays all quests, with options for filtering.
   search_quests(): Allows the user to search for quests by keyword.
   manage_categories(): Provides a sub-menu for category management.
   check_deadlines(): Checks for and notifies about upcoming quest deadlines.


## Database Models (models.py)
   The models.py file defines the database schema using SQLAlchemy ORM. It has the following main models:

   Quest: Represents individual bucket list items, with attributes like title, description, deadline, and completion status.
   User: Manages user accounts (for potential multi-user functionality).
   Category: Allows for the categorization of quests.
   ItemCategory: Facilitates many-to-many relationships between quests and categories.

   
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/toel-kamanda34/python-dream-catcher
   cd my-bucket-list-cli
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```
   alembic upgrade head
   ```

## Usage

To start the application, run:

```
python lib/cli.py
```

Follow the on-screen prompts to navigate through the application and manage your bucket list items.

## Database Schema

The application uses SQLAlchemy ORM with SQLite. Here's an overview of the main tables:

- **Quest**: Stores individual bucket list items
- **User**: Manages user accounts
- **Category**: Allows for quest categorization
- **ItemCategory**: Facilitates many-to-many relationships between quests and categories

For a detailed view of the schema, please refer to the `models.py` file.

📌 **Note**: This project is part of a learning journey and is continuously evolving. Feedback and suggestions are always welcome!

