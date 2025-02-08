from ETL_Pipeline.library.ext_to_csv import TGTToCSV

tables = ["D_RETAIL_CNTRY_T","D_RETAIL_RGN_T","D_RETAIL_CTGRY_T","D_RETAIL_SUB_CTGRY_T","D_RETAIL_PDT_T","D_RETAIL_CUSTOMER_T","D_RETAIL_LOCN_T","F_RETAIL_SLS_T"]
def main():
    for table in tables:
        to_csv = TGTToCSV(table)
        to_csv.target_to_csv()

if __name__ == "__main__":
    main()