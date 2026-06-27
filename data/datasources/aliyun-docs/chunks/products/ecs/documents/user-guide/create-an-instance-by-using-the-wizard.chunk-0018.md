| 参数 | 说明 |
| --- | --- |
| 实例名称 、 描述 、 主机名 、 有序后缀 | 创建多台实例时，设置有序的实例名称和主机名称便于从名称了解实例的批次等信息。关于设置有序名称的规则，请参见 [批量设置有序的实例名称或主机名称](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md) 。 |
| 实例 RAM 角色 | 实例通过实例 RAM 角色获得该角色拥有的权限，可以基于临时安全令牌 STS（Security Token Service）访问指定云服务的 API 和操作指定的云资源，安全性更高。 选择已有的实例 RAM 角色，或者单击 创建实例 RAM 角色 前往 RAM 控制台即时创建实例 RAM 角色。创建完成后，返回 ECS 实例创建向导并单击 图标，查看实例 RAM 角色列表。具体操作，请参见 [创建实例](attach-an-instance-ram-role-to-an-ecs-instance.md) [RAM](attach-an-instance-ram-role-to-an-ecs-instance.md) [角色并为角色授予权限](attach-an-instance-ram-role-to-an-ecs-instance.md) 。 |
| 元数据访问模式 | 实例元数据（metadata）包含了实例在阿里云系统中的信息，您可以在运行中的实例内方便地查看实例元数据，并基于实例元数据配置或管理实例。关于如何查看实例元数据，请参见 [实例元数据](view-instance-metadata.md) 。 |
| 自定义数据 | 实例自定义数据可以作为实例自定义脚本在启动实例时执行，实现自动化配置实例，或者仅作为普通数据传入实例。更多信息，请参见 [自定义实例初始化配置](customize-the-initialization-configuration-for-an-instance.md) 。 在输入框输入您准备的实例自定义数据。如果实例自定义数据已进行 Base64 编码，请选中 输入已采用 Base64 编码 。 |
| 资源组 | 资源组供您从业务角度管理跨地域、跨产品的资源，并支持针对资源组管理权限。更多信息，请参见 [资源组](resource-groups.md) 。 选择已有的资源组，或者单击 创建资源组 前往资源管理控制台即时创建资源组。创建完成后，返回 ECS 实例创建向导并单击 图标，查看资源组列表。具体操作，请参见 [创建资源组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/create-a-res
