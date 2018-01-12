select distinct a.seat_id
from cinema a, cinema b
where (a.seat_id = b.seat_id -1 or a.seat_id = b.seat_id +1 )
and a.free =1 and b.free=1
