
from models.__init__ import CURSOR, CONN
import re
from datetime import datetime

class User:

    all = {}

    def __init__(self, username, email, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = datetime.now()

    def __repr__(self):
        return f"<User {self.id}: {self.username}, {self.email}>"

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 3 <= len(username) <= 20:
            self._username = username
        else:
            raise ValueError(
                "Username must be a string with length between 3 and 20 characters"
            )

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and '@' in email:
            self._email = email
        else:
            raise ValueError("Invalid email format")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of User instances """
        sql = """
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists User instances """
        sql = """
            DROP TABLE IF EXISTS users;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the username, email, and created_at values of the current User instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO users (username, email, created_at)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.username, self.email, self.created_at))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, username, email):
        """ Initialize a new User instance and save the object to the database """
        user = cls(username, email)
        user.save()
        return user

    def update(self):
        """Update the table row corresponding to the current User instance."""
        sql = """
            UPDATE users
            SET username = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.username, self.email, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current User instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM users
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a User object having the attribute values from the table row."""

        # search using the row's primary key
        user = cls.all.get(row[0])
        if user:
            # match row values 
            user.username = row[1]
            user.email = row[2]
            user.created_at = row[3]
        else:
            # if not in the dictionary, create a new instance and add to dictionary
            user = cls(row[1], row[2])
            user.id = row[0]
            user.created_at = row[3]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        """Return a list containing a User object per row in the table"""
        sql = """
            SELECT *
            FROM users
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a User object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM users
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_username(cls, username):
        """Return a User object corresponding to the first table row matching the specified username"""
        sql = """
            SELECT *
            FROM users
            WHERE username = ?
        """

        row = CURSOR.execute(sql, (username,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_email(cls, email):
        """Return a User object corresponding to the first table row matching the specified email"""
        sql = """
            SELECT *
            FROM users
            WHERE email = ?
        """

        row = CURSOR.execute(sql, (email,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def quests(self):
        """Return list of quests associated with the current user"""
        from models.quest import Quest
        sql = """
            SELECT * FROM quests
            WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [
            Quest.instance_from_db(row) for row in rows
        ]
