# Write your MySQL query statement below

SELECT project_id
FROM
    (SELECT project_id, COUNT(employee_id) c
    FROM Project
    GROUP BY project_id) t1
WHERE t1.c=(SELECT COUNT(employee_id) c
    FROM Project
    GROUP BY project_id
    ORDER BY c DESC
    LIMIT 1)
ORDER BY project_id