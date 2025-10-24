Contact Management System

A simple command-line based Contact Management System built with Python. This tool allows users to add, view, edit, and delete contacts, with persistent storage using a JSON file.

Features

    Add new contacts with name, phone number, and email
    View all saved contacts in a formatted list
    Edit existing contact details
    Delete contacts by name
    Automatically saves data to contacts.json

Technologies Used

    Python 3.x
    JSON for data storage
    Standard libraries: os, json

File Structure contact_manager.py # Main script containing all functionality contacts.json # Auto-generated file storing contact data

How to Run

    Make sure you have Python 3 installed.
    Save the script as contact_manager.py.
    Open a terminal and run: python contact_manager.py

Menu Options

    Add a new contac
    View all contacts
    Edit an existing contact
    Delete a contact
    Save and exit program

Data Persistence All contacts are stored in a local file named contacts.json. This file is automatically created and updated as you use the system.

Notes

    Contact names must be unique.
    Leaving fields blank during editing retains the existing values.
    The program ensures data is saved before exiting.

