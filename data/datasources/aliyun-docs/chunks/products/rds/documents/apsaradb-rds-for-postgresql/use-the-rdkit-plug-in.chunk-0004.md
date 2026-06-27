## 函数示例
tanimoto_sml函数计算tanimoto相似度。
postgres=# \df tanimoto_sml List of functions Schema | Name | Result data type | Argument data types | Type --------+--------------+------------------+---------------------+------ public | tanimoto_sml | double precision | bfp, bfp | func public | tanimoto_sml | double precision | sfp, sfp | func (2 rows)
dice_sml函数计算dice相似度。
postgres=# \df dice_sml List of functions Schema | Name | Result data type | Argument data types | Type --------+----------+------------------+---------------------+------ public | dice_sml | double precision | bfp, bfp | func public | dice_sml | double precision | sfp, sfp | func (2 rows)
substruct函数，当函数的第二个参数是第一个参数的子结构时，函数返回结果为TRUE。
postgres=# \df substruct List of functions Schema | Name | Result data type | Argument data types | Type --------+-----------+------------------+---------------------+------ public | substruct | boolean | mol, mol | func public | substruct | boolean | mol, qmol | func public | substruct | boolean | reaction, reaction | func (3 rows)
