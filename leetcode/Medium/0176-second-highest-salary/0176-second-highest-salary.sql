# Write your MySQL query statement below

SELECT CASE
           WHEN COUNT(DISTINCT SALARY) = 1 THEN NULL
           ELSE
                  (SELECT DISTINCT SALARY
                   FROM EMPLOYEE
                   ORDER BY SALARY DESC
                   LIMIT 1,
                         1)
       END AS SecondHighestSalary
FROM EMPLOYEE;