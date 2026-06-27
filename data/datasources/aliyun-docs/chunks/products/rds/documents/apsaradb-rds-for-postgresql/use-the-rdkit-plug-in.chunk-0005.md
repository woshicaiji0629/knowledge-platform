## 基础操作说明
mol % mol、fp % fp
当Tanimoto相似度计算结果小于GUC配置参数rdkit.tanimoto_threshold时，该操作返回结果为TRUE。
mol # mol、fp # fp
当Dice相似度计算结果小于GUC配置参数rdkit.dice_threshold时，该操作返回结果为TRUE。
mol @> mol
如果操作符@>左边对象包含右边对象，该操作返回结果为TRUE。
mol <@ mol
如果操作符<@右边对象包含左边对象，该操作返回结果为TRUE。
该文章对您有帮助吗？
反馈
