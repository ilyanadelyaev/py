import pymongo


client = pymongo.MongoClient()
db = client.test

db.capped.drop()


db.create_collection('capped', capped=True, size=10000, max=2)


db.capped.insert_many((
    {
        'k': 'a',
    },
    {
        'k': 'b',
    },
))


print 'Count:', db.capped.count()
for o in db.capped.find().sort([('$natural', -1)]):
    print o


db.capped.insert_many((
    {
        'k': 'c',
    },
    {
        'k': 'd',
    },
))


print 'Count:', db.capped.count()
for o in db.capped.find():
    print o
