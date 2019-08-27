SELECT t1.Request_at Day, ROUND(ifnull(t2.cancel_count, 0.001)/t1.down, 2) 'Cancellation Rate'
FROM
    (SELECT Request_at, count(*) down
    FROM Trips
    WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE ROLE='client' and Banned='Yes')       GROUP BY Request_at) t1
LEFT JOIN
    (SELECT Request_at, count(*) cancel_count
    FROM Trips
    WHERE Client_Id NOT IN (SELECT Users_Id FROM Users WHERE ROLE='client' and Banned='Yes')            AND Status LIKE 'cancel%'
    GROUP BY Request_at) t2
ON t1.Request_at = t2.Request_at
WHERE t1.Request_at IN ("2013-10-01", "2013-10-02", "2013-10-03")
ORDER BY Day
