SELECT A.Score, C.Rank
FROM Scores A
INNER JOIN (
    SELECT Score, @ROWNAME := @ROWNAME +1 AS RANK
    From (SELECT Score FROM Scores Group by Score Order by Score DESC ) B, (SELECT @ROWNAME:=0) AS R
    ) C
ON A.Score = C.Score
ORDER BY Score DESC;


