# Write your MySQL query statement below
SELECT id, min(IF(month='Jan', revenue, NULL)) Jan_Revenue, 
            min(IF(month='Feb', revenue, NULL)) Feb_Revenue,
            min(IF(month='Mar', revenue, NULL)) Mar_Revenue,
            min(IF(month='Apr', revenue, NULL)) Apr_Revenue,
            min(IF(month='May', revenue, NULL)) May_Revenue,
            min(IF(month='Jun', revenue, NULL)) Jun_Revenue,
            min(IF(month='Jul', revenue, NULL)) Jul_Revenue,
            min(IF(month='Aug', revenue, NULL)) Aug_Revenue,
            min(IF(month='Sep', revenue, NULL)) Sep_Revenue,
            min(IF(month='Oct', revenue, NULL)) Oct_Revenue,
            min(IF(month='Nov', revenue, NULL)) Nov_Revenue,
            min(IF(month='Dec', revenue, NULL)) Dec_Revenue
FROM Department
GROUP BY id