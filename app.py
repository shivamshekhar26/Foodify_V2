# import mysql.connector
# mydb=mysql.connector.connect(host="localhost", user="root", password="root",port=3306)
# mycursor=mydb.cursor()
# mycursor.execute("show databases")
# for i in mycursor:
#     print(i)
# import mysql.connector
# from mysql.connector import Error

# try:
#     print("Connecting to MySQL database...")
#     connection = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='foodify_db'
#     )

#     if connection.is_connected():
#         print("Connected to foodify_db!")
#         cursor = connection.cursor()
#         cursor.execute("""
#             SELECT table_name 
#             FROM information_schema.tables 
#             WHERE table_schema = 'foodify_db' 
#             AND table_name IN ('categories', 'menu_items')
#         """)
#         tables = cursor.fetchall()

#         if tables:
#             print("Found tables:")
#             for table in tables:
#                 print(table[0])
#         else:
#             print("No tables named 'categories' or 'menu_items' found in 'foodify_db'.")

# except Error as e:
#     print("Error while connecting or querying MySQL:", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         connection.close()
#         print("MySQL connection closed.")

# import mysql.connector
# from mysql.connector import Error

# try:
#     print("Connecting to MySQL database...")
#     connection = mysql.connector.connect(
#         host='localhost',  # Use IP instead of 'localhost' to avoid socket issues
#         user='root',
#         password='root',
#         database='foodify_db'
#     )

#     if connection.is_connected():
#         print("Connected to foodify_db!")
#         cursor = connection.cursor()

#         # Fetch all tables in the database
#         cursor.execute("""
#             SELECT table_name 
#             FROM information_schema.tables 
#             WHERE table_schema = 'foodify_db'
#         """)
#         all_tables = cursor.fetchall()

#         if all_tables:
#             print("All tables in 'foodify_db':")
#             for table in all_tables:
#                 print(f"- {table[0]}")
#         else:
#             print("No tables found in 'foodify_db'.")

#         # Check specifically for 'categories' and 'menu_items'
#         cursor.execute("""
#             SELECT table_name 
#             FROM information_schema.tables 
#             WHERE table_schema = 'foodify_db' 
#             AND table_name IN ('categories', 'menu_items')
#         """)
#         specific_tables = cursor.fetchall()

#         if specific_tables:
#             print("\nFound specific tables:")
#             for table in specific_tables:
#                 print(f"- {table[0]}")
#         else:
#             print("\nNo tables named 'categories' or 'menu_items' found in 'foodify_db'.")

# except Error as e:
#     print("Error while connecting or querying MySQL:", e)

# finally:
#     if 'connection' in locals() and connection.is_connected():
#         conne

import pymysql
from config import DB_CONFIG
con=pymysql.connect(**DB_CONFIG)
cursor=con.cursor()
print("Connection created")
query='Select * from categories'
query1='Select * from menu_items'
cursor.execute(query)
cursor.execute(query1)
data=cursor.fetchall()
print(data)
print("table created")




