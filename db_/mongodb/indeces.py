import pprint

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


r = db.test.find({'name': 'cursor'}).explain()
pprint.pprint(r)


db.test.create_index('name')
print '=' * 20


r = db.test.find({'name': 'cursor'}, {'name': 1, '_id': 0}).explain()
pprint.pprint(r)
