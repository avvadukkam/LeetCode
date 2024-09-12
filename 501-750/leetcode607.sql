SELECT s.name
FROM SalesPerson s
WHERE s.sales_id not in (
    select o.sales_id
    from Orders o
    left join Company c
    on o.com_id = c.com_id
    where o.com_id = c.com_id and c.name='RED'
);