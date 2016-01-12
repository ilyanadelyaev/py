import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

# fill
for k, v in pymongo.__dict__.iteritems():
    try:
        db.test.insert({
            'name': k,
            'doc': v.__doc__,
            'file': v.__file__,
            'package': v.__package__,
            'items': [{'key': kk, 'value': vv.__doc__} for kk, vv in v.__dict__.iteritems()],
        })
    except AttributeError as ex:
        db.test.insert({
            'name': k,
            'error': str(ex),
        })


####################


r = db.test.count()
print 'Total items:', r

r = db.test.find_one({'name': 'cursor'}, {'_id': 0})
print 'Cursor:', r

c = db.test.find({'package': 'pymongo'}, {'_id': 0, 'name': 1}).sort([('name', pymongo.DESCENDING)])
for o in c:
    print 'PYMONGO:', o

r = db.test.find_one({'items': {'$elemMatch': {'key': 'RE_TYPE'}}}, {'items.$': 1, '_id': 0})
print 'RE_TYPE:', r

r = db.test.find_one({'name': 'cursor'}, {'items': {'$slice': [2, 3]}, '_id': 0})
print 'slice:', r
