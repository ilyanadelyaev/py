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
SELECT
    e.emp_id, e.fname, e.lname, b.name
FROM
    employee e
INNER JOIN
    branch b
ON
    e.assigned_branch_id = b.branch_id;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    a.account_id, c.fed_id, p.name
from
    account a
inner join
    customer c
on
    a.cust_id = c.cust_id
inner join
    product p
on
    a.product_cd = p.product_cd
where
    c.cust_type_cd = 'I'
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    e.emp_id, e.fname, e.lname
from
    employee e
inner join
    employee e_mng
on
    e.superior_emp_id = e_mng.emp_id
and
    e.dept_id != e_mng.dept_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
