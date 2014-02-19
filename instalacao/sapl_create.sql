--
-- Create the database and the user for SAPL in the MySQL
--

CREATE SCHEMA IF NOT EXISTS `openlegis` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;

GRANT ALL PRIVILEGES ON openlegis.* TO 'sapl'@'localhost' IDENTIFIED BY 'sapl';

FLUSH PRIVILEGES;

--
-- To complete the creation of the database structure run after the sapl.sql script
--
