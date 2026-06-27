| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSET key field value [EX time] [EXAT time] [PX time] [PXAT time] [NX | XX] [VER | ABS version] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 向 Key 指定的 TairHash 中插入一个 field。如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 您也可以通过 EXPIRE 或 EXPIREAT 命令设置 Key 的过期时间。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 value ：field 对应的值，一个 field 只能有一个 value。 EX ：指定 field 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 field 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 field 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 field 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 field 不存在时插入。 XX ：只在 field 存在时插入。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 KEEPTTL ：在不指定 EX、EXAT、PX 或 PXAT 选项时，使用 KEEPTTL 选项会保留 field 当前的过期设置。 说明 若不使用 KEEPTTL 选项，EXHSET 命令会默认删除 field 上原先设置的过期时间。 |
| 返回值 | 新建 field 并成功为它设置值：1。 field 已经存在，成功覆盖旧值：0。 指定了 XX 且 field 不存在：-1。 指定了 NX 且 field 已经存在：-1。 指定了 VER 且版本和当前版本不匹配："ERR update version is stale"。 其它情况返回相应的异常信息。
