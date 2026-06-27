## 步骤二：为RAM用户授权
设置内置角色或自定义角色后，如果需要使用RAM用户查询时序库或日志库，必须使用阿里云主账号为RAM用户添加如下权限策略，用于扮演相应的角色。为RAM用户授权的操作步骤，请参见[管理](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
{ "Action": "ram:PassRole", "Effect": "Allow", "Resource": "acs:ram::阿里云账号ID:角色ARN" }
该文章对您有帮助吗？
反馈
