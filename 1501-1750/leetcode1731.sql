# Write your MySQL query statement below
SELECT 
    mgr.employee_id,
    mgr.name,
    count(emp.employee_id) AS reports_count,
    round(avg(emp.age)) as average_age
 FROM employees emp JOIN employees mgr
 ON emp.reports_to = mgr.employee_id
 GROUP BY employee_id
 ORDER BY employee_id;