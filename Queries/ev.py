query1 = '''
             -- returns year with the highest number of electric vehicles produced
with 
    ev_count as (
             	 select 
                       distinct 
						       ev."Model_Year" as model_yr,
                               count(*) over w1 as vehicle_count
                 from state.electric_vehicles ev
                 window w1 as (partition by ev."Model_Year")
                )
select distinct * from ev_count order by vehicle_count desc limit 10

         '''



query2 = '''
          -- returns city and county with the highest count of electric vehicles
with 
    city_ev_count as (
                      select
                            distinct 
                                    ev."County" as county,
                                    ev."City" as city,
                                    count("Model") over w1 as vehicle_count
                      from state.electric_vehicles ev
                      window w1 as (partition by ev."City", ev."City")
                     )
select distinct * from city_ev_count order by vehicle_count desc limit 10;

         '''



query3 = '''
            -- returns the total count of electric vehicles by make and model produced each year
with 
    ev_make_count as (
                      select
                            distinct
                                    ev."Model_Year" as model_yr, 
                                    ev."Make" as make,
                                    ev."Model" as model,
                                    count(*) over w1 as cars_count
                      from state.electric_vehicles ev
                      window w1 as (partition by ev."Model_Year", ev."Make", ev."Model" order by ev."Make", ev."Model")
                     )
-- select all columns
select distinct * from ev_make_count order by cars_count desc 

         '''