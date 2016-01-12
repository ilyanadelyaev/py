import time
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
create table test (
    id int auto_increment,
    name varchar(30),
    constraint pk_test primary key (id)
);
"""
)
db.commit()


for i in xrange(1000):
    cur.execute(
    """
    insert into
        test (
            name
        )
    values
        (
            'test_data_{i}'
        )
    ;
    """.format(i=i)
    )
    db.commit()


st = time.time()
cur.execute(
"""
select * from test where name like 'te%';
"""
)
print time.time() - st


cur.execute(
"""
alter table
    test
add index
    idx_test_name (name)
;
"""
)


cur.execute(
"""
show index from test;
"""
)
for row in cur.fetchall():
    print row


st = time.time()
cur.execute(
"""
select * from test where name like 'te%';
"""
)
print time.time() - st


cur.execute(
"""
alter table
    test
drop index
    idx_test_name
;
"""
)


cur.execute(
"""
show index from test;
"""
)
for row in cur.fetchall():
    print row


st = time.time()
cur.execute(
"""
select * from test where name like 'te%';
"""
)
print time.time() - st


cur.execute(
"""
drop table test;
"""
)
db.commit()


db.close()
