## EXHINCRBY

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHINCRBY key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个整数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 num ：需要为 field 的 value 增加的整数值。 EX ：指定 field 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 field 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 field 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 field 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 MIN ：value 的最小值，小于该值则提示异常。 MAX ：value 的最大值，大于该值则提示异常。 KEEPTTL ：在不指定 EX、EXAT、PX 或 PXAT 选项时，使用 KEEPTTL 选项会保留 field 当前的过期设置。 |
| 返回值 | 成功：与 num 相加后 value 的值。 其它情况返回异常。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 命令。 命令示例： EXHINCRBY myhash field1 100 返回示例： (integer) 110 |
