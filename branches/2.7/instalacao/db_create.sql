--
-- Create the database and the user for OpenLegis in the MySQL
--

CREATE SCHEMA IF NOT EXISTS `interlegis` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci ;

GRANT ALL PRIVILEGES ON interlegis.* TO 'sapl'@'localhost' IDENTIFIED BY 'sapl';

FLUSH PRIVILEGES;

--
-- To complete the creation of the database structure run after the db_schema.sql script
--
