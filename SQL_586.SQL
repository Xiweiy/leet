#SOLUTION 1: SUBQUERY, HAVING
select customer_number 
from orders 
group by customer_number
having count(distinct order_number) in 
    (select max(total_count) 
     from 
         (select customer_number, count(distinct order_number) as total_count from orders group by customer_number) a )

#SOLUTION 2: ORDER BY, LIMIT
SELECT customer_number
from orders
group by customer_number
order by count(distinct order_number) desc limit 1
