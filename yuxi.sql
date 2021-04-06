CREATE DATABASE homework 
use homework
create table fmfrinends
( name varchar(10),
  gender varchar(2) default 'F',
  age int,
  is_used int default 0
)

select * from fmfrinends
insert into fmfrinends values('zhangsan','M',18,0),('lisi','F',25,0),('wangxiaowu','M',60,1)

select * from fmfrinends where age between 8 and 18

select * from fmfrinends where gender in ('F')

select * from fmfrinends limit 3,4

select * from fmfrinends where name like 'feng%'

select * from fmfrinends where name like '%cang%'

update fmfrinends set age=28 where age=60
delete from fmfrinends where age>20
