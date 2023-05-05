ALTER TABLE `sessao_plenaria` CHANGE `tip_expediente` `tip_expediente` TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL;

INSERT INTO tipo_sessao_plenaria (`nom_sessao`, `ind_excluido`, `num_minimo`)
SELECT * FROM (SELECT 'Audiência Pública', 0, 2) AS tmp
WHERE NOT EXISTS (
    SELECT nom_sessao FROM tipo_sessao_plenaria WHERE nom_sessao = 'Audiência Pública'
) LIMIT 1;
