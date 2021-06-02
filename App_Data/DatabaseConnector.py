import sqlite3
from sqlite3 import Error
import uuid
database_path = 'utils/database/database.db'

def get_connection(db_name):
	try:
		connection = sqlite3.connect(db_name)
	except Error:
		connection = None
		print(Error)
	return connection

def prepare_query():
    querys = []
    query = '''CREATE TABLE IF NOT EXISTS shop ( shop_id TEXT PRIMARY KEY, shop_name TEXT)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS account ( account_id TEXT PRIMARY KEY, shop_id TEXT,
    account_previlege INTEGER, username TEXT, account_password TEXT)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS supplier ( supplier_id TEXT PRIMARY KEY, shop_id TEXT,
    supplier_name TEXT, supplier_address TEXT, supplier_phone TEXT)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS product ( product_id TEXT PRIMARY KEY, product_name TEXT,
    product_sale_price INTEGER, shop_id TEXT)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS product_price ( price_id TEXT PRIMARY KEY, product_id TEXT,
    product_purchase_price INTEGER, product_stock INTEGER)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS purchase_header ( purchase_id TEXT PRIMARY KEY, supplier_id
    TEXT, shop_id TEXT, payment_status INTEGER, transaction_date_time DATETIME, transaction_status INTEGER, price_change INTEGER)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS purchase_detail( purchase_id TEXT,product_id TEXT, amount INTEGER)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS sales_header ( sales_id TEXT PRIMARY KEY, account_id TEXT,
    shop_id TEXT, payment_status INTEGER, transaction_date_time DATETIME, transaction_status INTEGER, price_change INTEGER)'''
    querys.append(query)
    query = '''CREATE TABLE IF NOT EXISTS sales_detail ( sales_id TEXT, product_id TEXT, price_id TEXT,
    product_sale_price INTEGER, amount INTEGER)'''
    querys.append(query)

    for query in querys:
        make_table(query)

def make_table(query):
    connection = get_connection(database_path)
    cursorObj = connection.cursor()
    cursorObj.execute(query)
    connection.commit()
    del connection, cursorObj, query

def view_table():
    connection = get_connection(database_path)
    cursorObj = connection.cursor()
    query = 'SELECT * FROM shop'
    cursorObj.execute(query)
    data = cursorObj.fetchall()
    for item in data:
        print(item)
    del connection, cursorObj, query, data

if __name__ == '__main__':
    print("Database Manager")
    print("="*20)

    # prepare_query()
    view_table()
    # get_table_details('database.db')