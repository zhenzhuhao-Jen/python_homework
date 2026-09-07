#Task1
import sqlite3

#define function to populate tables

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", [name])
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("SELECT * FROM Subscribers WHERE name = ? AND address = ?", (name, address))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"There is already a subscriber {name} at address {address}.")
            return
        cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
    except sqlite3.IntegrityError:
        print("error adding subscriber")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id , magazine_id))
        results = cursor.fetchall()
        if len(results) > 0:
            print(f"subscriber {subscriber_id } already subscribed magazine {magazine_id}.")
            return
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?,?,?)", (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print("error adding subscription")
    
# Connect to a new SQLite database
with  sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    try:
        # Task2
        # Create tables
        #publishers: publisher_id;name
        #magazines: magazine_id; name, publisher_id
        #subscribers: subscriber_id; name; address;
        #subscriptions: subscripotion_id; subscriber_id; magazine_id; expiration_date (a string) 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)   
        )
        """)

        add_publisher(cursor, "Time USA, LLC")
        add_publisher(cursor, "Hearst Magazines Inc.")
        add_publisher(cursor, "Dotdash Meredith")
        add_magazine(cursor, "Time", 1)
        add_magazine(cursor, "Cosmopolitan", 2)
        add_magazine(cursor, "People", 3)
        add_subscriber(cursor, "John", "12345 gold fish dr, Jersey City, NJ")
        add_subscriber(cursor, "William", "67890 green turtle ln, Vienna, VA")
        add_subscriber(cursor, "Jane", "45636 yellow bird ct, Miami, FL")
        add_subscription(cursor, 1, 1, "2027-10-02")
        add_subscription(cursor, 2, 2, "2027-11-12")
        add_subscription(cursor, 3, 3, "2028-03-05")

        conn.commit()
    except sqlite3.IntegrityError:
        print("ERROR")
    #conn.close()

#Task 4 

    #retrieve all information from the subscribers table

    cursor.execute("SELECT * FROM Subscribers")
    result = cursor.fetchall()
    for row in result:
        print(row)

    #retrieve all magazines sorted by name

    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    result = cursor.fetchall()
    for row in result:
            print(row)

    #find magazines for a particular publisher by using JOIN

    cursor.execute("SELECT Magazines.name  FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.name = 'Dotdash Meredith'")
    result = cursor.fetchall()
    for row in result:
            print(row)
