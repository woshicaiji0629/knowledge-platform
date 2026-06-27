## 操作步骤
登录[运维编排](https://oos.console.aliyun.com/)[OOS](https://oos.console.aliyun.com/)[控制台](https://oos.console.aliyun.com/)。
在左侧导航栏中，选择自动化任务>公共任务模板。
在公共任务模板页面中，搜索LogAgent，找到批量安装日志服务插件模板，然后单击创建执行。
在创建页面，完成如下配置。
在基本信息步骤中，保持默认配置，然后单击下一步：设置参数。
在设置参数步骤中，完成如下配置，然后单击下一步：确定。
重要参数说明如下：
是否覆盖LogAgent：打开是否覆盖LogAgent开关后，如果ECS实例内已存在Logtail，则将被覆盖。详细说明如下表所示。
重要
当ECS实例为Windows操作系统且使用upgrade操作时，仅支持覆盖原有的Logtail更新，是否覆盖LogAgent配置不会生效。

| 是否覆盖 LogAgent | install（安装） | upgrade（更新） | uninstall（卸载） |
| --- | --- | --- | --- |
| 覆盖 LogAgent | 卸载 Logtail，安装最新版本。 | 卸载 Logatil，安装最新版本。 | 卸载 Logtail |
| 不覆盖 LogAgent | 返回 Logtail 已存在，不会覆盖。 | 保留原有 Logtail 配置，安装最新版本，安装完成后按照之前进度继续采集。 | 卸载 Logtail |

目标实例：选择目标ECS实例。更多信息，请参见[实例选取方式](install-logtail-on-ecs-instances.md)。
确认信息无误后，单击创建。
查看执行结果。
您可以在执行结果区域，查看在每台ECS上执行Logtail安装命令的执行状态。执行详情页面显示执行状态为成功，模板名称为ACS-ECS-BulkyInstallLogAgent，执行模式为自动执行。执行结果流程依次经过输入、获取ECS实例、runCommand、输出四个节点，所有节点均已执行成功。您还可以通过查看输出、日志等内容，获取Logtail的安装目录等信息。
该文章对您有帮助吗？
反馈
