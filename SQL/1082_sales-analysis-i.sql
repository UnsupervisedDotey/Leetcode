-- # Write your MySQL query statement below
SELECT seller_id
FROM Product p
JOIN Sales s
ON p.product_id = s.product_id
GROUP BY seller_id
HAVING SUM(quantity*unit_price)=(SELECT MAX(r1.sale)
                                FROM (SELECT seller_id, sum(quantity*unit_price) sale
                                        FROM Product p
                                        JOIN Sales s
                                        ON p.product_id = s.product_id
                                        GROUP BY seller_id
                                     ) r1
                                )

