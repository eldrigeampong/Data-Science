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





-- Returns the longest trip duration

with
    trip_duration_tbl as (
                          select 
                                distinct 
                                        yt.tpep_pickup_datetime,
                                        yt.tpep_dropoff_datetime,
                                        (yt.tpep_dropoff_datetime - yt.tpep_pickup_datetime) as trip_duration,
                                        extract(day from (yt.tpep_dropoff_datetime - yt.tpep_pickup_datetime)) as duration_in_days
                          from yellow_taxi yt
                          where yt.trip_distance > 0
                         )
-- select all columns
select distinct * from trip_duration_tbl order by duration_in_days desc





-- Returns fare amount for each payment type

with 
    fare_amount_tbl as (
                       select
                             distinct
                                     (
                                      case
                                     	 when yt."VendorID" = 1 then 'Creative Mobile Technologies, LLC'
                                     	 when yt."VendorID" = 2 then 'VeriFone Inc'
                                       else 'unknown'
                                      end
                                     ) as vendor_name,
                                     (
                                      case
                                      	  when yt."RatecodeID" = 1 then 'Standard rate'
                                      	  when yt."RatecodeID" = 2 then 'JFK'
                                      	  when yt."RatecodeID" = 3 then 'Newark'
                                      	  when yt."RatecodeID" = 4 then 'Nassau or Westchester'
                                      	  when yt."RatecodeID" = 5 then 'Negotiated fare'
                                      	  when yt."RatecodeID" = 6 then 'Group ride'
                                      	else 'unknown' 
                                      end
                                     ) as ratecode_name,
                                     (
                                      case
                                      	  when yt.store_and_fwd_flag = 'Y' then 'store and forward trip'
                                      	  when yt.store_and_fwd_flag = 'N' then 'not a store and forward trip'
                                      	else 'unknown'
                                      end
                                     ) as Store_and_fwd_flag_name,
                                     (
                                      case
                                      	  when yt.payment_type = 1 then 'Credit card'
                                      	  when yt.payment_type = 2 then 'Cash'
                                      	  when yt.payment_type = 3 then 'No charge'
                                      	  when yt.payment_type = 4 then 'Dispute'
                                      	  when yt.payment_type = 5 then 'Unknown'
                                      	  when yt.payment_type = 6 then 'Voided trip'
                                        else null
                                      end
                                     ) as payment_type_name,
                                     yt.fare_amount 
                       from yellow_taxi yt 
                      )
-- select all columns
select
	  distinct 
              payment_type_name as payment_type,
	          round(sum(fare_amount)) as total_amount
from
	fare_amount_tbl
group by
	1
order by
	2 desc
	
	
	
	
	

-- Returns rate code with the highest fare amount in dollars
with
    amount_by_rate_code as (
                            select 
                                  distinct
                                          (
                                           case
									           when yt."RatecodeID" = 1 then 'Standard rate'
                                               when yt."RatecodeID" = 2 then 'JFK'
                                               when yt."RatecodeID" = 3 then 'Newark'
                                               when yt."RatecodeID" = 4 then 'Nassau or Westchester'
                                               when yt."RatecodeID" = 5 then 'Negotiated fare'
                                               when yt."RatecodeID" = 6 then 'Group ride'
                                             else 'Unknown' 
                                           end
                                          ) as ratecode_name,
                                          round(avg(yt.fare_amount) over w) as avg_fare_amount,
                                          cast(sum(yt.fare_amount) over w as int) as total_fare_amount
                            from yellow_taxi yt
                            where yt.fare_amount > 0
                            window w as (partition by yt."RatecodeID")
                           )
                                    
select * from amount_by_rate_code order by 3 desc








-- Returns rate code with the highest passenger count
with
    passenger_count_per_rate_code as (
                                      select 
                                            distinct
                                                    (
                                                     case
									                     when yt."RatecodeID" = 1 then 'Standard rate'
                                                         when yt."RatecodeID" = 2 then 'JFK'
                                                         when yt."RatecodeID" = 3 then 'Newark'
                                                         when yt."RatecodeID" = 4 then 'Nassau or Westchester'
                                                         when yt."RatecodeID" = 5 then 'Negotiated fare'
                                                         when yt."RatecodeID" = 6 then 'Group ride'
                                                       else 'Unknown' 
                                                      end
                                                     ) as ratecode_name,
                                                     sum(yt.passenger_count) over w as passenger_count
                                      from yellow_taxi yt
                                      where yt.fare_amount > 0
                                      window w as (partition by yt."RatecodeID")
                                     )
                                    
select * from passenger_count_per_rate_code where passenger_count notnull order by 2 desc







