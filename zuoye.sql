--新建一个男女朋友表 fmfriedns,
--字段：姓名 性别 年龄 is_used
create table fmfriedns(
	id int unsigned primary key not null auto_increment,
    name varchar(30),
    gender enum("男"，"女"),
    age tinyint unsigned default 0,
    is_used bit default=0
);

--插入三条以上的数据
insert into fmfriedns values(0,"小张","女",16),(0,"小李","女",30,1),(0,"小陈","男",27)(0,"小徐","男",37,1);

--查询出来年纪在8到18岁的人
select * from fmfriedns age between 8 and 18;

--使用in查询出 男的
select * from fmfriedns in ("男","女");

--跳过3个查4个数据
select * from fmfriedns limit 3,4;

--查询出名字是凤姐开头的
select * from fmfriedns where name="凤姐%";

--查询名字包含了苍老师
select * from fmfriedns where name="%苍老师%";

--更新年纪大于80岁 28的
update fmfriedns set age=28 where age>80;

--查询的时候记得给字段的名字去别名

select name as 姓名,gender as 性别 from fmfriedns;

--删除年纪大于20岁的

delete from fmfriedns where age>20;
	