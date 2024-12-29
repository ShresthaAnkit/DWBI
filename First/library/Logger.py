# Keep track of every query
import logging
from Variables import Variables
import datetime
import os

class Logger:
    def __init__(self,file_name):
        current_ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_dir = Variables.get_variable('log_path')
        self.file_name = f"{file_name}_{current_ts}"
        self.log_path = os.path.join(log_dir,self.file_name)

        self.logger = self.set_logger()

    def set_logger(self):
        logger = logging.getLogger(self.file_name)  # Use a unique name for each logger
        logger.setLevel(logging.INFO)

        # Avoid adding multiple handlers to the logger
        if not logger.handlers:
            file_handler = logging.FileHandler(self.log_path)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

    def log_info(self,msg):
        self.logger.info(msg)
    def log_error(self,msg):
        self.logger.error(msg)
        
