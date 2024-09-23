# My Bucket List CLI

A command-line interface application for managing your personal goals and dreams.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
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

