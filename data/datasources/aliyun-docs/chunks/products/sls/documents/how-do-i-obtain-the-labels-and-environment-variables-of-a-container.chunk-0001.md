## 获取容器Label
登录容器所在的宿主机。ECS实例的登录步骤，请参见[使用](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[工具以](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[SSH](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[协议登录](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](../../ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。
执行如下命令，列出所有正在运行的容器。
docker ps
返回结果，其中f******a是容器ID。
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg. CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES f******a docker.io/library/nginx:latest nginx -g daemon o... 6 seconds ago Up 7 seconds 0.0.0.0:8080->80/tcp my-nginx
执行如下命令，获取容器Label。
docker inspect ${容器ID}
返回结果中的Labels字段表示容器标签。
