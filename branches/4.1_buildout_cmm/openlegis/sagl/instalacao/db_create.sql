--
-- Create the databases for OpenLegis in the MySQL
--

CREATE SCHEMA IF NOT EXISTS `openlegis` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE SCHEMA IF NOT EXISTS `openlegis_logs` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'sagl'@'localhost' IDENTIFIED BY 'sagl';

GRANT ALL ON openlegis.* TO 'sagl'@'localhost' WITH GRANT OPTION;
GRANT ALL ON openlegis_logs.* TO 'sagl'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

--
