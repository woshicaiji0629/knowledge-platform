## EXSET

| 类别 | 说明 |
| --- | --- |
| 语法 | EXSET key value [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 若 key 不存在，则创建新的 key，并将 value 保存到 key 中；若 key 已存在，则覆盖原来 value 的值。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 value ：为 key 设置的 value。 EX ：指定 key 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 key 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 key 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 key 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 key 不存在时写入。 XX ：只在 key 存在时写入。 VER ：版本号。 如果 key 存在，和当前版本号做比较： 如果相等，写入，且版本号加 1。 如果不相等，返回异常。 如果 key 不存在或者 key 当前版本为 0，忽略传入的版本号直接设置 value，成功后版本号变为 1。 ABS ：绝对版本号。设置后，无论 key 当前的版本号是多少，完成写入并将 key 的版本号覆盖为该选项中设置的值。 KEEPTTL ：延用该 key 原本设置的过期时间（Time to live，TTL 信息），该参数不能与 EX 、 PX 、 EXAT 、 PXAT 参数同时设置。 说明 若未设置 KEEPTTL 参数，也未设置 EX 、 PX 等设置过期时间的参数，则该 key 的过期时间将被删除，即表示该 key 不会过期。 |
| 返回值 | 执行成功：OK。 指定了 XX 且 key 不存在：nil。 指定了 NX 且 key 已经存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXSET foo bar EX 10 NX ABS 100 返回示例： OK |
