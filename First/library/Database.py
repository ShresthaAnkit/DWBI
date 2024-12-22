import mysql.connector
import Variables

class Database():    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Variables('DB_HOST').get_variable(),
            user=Variables('DB_USER').get_variable(),
            password=Variables('DB_PASSWORD').get_variable(),
            database=Variables('DATABASE_NAME').get_variable()
        )
    def connect(self):
        pass
    def execute_query(self):
        pass
    
    def disconnect(self):
        pass
    
    def disconnect(self):
        self.conn.close()
    