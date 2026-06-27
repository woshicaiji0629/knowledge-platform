## 免登录运维
您可以通过云服务器ECS提供的原生自动化运维工具云助手，免密码、免登录，且无需使用跳板机，即可批量执行命令（Shell、PowerShell、Bat等），从而实现自动化运维脚本的执行、进程的轮询、软件的安装与卸载、服务的启动或停止，以及补丁或安全更新的安装等任务。更多详细信息，请参见[云助手概述](../user-guide/overview-10.md)。
例如在ECS中安装Java和Tomcat，您可以调用RunCommand接口执行命令：

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunCommand](../api-runcommand.md) | RegionId | 地域： cn-hangzhou |
| Type | 运维命令的语言类型： RunShellScript |  |
| CommandContent | 命令内容： #!/bin/bash if cat /etc/issue|grep -i Ubuntu ; then sudo apt-get update sudo apt-get install -y default-jdk sudo apt-get install -y tomcat9 else yum install -y java yum install -y tomcat fi |  |
| Timeout | 可选，执行命令的超时时间，单位：秒。 示例： 60 |  |
| InstanceId | ECS 实例 ID 集合： ["i-bp17f3kzgtzzj91r****"] |  |
