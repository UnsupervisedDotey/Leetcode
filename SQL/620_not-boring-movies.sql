# Write your MySQL query statement below
Select *
FROM cinema
WHERE MOD(id, 2) != 0 and description != 'boring'
ORDER BY rating DESC

# != 'boring'      还可以写成   <> 'boring'
# MOD(id, 2) != 0  还可以写成   id % 2 = 1