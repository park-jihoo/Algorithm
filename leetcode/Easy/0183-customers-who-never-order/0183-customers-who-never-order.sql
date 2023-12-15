# Write your MySQL query statement below
select Name as Customers from Customers left join Orders on Customers.Id = Orders.CustomerId where CustomerId is null