# Keep track of every query
import logging
from Variables import Variables
import datetime
import os

class Logger:
    def __init__(self,file_name):
        current_ts = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        self.file_name = f"{file_name}_{current_ts}"
        self.log_path = os.path.join(Variables.get_variable('log_path'),self.file_name)

        self.logger = self.set_logger()

    def set_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel('INFO')
        return self.logger

    def log_info(self,msg):
        self.logger.info(msg)
    def log_error(self,msg):
        self.logger.error(msg)
        

log = Logger('test')
