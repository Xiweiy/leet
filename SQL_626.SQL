##SOLUTION 1: UNION
SELECT id+1 as id, student from seat
where id%2 and id not in (select max(id) from seat)
union 
select id-1 as id, student from seat
where not id%2 
union 
select id, student from seat
where id%2 and id in (select max(id) from seat)
order by id



#SOLUTION 2: CASE
select 
    case 
      when id in (select max(id) from seat) and id%2 then id
      when id%2 then id+1
      else id-1 
      end as id,
    student
from seat
order by id
