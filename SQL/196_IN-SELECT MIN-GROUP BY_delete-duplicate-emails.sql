# Write your MySQL query statement below
DELETE FROM Person
WHERE Id NOT IN
    (SELECT t3.Id FROM
        (SELECT MIN(Id) Id
        FROM Person
        GROUP BY Email
        ) t3
    )