import mysql.connector
from Variables import Variables
from mysql.connector import Error
from Logger import Logger
import csv

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
        SELECT * from {Variables.get_variable('SRC_DB')}.{table_name}
        """
        data = self.execute_query(query)                
        # Get column names from the cursor description
        column_names = [desc[0] for desc in self.cursor.description]

        output_file = f"{Variables.get_variable('data_path')}/{table_name}.csv"
        # Write data to a CSV file
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(column_names)
            
            # Write the data rows
            writer.writerows(data)
        
        print(f"Data successfully written to {output_file}")

    def load_to_table(self,table_name,file_name):
        sql = f"""
            LOAD DATA LOCAL INFILE '{Variables.get_variable('data_path')}/{file_name}'
            INTO TABLE {Variables.get_variable('DB_NAME')}.{table_name}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS                 
        """
        self.logger.log_info(sql)
        # SET product_name = NULLIF(product_name, '');        
        try:
            # Execute the command
            self.cursor.execute(sql)
            self.conn.commit()        
            print(f"Data loaded successfully into '{table_name}'.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    