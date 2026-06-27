# 在Workbench或CloudShell上使用kubectl连接集群
阿里云提供浏览器命令行工具Workbench和CloudShell用于连接集群和管理集群资源，无需额外安装软件。登录阿里云控制台后，您可以在任何浏览器内使用Workbench或CloudShell，ACK会在工具启动时根据当前用户信息自动加载集群的KubeConfig文件。
[Workbench](../../../../ecs/documents/user-guide/workbench-overview.md)：阿里云提供的ECS实例远程连接工具，无需额外安装软件。支持通过公网和内网连接集群。
[CloudShell](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)：阿里云提供的Shell工具，相当于自动创建的一台Linux虚拟机，其中预装了多种语言及命令行工具。仅通过公网连接集群。
公网连接时，需要为集群API Server绑定阿里云EIP，实现集群的公网访问，请参见[实现从公网访问](control-public-access-to-the-api-server-of-a-cluster.md)[API Server](control-public-access-to-the-api-server-of-a-cluster.md)。
CloudShell创建的虚拟机使用期限为1小时，到期后会立即销毁。无交互式操作30分钟或关闭所有会话窗口，虚拟机将在15分钟后销毁。再次启动时，系统会重新创建新虚拟机。
