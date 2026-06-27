## CPC.UPDATE2EST

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.UPDATE2EST key item [EX|EXAT|PX|PXAT time ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中添加 item，返回更新后的基数估算值。若 TairCpc 不存在则自动新建。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 |
| 返回值 | 执行成功：返回更新后的估算值，数据类型为 double 类型。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.UPDATE2EST foo f3 返回示例： "3.0000004768373003" |
