可通过修改 SSH 服务的/etc/ssh/sshd_config配置文件 实现。
开启SSH密钥对认证（推荐、更安全）：由PubkeyAuthentication选项控制，设为yes代表开启密钥对认证。修改配置后需重启实例的SSH服务。
开启SSH密码认证（不推荐、安全系数低）：由PasswordAuthentication选项控制，设为yes代表开启密码认证。修改配置后需重启实例的SSH服务。
Q8：使用Terraform创建实例时，如何设置ECS登录用户名？
ECS 实例的默认用户名通常由镜像决定（Linux默认为root，Windows默认为Administrator）。[使用](../developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[Terraform](../developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[创建](../developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[ECS](../developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)[实例](../developer-reference/create-and-use-an-ecs-instance-by-using-terraform.md)时，可通过image_options块中的login_as_non_root参数来配置实例使用非root用户登录。
参数：login_as_non_root（布尔值）。
设置方法：将其设置为true。
结果：实例的登录用户名将变为ecs-user。
该文章对您有帮助吗？
反馈
