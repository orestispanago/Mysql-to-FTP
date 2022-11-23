import pandas as pd
from sqlalchemy import create_engine
from ftplib import FTP
import logging
import logging.config
import traceback
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger(__name__)
logging.config.fileConfig("logging.conf", disable_existing_loggers=False)


mysql_host = ""
mysql_port = ""
mysql_db = ""
mysql_user = ""
mysql_password = ""
mysql_table = ""

ftp_ip = ""
ftp_user = ""
ftp_password = ""
ftp_dir = ""

fname = f"{mysql_table}.csv"


def csv_to_ftp():
    logger.debug(f"Uploading {fname} to FTP server...")
    with FTP(ftp_ip, ftp_user, ftp_password) as ftp:
        ftp.cwd(ftp_dir)
        with open(fname, "rb") as f:
            ftp.storbinary(f"STOR {fname}", f)
    logger.info(f"Uploaded {fname} to FTP server...")

def mysql_table_to_csv():
    db_connection_str = (f'mysql+pymysql://{mysql_user}:'
                         f'{mysql_password}@{mysql_host}:'
                         f'{mysql_port}/{mysql_db}')
    db_connection = create_engine(db_connection_str)
    df = pd.read_sql(f'SELECT * FROM {mysql_table}', con=db_connection, 
                     index_col='time')
    logger.info(f"Retrieved {len(df)} records from database")
    df.to_csv(fname)

def main():
    mysql_table_to_csv()
    csv_to_ftp()


if __name__ == "__main__":
    try:
        main()
        logger.debug(f"{'-' * 20} SUCCESS {'-' * 20}")
    except:
        logger.error("uncaught exception: %s", traceback.format_exc())