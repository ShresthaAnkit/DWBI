from ETL_Pipeline.library.Database import Database
from ETL_Pipeline.library.Logger import Logger
from ETL_Pipeline.library.Variables import Variables

tables = ['COUNTRY','REGION','CATEGORY','SUBCATEGORY','PRODUCT','CUSTOMER','STORE','SALES']

TEMP_DB_NAME = Variables.get_variable('DB_TEMP')
STG_DB_NAME = Variables.get_variable('DB_STG')
def main():
    db = Database(Logger('test_logs'))
    db.execute_query("SET FOREIGN_KEY_CHECKS =0;")
    for table in tables:
        truncate_query = f"""            
            TRUNCATE TABLE {TEMP_DB_NAME}.{table};
        """
        db.execute_query(truncate_query)
        insert_query = f"""
            INSERT INTO {TEMP_DB_NAME}.{table}
            SELECT * FROM {STG_DB_NAME}.{table};
        """
        db.execute_query(insert_query)
    db.execute_query("SET FOREIGN_KEY_CHECKS = 1;")
    db.disconnect()

if __name__ == '__main__':
    main()