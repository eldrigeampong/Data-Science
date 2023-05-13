query1 = '''
         -- Returns Count Of Passengers Picked Up Over Time

with
    passenger_count_tbl as (
                            select 
                                  distinct 
                                          yt.tpep_pickup_datetime,
                                          yt.passenger_count 
                            from yellow_taxi yt 
                            )
select
	  distinct 
	          *
from
	passenger_count_tbl
order by
	1 asc
    
         '''