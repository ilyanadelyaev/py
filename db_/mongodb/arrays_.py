import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

db.test.insert_one(
    {
        'array': [],
    }
)
_id = db.test.find_one()['_id']


db.test.update(
    {'_id': _id},
    {'$push': {  # append to array
        'array': {
            '$each': ['C', 'A', 'B'],  # each item from sequence
            '$sort': -1,  # desc
            '$slice': -1,  # one from tail
        }
    }}
)



for o in db.test.find(projection={'_id': 0}):
    print o
