SELECT id+1 as id, student from seat
where id%2 and id not in (select max(id) from seat)
union 
select id-1 as id, student from seat
where not id%2 
union 
select id, student from seat
where id%2 and id in (select max(id) from seat)
order by id
