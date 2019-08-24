# Write your MySQL query statement below
SELECT Name Customers
FROM Customers
WHERE Id not in
    (SELECT c.Id
    FROM Customers c
    JOIN Orders o
    On c.Id = o.CustomerId)
