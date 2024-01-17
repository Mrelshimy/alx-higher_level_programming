-- Script that creates the table unique_id on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa `;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states `(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
