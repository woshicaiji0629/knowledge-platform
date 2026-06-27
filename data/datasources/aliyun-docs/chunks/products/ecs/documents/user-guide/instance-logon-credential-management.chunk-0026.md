## 四、常见问题
Q1：ECS默认用户名、初始用户名、默认登录名、初始登录名是什么？
Linux系统实例：默认为root，若创建实例时设置了使用ecs-user则为ecs-user。
Windows系统实例：默认为Administrator。
Q2：ECS默认密码、初始密码、默认远程密码、初始登录密码是什么？
没有。
出于安全考虑，阿里云不会为ECS实例设置默认或初始密码。如在创建实例时未设置密码，可使用[重置密码（不知道/忘记原密码）](instance-logon-credential-management.md)。
Q3：如何查看实例密码？
阿里云不会保存您设置的实例密码，因此不支持查看。
Q4：凭证找回（忘记登录名、忘记密码）
忘记登录名：可通过控制[重置密码](instance-logon-credential-management.md)功能查看。创建实例时设置的登录名会在重置实例密码对话框的最上方显示。
忘记密码：[重置密码（不知道/忘记原密码）](instance-logon-credential-management.md)。
Q5：在线重置密码失败的原因？
大多数情况下，是由于实例中的安全软件拦截云助手修改密码指令造成的。建议使用[离线重置密码](instance-logon-credential-management.md)。
Q6：「root」和「ecs-user」切换
原来使用root，切换到ecs-user
仅通过[自定义购买](create-an-instance-by-using-the-wizard.md)创建部分Linux镜像的实例时，支持设置ecs-user。
实例创建后，不支持直接切换到ecs-user，但可通过[添加多用户远程登录](instance-logon-credential-management.md)的方式自行创建ecs-user后，并为该用户授予sudo权限，达到切换的效果。
原来使用ecs-user，切换到root
强烈建议继续使用ecs-user并通过sudo执行需要特权的命令，而不是直接使用root用户登录。
如果确实需要在已登录的会话中切换到root用户，可通过ecs-user登录实例后，执行sudo su命令，切换到root用户。
控制台的离线重置密码、绑定密钥对等功能仅对创建实例时设置的登录名生效。
Q7：如何让Linux实例同时支持「SSH 密钥对」和「密码」两种登录方式？
可通过修改 SSH 服务的/etc/ssh/sshd_config配置文件 实现。
开启SSH密钥对认证（推荐、更安全）：由PubkeyAuthentication选项控制，设为yes代表开启密钥对认证。修改配置后需重启实例的SSH服务。
开启SSH密码认证（不推荐、安全系数低）：由PasswordAuthentic
