### 如何修改 loongcollector 组件配置参数 projectName？
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏，选择应用>Helm。
在 Helm 应用管理页面，找到loongcollector，单击其右侧操作列中的更新，进入更新发布页面。
在目标 Helm Chart 的参数配置（Values）区域，修改projectName（根级字段）的值，单击确定。
说明
配置环境变量时，若未显式指定ALICLOUD_LOG_PROJECT，系统将使用安装命令中传入的 Project 参数作为默认值，并自动在该 Project 下创建 LoongCollector 相关配置及集群默认机器组。
