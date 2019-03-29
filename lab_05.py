import psycopg2
import csv
from urllib.parse import urlparse, uses_netloc
import configparser

#######################################################################
# IMPORTANT:  You must set your config.ini values!
#######################################################################
# The connection string is provided by elephantsql.  Log into your account and copy it into the 
# config.ini file.  It should look something like this:
# postgres://vhepsma:Kdcads89DSFlkj23&*dsdc-32njkDSFS@foo.db.elephantsql.com:7812/vhepsma
# Make sure you copy the entire thing, exactly as displayed in your account page!
#######################################################################
config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['postgres_connection']

#  You may use this in seed_database.  The function reads the CSV files
#  and returns a list of lists.  The first list is a list of classes, 
#  the secode list is a list of ships.
def load_seed_data():
    classes = list()
    with open('classes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            classes.append(row)

    ships = list()
    with open('ships.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            ships.append(row)
    return [classes, ships]

def seed_database():
    with conn.cursor() as cursor:
        cursor.execute("create table if not exists Class (Class text, Type text, Country text, NumGuns integer, Bore real, Displacement real, primary key (Class))")
        cursor.execute("create table if not exists Ship (Name text, Class text, Launched integer, primary key (Name, Class), foreign key (Class) references Class(Class) on delete cascade)")

        try:
            data = load_seed_data()
            
            for d in data[0]:
                cursor.execute("insert into Class(Class, Type, Country, NumGuns, Bore, Displacement) values(%s, %s, %s, %s, %s, %s)", (d))

            for d in data[1]:
                cursor.execute("insert into Ship(Name, Class, Launched) values(%s, %s, %s)", (d))
        except:
            pass

        conn.commit()

# Return list of all classes.  Important, to receive full credit you
# should use a Python generator to yield each item out of the cursor.
# Column order should be class, type, country, guns, bore, displacement
def get_classes():
    with conn.cursor() as cursor:
        cursor.execute("select * from Class")

        for d in cursor.fetchall():
            yield d

        conn.commit()
   
# Return list of all ships, joined with class.  Important, to receive full credit you
# should use a Python generator to yield each item out of the cursor.
# Column order should be ship.class, name, launched, class.class, type, country, guns, bore, displacement
# If class_name is not None, only return ships with the given class_name.  Otherwise, return all ships
def get_ships(class_name):
    # If you select Ship.CLass before Name, they appear flipped in the UI, meaning the name would appear in the class column
    # and vice versa. I flipped them so that they would be in the correct order.

    with conn.cursor() as cursor:
        cursor.execute("select Name, Ship.Class, Launched, Class.Class, Type, Country, NumGuns, Bore, Displacement from Class join Ship on Ship.Class = Class.Class where Class.Class = %s;", (class_name, ))

        if not class_name:
            cursor.execute("select Name, Ship.Class, Launched, Class.Class, Type, Country, NumGuns, Bore, Displacement from Class join Ship on Ship.Class = Class.Class")

        for d in cursor.fetchall():
            yield d

    conn.commit()

# Data will be a list ordered with class, type, country, guns, bore, displacement.
def add_class(data):
    with conn.cursor() as cursor:
        cursor.execute("insert into Class (Class, Type, Country, NumGuns, Bore, Displacement) values (%s, %s, %s, %s, %s, %s)", (data))
        conn.commit()

# Data will be a list ordered with class, name, launched.
def add_ship(data):
    with conn.cursor() as cursor:
        cursor.execute("insert into Ship (Class, Name, Launched) values (%s, %s, %s)", (data))
        conn.commit()

# Delete class with given class name.  Note while there should only be one
# SQL execution, all ships associated with the class should also be deleted.
def delete_class(class_name):
    with conn.cursor() as cursor:
        cursor.execute("delete from Class where Class = %s;", (class_name, ))
        conn.commit()

# Delets the ship with the given class and ship name.
def delete_ship(ship_name, class_name):
    with conn.cursor() as cursor:
        cursor.execute("delete from Ship where Ship.Name = %s and Ship.Class = %s;", (ship_name, class_name))
        conn.commit()



# This is called at the bottom of this file.  You can re-use this important function in any python program
# that uses psychopg2.  The connection string parameter comes from the config.ini file in this
# particular example.  You do not need to edit this code.
def connect_to_db(conn_str):
    uses_netloc.append("postgres")
    url = urlparse(conn_str)

    conn = psycopg2.connect(database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port)

    return conn

# This establishes the connection, conn will be used across the lifetime of the program.
conn = connect_to_db(connection_string)
seed_database()