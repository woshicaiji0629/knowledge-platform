## 监控网络带宽
说明
目前不支持控制台查看ECS所在虚拟交换机的实时总内网流量。
您可以通过以下步骤在ECS控制台监控实例的内网带宽与公网带宽使用情况：
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到目标实例，点击进入实例详情页。
单击监控页签。
设置监控时间范围，查看内网带宽与公网带宽等信息。
由于监控曲线显示的聚合方式不一样，选择时间段的长短会影响显示的精度。选择的时间范围越小，显示效果越精细。例如，1小时和6小时的平均值会显示不一样的结果，请您根据实际需要选择适合的时间范围。
假设您购买的公网带宽为1 Mbps，当公网流出带宽达到1024 Kbit/s时，表示您的公网带宽已经满负荷。当您发现带宽使用率过高或过低时，可以考虑[修改带宽配置](modify-bandwidth-configurations.md)。
说明
如果此页面显示暂无数据，可能是由于此ECS实例的云监控插件未安装，或者云监控插件运行异常，您可以尝试重新安装云监控插件，详细信息，请参见[安装和卸载云监控插件](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/install-and-uninstall-the-cloudmonitor-agent-for-cpp)。
除了使用上述方式，您也可以通过[云监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor#concept-2452587)或[网络分析与监控](https://help.aliyun.com/zh/document_detail/341648.html#a9eff49079ji3)来监控网络带宽。
