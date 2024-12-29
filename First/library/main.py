from Database import Database
from Logger import Logger

select_query = 'SELECT * FROM products;'
insert_products = """
INSERT INTO products (product_name)
VALUES
    ('Desktop'),
    ('Walkie Talkie'),
    ('Earphone'),
    ('Powerbank'),
    ('Oculus Rift');
"""
def main():
    db = Database(Logger('test_logsw'))
    results = db.execute_query(select_query)
    print(results)
    db.disconnect()

if __name__ == '__main__':
    main()