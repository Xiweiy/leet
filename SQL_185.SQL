##SOLUTION 1: JOIN
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


##SOLUTION 2: VARIABLE
SELECT 
    Department.Name as Department,
    C.Name as Employee,
    C.Salary
FROM
    (SELECT 
        A.Id, A.Name, A.Salary, A.DepartmentId, 
        @COUNT := (CASE WHEN DepartmentId=@PREV_DEPARTMENT AND Salary=@PREV_SALARY THEN @COUNT
                        WHEN DepartmentId=@PREV_DEPARTMENT THEN @COUNT+1
                        ELSE 1 END) AS TIMES,
        @PREV_DEPARTMENT := DepartmentId,
        @PREV_SALARY := Salary
    FROM (SELECT * FROM Employee ORDER BY DepartmentId, Salary DESC) A, 
         (SELECT @COUNT :=0, @PREV_DEPARTMENT := NULL, @PREV_SALARY :=NULL) B
     ) C
    JOIN Department
    ON C.DepartmentId=Department.Id
WHERE C.TIMES<=3
