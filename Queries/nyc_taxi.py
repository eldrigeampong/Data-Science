query1 = '''
         -- Returns Total Passenger Count In The Current Year

with
    passenger_count_tbl as (
                            select
                                  distinct
                                          extract(year from yt.tpep_pickup_datetime) as pickup_yr,
                                          sum(yt.passenger_count) over w1 as passenger_count
                            from yellow_taxi yt
                            where extract(year from current_date) = extract(year from yt.tpep_pickup_datetime)
                            window w1 as (partition by extract(year from yt.tpep_pickup_datetime))
            			   )
-- select all columns
select distinct * from passenger_count_tbl

         '''



query2 = '''
          -- Returns the longest trip duration and tip amount paid

with
    cte1 as (
             select 
                   distinct 
                           yt.tpep_pickup_datetime,
                           yt.tpep_dropoff_datetime,
                           (yt.tpep_dropoff_datetime - yt.tpep_pickup_datetime) as trip_duration,
                           extract(day from (yt.tpep_dropoff_datetime - yt.tpep_pickup_datetime)) as duration_in_days,
						   yt.tip_amount
             from yellow_taxi yt
             where yt.trip_distance > 0
            )
-- select all columns
select distinct * from cte1 order by trip_duration desc

         '''