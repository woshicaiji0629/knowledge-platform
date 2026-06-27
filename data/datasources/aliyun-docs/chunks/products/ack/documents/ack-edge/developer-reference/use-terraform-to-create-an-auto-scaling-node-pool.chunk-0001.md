## 前提条件
自动伸缩功能依赖弹性伸缩（Auto Scaling，旧称ESS）服务。启动节点自动伸缩前，您需要开通弹性伸缩服务，并完成默认角色授权。具体操作，请参见[开通弹性伸缩服务](../../ack-managed-and-ack-dedicated/user-guide/auto-scaling-of-nodes.md)。
说明
如果您之前已经使用了alicloud_cs_kubernetes_autoscaler组件，默认已开通弹性伸缩服务。
已为系统运维管理 OOS（CloudOps Orchestration Service）服务授权。您可以通过创建AliyunOOSLifecycleHook4CSRole角色，为OOS服务授权。
单击[AliyunOOSLifecycleHook4CSRole](https://ram.console.aliyun.com/role/authorize?spm=5176.2020520152.0.0.5b4716ddI6QevL&request=%7B%22ReturnUrl%22%3A%22https%3A%2F%2Fram.console.aliyun.com%22%2C%22Services%22%3A%5B%7B%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunOOSLifecycleHook4CSRole%22%2C%22TemplateId%22%3A%22AliyunOOSLifecycleHook4CSRole%22%7D%5D%2C%22Service%22%3A%22OOS%22%7D%5D%7D)。
说明
如果当前账号是阿里云账号，单击AliyunOOSLifecycleHook4CSRole即可授权。
如果当前账号是RAM用户，请先确保对应的阿里云账号已授权AliyunOOSLifecycleHook4CSRole，并为RAM用户授予AliyunRAMReadOnlyAccess系统策略。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
在访问控制快速授权页面，单击确认授权。
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[在](https://help.aliy
