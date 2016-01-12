import MySQLdb


db = MySQLdb.connect(
    host="localhost",
    user="ilya",
    passwd="ilya",
    db="test",
)

cur = db.cursor()


cur.execute(
"""
select
    ( one.val + ten.val + 1 ) num
from
    (
        select 0 val
    union all
        select 1 val
    union all
        select 2 val
    union all
        select 3 val
    union all
        select 4 val
    union all
        select 5 val
    union all
        select 6 val
    union all
        select 7 val
    union all
        select 8 val
    union all
        select 9 val
    ) one
cross join
    (
        select 0 val
    union all
        select 10 val
    union all
        select 20 val
    union all
        select 30 val
    union all
        select 40 val
    union all
        select 50 val
    union all
        select 60 val
    union all
        select 70 val
    union all
        select 80 val
    union all
        select 90 val
    ) ten
order by
    num;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
create table test (
    id int
);
"""
)
db.commit()


for i in xrange(20):
    cur.execute("insert into test ( id ) values ( {} );".format(i + 1))
cur.execute("delete from test where id = 2;")
cur.execute("delete from test where id = 10;")
cur.execute("delete from test where id = 11;")
cur.execute("delete from test where id = 12;")
cur.execute("delete from test where id = 16;")
cur.execute("delete from test where id = 17;")
cur.execute("delete from test where id = 19;")
db.commit()


cur.execute(
"""
select * from test;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    t.id + 1, (select min(id) from test where id > t.id) - 1
from
    test t
where
    t.id + 1 != (select min(id) from test where id > t.id)
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    t1.id, t2.id
from
    test t1
right outer join
    (select id + 1 id from test) t2
on
    t1.id = t2.id
having
    t1.id is null;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
drop table test;
"""
)
db.commit()


db.close()
