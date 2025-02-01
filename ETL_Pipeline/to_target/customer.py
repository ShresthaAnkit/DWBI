from ETL_Pipeline.library.Database import Database
from ETL_Pipeline.library.Logger import Logger
from ETL_Pipeline.library.Variables import Variables

TABLE_NAME = 'D_RETAIL_CUSTOMER_T'
TGT_DB_NAME = Variables.get_variable('DB_TGT')
TEMP_DB_NAME = Variables.get_variable('DB_TEMP')
truncate_query = f"""
TRUNCATE TABLE {TGT_DB_NAME}.{TABLE_NAME};
"""
insert_query = f"""
INSERT INTO {TGT_DB_NAME}.{TABLE_NAME} (CUSTOMER_ID,CUSTOMER_FST_NM, CUSTOMER_MID_NM, CUSTOMER_LST_NM, CUSTOMER_ADDR, ROW_INSRT_TMS, ROW_UPDT_TMS)
SELECT 
    ID,
  CUSTOMER_FIRST_NAME, 
  CUSTOMER_MIDDLE_NAME, 
  CUSTOMER_LAST_NAME, 
  CUSTOMER_ADDRESS, 
  CURRENT_TIMESTAMP, 
  CURRENT_TIMESTAMP
FROM {TEMP_DB_NAME}.CUSTOMER;
"""

def load_customer_to_tgt():
    db = Database(Logger('test_logs'))
    db.execute_query(truncate_query)
    db.execute_query(insert_query)
    db.disconnect()