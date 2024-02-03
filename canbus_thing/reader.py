import cantools
from cantools.database import Database
import os

class CanbusReader:
    def __init__(self, location: str):
        self.location = location

    def read(self) -> Database:
        db = cantools.db.load_file(self.location)
        return db

    def get_path(self):
        return os.getcwd()

def create_canbus_reader(db_location: str) -> CanbusReader:
    if db_location is None:
        db_location = os.path.join(os.path.dirname(__file__), 'prod.dbc')
    return CanbusReader(db_location)

