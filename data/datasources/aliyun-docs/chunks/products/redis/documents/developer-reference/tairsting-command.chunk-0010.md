## EXINCRBYFLOAT

| 类别 | 说明 |
| --- | --- |
| 语法 | EXINCRBYFLOAT key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 对 TairString 的 value 进行自增自减操作，num 的范围为 double。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 num ：TairString 进行自增自减操作的数值，类型为浮点数。 EX ：指定 key 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 key 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 key 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 key 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 key 不存在时写入。 XX ：只在 key 存在时写入。 VER ：版本号。 如果 key 存在，和当前版本号做比较： 如果相等，进行自增，且版本号加 1。 如果不相等，返回异常。 如果 key 不存在或者 key 当前版本为 0，忽略传入的版本号并进行自增操作，成功后版本号变为 1。 ABS ：绝对版本号。设置后，无论 key 当前的版本号是多少，完成写入并将 key 的版本号覆盖为该选项中设置的值。 MIN ：设置 TairString value 的最小值。 MAX ：设置 TairString value 的最大值。 KEEPTTL ：延用该 key 原本设置的过期时间，该参数不能与 EX 、 PX 、 EXAT 、 PXAT 参数同时设置。 说明 若未设置 KEEPTTL 参数，也未设置 EX 、 PX 等设置过期时间的参数，则该 key 的过期时间将被删除，即表示该 key 不会过期。 |
| 返回值 | 执行成功：操作后 value 的值。 若设置了 MAX 或 MIN，而操作后的 value 超过了该范围：(error) ERR increment or decrement would overflow。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo 1 命令。 命令示例： EXINCRBYFLOAT foo 10.123 返回示例： (integer) 11.123 |
