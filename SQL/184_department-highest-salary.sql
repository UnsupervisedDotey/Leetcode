# Write your MySQL query statement below
SELECT dd.Name Department, ee.Name Employee, ee.Salary Salary
FROM
    Employee ee
JOIN Department dd
ON ee.DepartmentId = dd.Id
WHERE (ee.DepartmentId, Salary) IN (SELECT e.DepartmentId, MAX(Salary) Salary
                                    FROM Employee e
                                    JOIN Department d
                                    ON e.DepartmentId = d.Id
                                    GROUP BY d.Id)
