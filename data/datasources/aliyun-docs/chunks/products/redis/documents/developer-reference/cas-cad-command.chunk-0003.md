## CAS

| 类别 | 说明 |
| --- | --- |
| 语法 | CAS key oldvalue newvalue [EX|PX|EXAT|PXAT time] |
| 时间复杂度 | O(1) |
| 命令描述 | CAS（Compare And Set），查看指定的 oldvalue 是否与目标 Key 的 Value 相等，若相等则将 Value 修改成新的值（ newvalue ），不相等则不修改。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAS。 |
| 选项 | Key ：目标 Key，String 类型。 oldvalue ：原 Value 值，用于跟现有 Key 的 Value 进行比较。 newvalue ：当 oldvalue 与 Key 现有 Value 相等时，将 Value 修改为 newvalue。 EX ：指定 Key 的相对过期时间，单位为秒，为 0 表示马上过期，不传此参数表示不过期。 EXAT ：指定 Key 的绝对过期时间，单位为秒，为 0 表示马上过期，不传此参数表示不过期。 PX ：指定 Key 的相对过期时间，单位为毫秒，为 0 表示马上过期，不传此参数表示不过期。 PXAT ：指定 Key 的绝对过期时间，单位为毫秒 ，为 0 表示马上过期，不传此参数表示不过期。 说明 若原 String 已设置 TTL，在执行 CAS 命令时不加上 TTL，该 Key 将不过期。 |
| 返回值 | 执行成功：1 执行失败：0 若 Key 不存在：-1 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 SET foo bar 命令。 命令示例： CAS foo bar bzz EX 10 返回示例： (integer) 1 若此时执行 GET foo ，将返回 “bzz” 。 |
