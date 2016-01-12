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
    a.account_id, a.avail_balance, b.name
from
    account a
left outer join
    business b
on
    a.cust_id = b.cust_id
order by
    a.account_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    p.product_cd, p.name, a.account_id
from
    product p
left outer join
    account a
on
    p.product_cd = a.product_cd
order by
    a.account_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    a.account_id, a.avail_balance, a.cust_id,
    concat(i.fname, ' ', i.lname) i_name, b.name b_name
from
    account a
left outer join
    individual i
on
    a.cust_id = i.cust_id
left outer join
    business b
on
    a.cust_id = b.cust_id
order by
    a.account_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    a.account_id, a.avail_balance, a.cust_id, c.type, c.name
from
    account a
left outer join
    (
        select
            i.cust_id, 'I' type, concat(i.fname, ' ', i.lname) name
        from
            individual i
    union all
        select
            b.cust_id, 'B' type, b.name
        from
            business b
    ) c
on
    a.cust_id = c.cust_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
