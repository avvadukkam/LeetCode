# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE A FROM Person A, Person B WHERE A.id > B.id AND A.email=B.email;