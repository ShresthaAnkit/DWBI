from ETL_Pipeline.library.Database import Database
from ETL_Pipeline.library.Logger import Logger
from ETL_Pipeline.library.Variables import Variables

TABLE_NAME = 'F_RETAIL_SLS_T '
TGT_DB_NAME = Variables.get_variable('DB_TGT')
TEMP_DB_NAME = Variables.get_variable('DB_TEMP')
truncate_query = f"""
TRUNCATE TABLE {TGT_DB_NAME}.{TABLE_NAME};
"""
insert_query = f"""
INSERT INTO {TGT_DB_NAME}.{TABLE_NAME} (SLS_ID, PDT_KY, CUSTOMER_KY, TRANSACTION_TIME, QTY, AMT, DSCNT, ROW_INSRT_TMS, ROW_UPDT_TMS)
SELECT 
  S.ID,            
  P.PDT_KY,                  
  C.CUSTOMER_KY,             
  S.TRANSACTION_TIME,        
  S.QUANTITY AS QTY,         
  S.AMOUNT AS AMT,           
  S.DISCOUNT AS DSCNT,       
  CURRENT_TIMESTAMP,         
  CURRENT_TIMESTAMP          
FROM {TEMP_DB_NAME}.SALES S
JOIN {TGT_DB_NAME}.D_RETAIL_PDT_T P ON S.PRODUCT_ID = P.PDT_ID  
JOIN {TGT_DB_NAME}.D_RETAIL_CUSTOMER_T C ON S.CUSTOMER_ID = C.CUSTOMER_ID;
"""

def load_sales_to_tgt():
    db = Database(Logger('test_logs'))
    db.execute_query(truncate_query)
    db.execute_query(insert_query)
    db.disconnect()