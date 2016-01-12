import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

####################


# insert

db.test.insert_one(
    {
        'k': 'a',
        'v': 'A',
    }
)

db.test.insert_many((
    {
        'k': 'b',
        'v': 'B',
    },
    {
        'k': 'c',
        'v': 'C',
    },
))


####################

# show result

c = db.test.find({}, {'_id': 0})
for o in c:
    print o
