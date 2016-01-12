import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()


# bulk

bulk = db.test.initialize_ordered_bulk_op()

bulk.insert(
    {
        'key': 'a',
        'value': 'A',
    },
)

bulk.insert(
    {
        'key': 'b',
        'value': 'B',
    },
)

bulk.execute()


# show results

c = db.test.find(projection={'_id': 0})
for o in c:
    print o
