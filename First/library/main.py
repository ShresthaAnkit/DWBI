from Database import Database
from Logger import Logger

select_query = 'SELECT * FROM PRODUCT;'

def main():
    db = Database(Logger('test_logs'))
    results = db.execute_query(select_query)
    print(results)
    #db.ext_to_file('PRODUCT')
    #db.load_to_table(table_name='PRODUCT',file_name='PRODUCT.csv')
    db.disconnect()

if __name__ == '__main__':
    main()