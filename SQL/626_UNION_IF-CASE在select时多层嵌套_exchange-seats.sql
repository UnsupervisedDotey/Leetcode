# 我
SELECT id+1 id, student
  FROM seat
  WHERE id % 2 = 1 AND id <= (SELECT MAX(id) - MAX(id) % 2 FROM seat)
UNION
  SELECT id-1 id, student
  FROM seat
  WHERE id % 2 = 0 AND id <= (SELECT MAX(id) - MAX(id) % 2 FROM seat)
UNION
  SELECT id, student
  FROM seat
  WHERE id = (SELECT CASE WHEN MAX(id) % 2 = 1 THEN MAX(id) ELSE 0 END AS last
              FROM seat)
ORDER BY id




# top1
# ？？
# 所以有 CASE WHEN .c1. THEN .do1. ELSE .do2. END AS new_c1 等价于 IF(c1，do1，do2)

SELECT IF(id%2<>0,
          IF(id<>(SELECT MAX(id) FROM seat), id+1, id),
          id-1) id, student
FROM seat ORDER BY id;


# top2 这个好理解
SELECT CASE
		WHEN s.id % 2 = 1 AND s.id = (SELECT max(s2.id) FROM seat s2) then s.id
		when s.id % 2 = 1 then s.id+1
		when s.id % 2 = 0 then s.id-1
		END as id, student
from seat s
ORDER BY id


# top 3
select s1.id, s2.student
from seat s1, seat s2
where s1.id%2=1 and s2.id=s1.id+1
union
select s2.id, s1.student
from seat s1, seat s2
where s1.id%2=1 and s2.id=s1.id+1
union
select s1.id, s1.student
from seat s1
where s1.id%2=1 and s1.id = (select max(id) from seat)
order by id