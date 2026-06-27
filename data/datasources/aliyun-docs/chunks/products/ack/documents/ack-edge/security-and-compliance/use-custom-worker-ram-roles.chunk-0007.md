### 授予RAM 用户或 RAM 角色所需的权限
当您通过 RAM 用户或 RAM 角色使用本功能时，还需额外被授予ram:PassRole权限策略，以授权该用户或角色可以使用指定的 RAM 角色作为 Worker RAM 角色。具体操作，请参见[创建自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)、[为](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)、[为](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色授权](../../../../ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。
说明
如果 RAM 用户或 RAM 角色已被授予 AliyunCSFullAccess 权限，则无需额外进行ram:PassRole授权。
RAM 权限策略示例如下：
