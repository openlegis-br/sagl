CREATE DATABASE IF NOT EXISTS `openlegis_logs` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'sagl'@'localhost' IDENTIFIED BY 'sagl';

GRANT ALL ON openlegis_logs.* TO 'sagl'@'localhost' WITH GRANT OPTION;

USE `openlegis_logs`;

CREATE TABLE IF NOT EXISTS `logs` (
  `cod_log` int NOT NULL AUTO_INCREMENT,
  `data` datetime NOT NULL,
  `cod_registro` int NOT NULL,
  `modulo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `metodo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `usuario` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `IP` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `dados` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`cod_log`),
  KEY `usuario` (`usuario`),
  KEY `metodo` (`metodo`),
  KEY `data` (`data`),
  KEY `modulo` (`modulo`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
