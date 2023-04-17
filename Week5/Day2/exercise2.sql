-- select * from customer

-- select distinct create_date from customer

-- select * from customer order by first_name 

-- select film_id, description, release_year, rental_rate from film order by rental_rate asc

-- select address, phone from address where district = 'Texas'

-- select * from film where film_id in (15,150)

-- select * from film where title = 'Star Wars'

-- select film_id, title, description, length, rental_rate from film where left(title, 2) = 'St'

-- select title,rental_rate from film order by rental_rate limit 10

-- select title,rental_rate from film order by rental_rate offset 10 limit 10

-- select customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer
-- inner join payment on customer.customer_id = payment.customer_id

-- select * from film
-- where film_id not in (select film_id from inventory);

-- select city.city, country.country from city
-- inner join country on city.country_id = country.country_id


