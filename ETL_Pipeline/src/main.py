from ETL_Pipeline.library.Database import Database
from ETL_Pipeline.library.Logger import Logger

select_query = 'SELECT * FROM PRODUCT;'

def main():
    db = Database(Logger('test_logs'))
    results = db.execute_query(select_query)
    print(results)
    db.disconnect()

if __name__ == '__main__':
    main()