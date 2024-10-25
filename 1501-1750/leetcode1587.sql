# Write your MySQL query statement below
select u.name, sum(t.amount) as balance
from Transactions t left join Users u
using (account)
group by u.account
having balance > 10000;