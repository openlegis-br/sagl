--
-- Create the database and the user for OpenLegis in the MySQL
--

CREATE SCHEMA IF NOT EXISTS `openlegis` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;

GRANT ALL PRIVILEGES ON openlegis.* TO 'sagl'@'localhost' IDENTIFIED BY 'sagl';

FLUSH PRIVILEGES;

--
-- To complete the creation of the database structure run after the db_schema.sql script
--
