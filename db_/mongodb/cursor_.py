import pymongo


client = pymongo.MongoClient()
db = client.test


db.test.drop()


cur = db.test.find()
print 'count:', cur.count()


db.test.insert_one({'a': 'A'})


print 'count:', cur.count()
for o in cur:
    print o
