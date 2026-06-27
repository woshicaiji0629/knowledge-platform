### 管理设置
管理设置包括登录凭证和标签，用于远程连接实例和方便地检索和管理资源。
登录凭证
登录凭证用于安全地登录实例，关于实例连接方式的介绍，请参见[选择](connect-to-instance.md)[ECS](connect-to-instance.md)[远程连接方式](connect-to-instance.md)。

| 登录凭证 | 说明 |
| --- | --- |
| 密钥对 说明 仅 Linux 实例支持使用密钥对登录认证。 | 选择登录实例的用户名和已有的密钥对，或者单击 创建密钥对 即时创建密钥对。创建完成后，返回 ECS 实例创建向导并单击 图标，查看密钥对列表。具体操作，请参见 [创建](create-an-ssh-key-pair.md) [SSH](create-an-ssh-key-pair.md) [密钥对](create-an-ssh-key-pair.md) 。 用户名支持设置为 root 或 ecs-user 。 警告 root 具有操作系统的最高权限，使用 root 作为用户名可能会导致安全风险，建议您使用普通用户 ecs-user 作为用户名。 |
| 使用镜像预设密码 说明 仅 自定义镜像 和 共享镜像 支持此认证方式。 | 可以直接使用所选镜像的预设密码进行登录认证。为了保证您的正常使用，请确保所选镜像中已经设置了密码。 |
| 自定义密码 | 输入并确认密码。使用登录名和密码登录实例时，用户名信息如下： Linux 实例：支持设置为 root 或 ecs-user 。 警告 root 具有操作系统的最高权限，使用 root 作为用户名可能会导致安全风险，建议您使用普通用户 ecs-user 作为用户名。 Windows 实例：默认为 administrator 。 |
| 创建后设置 | 在实例创建完成后，自行绑定密钥对或者重置实例密码。具体操作，请参见 [绑定](bind-an-ssh-key-pair-to-an-instance.md) [SSH](bind-an-ssh-key-pair-to-an-instance.md) [密钥对](bind-an-ssh-key-pair-to-an-instance.md) 和 [重置实例登录密码](reset-the-logon-password-of-an-instance.md) 。 |

（可选）标签
标签由一对键值（Key-Value）组成，用来标识创建的实例、云盘、弹性网卡主网卡，便于检索和管理资源。可选择已有的标签，或者填写标签键和标签值即时创建标签。关于标签的更多信息，请参见[标签](label-overview.md)。
