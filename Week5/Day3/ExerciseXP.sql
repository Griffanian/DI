-- Exercise 1

-- select distinct language.name from film
-- inner join language on film.language_id = language.language_id;

-- select film.title,film.description,language.name from film
-- right join language on film.language_id = language.language_id;

-- create table new_film (id serial primary key,name varchar(50));

-- insert into new_film(name)
-- values
-- ('Chamber Italian'),
-- ('Grosse Wonderful');

-- create table customer_review (
-- 	review_id serial primary key,
-- 	film_id int references new_film(id) on delete cascade,
-- 	language_id int references language(language_id),
-- 	title varchar(50),
-- 	score int,
-- 	review_text text,
-- 	last_update date
-- );

-- insert into customer_review (film_id, language_id, title, score, review_text, last_update)
-- values
-- (2, 1, 'Chamber Italian', 9, 'it was ok', '2022-10-23')

-- delete from new_film where id=1;

-- Exercise 2

-- update film 
-- set language_id = 3
-- where film_id%4=0

-- select count(*) from rental
-- where return_date is null

-- select * from film order by rental_rate limit 30

-- select * from film where description like '%sumo wrestler%' or fulltext like '%sumo wrestler%'

create or replace function full_name(first_name varchar(50), last_name varchar(50))
returns varchar(100) as $$
	begin 
		return first_name ||' '|| last_name; 
	end
$$ language plpgsql; 

-- select film.* from film 
-- inner join film_actor on film_actor.film_id = film.film_id
-- inner join actor on actor.actor_id = film_actor.actor_id
-- where film.fulltext @@ to_tsquery('sumo & wrestler') and full_name(first_name,last_name) = 'Penelope Monroe'

-- select film.* from film
-- inner join film_category on film.film_id = film_category.film_id
-- inner join category on film_category.category_id = category.category_id
-- where film.length < 60 and film.rating = 'R' and category.name = 'Documentary'

-- select film.* from rental
-- inner join payment on rental.rental_id =  payment.rental_id
-- inner join inventory on rental.inventory_id = inventory.inventory_id
-- inner join film on inventory.film_id = film.film_id
-- where rental.customer_id=(select customer_id from customer where first_name = 'Matthew' and last_name = 'Mahan')
-- and payment.amount > 4
-- and rental.return_date between '2005-07-28' and '2005-08-01' 

select film.*, payment.amount from rental
inner join payment on rental.rental_id =  payment.rental_id
inner join inventory on rental.inventory_id = inventory.inventory_id
inner join film on inventory.film_id = film.film_id
where rental.customer_id=(select customer_id from customer where first_name = 'Matthew' and last_name = 'Mahan')
and film.description like '%Boat%'
order by payment.amount desc 
