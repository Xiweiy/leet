SELECT FirstName, LastName, City,State
FROM Person AS A
LEFT JOIN Address AS B
ON A.PersonId = B.PersonId;

