SELECT C.Name  AS Department, B.Name AS Employee, B.Salary
FROM (
    SELECT MAX(SALARY) AS HIGHEST, DepartmentId FROM Employee GROUP BY DepartmentId) A
INNER JOIN Employee B
    ON A.HIGHEST = B.SALARY
    AND A.DepartmentId = B.DepartmentId
INNER JOIN Department C
    ON A.DepartmentId = C.Id;
