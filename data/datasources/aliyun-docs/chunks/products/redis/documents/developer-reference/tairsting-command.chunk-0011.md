## EXCAS

| 类别 | 说明 |
| --- | --- |
| 语法 | EXCAS key newvalue version |
| 时间复杂度 | O(1) |
| 命令描述 | 当目标 key 的 version 值与指定的 version 相等时，则更新 key 的 value 值；version 不相等，则返回旧的 value 和 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 newvalue ：若 key 的 version 值与指定的 version 相等，将 value 修改为 newvalue。 version ：用于跟 key 的现有 version 值比较的值。 |
| 返回值 | 执行成功：["OK", "",最新的 version]。中间的""为无意义的空字符串。 执行失败：["ERR update version is stale", value, version]。value 和 version 为 key 当前的 value 和版本。 若 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo bar 命令。 命令示例： EXCAS foo bzz 1 返回示例： 1) OK 2) 3) (integer) 2 |
