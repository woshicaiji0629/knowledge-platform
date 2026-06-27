返回值 | 新建 field 并成功为它设置值：1。 field 已经存在，成功覆盖旧值：0。 指定了 XX 且 field 不存在：-1。 指定了 NX 且 field 已经存在：-1。 指定了 VER 且版本和当前版本不匹配："ERR update version is stale"。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHSET myhash field1 val EX 10 返回示例： (integer) 1 |
