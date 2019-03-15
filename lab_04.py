# ~~~~~~~~~~~~~~~~~~~~~~~~~
# Written by Harrison Weiss
# ~~~~~~~~~~~~~~~~~~~~~~~~~

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
            print()
            id_from_user = int(input("Please enter a user id (-1 to exit): "))
            if id_from_user == -1:
                print('Program exiting.')
                sys.exit(0)
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
            totals = list()
            cursor.execute(
                'Select o.serialnumber, m.price, m.ManufacturerID \
                    from Orders o \
                        join machines ma on o.serialnumber = ma.serialnumber \
                        join models m on ma.modelnumber = m.id \
                        where o.customerid = %s',
                (id, )
            )
            totals.append(cursor.rowcount)
            item = cursor.fetchone()
            while item != None:
                print(f'    {item[0]:5}      {item[1]:5}            {item[2]}')
                item = cursor.fetchone()
            print('---------------------------------------------------------')
            cursor.execute(
                'Select SUM(m.price)\
                    from Orders o \
                        join machines ma on o.serialnumber = ma.serialnumber \
                        join models m on ma.modelnumber = m.id \
                        where o.customerid = %s',
                (id, )
            )
            totals.append(cursor.fetchone())
            print(f'Total number of machines purchased:        {totals[0]}')
            print(f'Total cost of purchases:              {totals[1][0]:5}')

        print_customers()
        print("~~~~~~~~~~~~~")
        while(True):
            id_from_user = get_id()

            print()
            print('----- Purchase History ----------------------------------')
            print('{0:5} {1:5} {2:5}'.format(
                '  Serial #  |', '  Price  |', '   Manufacturer'))
            print('---------------------------------------------------------')
            purchase_history(id_from_user)
