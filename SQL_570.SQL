select b.Name
from Employee a
join Employee b
on a.ManagerId = b.Id
group by b.Name
having count(distinct a.Name)>=5
