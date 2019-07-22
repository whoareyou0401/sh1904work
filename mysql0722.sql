-- CREATE TABLE fmfriends (name VARCHAR(10),sex CHAR(1),age int ,is_used TINYINT)
-- ALTER TABLE fmfriends ADD ID INT PRIMARY KEY AUTO_INCREMENT

-- INSERT INTO  fmfriends(`name`,sex,age,is_used) 
-- VALUES
-- ("李九","男",11,0),
-- ("张三","男",22,0),
-- ("李四","男",21,0),
-- ("王五","男",17,0),
-- ("翠花","女",19,0),
-- ("春花","女",23,0),
-- ("秋月","女",27,0),
-- ("闲林","男",88,0),
-- ("花花","女",31,0),
-- ("花月","女",26,0);


-- SELECT * FROM fmfriends WHERE 8<=age AND age<=18；
-- SELECT * FROM fmfriends WHERE sex IN ("男");
-- SELECT * FROM fmfriends LIMIT 3,4;
-- SELECT * FROM fmfriends WHERE `name` LIKE "花%";
-- SELECT * FROM fmfriends WHERE `name` LIKE "%花%";
-- UPDATE fmfriends set age=28 WHERE age>=80 ;
-- SELECT name as "xm",sex as "xb" FROM fmfriends;
-- UPDATE fmfriends set is_used=1 WHERE age >20;


