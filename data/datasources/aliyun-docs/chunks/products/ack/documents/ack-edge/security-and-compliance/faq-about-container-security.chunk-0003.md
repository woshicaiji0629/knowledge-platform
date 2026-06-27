## 如何给Kubernetes集群指定安全组？
创建集群时指定安全组
创建Kubernetes集群时，容器服务ACK会自动创建一个默认安全组，您可以通过修改默认安全组的规则，达到指定安全组的效果。请参见[配置集群安全组](../../ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters.md)。
在已创建集群中修改关联的安全组
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，选择基本信息页签，然后在网络区域单击控制面安全组后的编辑。
在弹出的对话框中选中要切换的安全组，然后单击确定完成。
