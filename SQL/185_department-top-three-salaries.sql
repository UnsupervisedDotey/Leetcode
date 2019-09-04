# JOIN ON 比 FROM WHERE t1, t2慢得多
# 少写子查询


# FROM 自己表 然后 WHERE 里面的条件，左边是自己表的和外面自己表的self join 结果，右边是数字

SELECT P1.Name AS Department, P2.Name AS Employee, P2.Salary AS Salary
FROM Employee AS P2
JOIN Department AS P1
ON P1.Id = P2.DepartmentId
WHERE (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee AS P3
    WHERE P2.DepartmentId = P3.DepartmentId
    AND P3.Salary >= P2.Salary
) <= 3
ORDER BY DepartmentId, Salary DESC


# TOP 97%

SELECT d.name Department, e.name Employee, e.Salary
FROM
    (SELECT *, @rank := if(@pre=DepartmentId, if(@spre=salary,@rank,@rank+1), 1) rank, @pre:=departmentid, @spre:=salary
    FROM employee,
        (SELECT @pre:=null, @spre:=null, @rank:=1) temp
    ORDER BY departmentid, salary DESC, id) e,
    department d
WHERE e.rank<=3 AND e.departmentid=d.id
