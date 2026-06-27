## 步骤二：创建机器组
使用阿里云账号A登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
选择机器组右侧的>创建机器组。
在创建机器组对话框中，配置如下参数，然后单击确定。
其中用户自定义标识需设置为您在[步骤一：设置阿里云账号为用户标识](use-logtail-to-collect-container-logs-across-accounts.md)中获取的机器组标识（例如k8s-group-cc47****54428）。其他参数说明，请参见[创建用户自定义标识机器组](create-a-user-defined-identity-machine-group.md)。名称设置为k8s-group，机器组标识选择用户自定义标识，在用户自定义标识输入框中填写自定义标识值（如k8s-group-cc{实例标识}）。
检查机器组中的服务器心跳都为OK。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看容器节点（ECS）的心跳状态。
心跳为OK表示容器节点与日志服务的连接正常。如果显示FAIL请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。确认所有节点的心跳状态均显示为OK，表示机器组创建成功。
