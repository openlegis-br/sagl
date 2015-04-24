SELECT DISTINCT
  CONCAT("UPDATE filiacao SET cod_partido=",partido.cod_partido," WHERE dat_filiacao=", "'", dat_filiacao,"'", " and cod_partido=",partido_old.cod_partido," and cod_parlamentar=",cod_parlamentar,";") as comando_sql
FROM
  filiacao 
  LEFT JOIN partido_old on partido_old.cod_partido = filiacao.cod_partido,
  partido
WHERE
  partido.sgl_partido = partido_old.sgl_partido
