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
    cust_id, count(*)
from
    account
group by
    cust_id
having
    count(*) >= 2
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    product_cd, open_branch_id, SUM(avail_balance) total_balance
from
    account
group by
    product_cd, open_branch_id
having
    count(*) > 1
order by
    total_balance
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
