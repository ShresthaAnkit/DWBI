import mysql.connector
from Variables import Variables
from mysql.connector import Error
from Logger import Logger

class Database():    
    def __init__(self, logger: Logger):
        try:
            self.logger = logger
            self.conn = mysql.connector.connect(
                host=Variables.get_variable('DB_HOST'),
                user=Variables.get_variable('DB_USER'),
                password=Variables.get_variable('DB_PASSWORD'),
                database=Variables.get_variable('DB_NAME'),
                allow_local_infile=True
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
            self.logger.log_info(query)
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
    
    def ext_to_file(self,table_name):
        query = f"""
        SELECT fields from {Variables.SRC_DB}.{Variables.SCHEMA}.{table_name}
        """

    def load_to_table(self,table_name):
        sql = f"""
            LOAD DATA LOCAL INFILE 'D:/Programming/Python/College/First/data/products.csv'
            INTO TABLE products
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS
            (product_name,price)
            SET product_name = NULLIF(product_name, '');
        """
        try:
            # Execute the command
            self.cursor.execute(sql)
            self.conn.commit()
            print(f"Data loaded successfully into '{table_name}'.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            # Close the connection
            self.cursor.close()
            self.conn.close()

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    