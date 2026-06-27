## 已创建集群
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏单击集群列表。
在集群列表页面，单击目标集群名称，然后在集群详情页面单击基本信息页签，在安全与审计区域打开Secret 落盘加密开关。
首次开启时，请根据提示单击前往RAM进行授权进入访问控制快速授权页面，然后单击确认授权完成授权。
说明
如需开启落盘加密功能，请确保当前登录的RAM用户或RAM角色对该集群有RBAC的管理员或运维人员权限。具体操作，请参考[使用](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)[为集群内资源操作授权](../../ack-managed-and-ack-dedicated/user-guide/grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
如需授权aliyuncsmanagedsecurityrole角色，请确保已使用阿里云账号（主账号）或拥有RAM管理权限的RAM用户或RAM角色登录。
在弹出的Secret 落盘加密对话框，选择已有的KMS密钥，然后单击确定。
如果您未创建KMS密钥，请单击创建密钥，前往[密钥管理服务控制台](https://kms.console.aliyun.com)创建密钥。具体操作，请参见[创建密钥](../../../../kms/documents/key-management-service/support/create-a-cmk.md)。
当集群状态由更新中变为运行中时，表明该集群的Secret落盘加密特性已开启。
当您不需要使用Secret落盘加密功能时，可在安全与审计区域关闭Secret 落盘加密开关。
