import mysql.connector
from Variables import Variables
from mysql.connector import Error

class Database():    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=Variables('DB_HOST').get_variable(),
                user=Variables('DB_USER').get_variable(),
                password=Variables('DB_PASSWORD').get_variable(),
                database=Variables('DATABASE_NAME').get_variable()
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f'Error connecting to Database: {e}')
            self.conn = None
            self.cursor = None
    def connect(self):
        pass
    def execute_query(self,query):
        try:
            if not self.conn or not self.cursor:
                print("No active database connection.")
                return None
            self.cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
                print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")
            return None
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    