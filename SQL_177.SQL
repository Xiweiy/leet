CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N -1;     ##SET THE N VALUE BEFORE RETURN;
  RETURN (
      # Write your MySQL query statement below.

      SELECT (
          SELECT DISTINCT Salary FROM Employee    ##DISTINCT IS IMPORTANT
          ORDER BY Salary DESC
          LIMIT 1 OFFSET N
          )
  );
END
