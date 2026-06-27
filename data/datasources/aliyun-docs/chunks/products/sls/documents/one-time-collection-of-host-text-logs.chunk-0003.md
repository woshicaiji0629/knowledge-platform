## 步骤一：配置机器组（安装LoongCollector）
在完成[准备工作](one-time-collection-of-host-text-logs.md)后，为不同类型的服务器安装LoongCollector并将其加入机器组。
说明
以下安装步骤仅适用于日志源为阿里云ECS实例，且该实例与日志服务Project属于同一阿里云账号和相同地域的场景。
如果您的ECS实例与Project不在同一账号或地域，或者日志源为自建服务器，请参考[LoongCollector 安装与配置](loongcollector-installation-linux.md)进行操作。
配置步骤：
在日志库页面，单击目标LogStore名称前的展开。
单击数据接入>Logtail配置，在Logtail一次性配置页签下，单击添加Logtail配置。
在快速数据接入弹框中，单击一次性文件采集 - 主机卡片上的立即接入。
在机器组配置页面，配置如下参数：
使用场景：主机场景
安装环境：ECS
配置机器组：根据目标服务器的LoongCollector安装情况与机器组配置状态，选择对应操作：
已安装LoongCollector且已加入某个机器组，直接在源机器组列表中勾选，将其添加至应用机器组列表，无需重复创建。
未安装LoongCollector，单击创建机器组：
以下步骤将引导您完成LoongCollector的一键自动安装并创建机器组。
系统会自动列出与 Project 同地域的 ECS 实例，勾选需要采集日志的一台或多台实例。
单击安装并创建为机器组，系统将自动在所选ECS实例上安装LoongCollector。
配置机器组名称并单击确定。
说明
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
如需将已安装LoongCollector的服务器加入已有机器组，请参考常见问题[如何将服务器加入到已有机器组？](one-time-collection-of-host-text-logs.md)
检查心跳状态：单击下一步，如页面出现机器组心跳情况。查看心跳状态，若为OK表示机器组连接正常，单击下一步，进入Logtail配置页面。
若为FAIL，可能是初次建立心跳需要花费一些时间，请等待两分钟左右，再刷新心跳状态。若刷新后仍为FAIL，请参考[机器组心跳连接为](one-time-collection-of-host-text-logs.md)[fail](one-time-collection-of-host-text-logs.md)进一步排查。
