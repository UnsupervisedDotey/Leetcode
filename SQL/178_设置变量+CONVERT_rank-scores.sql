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



# @rowNum 等参数+1后变成浮点，需要直接转换为整数：cast( s.Rank as signed integer)






###############
# topN
# self join的形式，把select里面装个同表子查询，再from相同的表
# count discint就可以了查出有多少个不同的分数，是大于当前最高分的（然后遍历往下）。。。

select b.Score as Score,
    (select count(distinct a.Score)
    from Scores a
    where a.Score>=b.Score) as Rank
from Scores b order by Score desc;









#######
# top1 神仙

select s1.Score,s1.rank from
(

  # 找出有哪些不重复的分数，从高到低编号,然后这个像字典一样的小表，join原表即可
  # * join 一个参数 不用写 on

  select @row_num := @row_num+1 rank, score from
    (
        select distinct score from scores order by score desc
    ) t1 join
    (
        select @row_num :=0 from dual
    ) t2
) s1
join scores s2
where s1.score = s2.score order by s1.rank;