select a.name, b.bonus
from Employee a
left join Bonus b
on a.empId = b.empId
where (b.bonus<1000 or b.bonus is null) 
##need to add condition(bonus is null) since employee will not show up in the bonus table if there's no bonus
