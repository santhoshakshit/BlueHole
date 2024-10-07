import csv
import sqlite3
from venv import create

# Connect to SQLite database
conn = sqlite3.connect("chitti.db")
cursor = conn.cursor()

def add_single_contact(name, mobile_no):
    """Insert a single contact into the contacts table."""
    conn = sqlite3.connect('chitti.db')
    cursor = conn.cursor()
    
    try:
        # Insert the new contact
        cursor.execute('''INSERT INTO contacts (name, mobile_no) VALUES (?, ?)''', (name, mobile_no))
        conn.commit()
        print(f"Added new contact: {name} with mobile number: {mobile_no}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Example usage: Adding a single contact
# You can replace these values with actual input or use this as a function call
contact_name = "enter_name"
contact_mobile_no = "enter_no"

add_single_contact(contact_name, contact_mobile_no)
