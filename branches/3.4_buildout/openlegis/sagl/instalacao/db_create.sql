--
-- Create the database for OpenLegis in the MySQL
--

CREATE SCHEMA IF NOT EXISTS `interlegis` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'sagl'@'localhost' IDENTIFIED BY 'sagl';

GRANT ALL ON interlegis.* TO 'sagl'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

--
-- To complete the creation of the database structure run after the db_schema.sql and the db_initial_data.sql scripts
--
