import pymongo


client = pymongo.MongoClient()
db = client.test

r_coll = db.restaurants
z_coll = db.zips


# $project

for o in z_coll.aggregate([
    {'$project': {'_id': 0, 'c': '$city'}},
    {'$limit': 1},
]):
    print o

# $match

for o in z_coll.aggregate([
    {'$match': {'state': 'NY'}},
    {'$limit': 1},
]):
    print o

# $or

for o in z_coll.aggregate([
    {'$match': {'$or': [ {'pop': {'$lt': 10}}, {'pop': {'$gt': 100000}} ]}},
    {'$sort': {'pop': -1}},
    {'$limit': 1},
]):
    print o

# $literal

for o in z_coll.aggregate([
    {'$project': {'_id': 0,
        'name': {'$literal': 'name'},
        'key.value_a': {'$literal': 'A'},
        'key.value_b': {'$literal': 'B'},
    }},
    {'$limit': 1},
]):
    print o

# $slice

for o in z_coll.aggregate([
    {'$project': {'_id': 0,
        'val': {'$slice': ['$loc', 0, 1]},
    }},
    {'$limit': 1},
]):
    print o

# $concat

for o in z_coll.aggregate([
    {'$project': {'_id': 0,
        'val': {'$concat': ['$state', '.', '$city']},
    }},
    {'$limit': 1},
]):
    print o

# $skip

for o in z_coll.aggregate([
    {'$sort': {'pop': -1}},
    {'$skip': 1},
    {'$limit': 1},
]):
    print o

# $unwind

for o in z_coll.aggregate([
    {'$unwind': '$loc'},
    {'$limit': 2},
]):
    print o

# $unwind with pos

for o in z_coll.aggregate([
    {'$unwind': {'path': '$loc', 'includeArrayIndex': 'loc_pos'}},
    {'$limit': 2},
]):
    print o

# $group / $sum

for o in z_coll.aggregate([
    {'$group': {'_id': '$state', 'total_pop': {'$sum': '$pop'}}},
    {'$sort': {'total_pop': -1}},
    {'$limit': 1},
]):
    print o

# $group / $push

for o in z_coll.aggregate([
    {'$sort': {'state': 1, 'pop': 1}},
    {'$group': {'_id': '$state', 'total_pop': {'$push': {'pop': '$pop', 'city': '$city'}}}},
    {'$limit': 1},
]):
    print o

# $first / $last

for o in z_coll.aggregate([
    {'$sort': {'state': 1, 'pop': 1}},
    {'$group': {
        '_id': '$state',
        'mi_pop': {'$first': '$pop'},
        'mi_city': {'$first': '$city'},
        'mx_pop': {'$last': '$pop'},
        'mx_city': {'$last': '$city'},
    }},
    {'$project': {
        '_id': 1,
        'mi.pop': '$mi_pop',
        'mi.city': '$mi_city',
        'mx.pop': '$mx_pop',
        'mx.city': '$mi_city',
    }},
    {'$limit': 1},
]):
    print o

import sys; sys.exit(-1)


# Top-10 by cuisine in Manhattan

for o in r_coll.aggregate([
    {'$match': {'borough': 'Manhattan'}},
    {'$group': {'_id': '$cuisine', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}},
    {'$limit': 10},
    {'$project': {'_id': 1}},
]):
    print o

# Count grades via $unwind

for o in r_coll.aggregate([
    {'$unwind': '$grades'},
    {'$group': {'_id': '$grades.grade', 'count': {'$sum': 1}}}
]):
    print o

# 10M states

for o in z_coll.aggregate([
    {'$group': {'_id': '$state', 'pop': {'$sum': '$pop'}}},
    {'$sort': {'pop': -1}},
    {'$match': {'pop': {'$gte': 10000000}}},
]):
    print o

# Avg population per state

for o in z_coll.aggregate([
    {'$group': {'_id': {'state': '$state', 'city': '$city'}, 'pop': {'$sum': '$pop'}}},
    {'$group': {'_id': '$_id.state', 'pop_avg': {'$avg': '$pop'}}},
    {'$sort': {'pop_avg': -1}},
]):
    print o

# Biggest city in state

for o in z_coll.aggregate([
    {'$group': {'_id': {'state': '$state', 'city': '$city'}, 'pop': {'$sum': '$pop'}}},
    {'$sort': {'pop': 1}},
    {'$group': {'_id': '$_id.state','mx_city_name': {'$last': '$_id.city'}, 'mx_city_pop': {'$last': '$pop'}}},
    {'$project': {'_id': '$_id', 'biggest_city': {'name': '$mx_city_name', 'pop': '$mx_city_pop'}}},
    {'$sort': {'biggest_city.pop': -1}},
]):
    print o
