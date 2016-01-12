import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

# insert

def insert():
    db.test.insert_many((
        {
            'k': 'a',
            'v': 'A',
        },
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


# delete

db.test.delete_one(
    {'k': 'c'}
)

# delete all by criteria

db.test.delete_many(
    {'k': {'$exists': 1}}
)

# find last one and delete

insert()

db.test.find_one_and_delete(
    {'k': {'$exists': 1}},
    sort=[('k', pymongo.DESCENDING)]
)


####################

# show result

c = db.test.find({}, {'_id': 0})
for o in c:
    print o
