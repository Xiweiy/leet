##SOLUTION 1
SELECT DISTINCT A.EMAIL AS EMAIL
FROM Person AS A, Person AS B
WHERE A.ID != B.ID
AND A.EMAIL = B.EMAIL;


##SOLUTION 2
SELECT EMAIL FROM Person
GROUP BY EMAIL
Having Count(ID)>1
