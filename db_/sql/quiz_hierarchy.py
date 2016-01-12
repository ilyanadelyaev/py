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
create table hierarchy (
    id smallint,
    f_id smallint,
    m_id smallint,
    name varchar(20),
    constraint pk_hierarchy primary key (id),
    constraint fk_hierarchy_f_id foreign key (f_id) references hierarchy (id),
    constraint fk_hierarchy_m_id foreign key (m_id) references hierarchy (id)
);
"""
)
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (1, null, null, 'father father');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (2, null, null, 'father mother');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (3, null, null, 'mother father');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (4, null, null, 'mother mother');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (5, 1, 2, 'father');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (6, 3, 4, 'mother');")
cur.execute("insert into hierarchy ( id, f_id, m_id, name ) values (7, 5, 6, 'son');")
db.commit()


cur.execute(
"""
select * from hierarchy;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
drop table hierarchy;
"""
)
db.commit()


db.close()
