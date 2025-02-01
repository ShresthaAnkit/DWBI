MERGE INTO DW_TGT.PRODUCT AS TGT
USING DW_TMP.product AS TMP
ON TGT.product_id = TMP.product_id                        
WHEN MATCHED AND TGT.product_name <> TMP.product_name
THEN UPDATE SET 
    TGT.product_name = TMP.product_name,
    TGT.rcd_upd_ts = CURRENT_TIMESTAMP()        
WHEN NOT MATCHED 
THEN INSERT (product_key, product_id, product_name, product_price, product_desc, rcd_ins_ts, rcd_upd_ts)
VALUES (
    generate_product_key,  -- Ensure this function exists
    TMP.product_id,
    TMP.product_name,
    TMP.product_price,
    TMP.product_desc,
    CURRENT_TIMESTAMP(),
    CURRENT_TIMESTAMP()
);

MERGE INTO DW_TGT.PRODUCT
USING DW_TMP.product as TMP
ON TGT.product_id = TMP.product_id
WHEN MATCHED AND TGT.product_name <> TMP.product_name
THEN 
TGT.eff_end_date = CURRENT_DATETIME() - 1
TGT.active_flag = FALSE
TGT.rcd_upd_ts = CURRENT_TIMESTAMP()

-- Latest Records
WHEN MATCHED AND TGT.product_name = TMP.product_name  
INSERT into DW_TGT.PRODUCT
SELECT 
generate_product_key,
product_id as product_id,
product_name,
product_price,
product_desc,
CURRENT_TIMESTAMP() as rcd_ins_ts,
CURRENT_TIMESTAMP() as rcd_upd_ts,
CURRENT_DATE() AS eff_start_date,
'9999-12-31' AS eff_end_date,
TRUE AS active_flag
from DW_STG.PRODUCT

INSERT INTO D_TGT.PRODUCT TGT
SELECT * FROM DW_TMP.PRODUCT TMP
WHERE TMP.product_id
NOT IN
(
SELECT product_id FROM DW_TGT.PRODUCT
)
 