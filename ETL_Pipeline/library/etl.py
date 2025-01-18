from .Logger import Logger
from .Database import Database
from .Variables import Variables
import csv

class ETL:
    def __init__(self,table):
        self.logger = Logger('test_logs')
        self.db = Database(self.logger)
        self.table = table

    def ext_to_file(self):
        try:
            query = f"""
            SELECT * from {Variables.get_variable('SRC_DB')}.{self.table}
            """
            data = self.db.execute_query(query)
            # Get column names from the cursor description
            column_names = [desc[0] for desc in self.db.cursor.description]
            output_file = f"{Variables.get_variable('data_path')}/{self.table}.csv"
            # Write data to a CSV file
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(column_names)
                writer.writerows(data)
            self.logger.log_info(f"Data successfully written to {output_file}")
        except Exception as e:
            self.logger.log_info(f"Error: {e}")

    def load_to_table(self):
        sql = f"""
            LOAD DATA LOCAL INFILE '{Variables.get_variable('data_path')}/{self.table}.csv'
            INTO TABLE {Variables.get_variable('DB_NAME')}.{self.table}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS                 
        """
        self.logger.log_info(sql)
        # SET product_name = NULLIF(product_name, '');
        try:
            # Execute the command
            self.db.execute_query(sql)
            self.logger.log_info(f"Data loaded successfully into '{self.table}'.")
        except Exception as err:
            self.logger.log_info(f"Error: {err}")
            raise Exception(f"Error: {err}")
