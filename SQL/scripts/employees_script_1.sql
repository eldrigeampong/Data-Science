use employees;

with 
	employees_table_tbl as (select
								   distinct 
									       e.emp_no, 
									       e.birth_date, 
                                           e.first_name,
                                           e.last_name,
                                           e.gender,
                                           e.hire_date
					         from employees e
					       ),
	
    department_employees_tbl as (select 
								       distinct
                                               de.emp_no,
                                               de.dept_no,
                                               de.from_date,
                                               de.to_date
								  from dept_emp de
						        ),
                            
	departments_tbl as (select
							  distinct
                                      d.dept_no,
                                      d.dept_name
					    from departments d
				      ),
                   
	merged_employees_departments_tbl as (select
                                               distinct 
                                                       et.emp_no,
                                                       count(et.emp_no) over () as employees_count,
													   et.first_name,
                                                       et.last_name,
                                                       et.gender,
                                                       count(*) over (partition by et.gender) as employees_count_by_gender,
									                   et.birth_date,
                                                       timestampdiff(year, et.birth_date, current_date) as employee_age,
                                                       et.hire_date,
                                                       timestampdiff(year, et.hire_date, current_date) as employee_work_experience,
                                                       det.dept_no,
                                                       dt.dept_name,
                                                       count(*) over (partition by dt.dept_name) as dept_name_count,
                                                       det.from_date,
                                                       det.to_date,
                                                       timestampdiff(year, det.from_date, det.to_date) as years_spent_per_department
										  from employees_table_tbl et
                                          left join department_employees_tbl det on et.emp_no = det.emp_no
                                          left join departments_tbl dt on det.dept_no = dt.dept_no
                                          where to_date != (select max(de.to_date) from dept_emp de)
									    ),
                                        
	transformed_tbl as (select
							   distinct  
                                       emp_no,
                                       employees_count,
                                       first_name,
                                       last_name,
                                       gender,
                                       employees_count_by_gender,
                                       birth_date,
                                       rank() over (order by employee_age desc) as employees_age_rank,
                                       employee_age,
                                       min(employee_age) over () as minimum_employee_age,
                                       avg(employee_age) over () as average_employee_age,
                                       max(employee_age) over () as maximum_employee_age,
                                       hire_date,
                                       employee_work_experience,
                                       min(employee_work_experience) over () minimum_work_experience,
                                       avg(employee_work_experience) over () average_work_experience,
                                       max(employee_work_experience) over () maximum_work_experience,
                                       dept_no,
                                       dept_name,
                                       dept_name_count,
                                       from_date,
                                       to_date,
                                       years_spent_per_department,
                                       dense_rank() over (order by years_spent_per_department desc) as experience_rank
						from merged_employees_departments_tbl
					),
                    
	final_employees_table as (
							   select 
									  distinct
                                               emp_no,
                                               employees_count,
                                               first_name,
                                               last_name,
                                               gender,
                                               employees_count_by_gender,
                                               birth_date,
                                               employees_age_rank,
                                               employee_age,
                                               minimum_employee_age,
                                               round(average_employee_age) as average_employee_age,
                                               maximum_employee_age,
                                               hire_date,
                                               employee_work_experience,
                                               minimum_work_experience,
                                               round(average_work_experience) as average_work_experience,
                                               maximum_work_experience,
                                               dept_no,
                                               dept_name,
                                               dept_name_count,
                                               from_date,
                                               to_date,
                                               years_spent_per_department,
                                               experience_rank
							from transformed_tbl
						)
            
	
select * from final_employees_table;