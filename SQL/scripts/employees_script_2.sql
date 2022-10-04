
/* Employees Script 2 */

select
	distinct
    e.emp_no,
	e.first_name,
	e.last_name,
	e.gender,
	t.title,
	s.salary,
	de.dept_no,
	d.dept_name
from
	employees e
left join
    titles t on
	e.emp_no = t.emp_no
left join
    salaries s on
	e.emp_no = s.emp_no
left join
    dept_emp de on
	e.emp_no = de.emp_no
left join
    departments d on
	de.dept_no = d.dept_no
group by
	1
order by
	1 asc;