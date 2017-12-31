--SOLUTION 1: SUBQUERY
select name from salesperson
where name not in 
	(select salesperson.name 
	from salesperson 
	join orders 
	on salesperson.sales_id = orders.sales_id 
	join company 
	on orders.com_id = company.com_id 
	where company.name = 'RED')


--SOLUTION 2: NO SUBQUERY
select salesperson.name
from orders o join company c on (o.com_id = c.com_id and c.name = 'RED')
right join salesperson on salesperson.sales_id = o.sales_id
where o.sales_id is null
