## 常见的SQL用例
常见的SQL用例包括CSV及JSON两种。
CSV

| 应用场景 | SQL 语句 |
| --- | --- |
| 返回前 10 行数据 | select * from ossobject limit 10 |
| 返回第 1 列和第 3 列的整数，并且第 1 列大于第 3 列 | select _1, _3 from ossobject where cast(_1 as int) > cast(_3 as int) |
| 返回第 1 列以'陈'开头的记录的个数（注：此处 like 后的中文需要用 UTF-8 编码） | select count(*) from ossobject where _1 like '陈%' |
| 返回所有第 2 列时间大于 2018-08-09 11:30:25 且第 3 列大于 200 的记录 | select * from ossobject where _2 > cast('2018-08-09 11:30:25' as timestamp) and _3 > 200 |
| 返回第 2 列浮点数的平均值，总和，最大值，最小值 | select AVG(cast(_6 as double)), SUM(cast(_6 as double)), MAX(cast(_6 as double)), MIN(cast(_6 as double)) from ossobject |
| 返回第 1 列和第 3 列连接的字符串中以'Tom'为开头以’Anderson‘结尾的所有记录 | select * from ossobject where (_1 || _3) like 'Tom%Anderson' |
| 返回第 1 列能被 3 整除的所有记录 | select * from ossobject where (_1 % 3) = 0 |
| 返回第 1 列大小在 1995 到 2012 之间的所有记录 | select * from ossobject where _1 between 1995 and 2012 |
| 返回第 5 列值为 N,M,G,L 的所有记录 | select * from ossobject where _5 in ('N', 'M', 'G', 'L') |
| 返回第 2 列乘以第 3 列比第 5 列大 100 以上的所有记录 | select * from ossobject where _2 * _3 > _5 + 100 |
