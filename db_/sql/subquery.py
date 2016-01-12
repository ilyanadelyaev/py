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
    emp_id, fname, lname, title
from
    employee
where
    emp_id in (
        select
            distinct superior_emp_id
        from
            employee
        where
            superior_emp_id is not null
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    account_id, cust_id
from
    account
where
    (open_emp_id, open_branch_id)
    in (
        select
            e.emp_id, b.branch_id
        from
            employee e
        inner join
            branch b
        on
            e.assigned_branch_id = b.branch_id
        where
            e.title = 'Head Teller'
        and
            b.name = 'Woburn Branch'
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
SELECT
    c.cust_id, c.cust_type_cd, c.city
FROM
    customer c
WHERE
    (
    SELECT
        SUM(a.avail_balance)
    FROM
        account a
    WHERE
        a.cust_id = c.cust_id
    )
BETWEEN 5000 AND 10000
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    a.account_id, a.cust_id, a.avail_balance
from
    account a
where
    exists (
        select
            txn_id
        from
            transaction t
        where
            a.account_id = t.account_id
        and
            date(txn_date) = '2001-05-23'
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    g.id, count(*)
from
    (
    select
        cust_id, sum(avail_balance) total_balance
    from
        account
    group by
        cust_id
    ) c
inner join
    (
        select
            'low' id, 0.00 low, 4999.99 high
    union all
        select
            'medium' id, 5000.00 low, 9999.99 high
    union all
        select
            'high' id, 10000.00 low, 9999999.99 high
    ) g
on
    c.total_balance between g.low and g.high
group by
    g.id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    p.name, b.name, concat(e.fname, ' ', e.lname), a.total_balance
from
    (
    select
        product_cd, open_branch_id, open_emp_id, sum(avail_balance) total_balance
    from
        account
    group by
        product_cd, open_branch_id, open_emp_id
    ) a
inner join
    product p
on
    a.product_cd = p.product_cd
inner join
    branch b
on
    a.open_branch_id = b.branch_id
inner join
    employee e
on
    a.open_emp_id = e.emp_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    concat(e.lname, ' ', e.fname), e.title, count(*)
from
    account a
inner join
    employee e
on
    a.open_emp_id = e.emp_id
group by
    a.open_emp_id
having
    count(*) = (
        select
            max(a_mx.mx)
        from
            (
            select
                count(*) mx
            from
                account
            group by
                open_emp_id
            ) a_mx
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    account_id, product_cd, cust_id, avail_balance
from
    account
where
    product_cd in (
        select
            product_cd
        from
            product
        where
            product_type_cd = 'LOAN'
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    a.account_id, a.product_cd, a.cust_id, a.avail_balance
from
    account a
where
    exists (
        select
            1
        from
            product p
        where
            a.product_cd = p.product_cd
        and
            p.product_type_cd = 'LOAN'
    )
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    e.emp_id id,
    concat(e.fname, ' ', e.lname) name,
    (
        select
            d.name
        from
            department d
        where
            d.dept_id = e.dept_id
    ) dept,
    (
        select
            b.name
        from
            branch b
        where
            e.assigned_branch_id = b.branch_id
    ) branch
from
    employee e;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
