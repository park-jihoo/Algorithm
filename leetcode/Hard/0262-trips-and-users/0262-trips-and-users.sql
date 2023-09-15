# Write your MySQL query statement below

SELECT A.REQUEST_AT AS DAY,
       ROUND(COUNT(IF(A.STATUS = 'completed', NULL, A.STATUS)) / COUNT(A.STATUS), 2) AS 'Cancellation Rate'
FROM TRIPS A
JOIN
  (SELECT *
   FROM USERS
   WHERE BANNED = 'No'
     AND ROLE = 'driver') B ON a.driver_id = b.users_id
JOIN
  (SELECT *
   FROM USERS
   WHERE BANNED = 'No'
     AND ROLE = 'client') C ON a.client_id = c.users_id
WHERE DATE_FORMAT(A.REQUEST_AT, '%Y%m%d') BETWEEN '20131001' AND '20131003'
GROUP BY A.REQUEST_AT