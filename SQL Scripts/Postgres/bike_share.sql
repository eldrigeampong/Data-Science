-- Returns bike rental history overtime

with
    bike_rental_tbl as (
                        select 
                              distinct 
                                      bs.trip_id,
                                      bs.start_time,
                                      bs.end_time,
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