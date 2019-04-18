import pymongo
from pymongo import MongoClient
import csv
import configparser

"""
Connection Information
"""
config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['mongo_connection']


ships = None
classes = None


def load_data():
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

    existing = classes.find({})

    if existing.count() < 1:
        data = load_data()
        for d in data[0]:
            add_class(d)
        for d in data[1]:
            add_ship(d)


class_keys = ('class', 'type', 'country', 'numGuns', 'bore', 'displacement')
ship_keys = ('class', 'name', 'launched')


def to_list(keys, document):
    record = []
    for key in keys:
        record.append(document[key])
    return record


def join(keys, document, record):
    for key in keys:
        record.append(document[key])
    return record


def get_classes():
    for item in classes.find({}):
        yield to_list(class_keys, item)


def get_ships(class_name):
    if not class_name:
        for item in ships.find({}):
            yield to_list(ship_keys, item)
    else:
        matching_ships = ships.find({'class': class_name})
        for item in matching_ships:
            yield to_list(ship_keys, item)


def add_class(data):
    classes.insert({'class': data[0], 'type': data[1], 'country': data[2], 'numGuns': data[3], 'bore': data[4], 'displacement': data[5]})


def add_ship(data):
    ships.insert({'name': data[0], 'class': data[1], 'launched': data[2]})


def delete_class(class_name):
    ships.delete_many({'class': class_name})
    classes.delete_one({'class': class_name})


def delete_ship(ship_name, class_name):
    ships.delete_one({'name': ship_name, 'class': class_name})


def connect_to_db(conn_str):
    global classes
    global ships
    client = MongoClient(conn_str)
    classes = client.cmps364.classes
    ships = client.cmps364.ships
    return client


# This establishes the connection, conn will be used across the lifetime of the program.
conn = connect_to_db(connection_string)
seed_database()