### 步骤二： 配置机器组（安装LoongCollector）
在成功[创建](log-collection-supports-nanosecond-precision-timestamps.md)[Project](log-collection-supports-nanosecond-precision-timestamps.md)[和](log-collection-supports-nanosecond-precision-timestamps.md)[LogStore](log-collection-supports-nanosecond-precision-timestamps.md)后，为服务器安装LoongCollector并将其加入机器组。本文以ECS实例安装LoongCollector（ECS与日志服务Project属于同一阿里云账号和地域）为例，若ECS实例与Project不属于同一账号或地域，或为自建服务器请参考[安装采集器](loongcollector-installation-linux.md)手动安装。
此功能仅支持 Linux 系统的LoongCollector（ Logtail），在 Windows 系统上配置不生效，Logtail版本为1.8.0及以上。

| 单击目标 Project，在日志库（LogStore） 页面： 单击目标 LogStore 名称前的 展开， 单击 数据接入 后的 ， 在弹框中选择文本日志接入模板，本文以 单行-文本日志 模板为例，单击 立即接入 。 所有文本日志接入模板仅在解析插件上有所差异，其余配置流程一致，后续均可修改。 |
| --- |

配置步骤：
在机器组配置页面，配置如下参数：
使用场景：主机场景
安装环境：ECS
配置机器组：根据目标服务器的LoongCollector安装情况与机器组配置状态，选择对应操作：
已安装LoongCollector且已加入某个机器组，可直接在源机器组列表中勾选，将其添加至应用机器组列表，无需重复创建。
未安装LoongCollector，单击创建机器组：
以下步骤将引导您完成LoongCollector的自动安装并创建新机器组。
系统会自动列出与 Project 同地域的 ECS 实例，勾选需要采集日志的一台或多台实例。
单击安装并创建为机器组，系统将自动在所选ECS实例上安装LoongCollector。
配置机器组名称并单击确定。
说明
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
如需将已安装LoongCollector的服务器加入已有机器组，请参考常见问题[如何将服务器加入到已有机器组？](host-text-log-collection-auto-install.md)
