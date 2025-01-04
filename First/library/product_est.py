import os
from ..First.library import Logger
from First.library import Database

try:
    logger = Logger('Test')
    db = Database(logger)

except Exception as e:
    print(f"[ERROR]: {e}")
finally:
    db.disconnect()