## Instructions
1. Clone this repo with `git clone https://github.com/ShresthaAnkit/DWBI.git`

2. Open the project in PyCharm

3. Run `pip install -r requirements.txt` 

4. Add `config.cfg` in the `config` folder with the following structure
```
{
    "DB_HOST":"localhost",
    "DB_USER":"root",
    "DB_PASSWORD":"admin",
    "DB_STG":"OLAP_ANKIT_STG",
    "log_path":"D:/Programming/Python/College/ETL_Pipeline/logs",
    "data_path":"C:/ProgramData/MySQL/MySQL Server 9.2/Uploads",
    "DB_SRC": "OLTP_ANKIT",
    "DB_TEMP": "OLAP_ANKIT_TEMP",
    "DB_TGT": "OLAP_ANKIT_TGT"
}
```
Add your own values for each variable.

5. Open the `Variables.py` file in the `library` directory and replace the path with the path to your `config.cfg` file.

6. Open the `all_sql.sql` file in `sql_queries` directory and replace `ANKIT` with `YOUR_NAME` and run the entire file.

7. Now open the `product_ext.py` file in the `src` directory and run it.

8. Open the `load_sales.sql` file in `sql_queries` directory and replace the `INFILE` path there with your own path. You can get your path by running `SHOW VARIABLES LIKE 'secure_file_priv';`. Remember to add the full path to the csv file from the next step and replace the database name in `OLAP_ANKIT_STG.SALES` with your database name.

9. Copy the `Sales Data.csv` file sent by sir to the uploads folder.

10. Run the `load_sales.sql` file.

11. Open the `stage_to_temp.py` file and run it.

12. Open the `temp_to_target.py` file and run it.

13. To test if the process was successful run `SELECT * FROM OLAP_{Your_name}_TGT.F_RETAIL_SLS_T;` in Mysql workbench.