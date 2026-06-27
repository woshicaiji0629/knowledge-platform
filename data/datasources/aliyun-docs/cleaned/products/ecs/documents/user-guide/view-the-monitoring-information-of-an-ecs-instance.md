# 查看ECS实例的监控信息-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/view-the-monitoring-information-of-an-ecs-instance

# 查看ECS实例的监控信息
监控您的ECS实例是否健康非常重要，您需要确保用户始终可以快速打开您的网站和应用，或者快速完成数据处理和渲染等任务。阿里云提供了监控数据收集、可视化以及实时监控告警等服务，确保您的实例始终处于正常的运行状态。
## 背景信息
您可以通过ECS控制台和云监控控制台监控实例信息。
ECS控制台：提供vCPU使用率、网络流量和磁盘I/O监控。
云监控控制台：提供更加精细化的监控粒度。
## 监控信息说明
主要监控项说明如下所示：
vCPU：阿里云提供实例vCPU使用率监控数据，单位为百分比。百分比数值越高，实例vCPU负载越高。您可以通过ECS管理控制台、云监控管理控制台、调用ECS API或者远程连接实例后查询监控数据。
以下是远程连接实例后查看vCPU使用率的方式：
Windows实例：在任务管理器中查看vCPU使用情况，您可以按vCPU使用率排序，定位占用实例vCPU资源的进程。
Linux实例：运行top命令查看vCPU使用情况。在键盘上按下Shift+P根据vCPU使用率排序，定位占用实例vCPU资源的进程。
重要
如果CPU持续保持高使用率，则会对系统稳定性和业务运行造成影响。您可以参见以下方法进行优化：
Linux实例请参见[Linux](../support/query-and-case-analysis-linux-cpu-load.md)[系统](../support/query-and-case-analysis-linux-cpu-load.md)[CPU](../support/query-and-case-analysis-linux-cpu-load.md)[负载的查询和案例分析](../support/query-and-case-analysis-linux-cpu-load.md)。
Windows实例请参见[Windows](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[实例中](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[CPU](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)[使用率较高问题的排查及解决方法](../what-do-i-do-if-cpu-utilization-is-high-on-a-windows-instance.md)。
网络流量：阿里云提供实例出方向和入方向的网络流量监控数据，单位为kbps。
ECS控制台一般提供公网流量监控，云监控控制台可以提供公网和内网流量监控。例如，您的公网出网带宽为1 Mbps，当出网流量达到1024 kbps，表示您的公网带宽已经满负荷。
## 通过ECS控制台查看监控信息
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
单击目标实例ID进入实例详情页，选择监控页签。
设置监控时间范围，可以查看vCPU使用率、内存使用率等监控信息。
由于监控曲线显示的聚合方式不一样，选择时间段的长短会影响显示的精度。选择的时间范围越小，显示效果越精细。例如，1小时和6小时的平均值会显示不一样的结果，请您根据实际需要选择适合的时间范围。
说明
您也可以使用DescribeInstanceMonitorData、DescribeDiskMonitorData和DescribeEniMonitorData接口获取监控数据。
实例是否安装云监控插件会导致在ECS管理控制台查看到的监控数据不同：
实例已安装云监控插件：ECS管理控制台的监控项中，CPU、内存、系统负载数据为云监控的操作系统监控项，其他监控项与云监控的基础监控项一致。
实例未安装云监控插件：在ECS管理控制台查看到的监控项与云监控的基础监控项一致。
说明
基础监控项数据采集频率为每1分钟一次，操作系统监控项数据采集频率为每15秒一次。更多信息，请参见[操作系统监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/operating-system-monitoring#concept-gdq-tgc-5db)。
以下是实例未安装插件时在ECS控制台上的监控项详细列表，指标采集粒度为1分钟。
| 监控指标名称 | 监控指标含义 | 单位 | MetricName | Dimensions | Statistics |
| --- | --- | --- | --- | --- | --- |
| （ECS）CPU 使用率 | CPU 使用率 | % | CPUUtilization | userId、instanceId | Maximum、Minimum、Average |
| （ECS）经典网络公网流入带宽 | 公网入流量平均速率 | bit/s | InternetInRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）内网流入带宽 | 私网入流量平均速率 | bit/s | IntranetInRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）经典网络公网流出带宽 | 公网出流量平均速率 | bit/s | InternetOutRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）内网流出带宽 | 私网出流量平均速率 | bit/s | IntranetOutRate | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘读取 BPS | 系统磁盘每秒读取字节总数 | Byte/s | DiskReadBPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘写入 BPS | 系统磁盘每秒写入字节总数 | Byte/s | DiskWriteBPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘每秒读取次数 | 所有磁盘读 IOPS | 次/秒 | DiskReadIOPS | userId、instanceId | Maximum、Minimum、Average |
| （ECS）所有磁盘每秒写入次数 | 所有磁盘写 IOPS | 次/秒 | DiskWriteIOPS | userId、instanceId | Average、Minimum、Maximum |
| （ECS）IP 维度公网流入带宽 | 公网流入带宽 | bit/s | VPC_PublicIP_InternetInRate | userId、instanceId、ip | Maximum、Minimum、Average |
| （ECS）IP 维度公网流出带宽 | 公网流出带宽 | bit/s | VPC_PublicIP_InternetOutRate | userId、instanceId、ip | Maximum、Minimum、Average |
| （ECS）IP 维度公网流出带宽使用率 | 公网流出带宽使用率 | % | VPC_PublicIP_InternetOutRate_Percent | userId、instanceId、ip | Average |
| （ECS）经典网络公网流入流量 | 公网流入流量 | Byte | InternetIn | userId、instanceId | Average、Minimum、Maximum、Sum |
| （ECS）经典网络公网流出流量 | 公网流出流量 | Byte | InternetOut | userId、instanceId | Maximum、Minimum、Average |
## 通过云监控控制台查看监控信息
云监控为您提供开箱即用的企业级开放型一站式监控解决方案。云监控为您的ECS提供主机监控服务，关于主机监控和主机监控项的更多信息，请参见[概览](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/overview-8#concept-ypb-thv-vdb)和[操作系统监控](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/operating-system-monitoring#concept-gdq-tgc-5db)。
说明
当您需要监控各云产品资源的使用情况时，可以在云监控控制台创建报警规则。如果资源的监控指标达到报警条件，云监控自动发送报警通知，帮助您及时得知异常监控数据，并快速处理。具体操作，请参见[创建报警规则](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/create-an-alert-rule)。
登录[云监控管理控制台](https://cloudmonitor.console.aliyun.com/)。
在左侧导航栏中，单击主机监控。
可选：找到并选中目标实例，在主机监控页面底部，单击批量安装或升级插件，然后单击确定。
如果实例未安装云监控插件，您可以为实例安装插件。具体操作，请参见[安装和卸载云监控插件](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/install-and-uninstall-the-cloudmonitor-agent-for-cpp#task-1950491)。
实例未安装插件：在云监控控制台查看到的是基础监控项。
实例已安装插件：在云监控控制台可以查看基础监控项和操作系统监控项。
单击目标实例ID，在基础监控或操作系统监控页签下获取监控数据。
说明
监控数据保留最大天数为30天。
## 相关文档
[DescribeInstanceMonitorData](../api-describeinstancemonitordata.md)
[DescribeDiskMonitorData](../api-describediskmonitordata.md)
[DescribeEniMonitorData](../api-describeenimonitordata.md)
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
