# Write your MySQL query statement below
Select *
FROM cinema
WHERE MOD(id, 2) != 0 and description != 'boring'
ORDER BY rating DESC