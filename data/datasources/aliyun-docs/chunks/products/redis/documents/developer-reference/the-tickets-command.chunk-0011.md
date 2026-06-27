## EXTS.P.CREATE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.P.CREATE Pkey |
| 时间复杂度 | O(1) |
| 命令描述 | 创建一个新的 Pkey（TairTS 数据结构），若 Pkey 已存在则创建失败。 |
| 选项 | Pkey ：Key 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.P.CREATE foo 返回示例： OK |
