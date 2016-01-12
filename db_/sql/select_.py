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
    emp_id, fname, lname
from
    employee
order by
    lname, fname
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    account_id, cust_id, avail_balance
from
    account
where
    status = 'ACTIVE'
and
    avail_balance > 2500
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    open_emp_id, count(*)
from
    account
group by
    open_emp_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
SELECT
    p.product_cd, a.cust_id, a.avail_balance
FROM
    product p
INNER JOIN
    account a
ON
    p.product_cd = a.product_cd
WHERE
    p.product_type_cd = 'ACCOUNT'
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    account_id
from
    account
where
    year(open_date) = 2002
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    cust_id, lname
from
    individual
where
    lname like '_a%e%'
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
