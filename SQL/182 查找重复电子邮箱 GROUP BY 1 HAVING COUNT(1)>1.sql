# Write your MySQL query statement below
SELECT Email 
FROM 
    (SELECT Email, COUNT(*) email_count 
     FROM Person GROUP BY 1) c
WHERE C.email_count > 1

# Write your MySQL query statement below
select email from person group by email having count(email) > 1

# Best
select Email from Person group by Email having count(distinct Id) > 1;