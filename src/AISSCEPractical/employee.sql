-- used databse tenughat

create table employee(
	empid  integer primary key,
	fname varchar(20),
	lname varchar(20),
	city varchar(20),
	salary integer,
	designation varchar(20)
);

insert into employee(empid,fname,lname,city,salary,designation)
	values(10,'RAVI','KUMAR','MUMBAI',15000,'MANAGER');
insert into employee(empid,fname,lname,city,salary,designation)
	values(101,'HARRY','WALTOR','PUNE',12000,'CLERK');
insert into employee(empid,fname,lname,city,salary,designation)
	values(215,'ARUN','KUMAR','DELHI',13000,'CLERK');
insert into employee(empid,fname,lname,city,salary,designation)
	values(152,'SAM','LEE','MUMBAI',20000,'DIRECTOR');