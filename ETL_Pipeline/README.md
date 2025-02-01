## Instructions
1. Clone this repo with `git clone https://github.com/ShresthaAnkit/DWBI.git`
2. Open the project in PyCharm
3. Add `config.cfg` in the `config` folder with the following structure
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
4. Open the `all_sql.sql` file in `sql_queries` directory and replace `ANKIT` with `YOUR_NAME` and run the entire file.
5. 
SHOW VARIABLES LIKE 'secure_file_priv';