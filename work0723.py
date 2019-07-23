NSERT INTO stu(name)VALUES("tom2");
-- SELECT * FROM stu
-- INSERT INTO stu VALUES(24,"tony",90,"m",1234)
-- INSERT INTO stu(name,score,sno,sex)VALUES("lucy",67,12345,"f"),("lihua",89,321,"m")
-- SELECT * FROM stu;
-- UPDATE stu SET name="xiaoming"
-- SELECT * FROM stu
-- UPDATE stu SET name="Tom" WHERE id=23
-- UPDATE stu SET name="Tom2",score=30 WHERE id=26
-- DELETE FROM stu WHERE id=22;
-- ALTER TABLE stu ADD is_delete TINYINT DEFAULT 0
-- UPDATE stu SET is_delete=1 WHERE score=30
-- SELECT * FROM stu WHERE is_delete=0

-- id大于3的记录
-- SELECT name,score,sex FROM stu WHERE id>3;

-- 查询等于某一个值的情况
-- SELECT * FROM stu WHERE id!=23;

-- 查询以to开头的数据
-- SELECT * FROM stu WHERE `name` LIKE "to%"

-- 查询名字以2结尾的数据
-- SELECT * FROM stu WHERE name LIKE "%2"

-- 查询名字包含ao的数据
-- SELECT * FROM stu WHERE name LIKE "%ao%"

-- 查询名字是to开头，后面只允许与一个字符
-- SELECT * FROM stu WHERE name LIKE "to_"

-- 查询成绩大于60小于80的数据
-- SELECT * FROM stu WHERE score BETWEEN 60 and 80

-- in 某个字段的值在我们括号里面出现
-- SELECT * FROM stu WHERE score IN (59,89,90)

-- 查询没有被删除分数小于80的数据
-- SELECT * FROM stu WHERE is_delete=0 AND score<80

-- 查询数据的时候，不仅仅可以从真实数据表查询，还可以通过某一个查询语句的输出去查询
-- SELECT * FROM(SELECT * FROM stu WHERE is_delete=0)as tmp WHERE tmp.score<80;

-- 给查询的字段取一个别名
-- SELECT name AS 姓名, sex AS 性别 FROM stu;

-- 需求：分数大于90分，给10块钱，并且保存到三好学生表中
-- 1新建一个三好学生表
-- 2查询出满足条件的数据
-- 3插入到三好学生表里
-- show CREATE TABLE stu
-- CREATE TABLE `goodstu` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `name` varchar(20) DEFAULT NULL,
--   `score` int(11) DEFAULT NULL,
--   `sex` varchar(2) DEFAULT NULL,
--   `sno` varchar(20) DEFAULT NULL,
--   `is_delete` tinyint(4) DEFAULT '0',
--   PRIMARY KEY (`id`)
-- ) 
-- 解决查询插入的问题
-- INSERT INTO goodstu SELECT * FROM stu WHERE score>=90
-- 指定具体的字段进行插入
-- INSERT INTO goodstu(name,score)SELECT name,score FROM stu WHERE score>=90

-- 去重
-- SELECT DISTINCT name,score FROM good_stu;
-- 跨过n+1个，最多拿m个（limit）
-- SELECT * FROM stu WHERE is_delete=0 LIMIT 1 OFFSET 1

-- LIMIT 跨过n个，取m个
-- SELECT * FROM stu LIMIT 3,2

-- 因为都漂亮，所以拟添加逻辑删除
ALTER TABLE fmfriends ADD is_del=0 INT DEFAULT 0 ;
-- 添加三个追求者
INSERT INTO fmfriends(name,sex,age,is_used)VALUES("林允儿",'m',20,"没"),("章若楠",'m',18,'没'),("星狗",'m',19,'没');
-- 查询出来年纪在8到18岁的人
SELECT * FROM fmfriends WHERE age BETWEEN 8 and 18;
-- 使用in查询出 男的 
SELECT * FROM fmfriends WHERE sex IN ('m','m','m');
-- ​跳过3个查4个数据
SELECT * FROM fmfriends LIMIT 3,4;
-- 查询出名字是凤姐开头
SELECT * FROM fmfriends WHERE 'name' LIKE '凤姐%';
-- ​查询名字包含了苍老师 
SELECT * FROM fmfriends WHERE 'name' LIKE '%苍老师%';
-- ​更新 年纪大于80岁 28的
UPDATE fmfriends SET 'age'=28 WHERE 'age'>80;
-- ​查询的时候 记得字段的时候取别名
SELECT NAME AS 追求者姓名,sex 性别,age 芳龄,is_used 是否答应她了 FROM fmfriends;
-- ​删除年纪大于20岁的 
UPDATE fmfriends SET is_del=1 WHERE age>20; 



