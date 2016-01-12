import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

db.test.insert_many((
    {
        'key': 'a',
        'value': 'A',
        'values': {
            'info': 'AAA',
            'doc': 'aaa',
        }
    },
    {
        'key': 'b',
        'value': 'B',
        'items': ['X', 'Y', 'Z'],
    },
    {
        'key': 'c',
        'value': 'C',
        'embedded': [
            {'info': 'E1', 'misc': 'e1'},
            {'info': 'E2', 'misc': 'e2'},
        ]
    },
))


# find

for o in db.test.find(projection={'_id': 0}):
    print o

# key in

for o in db.test.find({'key': {'$in': ('a', 'b')}}, {'key': 1, '_id': 0}):
    print o

# and

for o in db.test.find({'key': 'a', 'value': 'A'}, {'_id': 0}):
    print o

# or

for o in db.test.find({'$or': [{'key': 'c'}, {'value': 'B'}]}, {'value': 1, '_id': 0}):
    print o

# and / or

for o in db.test.find({'key': {'$exists': 1}, '$or': [{'key': 'c'}, {'value': 'B'}]}, {'key': 1, '_id': 0}):
    print o

# embedded document

for o in db.test.find({'values': {'info': 'AAA', 'doc': 'aaa'}}):
    print o

# emdedded dot notation

for o in db.test.find({'values.doc': 'aaa'}):
    print o

# array exact match

for o in db.test.find({'items': ['X', 'Y', 'Z']}, {'_id': 0}):
    print o

# array element

for o in db.test.find({'items': 'X'}, {'_id': 0}):
    print o

# array element position

for o in db.test.find({'items.2': 'Z'}, {'_id': 0, 'items.$': 1}):
    print o

# array element criteria

for o in db.test.find({'items': {'$in': ['A', 'Y']}}, {'_id': 0}):
    print o

# array.embedded exact position in array

for o in db.test.find({'embedded.0.info': 'E1'}):
    print o

# array.embedded any position in array

for o in db.test.find({'embedded.info': 'E2'}):
    print o

# array.embedded elemMatch

for o in db.test.find({'embedded': {'$elemMatch': {'info': 'E1', 'misc': 'e1'}}}, {'embedded.$': 1}):
    print o

# array embedded multy conditions

for o in db.test.find({'embedded.info': 'E2', 'embedded.misc': 'e2'}):
    print o
