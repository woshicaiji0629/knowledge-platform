### 如何设置别名？
JSON叶子节点的路径较长，您可以为其设置别名。更多信息，请参见[列的别名](column-aliases.md)。
说明
在设置索引时，不同字段的字段名或别名不能重复。
对于JSON类型的字段，JSON叶子节点的名称是按照全路径进行重名判定的。例如为response字段设置别名为clientIp，系统不会判定该别名与request.clientIp字段名重复。
