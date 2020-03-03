ALTER TABLE `relatoria` ADD `num_protocolo` INT(11) NULL AFTER `num_parecer`;
ALTER TABLE `relatoria` ADD INDEX(`num_protocolo`);
