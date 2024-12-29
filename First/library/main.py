from Database import Database

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
    db = Database()
    results = db.execute_query(select_query)
    print(results)
    db.disconnect()

if __name__ == '__main__':
    main()