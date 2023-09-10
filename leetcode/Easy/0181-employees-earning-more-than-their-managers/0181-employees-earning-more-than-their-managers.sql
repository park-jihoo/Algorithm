# Write your MySQL query statement below
select a.Name as Employee from Employee a, Employee b where a.ManagerId=b.Id and a.Salary>b.Salary