USE OLTP_ANKIT;

SELECT 
st.STORE_DESC,
CONCAT(c.CUSTOMER_FIRST_NAME,' ',COALESCE(c.CUSTOMER_MIDDLE_NAME,''),' ',c.CUSTOMER_LAST_NAME) AS c_name,
MONTH(s.TRANSACTION_date),
SUM(s.Quantity) OVER (PARTITION BY MONTH(s.TRANSACTION_date)) AS Total_Quantity
FROM Sales_v2 AS s
LEFT JOIN Store AS st
ON st.id = s.STORE_ID
LEFT JOIN Customer AS c
ON c.id = s.CUSTOMER_ID;

SELECT 
st.STORE_DESC,

CONCAT(c.CUSTOMER_FIRST_NAME,' ',COALESCE(c.CUSTOMER_MIDDLE_NAME,''),' ',c.CUSTOMER_LAST_NAME) AS c_name,
MONTH(s.TRANSACTION_date),
SUM(s.AMOUNT)
FROM Sales_v2 AS s
LEFT JOIN Store AS st
ON st.id = s.STORE_ID
LEFT JOIN Customer AS c
ON c.id = s.CUSTOMER_ID
GROUP BY st.STORE_DESC,MONTH(s.TRANSACTION_date),CONCAT(c.CUSTOMER_FIRST_NAME,' ',COALESCE(c.CUSTOMER_MIDDLE_NAME,''),' ',c.CUSTOMER_LAST_NAME) ;

SELECT 
c_name,
monthh,
MAX(amountt) AS max_amount FROM
(
select 
r.region_desc AS region, 
CONCAT(c.CUSTOMER_FIRST_NAME,' ',COALESCE(c.CUSTOMER_MIDDLE_NAME,''),' ',c.CUSTOMER_LAST_NAME) AS c_name,
MONTH(s.TRANSACTION_date) AS monthh,
SUM(amount) AS amountt
from sales_v2 as s 
	left join store as st on s.store_id= st.id 
	left join region as r on st.region_id = r.id
	left join customer as c on s.customer_id = c.id
	GROUP BY region_desc, CONCAT(c.CUSTOMER_FIRST_NAME,' ',COALESCE(c.CUSTOMER_MIDDLE_NAME,''),' ',c.CUSTOMER_LAST_NAME),
	MONTH(s.TRANSACTION_date)
) AS total_table
GROUP BY c_name,monthh
;

SELECT * FROM CUSTOMER;