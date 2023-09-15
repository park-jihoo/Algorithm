# Write your MySQL query statement below

SELECT d.name AS department,
       e.name AS employee,
       e.salary AS salary
FROM EMPLOYEE e
JOIN DEPARTMENT d ON e.DepartmentId = d.id
WHERE 3 >
    (SELECT COUNT(DISTINCT (e2.Salary))
     FROM EMPLOYEE e2
     WHERE e2.Salary > e.Salary
       AND e.DepartmentId = e2.DepartmentId )