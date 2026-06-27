## 常见问题
Q：OPERATION need to be executed set by ADMIN报错怎么解决？
A：可能是SQL脚本里面包括视图，触发器，存储过程等对象的definer问题，或者含有set global类SQL导致。详情请参见[RDS MySQL](../support/what-do-i-do-if-the-operation-need-to-be-executed-set-by-admin-error-message-is-displayed.md)[出现“OPERATION need to be executed set by ADMIN”报错](../support/what-do-i-do-if-the-operation-need-to-be-executed-set-by-admin-error-message-is-displayed.md)。
Q：Access denied; you need (at least one of) the SUPER privilege(s) for this operation报错怎么解决？
A：SQL脚本里面包括SUPER权限的语句，将相关语句删除再执行。
该文章对您有帮助吗？
反馈
