import pymongo


client = pymongo.MongoClient()
db = client.test

db.test.drop()

db.test.insert_many((
    {
        'k': 'a',
        'v': 'A',
        'values': {
            'info': 'AAA',
            'doc': 'aaa',
        }
    },
    {
        'k': 'b',
        'v': 'B',
        'items': ['X', 'Y', 'Z'],
    },
    {
        'k': 'c',
        'v': 'C',
        'embedded': [
            {'info': 'E1', 'misc': 'e1'},
            {'info': 'E2', 'misc': 'e2'},
        ]
    },
    {
        'k': 'f',
        'v': 'F',
    },
))

####################


# update

db.test.update_one(
    {'k': 'a'},
    {'$set': {'v': 'AA'}},
)

# update missed (have to insert)

db.test.update_one(
    {'k': 'd'},
    {'$set': {'v': 'D'}},
)

# insert

db.test.update_one(
    {'k': 'd'},
    {'$set': {'v': 'D'}},
    upsert=True,
)

# delete field

db.test.update_one(
    {'k': 'd'},
    {'$unset': {'v': 1}},
)

# rename field

db.test.update_one(
    {'k': 'd'},
    {'$rename': {'k': 'key'}},
)

# update with sort

db.test.find_one_and_update(
    {'k': {'$exists': 1}},
    {'$set': {'v': 'CC'}},
    sort=[('k', pymongo.DESCENDING)]
)

# update all from query

db.test.update_many(
    {'k': {'$exists': 1}},
    {'$set': {'num': 1}},
    #multi=True,
)

# replace

db.test.replace_one(
    {'key': 'f'},
    {'k': 'f', 'v': 'FF'}
)

# save

db.test.save(  # insert
    {
        'k': 'g',
        'v': 'G',
    },
)

_id = db.test.find_one({'k': 'g'}, {'_id': 1})['_id']
db.test.save(  # update because _id specified
    {
        '_id': _id,
        'k': 'gg',
        'v': 'GG',
    },
)

# push into array

db.test.update_one(
    {'k': 'gg'},
    {'$push': {'array': 'one'}}
)

db.test.update_one(
    {'k': 'gg'},
    {'$push': {'array': 'two'}}
)

# pull

db.test.update_one(
    {'k': 'gg'},
    {'$pull': {'array': 'one'}}
)

# current date

db.test.update_one(
    {'k': 'd'},
    {
        #'$set': {'date': '1'},
        '$currentDate': {'date': True},
    }
)

# update embedded

db.test.update_one(
    {'k': 'a'},
    {
        '$set': {'values.info': '*AAA'},
    }
)


####################

# show result

c = db.test.find({}, {'_id': 0})
for o in c:
    print o
