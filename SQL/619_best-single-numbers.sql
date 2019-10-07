# Write your MySQL query statement below
SELECT (SELECT num
    FROM my_numbers t1
    GROUP BY num
    HAVING count(t1.num)=1
    ORDER BY num DESC
    LIMIT 1
) AS num