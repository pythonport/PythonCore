show databases;
use world;
create database school;
use school;
show tables;

create table teacher (
	tid int,
	tname varchar(30),
	subject varchar(20),
	design varchar(10)
);

desc teacher;

insert into teacher(tid, tname, subject, design) values(1,'P S Rana', 'English','PGT');
insert into teacher(tid, tname, subject, design) values(2,'C K Yadav', 'Math','PGT');
insert into teacher(tid, tname, subject, design) values(3,'N K Nirala', 'Physics','PGT');
insert into teacher(tid, tname, subject, design) values(1,'S K Singh', 'Chemistry','PGT');
insert into teacher(tid, tname, subject, design) values(1,'Rajesh Kumar Jha', 'Computer Sc','PGT');

update teacher set tid=4 where subject='Chemistry';	
update teacher set tid=5 where subject='Computer Sc';	

select * from teacher;

create table employee1(
	ecode integer,
	ename varchar(20),
	sex char(1),
	grade char(2),
	gross decimal(2),
	dob date
);

insert into employee values(1001,'ravi','M','E4',4670.50);
insert into employee(ecode, ename, sex, grade, gross) values(1002,'sami','M','E3',5670.50);
insert into employee(ecode, ename, sex) values(1003,'Komal','F');
insert into employee(ecode, ename, sex, grade, gross) values(1004,'Arun','M',NULL,NULL);
insert into employee(ecode, ename, sex, grade, gross) values(1005,'Varun','M','B1',4411.20);
insert into employee(ecode, ename, sex, grade, gross) values(1006,'Vinita','F','B1',4747.47);
insert into employee(ecode, ename, sex, grade, gross) values(1007,'Anita','F','C1',6510.66);
insert into employee(ecode, ename, sex, grade, gross) values(1008,'Guddu','M','D1',NULL);
insert into employee values(null,null,null,null,null,null);

alter table employee add dob date;

update employee set dob = '2001-01-26' where ecode=1001;
update employee set dob = '1999-07-05' where ecode=1002;
update employee set dob = '1998-10-20' where ecode=1003;
update employee set dob = '2001-15-12' where ecode=1004;
update employee set gross = 5644 where ecode in (1003, 1004);


select * from employee where dob>='2000-01-01';
select * from employee where grade is null;
select * from employee where grade is not null;
select * from employee where sex = 'F';
select * from employee where sex != 'F';

select ecode, ename, sex from employee;
select ename, dob from employee;
select distinct sex from employee;
select all sex from employee;

select 45*45+45 as math;
select curdate();

select ename, gross
from employee
where gross between 5000 and 5800;

select distinct grade from employee;

select 45*45+45/34+56/2 as mycalc;

--Previous Date from today
SELECT SUBDATE(CURDATE(), 1);
--Next Date from today
SELECT SUBDATE(CURDATE(), -1);

select ename, gross
from employee
where gross between 4500 and 5000;

select * from employee where grade not in('B1','C1');

select * from employee where ename like 'A%';
select * from employee where ename like 'A___';
select * from employee where ename like '%ta';
select * from employee where ename like '%u%';

select ename, grade
from employee
where dob is null;

alter table employee modify gross decimal(8,2);
update employee set gross=5655.50 where ecode=1001;
update employee set dob='2002-12-02' where ecode=1001;
-----------

--SQL Constraints
create table customer(
	cid integer primary key,
	cname varchar(30) not null,
	address varchar(50) default 'dhanbad'
);

insert into customer values(1,'harish','dhanbad');
insert into customer(cid, cname) values(2, 'hari');
insert into customer(cid, cname, address) values(3, 'vimal','ranchi');

alter table employee add primary key(ecode);

create table orders(
	orderid integer not null,
	orderdate date not null,
	sid integer,
	amount decimal(8,2),
	PRIMARY KEY (orderid),
    FOREIGN KEY (sid) REFERENCES customer(cid)
);

insert into orders values (11,'2023-10-27',3,500);
insert into orders values (12,'2023-10-26',2,550);
insert into orders values (13,'2023-10-25',3,578);
insert into orders values (14,'2023-10-25',null,578);

insert into employee1(select * from employee where gross between 4500 and 5500);

delete from employee where gross is null;

----------------Joining Tables
-- Equi Join
select cid, cname, address
from customer, orders
where customer.cid = orders.sid
and orderid=13;

-- Cartesion Product
select *
from customer, orders;

-- Inner Join
select *
from customer
inner join orders
where customer.cid = orders.sid;

-- Left join
select *
from customer
left join orders
on customer.cid = orders.sid;

-- Right join
select *
from customer
right join orders
on customer.cid = orders.sid;