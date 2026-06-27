## 方式一：系统策略授权
重要
系统策略需使用AliyunRAMReadOnlyAccess和AliyunCSFullAccess，权限较大。如需精细化授权，请使用[方式二：自定义策略精细化授权](grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
使用阿里云账号登录[RAM](https://ram.console.aliyun.com/)[管理控制台](https://ram.console.aliyun.com/)，定位目标RAM用户或角色。
RAM用户：选择身份管理>用户，在用户列表的操作列，单击添加权限。
RAM角色：选择身份管理>角色，在角色列表的操作列，单击添加权限。
选择资源范围为账号级别，在权限策略区域定位并选中系统策略AliyunRAMReadOnlyAccess和AliyunCSFullAccess，按照页面提示完成授权。
