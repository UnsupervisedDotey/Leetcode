SELECT finalscore.Score, CONVERT(IF(finalscore.Score = maxscorescol.maxscore,
                            @ranks:=@ranks,
                           @ranks:=@ranks+1), SIGNED) AS Rank
FROM
    (SELECT Score, CONVERT((@rowNum:=@rowNum+1), SIGNED) AS SRank
     FROM Scores sS,
          (SELECT (@rowNum :=0)) bb,
          (SELECT (@ranks :=1)) cc
     ORDER BY Score DESC) finalscore
JOIN
    (SELECT MAX(Score) AS maxscore, 1 AS Rank From Scores
    UNION ALL
    SELECT o1.Score AS maxscore, (Rank+1) AS Rank
    FROM
        (SELECT s.Score, CONVERT((@rowNum1:=@rowNum1+1), SIGNED) AS Rank
        FROM Scores s, (SELECT (@rowNum1 :=0)) b
        ORDER BY s.Score DESC) o1
    WHERE o1.Rank < @rowNum1) maxscorescol
On finalscore.SRank=maxscorescol.Rank