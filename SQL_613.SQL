select min(b.x - a.x) as shortest
from point a, point b
where a.x < b.x
