class SingletonMeta(type):
    _instances = {}  # storage for created object. Key - Class, value - unique instance

    def __call__(cls, *args, **kwargs): # its call when instance of Database is creating
        if cls not in cls._instances: # check if such class exists in dict
            cls._instances[cls] = super().__call__(*args, **kwargs) # create object for cls class
        return cls._instances[cls] # return already existed or new object

class Database(metaclass=SingletonMeta):
    def __init__(self, db_name):
        self.db_name = db_name

db1 = Database("db1")
db2 = Database("db2")
db2.db_name = "db2"

print(db1 is db2)  # True
print(db1.db_name)