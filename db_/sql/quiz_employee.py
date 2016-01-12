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
create table department (
    dept_id smallint auto_increment,
    name varchar(30),
    constraint pk_department primary key (dept_id)
);
"""
)
cur.execute("insert into department ( name ) values ( 'Management' );")
cur.execute("insert into department ( name ) values ( 'Design' );")
cur.execute("insert into department ( name ) values ( 'Service' );")
cur.execute("insert into department ( name ) values ( 'Account' );")
cur.execute(
"""
create table employee (
    emp_id int auto_increment,
    name varchar(30),
    dept_id smallint,
    salary int,
    constraint pk_employee primary key (emp_id),
    constraint fk_dept_id foreign key (dept_id) references department (dept_id)
);
"""
)
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Mary', 3, 10000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Max', 3, 12000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'John', 3, 8000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Henry', 1, 50000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Susan', 1, 51000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Charles', 2, 22000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Louis', 2, 16000 );")
cur.execute("insert into employee ( name, dept_id, salary ) values ( 'Frank', 3, 12000 );")
db.commit()


cur.execute(
"""
select
    name, salary
from
    employee
where
    salary in (
        select max(salary) from employee
        where
            salary not in (
                select max(salary) from employee
            )
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
    d.name, max(e.salary)
from
    employee e
right outer join
    department d
on
    d.dept_id = e.dept_id
group by
    d.dept_id
order by
    d.dept_id
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    emp_id, name, salary
from
    employee
where
    salary >= 10000
order by
    salary desc
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
select
    emp_id, name
from
    employee
where
    upper(name) like '%MA%'
;
"""
)
for row in cur.fetchall():
    print row
print '=' * 20


cur.execute(
"""
drop table employee;
"""
)
cur.execute(
"""
drop table department;
"""
)
db.commit()


db.close()
