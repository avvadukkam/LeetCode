# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE A FROM Person A, Person B WHERE A.id > B.id AND A.email=B.email;

# or

# Write your MySQL query statement below
delete p1 from Person p1 join Person p2
on p1.email = p2.email
where p1.id > p2.id