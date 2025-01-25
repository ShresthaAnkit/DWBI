##Seed 
#Insert into Country

INSERT INTO OLTP_ANKIT.COUNTRY VALUES
(1, 'Nepal'),
(2, 'India');

#Insert into Region

INSERT INTO OLTP_ANKIT.REGION VALUES
(1, 1, 'Kathmandu'),
(2, 1, 'Lalitpur'),
(3, 2, 'Punjab'),
(4, 2, 'Bangalore');


#insert into Store

INSERT INTO OLTP_ANKIT.STORE VALUES
(1, 1, 'RETAIL Chakrapath'),
(2, 2, 'RETAIL Pulchowk'),
(3, 3, 'RETAIL Chandigarh'),
(4, 4, 'RETAIL Jayanagar');

#Insert into Categories

INSERT INTO OLTP_ANKIT.CATEGORY VALUES
(1,'Garment'),
(2,'GROCERY'),
(3,'KitchenWares');

#Insert into SubCategories

Insert into OLTP_ANKIT.SUBCATEGORY values
(1, 1,'MENS WEAR'),
(2, 1,'WOMENS WEAR'),
(3,1,'KIDS WEAR'),
(4,2,'Dairy'),
(5,2,'Fruits'), 
(6,2,'Packed Items'),
(7,3,'Utensils') ,
(8,3,'Glassware'),
(9,3,'ElectricAppliances');


#Insert into Product
insert into OLTP_ANKIT.PRODUCT values
(1,1,'Jeans'),
(2,2,'Shirt'),
(3,1,'Shoes'),
(4,5,'Apple'),
(5,5,'Oranges'),
(6,4,'Milk'),
(7,4,'Butter'),
(8,9, 'Microwave'),
(9,9, 'Coffee Maker'),
(10,7, 'Plate'),
(11,6,'Wai Wai'),
(12,6,'Oats'),
(13,3,'Diaper'),
(14,8,'Glass'),
(15,8,'Jug'),
(16,2,'Skirt'),
(17,7,'Spoon'),
(18,3,'Kids Jacket');

#Insert into Customer

insert into OLTP_ANKIT.CUSTOMER values
(1,'Ram',null,'Adhikari','Kathmandu'),
(2,'Shyam','Prasad','Sharma','lalitpur'),
(3,'Hari',null,'Poudel','Bhaktapur'),
(4, 'Saurav','Muhammed', 'Ali','Banglore'),
(5,'Kannur','Lokesh','Rahul','Punjab'),
(6, 'James',null,'Singh','Chennai');

INSERT INTO OLTP_ANKIT.SALES (ID, STORE_ID, PRODUCT_ID, CUSTOMER_ID, TRANSACTION_TIME, QUANTITY, AMOUNT, DISCOUNT)
VALUES
(1, 1, 6, 3, '00:00:00', 1, 1.66, 0),
(4, 2, 11, 2, '03:56:00', 5, 50, 0),
(3, 1, 15, NULL, '03:56:00', 1, 6.99, 0),
(2, 1, 14, NULL, '03:56:00', 3, 29.97, 0),
(5, 3, 9, 6, '03:59:00', 1, 41.66, 0),
(6, 4, 9, NULL, '04:03:00', 1, 66.66, 0),
(7, 3, 16, NULL, '08:53:00', 1, 10.63, 1.84),
(8, 4, 7, NULL, '13:51:00', 1, 238.49, 0),
(9, 2, 10, 2, '13:59:00', 2, 53.98, 0),
(12, 1, 10, NULL, '14:05:00', 1, 27.23, 0),
(11, 4, 13, 4, '14:05:00', 1, 40.91, 0),
(10, 3, 17, 1, '14:05:00', 1, 27.23, 0),
(13, 3, 7, 2, '14:09:00', 1, 144.16, 10),
(14, 2, 18, NULL, '18:49:00', 1, 54.16, 0),
(15, 1, 11, NULL, '18:53:00', 3, 36, 0),
(16, 1, 17, NULL, '22:17:00', 1, 18, 0),
(17, 3, 4, 3, '22:49:00', 1, 40.91, 0),
(18, 1, 13, 3, '23:51:00', 2, 26.07, 0),
(19, 4, 11, 2, '24:58:00', 1, 4.55, 0),
(20, 1, 13, NULL, '26:44:00', 1, 5.83, 0),
(22, 1, 3, 6, '28:52:00', 1, 15.99, 0),
(21, 1, 18, 6, '28:52:00', 1, 13.99, 0),
(23, 1, 10, 3, '31:03:00', 1, 28.99, 0),
(25, 3, 8, NULL, '31:16:00', 1, 32.26, 0);

INSERT INTO OLTP_ANKIT.SALES_v2 (ID, STORE_ID, PRODUCT_ID, CUSTOMER_ID, TRANSACTION_date, QUANTITY, AMOUNT, DISCOUNT)
VALUES
(1, 1, 6, 3, '2023-01-01', 1, 1, 0),
(4, 2, 11, 2, '2023-01-03', 5, 50, 0),
(3, 1, 15, 1, '2023-04-01', 1, 7, 0),
(2, 1, 14, 2, '2023-02-01', 3, 30, 0),
(5, 3, 9, 6, '2023-05-01', 1, 42, 0),
(6, 4, 9, 3, '2023-02-01', 1, 67, 0),
(7, 3, 16, 1, '2023-03-01', 1, 11, 2),
(8, 4, 7, 2, '2023-05-01', 1, 238, 0),
(9, 2, 10, 2, '2023-01-01', 2, 54, 0),
(12, 1, 10, 3, '2023-01-01', 1, 27, 0),
(11, 4, 13, 4, '2023-01-01', 1, 41, 0),
(10, 3, 17, 1, '2023-06-01', 1, 27, 0),
(13, 3, 7, 2, '2023-07-01', 1, 144, 10),
(14, 2, 18, 2, '2023-08-01', 1, 54, 0),
(15, 1, 11, 1, '2023-2-01', 3, 36, 0),
(16, 1, 17, 2, '2023-3-01', 1, 18, 0),
(17, 3, 4, 3, '2023-07-01', 1, 41, 0),
(18, 1, 13, 3, '2023-06-01', 2, 26, 0),
(19, 4, 11, 2, '2023-05-01', 1, 5, 0),
(20, 1, 13, 3, '2023-09-01', 1, 6, 0),
(22, 1, 3, 6, '2023-08-01', 1, 16, 0),
(21, 1, 18, 6, '2023-01-01', 1, 14, 0),
(23, 1, 10, 3, '2023-08-01', 1, 29, 0),
(25, 3, 8, 1, '2023-07-01', 1, 32, 0);



SELECT * FROM OLTP_ANKIT.SALES;
SELECT * FROM OLAP_ANKIT_STG.CUSTOMER;