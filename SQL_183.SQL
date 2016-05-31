SELECT  Name AS Customers
FROM Customers AS A
LEFT JOIN Orders AS B
ON A.Id = B.CustomerId
WHERE B.ID IS NULL;
