from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:45723/?authMechanism=DEFAULT&authSource=animals' % (username, password)) # Indicates proper ip address, port, and authorization db used for login
        self.database = self.client['animals'] # Marking animals as target database

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary, defined in unit test
            return True # Returning true if insert is successful
        else:
            raise Exception("Nothing to save, because data parameter is empty.") # Returning error if insert is not successful
            
# Create method to implement the R in CRUD.
    def read(self, param):
        if param is not None:
            return self.database.animals.find(param,{"_id":False}) # Finds documents matching param value. Excludes the "_id" field for the purposes of the dashboard
        else:
            raise Exception("Nothing to search, because search parameter is empty.") # Returning error if read is not  successful

# Create method to implement the U in CRUD.
    def update(self, data, updatedData): # this method has an additional argument, which is the new dictionary that will replace the original
        if data is not None:
            return self.database.animals.update_one(data, {'$set': updatedData}) # Returns cursor indicating successful update
        else:
            raise Exception("Nothing to update, because data parameter is empty.") # Returning error if update is not successful
            
# Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data) # Returns cursor indicating successful removal of file
        else:
            raise Exception("Nothing to delete, because data parameter is empty") # Returning error if deletion is not  successful
