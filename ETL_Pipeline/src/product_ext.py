from ETL_Pipeline.library.etl import ETL

tables = ['COUNTRY','REGION','CATEGORY','SUBCATEGORY','PRODUCT','CUSTOMER','STORE']
def main():
    for table in tables:
        etl = ETL(table)
        etl.ext_to_file()
        etl.load_to_table()
        etl.db.disconnect()

if __name__ == '__main__':
    main()