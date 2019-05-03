import pymongo
from pymongo import MongoClient
import csv
import configparser

customers = None
products = None
orders = None


def initialize():
    config = configparser.ConfigParser()
    config.read('config.ini')
    connection_string = config['database']['mongo_connection']
    connect_to_db(connection_string)


def get_customers():
    for item in customers.find({}):
        yield item


def get_customer(id):
    return customers.find_one({'_id': ObjectId(id)})


def upsert_customer(customer):
    if '_id' in customers.keys():
        customers.update_one({'_id': ObjectId(), 'firstName': customer[0], 'lastName': customer[1],
                              'street': customer[2], 'city': customer[3],
                              'state': customer[4], 'zip': customer[5]})
    else:
        customer.insert_one(customer)


def delete_customer(id):
    customers.delete_one({'_id': ObjectId(id)})


def get_products():
    for item in products.find({}):
        yield item


def get_product(id):
    return products.find_one({'_id': ObjectId(id)})


def upsert_product(product):
    if '_id' in products.keys():
        products.update_one(
            {'_id': ObjectId(), 'name': product[0], 'price': product[1]})
    else:
        products.insert_one(product)


def delete_product(id):
    products.delete_one({'_id': ObjectId(id)})


def get_orders():
    for item in orders.find({}):
        yield item


def get_order(id):
    return orders.find_one({'_id': ObjectId(id)})


def upsert_order(order):
    orders.insert_one(order)


def delete_order(id):
    orders.delete_one({'_id': ObjectId(id)})


def customer_report(id):
    return None


def sales_report():
    return list()

############################
# Connects to the database #
############################


def connect_to_db(conn_str):
    global customers
    global products
    global orders
    client = MongoClient(conn_str)
    customers = client.project2.customers
    products = client.project2.products
    orders = client.project2.orders
    return client
