Simple Tkinter GUI for Displaying a List of People from an SQLite Database
==========================================================================

.. module:: people_list_gui
   :platform: any
   :synopsis: A program for displaying a list of people from an SQLite database using a Tkinter graphical interface.

.. moduleauthor:: Your Name

Tkinter and SQLite Module
--------------------------

.. note::
   To run this program, you need to have the Tkinter and SQLite modules installed for Python.

Code Example
------------

.. code-block:: python

   import tkinter as tk
   import sqlite3

   # Establish or connect to the database
   conn = sqlite3.connect('people.db')
   c = conn.cursor()

   # ... (other code)

   root = tk.Tk()
   root.title("List of People")

   # ... (other code)

   root.mainloop()

Functions
---------

.. autofunction:: display_people
   :noindex:

   Function to retrieve and display a list of people from the database.

   :return: None

Database Structure
------------------

The database contains a single table "people" with the following fields:
- `id` (INTEGER): unique identifier
- `first_name` (TEXT): person's first name
- `last_name` (TEXT): person's last name
- `age` (INTEGER): person's age

Notes
-----

The program automatically creates the `people.db` database file if it doesn't exist and populates it with data from a dictionary on first run.

The program automatically closes the connection to the database upon exiting.

This is the translated documentation for a program that displays a list of people from an SQLite database using a Tkinter graphical interface. The documentation describes the database structure, functions, and program features.
