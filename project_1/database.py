import psycopg2
import psycopg2.extras
import configparser
import csv

from urllib.parse import urlparse, uses_netloc

#######
# Needed to use cursor_factory RealDictCursor to extract
# dictionary objects from the cursor
#######

"""
Connects to the database - don't change
"""


def connect_to_db(conn_str):
    uses_netloc.append('postgres')
    url = urlparse(conn_str)

    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)

    return conn


config = configparser.ConfigParser()
config.read('config.ini')
connection_string = config['database']['postgres_connection']
conn = connect_to_db(connection_string)
"""
Don't change
"""


def initialize():
    with conn.cursor() as cursor:
        cursor.execute('create table if not exists Customers(id serial primary key, firstName text, lastName text, \
                        street text, city text, state text, zip text);')
        cursor.execute('create table if not exists \
                        Products(id serial primary key, name text, price real);')
        cursor.execute('create table if not exists Orders(id serial primary key, customerId int, productId int, foreign key(customerId) \
                        references Customers(id) on delete cascade, \
                        foreign key (productId) references Products(id) on delete cascade, \
                        date date);')
    conn.commit()


def get_customers():
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from customers')
        for d in cursor:
            yield d


def get_customer(id):
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from customers where customers.id = %s', [id])
        return cursor.fetchone()


def upsert_customer(customer):
    with conn.cursor() as cursor:
        customer_info = [customer['firstName'], customer['lastName'], customer['street'], customer['city'], customer['state'], customer['zip']]
        if 'id' not in customer.keys():
            cursor.execute('insert into customers (firstName, lastName, street, \
                            city, state, zip) values (%s, %s, %s, %s, %s, %s)', (customer_info))
        else:
            customer_info.append(customer['id'])
            cursor.execute('update customers set firstName = %s, lastName = %s, street = %s, \
                            city = %s, state = %s, zip = %s where customers.id = %s', (customer_info))
    conn.commit()


def delete_customer(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from customers where customers.id = %s', [id])
    conn.commit()


def get_products():
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from products')
        for d in cursor:
            yield d


def get_product(id):
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from products where product.id = %s', [id])
        return cursor.fetchone()


def upsert_product(product):
    with conn.cursor() as cursor:
        product_info = [product['name'], product['price']]
        if 'id' not in product.keys():
            cursor.execute(
                'insert into products (name, price) values (%s, %s)', (product_info))
        else:
            product_info.append(product['id'])
            cursor.execute('update products set name = %s, price = %s \
                where products.id = %s', (product_info))
    conn.commit()


def delete_product(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from products where product.id = %s', [id])
    conn.commit()


def get_orders():
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from orders')
        for d in cursor:
            d['customer'] = get_customer(d['customerid'])
            d['product'] = get_customer(d['productid'])
            yield d


def get_order(id):
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute('select * from orders where order.id = %s', [id])
        return cursor.fetchone()

def upsert_order(order):
    with conn.cursor() as cursor:
        order_info = [order['customerId'], order['productId'],
                      order['date']]
        if 'id' not in order.keys():
            cursor.execute('insert into orders (customerId, productId, date) \
                values (%s, %s, %s)', (order_info))
        else:
            order_info.append(order_info['id'])
            cursor.execute('update orders set customerId = %s, productId = %s, \
                date = %s where orders.id = %s', (order_info))
        conn.commit()


def delete_order(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from orders where orders.id = %s', [id])
    conn.commit()


def customer_report(id):
    customer = get_customer(id)
    customer['orders'] = list()

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute(
            'select * from orders where orders.customerId = %s', [id])
        for d in cursor:
            d['product'] = get_product(d['productId'])
            customer['orders'].append(d)
    return customer



def sales_report():
    with conn.cursor() as cursor:
        cursor.execute('select name, avg(price) * count(orders.productId), \
                        count(orders.productId), max(date) from \
                        products left join orders on \
                        orders.productId = products.id group by products.id')
        for d in cursor:
            yield {'name': d[0], 'gross_revenue': d[1],
                   'total_sales': d[2], 'last_order_date': d[3]}