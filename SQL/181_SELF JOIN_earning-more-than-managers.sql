# Write your MySQL query statement below
SELECT e1.name as Employee
FROM Employee e1
JOIN Employee e2
ON e1.ManagerId = e2.Id
WHERE e1.Salary > e2.Salary

# FROM后面接，隔开的两个表，是并排，且合并后的
SELECT Name AS Employee
FROM Employee AS E,
    (SELECT DISTINCT Id, Salary
    FROM Employee) AS M
WHERE E.ManagerId = M.Id AND E.Salary > M.Salary
