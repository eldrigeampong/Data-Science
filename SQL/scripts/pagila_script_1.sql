/* Pagila SQL Script */


/*
 List of Tables Joined 
 
select * from film_category fc;
select * from film f;
select * from category c;
select * from "language" l;

 */


select 
	  distinct 
	          fc.film_id,
	          f.title,
	          f.release_year,
	          f.rental_duration,
	          f.rental_rate,
	          f."length",
	          f.rating,
	          fc.category_id,
	          c."name",
	          f.language_id,
	          l."name"
from
	film_category fc
left join film f on
	f.film_id = fc.film_id
left join category c on
	fc.category_id = c.category_id
left join "language" l on
	f.language_id = l.language_id;









