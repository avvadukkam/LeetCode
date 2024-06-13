# Write your MySQL query statement below
SELECT e2.name as Employee
FROM employee e1
LEFT JOIN employee e2 ON e1.id = e2.managerID
WHERE
e1.salary < e2.salary