import psycopg2
from urllib.parse import urlparse, uses_netloc
import configparser


def initialize():
    with conn.cursor() as cursor:
        cursor.execute(
            'create table if not exists Customers(id serial primary key, first_name text, last_name text, street text, city text, state text, zip text);')
        cursor.execute(
            'create table if not exists Products(id serial primary key, name text, price real);')
        cursor.execute('create table if not exists Orders(id serial primary key, customer_id int, product_id int, foreign key(customer_id) \
                        references Customers(id) on delete cascade, \
                        foreign key (product_id) references Products(id) on delete cascade, \
                        date date);')
    conn.commit()


def get_customers():
    """
    Returns all of the customers
    in the database
    """
    with conn.cursor() as cursor:
        cursor.execute('select * from customers')
        for d in cursor:
            yield d
    conn.commit()


def get_customer(id):
    """
    Returns a single customer from the
    the customers table in the database
    """
    with conn.cursor as cursor:
        cursor.execute('select * from customers where Customers.id = %s', (id))
        cursor.fetchall()
    conn.commit()


def upsert_customer(customer):
    customer_info = list(customer.values())
    with conn.cursor() as cursor:
        if 'id' in customer.keys():  # if the customer already exists in the database
            customer_info.append(customer_info[0])
            customer_info.pop(0)
            cursor.execute(cursor.execute('update customers set first_name=%s, last_name=%s, street=%s, city=%s, state=%s, zip=%s where Customers.id=%s;', customer_info))
        else:
            cursor.execute('insert into Customers (first_name, last_name, street, \
                                city, state, zip) values (%s, %s, %s, %s, %s, %s)', (customer_info))
    conn.commit()


def delete_customer(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from Customers where Customers.id = %s', (id))
    conn.commit()


def get_products():
    with conn.cursor() as cursor:
        cursor.execute('select * from Products')
        if cursor.fetchone() != None:
            for d in cursor.fetchone():
                yield d
    conn.commit()


def get_product(id):
    with conn.cursor() as cursor:
        cursor.execute('select * from Products where Product.id = %s', (id))
        cursor.fetchall()
    conn.commit()


def upsert_product(product):
    product_info=list(product.values)
    with conn.cursor() as cursor:
        if 'id' in product.keys():
            product_info.append(product_info[0])
            product_info.pop(0)
            cursor.execute('update products set name = %s, price = %s \
                where products.id = %s', (product_info))
        else:
            cursor.execute(
                'insert into products (name, price) values (%s, %s)', (product_info))
    conn.commit()


def delete_product(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from products where product.id = %s', (id))
    conn.commit()


def get_orders():
    with conn.cursor() as cursor:
        cursor.execute('select * from orders')
        if cursor.fetchone() != None:
            for d in cursor.fetchone():
                yield d
    conn.commit()


def get_order(id):
    with conn.cursor() as cursor:
        cursor.execute('select * from orders where order.id = %s', (id))
        for d in cursor.fetchall():
            yield d
    conn.commit()


def upsert_order(order):
    order_info=list(order.values())
    with conn.cursor() as cursor:
        order_info.append(order_info[0])
        order_info.pop(0)
        if 'id' in order.keys():
            cursor.execute('update orders set customer_id = %s, product_id = %s, \
                date = %s where orders.id = %s', (order_info))
        else:
            cursor.execute('insert into orders (customer_id, product_id, date) \
                values (%s, %s, %s)', (order_info))
        conn.commit()


def delete_order(id):
    with conn.cursor() as cursor:
        cursor.execute('delete from orders where orders.id = %s', (id))
    conn.commit()


def customer_report(id):
    with conn.cursor() as cursor:
        customer=get_customer(id)
        customer['orders']=[]
        cursor.execute('select * from orders where customer_id = %s', (id))
        for order in cursor:
            order['product']=get_product(order['product_id'])
            customer['orders'].append(order)
    conn.commit()

# Return a list of products.  For each product, build
# create and populate a last_order_date, total_sales, and
# gross_revenue property.  Use JOIN and aggregation to avoid
# accessing the database more than once, and retrieving unnecessary
# information


def sales_report():
    products=get_products()
    for product in products:
        orders=[o for o in get_orders() if o['productId'] == product['id']]
        orders=sorted(orders, key=lambda k: k['date'])
        product['last_order_date']=orders[-1]['date']
        product['total_sales']=len(orders)
        product['gross_revenue']=product['price'] * product['total_sales']
    return products


def connect_to_db(conn_str):
    uses_netloc.append("postgres")
    url=urlparse(conn_str)

    conn=psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)

    return conn


config=configparser.ConfigParser()
config.read('config.ini')
connection_string=config['database']['postgres_connection']
conn=connect_to_db(connection_string)
