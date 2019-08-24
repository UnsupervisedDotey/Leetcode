SELECT IF(result.ConsecutiveNum>=3.0, result.Num, Null) ConsecutiveNums
FROM
    (SELECT target_t0.Num,
            IF(cur_num_t1.cur_num = target_t0.Num, @count_n:=@count_n+1, @count_n:=1) ConsecutiveNum
    FROM
        (SELECT Num, CONVERT((@rowNum:=@rowNum+1), SIGNED) AS SRank
         FROM Logs ss,
              (SELECT (@rowNum :=0)) bb,
              (SELECT (@count_n :=0)) cc) target_t0
    JOIN
        (SELECT (SELECT Num FROM Logs WHERE Id=1) AS cur_num, 1 AS Rank
        UNION ALL
        SELECT o1.Num AS cur_num, (Rank+1) AS Rank
        FROM
            (SELECT s.Num, CONVERT((@rowNum1:=@rowNum1+1), SIGNED) AS Rank
            FROM Logs s, (SELECT (@rowNum1 :=0)) b) o1
        WHERE o1.Rank <= (SELECT MAX(Id) FROM Logs)-1) cur_num_t1
    On target_t0.SRank=cur_num_t1.Rank) result
GROUP BY ConsecutiveNums
HAVING ConsecutiveNums IS NOT NULL