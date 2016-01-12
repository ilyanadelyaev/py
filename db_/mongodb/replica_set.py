import pymongo


# initialize

client = pymongo.MongoClient('localhost', 27020)

config = {'_id': 'rs0', 'members': [
    {'_id': 0, 'host': 'localhost:27020'},
    {'_id': 1, 'host': 'localhost:27021'},
    {'_id': 2, 'host': 'localhost:27022'},
]}

try:
    print client.admin.command("replSetInitiate", config)
except pymongo.errors.OperationFailure as ex:
    print 'ERROR:', str(ex)


# connect

client = pymongo.MongoClient(
    'mongodb://localhost:27020,localhost:27021,localhost:27022/?replicaSet=rs0')
print client

db = client.test


# execute

db.test.insert_one({'k': 1})

for o in db.test.find():
    print o
