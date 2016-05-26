
SELECT E.Name AS Department, D.Name AS Employee, C.Salary 
FROM (
    SELECT B.Salary, B.DepartmentId 
    FROM (SELECT Salary, DepartmentId, max(id) as id FROM Employee Group by DepartmentId, Salary) A   ##TOP 3 SALARY without repetition
    INNER JOIN Employee B
    ON A.DepartmentId = B.DepartmentId
    AND A.Salary >= B.Salary
    GROUP BY B.DepartmentId, B.Salary
    HAVING COUNT(DISTINCT A.ID)<=3 
    ) C
INNER JOIN Employee D
ON D.DepartmentId = C.DepartmentId 
AND D.Salary = C.Salary
INNER JOIN Department E
ON D.DepartmentId = E.Id
ORDER BY Salary DESC;
