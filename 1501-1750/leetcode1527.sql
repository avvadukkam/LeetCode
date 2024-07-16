#Simple Solution
# Write your MySQL query statement below
select * from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'


# or
# Write your MySQL query statement below
select * from Patients
where conditions REGEXP '\\bDIAB1'