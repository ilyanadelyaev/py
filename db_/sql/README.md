# py-sql-account

## MySQL
```
mysql> create database bank;
Query OK, 1 row affected (0.01 sec)

mysql> use bank;
Database changed

mysql> source ./source.sql
Query OK, 0 rows affected (0.04 sec)
...
Records: 21  Duplicates: 0  Warnings: 0

mysql> show tables;
+----------------+
| Tables_in_bank |
+----------------+
| account        |
...
| transaction    |
+----------------+
11 rows in set (0.00 sec)
```
