CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (

    SELECT Salary
    FROM
        (SELECT Salary, @i:=@i+1 orders
        FROM
            (SELECT DISTINCT Salary
             FROM Employee e
             ORDER BY Salary DESC) t1,
            (SELECT @i:=0) ii) t2
        WHERE t2.orders = N

  );
END