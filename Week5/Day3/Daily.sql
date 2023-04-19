-- create table customer (
-- id serial primary key,
-- first_name varchar(50) not null,
-- last_name varchar(50) not null)

-- create table customer_profile (
-- id serial primary key,
-- isLoggedIn bool default false,
-- customer_id int references customer(id)
-- )

-- insert into customer (first_name,last_name)
-- values
-- ('John','Doe'),
-- ('Jewome','Lalu'),
-- ('Lea','Rive')

insert into customer_profile (isLoggedIn,customer_id)
values
('')