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

5. Open the `all_sql.sql` file in `sql_queries` directory and replace `ANKIT` with `YOUR_NAME` and run the entire file.

6. Now open the `product_ext.py` file in the `src` directory and run it.

7. Open the `load_sales.sql` file in `sql_queries` directory and replace the `INFILE` path there with your own path. You can get your path by running `SHOW VARIABLES LIKE 'secure_file_priv';`. Remember to add the full path to the csv file from the next step.

8. Copy the `Sales Data.csv` file sent by sir to the uploads folder.

9. Run the `load_sales.sql` file.

10. Open the `stage_to_temp.py` file and run it.

11. Open the `temp_to_target.py` file and run it.
