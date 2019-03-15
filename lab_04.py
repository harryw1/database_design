import psycopg2
import sys
from urllib.parse import urlparse, uses_netloc

uses_netloc.append("postgres")

##############################################################################
# You need to change the line below to use your own connection string!!!
url = urlparse(
    "postgres://jzodzvlj:j5LSIIzVVuKtJM87N9tdmCcditjMOnm2@isilo.db.elephantsql.com:5432/jzodzvlj")
##############################################################################

with psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port) as conn:
    with conn.cursor() as cursor:
        ###
        # functions go here
        ###

        def print_customers():
            """
            Program starts by printing a
            formatted list of customers
            """
            cursor.execute('Select * from Customers')
            print('~~~~~~~~~~~ Customers ~~~~~~~~~~~')
            for customer in cursor:
                print(f'{customer[0]:5}     {customer[1]:10}')

        def get_id():
            """
            Asks the user for an id and
            makes sure that the entered id
            exists in the db
            """
            existing_ids = list()
            cursor.execute('Select * from Customers')
            for customer in cursor:
                existing_ids.append(customer[0])
            id_from_user = int(input("Please enter a user id: "))
            if id_from_user not in existing_ids:
                print("User ID does not exist. Exiting.")
                sys.exit(1)
            return id_from_user

        def purchase_history(id):
            """
            Using the user ID we got from
            terminal, we are going to return
            the serial #, price, and manufacturer
            for each purchased item by that customer
            """
            cursor.execute(
                'Select * from Orders where CustomerID = %s',
                (id, )
            )
            item = cursor.fetchone()
            while item != None:
                print(f' {item[0]:5}       {item[1]:5d}           {item[2]:5}   ')
                item = cursor.fetchone()
        
        def get_machines_info(id):
            """
            Using the user ID we got from
            the terminal, we are going to 
            return the total number of mahcines
            purchased by that user
            """
            machine_info = list()
            cursor.execute(
                'Select * from Orders where CustomerID = %s;',
                (id, ))
            machine_info.append(cursor.rowcount)
            cursor.execute(
                'Select Sum(Price) from Model m Join Orders o on \
                    m.ID = o.SerialNumber where o.CustomerID = %s',
                (id, ))
            machine_info.append(cursor.fetchone())

        print_customers()
        print("~~~~~~~~~~~~~")
        while(True):
            id_from_user = get_id()

            print()
            print('----- Purchase History ----------------------------------')
            print('{0:5} {1:5} {2:5}'.format('  Serial #  |', '  Price  |', '   Manufacturer'))
            print('---------------------------------------------------------')
            print(purchase_history(id_from_user))
