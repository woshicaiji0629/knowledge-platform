## EXHLEN

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHLEN key [NOEXP] |
| 时间复杂度 | 未设置 NOEXP 选项时是 O(1)，设置 NOEXP 选项时是 O(N)。 |
| 命令描述 | 获取 key 指定的 TairHash 中 field 个数，该命令不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 NOEXP ：该命令默认不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。在设置 NOEXP 时： 因为要遍历整条 TairHash 数据， EXHLEN 命令的响应时间将受到 Tairhash 大小的影响。 EXHLEN 命令的返回结果中会过滤掉过期的 field，但过期 field 不会被淘汰。 |
| 返回值 | key 不存在或者 field 不存在：0。 成功：field 个数。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHLEN myhash 返回示例： (integer) 2 |
