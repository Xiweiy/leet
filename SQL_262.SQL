SELECT A.Request_at AS Day,
    ROUND(SUM(CASE WHEN A.Status LIKE 'cancelled%' THEN 1 ELSE 0 END)/COUNT(*) ,2) AS 'Cancellation Rate'
FROM Trips A
INNER JOIN Users B
ON A.Client_Id = B.Users_Id 
WHERE B.Banned = 'No'
AND (A.Request_at BETWEEN '2013-10-01' AND '2013-10-03')
GROUP BY Day;
