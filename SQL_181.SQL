SELECT A.Name as Employee
FROM Employee A
INNER JOIN Employee B
WHERE A.ManagerID = B.ID
AND A.SALARY > B.SALARY;
