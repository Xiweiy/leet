
Select class
from courses
group by class
having count(distinct student)>=5
##Have to consider duplicate item
