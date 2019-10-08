-- inner join 就是排列组合

SELECT min(abs(p1.x-p2.x)) as shortest
FROM point p1, point p2
WHERE p1.x!=p2.x