import pprint

import pymongo


client = pymongo.MongoClient()
db = client.test

db.data.drop()

db.data.insert({'a': 0, 'b': 10})
db.data.insert({'a': 1, 'b': 11})
db.data.insert({'a': 2, 'b': 12})
db.data.insert({'a': 3, 'b': 13})
db.data.insert({'a': 4, 'b': 14})
db.data.insert({'a': 5, 'b': 15})

db.data.ensure_index([('a', 1), ('b', 1)])

#pprint.pprint(db.data.find( { 'a': { '$gt': 4 } } ).sort( [('a', 1), ('b', 1)] ).explain())
#pprint.pprint(db.data.find( { 'a': 5, 'b': { '$lt': 3} } ).sort( [( 'b', 1 )] ).explain())
#pprint.pprint( db.data.find( { 'b': 5 } ).sort( [( 'a', 1)] ).explain())  # sort only
#pprint.pprint( db.data.find( { 'a': 1 } ).explain())
#pprint.pprint( db.data.find( { 'b': 1 } ).explain())

db.data.drop()


db.data.insert( { '_id': 0, 'a': 1 } )
db.data.insert( { '_id': 1, 'a': { 'b': 1 } } )
db.data.insert( { '_id': 2, 'a': [ 1, 2, 4 ] } )
db.data.insert( { '_id': 3, 'a': None } )
db.data.insert( { '_id': 4 } )

#for o in db.data.find( { 'a': { '$exists': True } } ).sort([('_id', 1)]):
#    print o

db.data.drop()


db.data.insert({'a': 1, 'b': 10, 'c': 100, 'd': 1000})
db.data.insert({'a': 2, 'b': 20, 'c': 200, 'd': 2000})
db.data.insert({'a': 3, 'b': 30, 'c': 300, 'd': 3000})
db.data.insert({'a': 4, 'b': 40, 'c': 400, 'd': 4000})
db.data.insert({'a': 5, 'b': 50, 'c': 500, 'd': 5000})
db.data.insert({'a': 6, 'b': 60, 'c': 600, 'd': 6000})

db.data.ensure_index([('a', 1), ('b', 1), ('c', 1), ('d', 1)])

#pprint.pprint(db.data.find({ 'a': 5, 'b': 3 }).sort([ ('a', 1), ('b', 1), ('c', 1) ]).explain())
#pprint.pprint(db.data.find({ 'a': 5, 'b': 3 }).sort([ ('a', 1) ]).explain())
#pprint.pprint(db.data.find({ 'a': 5, 'b': 3 }).sort([ ('c', 1) ]).explain())
#pprint.pprint(db.data.find({ 'a': 5, 'b': 3 }).sort([ ('c', 1), ('d', 1) ]).explain())

db.data.drop()


db.data.insert({ 'a': [ 5 ] })
db.data.insert({ 'a': [ 5, 3 ] })
db.data.insert({ 'a': [ 3 ] })
db.data.insert({ 'a': [ 3, 'dsaf' ] })

#for o in db.data.find( { 'a': [ 5, 3 ] } ):  # ok
#    print o
#for o in db.data.find( { 'a': {'$and': [ 5, 3 ]} } ):  # WTF
for o in db.data.find( { '$and': [ { 'a': { '$in': [3] } }, { 'a': { '$in': [5] } } ] } ):  # fixed
    print o
#for o in db.data.find( { 'a': {'$all': [ 5, 3 ]} } ):
#    print o
