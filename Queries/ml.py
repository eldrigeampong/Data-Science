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



query2 = '''
         -- Returns bike rental history overtime

with
    bike_rental_tbl as (
                        select 
                              distinct 
                                      bs.trip_id,
                                      bs.start_time::timestamp,
                                      bs.duration,
                                      bs.start_lat,
                                      bs.start_lon,
                                      bs.end_lat,
                                      bs.end_lon,
                                      bs.plan_duration,
                                      bs.trip_route_category 
                        from bike_share bs
                       )
select
	  distinct *
from
	bike_rental_tbl
order by
	start_time asc
    
         '''