import bson.code

import pymongo


client = pymongo.MongoClient()
db = client.test

db.map_reduce__coll.drop()

r_coll = db.restaurants
z_coll = db.zips


# calculate total score for each grade

map_f = bson.code.Code("""
    function () {
        this.grades.forEach( function ( obj ) {
            emit(
                obj.grade,
                {
                    score: obj.score,
                    count: 1,
                }
            );
        });
    }
""")

reduce_f = bson.code.Code("""
    function ( grade, scores ) {
        var result = {score: 0, count: 0};
        scores.forEach( function ( obj ) {
            result.score += obj.score;
            result.count += obj.count;
        });
        return result;
    }
""")

fin_f = bson.code.Code("""
    function ( grade, result ) {
        if ( result.count == 0 )
            return result;
        result.avg = result.score / result.count;
        return result;
    }
""")


ret = r_coll.map_reduce(
    map_f, reduce_f,
    out='map_reduce__coll',
    finalize=fin_f,
    query={
        'cuisine': 'Irish',
    },
)
for o in ret.find():
    print o


print '=' * 20


# calculate population per state

map_f = bson.code.Code("""
    function () {
        emit(this.state, this.pop);
    }
""")

reduce_f = bson.code.Code("""
    function ( key, values ) {
        return Array.sum(values);
    }
""")

ret = z_coll.map_reduce(
    map_f, reduce_f,
    out='map_reduce__coll',
)
for o in ret.find():
    print o
