-- CREATE TABLE Students (
-- 	ID SERIAL PRIMARY KEY ,
-- 	last_name varchar(255),
-- 	first_name varchar(255),
-- 	birthdate date);
	
-- INSERT INTO Students (first_name, last_name, birthdate)
-- VALUES 
-- ('Marc', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03');

-- INSERT INTO Students (first_name, last_name, birthdate)
-- VALUES 
-- ('Miles','Bloom','2004-05-13')

-- SELECT * FROM Students

-- SELECT first_name, last_name FROM Students

-- SELECT first_name, last_name FROM Students WHERE ID = 2

-- SELECT first_name, last_name FROM Students WHERE last_name = 'Benichou' AND first_name = 'Marc' 

-- SELECT first_name, last_name FROM Students WHERE last_name = 'Benichou' or first_name = 'Marc' 

-- SELECT first_name, last_name FROM Students WHERE first_name LIKE '%a%';

-- SELECT first_name, last_name FROM Students WHERE first_name LIKE 'A%';

-- SELECT first_name, last_name FROM Students WHERE first_name LIKE '%a';

-- SELECT first_name, last_name FROM Students WHERE SUBSTRING(first_name,LENGTH(first_name)-1,1) = 'a'

-- SELECT first_name, last_name FROM Students WHERE ID = 1 and ID = 3

-- SELECT * FROM Students WHERE birthdate >= '2000/01/01'