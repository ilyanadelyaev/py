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
    a.account_id, a.avail_balance, a.cust_id,
    c.cust_type_cd,
    case
        when c.cust_type_cd = 'I' then
            concat(i.fname, ' ', i.lname)
        when c.cust_type_cd = 'B' then
            b.name
        else
            'UNKNOWN'
        end
    name
from
    account a
inner join
    customer c
on
    a.cust_id = c.cust_id
left outer join
    individual i
on
    c.cust_id = i.cust_id
left outer join
    business b
on
    c.cust_id = b.cust_id
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
    c.cust_type_cd,
    case
        when c.cust_type_cd = 'I' then
            (
            select
                concat(i.fname, ' ', i.lname)
            from
                individual i
            where
                c.cust_id = i.cust_id
            )
        when c.cust_type_cd = 'B' then
            (
            select
                b.name
            from
                business b
            where
                c.cust_id = b.cust_id
            )
        else
            'UNKNOWN'
        end
    name
from
    account a
inner join
    customer c
on
    a.cust_id = c.cust_id
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    emp_id, title,
    case
        when title in ('President', 'Vice President', 'Treasurer', 'Loan Manager') then
            'Management'
        when title in ('Operations Manager', 'Head Teller', 'Teller') then
            'Operations'
        else
            'Unknown'
    end
    title_2
from
    employee
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


db.close()
