from Database import Database
from Logger import Logger

select_query = 'SELECT * FROM PRODUCT;'
tables = ['COUNTRY','REGION','CATEGORY','SUBCATEGORY','PRODUCT','CUSTOMER','STORE','SALES']
def main():
    db = Database(Logger('test_logs'))
    # results = db.execute_query(select_query)
    # print(results)
    for table in tables:
        db.ext_to_file(table)
        db.load_to_table(table_name=table,file_name=f'{table}.csv')
    db.disconnect()

if __name__ == '__main__':
    main()