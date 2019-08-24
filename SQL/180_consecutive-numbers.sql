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


#leetcode
SELECT *
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num



# top 1
select distinct Num as "ConsecutiveNums"
from Logs
where (Id + 1, Num) in (select * from Logs) and (Id + 2, Num) in (select * from Logs)