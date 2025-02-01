from ETL_Pipeline.library.Database import Database
from ETL_Pipeline.library.Logger import Logger
from ETL_Pipeline.library.Variables import Variables

TABLE_NAME = 'D_RETAIL_PDT_T'
TGT_DB_NAME = Variables.get_variable('DB_TGT')
TEMP_DB_NAME = Variables.get_variable('DB_TEMP')
truncate_query = f"""
TRUNCATE TABLE {TGT_DB_NAME}.{TABLE_NAME};
"""
insert_query = f"""
INSERT INTO {TGT_DB_NAME}.{TABLE_NAME} (PDT_ID,SUB_CTGRY_KY,PDT_DESC, ROW_INSRT_TMS, ROW_UPDT_TMS)
    SELECT 
        P.ID,
        S.SUB_CTGRY_KY,        
        P.PRODUCT_DESC,
        CURRENT_TIMESTAMP, 
        CURRENT_TIMESTAMP
FROM {TEMP_DB_NAME}.PRODUCT P
JOIN {TGT_DB_NAME}.D_RETAIL_SUB_CTGRY_T S 
  ON P.SUBCATEGORY_ID = S.SUB_CTGRY_ID;
"""

def load_product_to_tgt():
    db = Database(Logger('test_logs'))
    db.execute_query(truncate_query)
    db.execute_query(insert_query)
    db.disconnect()