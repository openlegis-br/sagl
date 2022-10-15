ALTER TABLE tipo_peticionamento CHANGE `cod_unid_tram_dest` `cod_unid_tram_dest` INT NULL;

ALTER TABLE tipo_peticionamento DROP FOREIGN KEY tipo_peticionamento_ibfk_1;

ALTER TABLE peticao ADD `cod_unid_tram_dest` INT NULL AFTER `txt_observacao`;
