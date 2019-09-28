# Write your MySQL query statement below
SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING max(s.sale_date) <= '2019-03-31' AND max(s.sale_date) >= '2019-01-01'
        AND min(s.sale_date) <= '2019-03-31' AND min(s.sale_date) >= '2019-01-01'

