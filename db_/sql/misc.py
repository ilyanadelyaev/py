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
create table corporation (
    corp_id smallint,
    name varchar(30),
    constraint pk_corporation primary key (corp_id)
);
"""
)
db.commit()


cur.execute(
"""
insert into corporation
    (corp_id, name)
select
    27, 'Acme paper corp'
where not exists
    (select corp_id, name from corporation where corp_id = 27);
"""
)
db.commit()


cur.execute(
"""
select name from corporation where corp_id = 27;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
drop table corporation;
"""
)
db.commit()


db.close()
