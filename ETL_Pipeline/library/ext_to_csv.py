from .Logger import Logger
from .Database import Database
from .Variables import Variables
import csv

class TGTToCSV:
    def __init__(self,table):
        self.logger = Logger('test_logs')
        self.db = Database(self.logger)
        self.table = table

    def target_to_csv(self):
        try:
            query = f"""
            SELECT * from {Variables.get_variable('DB_TGT')}.{self.table}
            """
            data = self.db.execute_query(query)
            # Get column names from the cursor description
            column_names = [desc[0] for desc in self.db.cursor.description]
            output_file = f"{Variables.get_variable('data_path')}/target/{self.table}.csv"
            # Write data to a CSV file
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(column_names)
                writer.writerows(data)
            self.logger.log_info(f"Data successfully written to {output_file}")
        except Exception as e:
            self.logger.log_error(f"Error: {e}")
