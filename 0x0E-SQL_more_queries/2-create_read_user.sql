-- Script creates the database hbtn_0d_2 with some privileges to certain users.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2` TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
