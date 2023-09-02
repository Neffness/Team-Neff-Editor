from  sqlite4  import  SQLite4


class Database:
    _db = None
    _db_name = None
    
    def __init__(self, db_name):
        self._db_name = db_name
        # Init database object, singleton pattern restricts multiple objects per db
        self._db = SQLite4(self.db_name)
        # Connect to db and creates execution thread
        self.db.connect()

    @property
    def db_name(self):
        return self._db_name
        
    @property
    def db(self):
        return self._db