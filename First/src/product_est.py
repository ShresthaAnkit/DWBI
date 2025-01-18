import os
from library.Logger import Logger
from library.Database import Database

try:
    logger = Logger('Test')
    db = Database(logger)

except Exception as e:
    print(f"[ERROR]: {e}")
finally:
    db.disconnect()