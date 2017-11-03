DELETE FROM Person 
WHERE ID NOT IN (SELECT ID 
		FROM (SELECT MIN(Id) AS ID 
			FROM Person 
			GROUP BY Email) AS A
		);


##Solution 2
Delete from Person
wHERE id in (Select * FROM (SELECT a.ID from Person a, Person b Where a.Email=b.Email and a.Id > b.Id) A)

Note： If want to do delete and join together, have to bury the subquery deeper. In this case, the join is unnecessary.
