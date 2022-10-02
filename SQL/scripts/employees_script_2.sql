use employees;

SELECT DISTINCT
    e.emp_no,
    e.first_name,
    e.last_name,
    e.gender,
    t.title,
    s.salary,
    de.dept_no,
    d.dept_name
FROM
    employees e
        LEFT JOIN
    titles t ON e.emp_no = t.emp_no
        LEFT JOIN
    salaries s ON e.emp_no = s.emp_no
        LEFT JOIN
    dept_emp de ON e.emp_no = de.emp_no
        LEFT JOIN
    departments d ON de.dept_no = d.dept_no
GROUP BY 1
ORDER BY 1 ASC



/*

select * from employees e;
select * from titles t;
select * from salaries s;
select * from dept_emp de;
select * from departments d;

*/




