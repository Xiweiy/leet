SELECT A.id AS ID 
FROM Weather AS A, Weather AS B
WHERE DATEDIFF(A.DATE, B.DATE) =1
AND A.Temperature > B.Temperature;
##DATE cannot be add/subtract directly in mysql
##has to use the function to do the substraction
##or use to_days function to convert the date to a number
