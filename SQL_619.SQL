select max(num) as num
from (
select num
from number
group by 1
having count(num)=1) a
