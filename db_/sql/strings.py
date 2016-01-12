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
create table string_tbl (
    char_fld char(30),
    vchar_fld varchar(30),
    text_fld text
);
"""
)
db.commit()


cur.execute(
"""
insert into
    string_tbl
    (
        char_fld, vchar_fld, text_fld
    )
values
    (
        'char string', 'varchar string', 'text string''s'
    )
;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
update
    string_tbl
set
    char_fld = concat(char_fld, ' 2')
where
    text_fld = 'text string''s'
;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
select char_fld, vchar_fld, quote(text_fld) from string_tbl;
"""
)
for row in cur.fetchall():
    print row


cur.execute(
"""
drop table string_tbl;
"""
)
db.commit()


db.close()
