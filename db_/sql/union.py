import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="ilya",
    passwd="ilya",
    db="bank",
)

cur = db.cursor()


cur.execute(
"""
    select
        'I', cust_id, fname, lname
    from
        individual
union all
    select
        'E', emp_id, fname, lname
    from
        employee
order by
    lname
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20

db.close()
