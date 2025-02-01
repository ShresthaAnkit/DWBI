LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/SALES.csv'

INTO TABLE OLAP_ANKIT_STG.SALES
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID, STORE_ID, PRODUCT_ID, @CUSTOMER_ID, TRANSACTION_TIME, QUANTITY, AMOUNT, @DISCOUNT)
SET 
    CUSTOMER_ID = NULLIF(@CUSTOMER_ID, ''),
    DISCOUNT = NULLIF(@DISCOUNT, '');
    

