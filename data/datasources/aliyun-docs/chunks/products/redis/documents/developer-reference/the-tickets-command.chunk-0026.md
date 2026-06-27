时，必须存在 EQ、CONTAINS、LIST_MATCH 逻辑中的任意一个，否则会查询失败。 |
| 返回值 | 执行成功：返回聚合结果。 nil：表示 Pkey 或 Skey 不存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.P.RANGE foo 1644451031662 * SUM 500000 AGGREGATION SUM 10000 FILTER sensor_id=1 返回示例： 1) 1) 1) (integer) 1644459500000 2) "40" 2) 1) (integer) 1644460500000 2) "29" 3) 1) (integer) 1644481000000 2) "30" 2) (integer) 0 |
