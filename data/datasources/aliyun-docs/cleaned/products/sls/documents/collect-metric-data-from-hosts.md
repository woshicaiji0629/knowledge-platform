# 如何通过Logtail采集主机监控数据-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-metric-data-from-hosts

# 采集主机监控数据
日志服务Logtail支持采集主机CPU、内存、负载、磁盘、网络等监控数据。本文介绍通过Logtail采集主机监控数据的操作步骤。
## 前提条件
已创建Project和MetricStore。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[创建](manage-a-metricstore.md)[MetricStore](manage-a-metricstore.md)。
## 使用限制
不支持Windows版本。
不支持采集GPU、硬件状态等监控数据。
只有Linux Logtail 0.16.40及以上版本的Logtail支持采集主机监控数据。如果您已在服务器上安装旧版本的Logtail，需先升级。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
## 数据采集配置
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击控制台右侧的快速接入数据卡片。
在接入数据页面，查找主机监控并单击。
选择目标Project和时序库MetricStore，单击下一步。在选择日志空间步骤中，选择已有的项目Project和时序库MetricStore，或单击右侧立即创建新建，然后单击下一步。
在创建机器组页签中。
如果已有可用的机器组，请单击使用现有机器组。选择主机场景和ECS安装环境，从源机器组列表中选择目标机器组，单击>将其移至应用机器组列表，然后单击下一步。
如果您还没有可用的机器组，请执行以下操作（以ECS为例）。
在ECS机器页签中，通过手动选择实例方式选择目标ECS实例，单击创建。
具体操作，请参见[安装](install-logtail-on-ecs-instances.md)[Logtail（ECS](install-logtail-on-ecs-instances.md)[实例）](install-logtail-on-ecs-instances.md)。
重要
如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器和自建IDC时，您需要手动安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。手动安装Logtail后，您必须在该服务器上手动配置用户标识。具体操作，请参见[配置用户标识](configure-a-user-identifier.md)。
安装完成后，单击确认安装完毕。
在创建机器组页面，输入名称，单击下一步。
日志服务支持创建IP地址机器组和用户自定义标识机器组，具体操作，请参见[创建机器组](manage-machine-groups.md)。
在数据源设置页签中，设置配置名称和插件配置，然后单击下一步。
重要
inputs为数据源配置，必选项。一个inputs中只允许配置一个类型的数据源。
{ "inputs": [ { "detail": { "IntervalMs": 30000 }, "type": "metric_system_v2" } ] }
| 参数 | 类型 | 是否必选 | 参数说明 |
| --- | --- | --- | --- |
| type | string | 是 | 数据源类型，固定为 metric_system_v2。 |
| IntervalMs | int | 是 | 每次请求的间隔，单位：ms。不能低于 5000，建议设置为 30000。 |
单击查询日志，进入时序库。
## 数据监控
在目标时序库首页单击指标统计，打开指标统计大盘。
在指标统计查看所有已采集到的数据指标，也可以按时间周期或者指标参数进行数据过滤。
在时序库首页，单击Metrics 探索（指标数：48），可探索、查看和过滤所有可用的指标名称及其元数据。如需查看CPU 和内存数据，可以使用cpu_count{}和mem_cache{}语句查询。更多查询与分析操作，请参见[查询和分析时序数据](query-and-analyze-metric-data.md)。
当您采集的数据中包含多台机器时，可使用hostname或ip进行筛选。为保证筛选数据的准确性，进行筛选前，请先清除历史查询数据。选择指标（如cpu_count）后，页面展示该指标的标签列表（如hostname、ip）及其唯一值数量和示例值。单击标签操作列的筛选，选择运算符并输入筛选值（如 ip = 172.26.150.228），然后单击+ 添加到查询框将筛选条件应用到查询语句中。
## 指标说明
主机CPU、内存、负载、磁盘、网络等指标说明如下：
CPU相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| cpu_count | CPU 核数 | 个 | 2.0 |
| cpu_util | CPU 使用率，计算方式为排除 idle、wait、steal 后的占比 | 百分号（%） | 7.68 |
| cpu_guest_util | 客户时间（guest time）占比 | 百分号（%） | 0.0 |
| cpu_guestnice_util | Nice 进程客户时间（nice guest time）占比 | 百分号（%） | 0.0 |
| cpu_irq_util | 硬中断处理时间（Hard Irq time）占比 | 百分号（%） | 0.0 |
| cpu_nice_util | Nice 时间（Nice time）占比 | 百分号（%） | 0.0 |
| cpu_softirq_util | 软中断处理时间（Soft Irq time）占比 | 百分号（%） | 0.06 |
| cpu_steal_util | 等待宿主机 CPU 时间（Steal time）占比 | 百分号（%） | 0.0 |
| cpu_sys_util | 内核态（System time）占比 | 百分号（%） | 2.77 |
| cpu_user_util | 用户态（User time）占比 | 百分号（%） | 4.84 |
| cpu_wait_util | 等待 IO（Waiting time）占比 | 百分号（%） | 0.11 |
内存相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| mem_util | 内存使用率 | 百分号（%） | 51.03 |
| mem_cache | 已申请但未使用的内存 | byte | 3566386668.0 |
| mem_free | 未使用的内存 | byte | 177350084.0 |
| mem_available | 可用内存 | byte | 3699885553.0 |
| mem_used | 已使用内存 | byte | 4041510463.0 |
| mem_swap_util | swap 内存使用率 | 百分号（%） | 0.0 |
| mem_total | 内存总量 | byte | 7919128576.0 |
磁盘相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| disk_rbps | 硬盘每秒读取流量 | byte/s | 8376.81 |
| disk_wbps | 硬盘每秒写入流量 | byte/s | 247633.58 |
| disk_riops | 硬盘每秒读取次数 | 次/s | 0.22 |
| disk_wiops | 硬盘每秒写入次数 | 次/s | 43.39 |
| disk_rlatency | 平均读延迟 | ms | 2.83 |
| disk_wlatency | 平均写延迟 | ms | 2.15 |
| disk_util | IO 使用率 | 百分号（%） | 0.27 |
| disk_space_usage | 磁盘使用百分比 | 百分号（%） | 9.12 |
| disk_inode_usage | inode 使用率 | 百分号（%） | 1.18 |
| disk_space_used | 磁盘已使用容量 | byte | 11068512238.59 |
| disk_space_total | 磁盘总量 | byte | 126692061184.0 |
| disk_inode_total | inode 总量 | 个 | 7864320.0 |
| disk_inode_used | inode 已使用容量 | 个 | 93054.78 |
NET相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| net_drop_util | 丢弃的数据包占总数据包的比值 | 百分号（%） | 0.0 |
| net_err_util | 报错数据包占总数据包的比值 | 百分号（%） | 0.0 |
| net_in | 网络接收速率 | byte/s | 8440.91 |
| net_in_pkt | 每秒接收的数据包 | 个/s | 40.83 |
| net_out | 网络发送速率 | byte/s | 12446.53 |
| net_out_pkt | 每秒发送的数据包 | 个/s | 39.95 |
TCP相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| protocol_tcp_established | 已建立连接数 | 个 | 205.0 |
| protocol_tcp_insegs | 接收的所有报文数 | 个 | 4654.0 |
| protocol_tcp_outsegs | 发送的报文数 | 个 | 4870.0 |
| protocol_tcp_retran_segs | 重传报文数 | 个 | 0.0 |
| protocol_tcp_retran_util | 重传报文占总发送报文数量的比值 | 百分号（%） | 0.0 |
system相关指标
| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| system_boot_time | 系统启动时间 | s | 1578461935.0 |
| system_load1 | 系统平均负载，1 分钟平均值 | 不涉及 | 0.58 |
| system_load5 | 系统平均负载，5 分钟平均值 | 不涉及 | 0.68 |
| system_load15 | 系统平均负载，15 分钟平均值 | 不涉及 | 0.60 |
## 后续步骤
关于日志服务可视化，请参见[时序图](time-series-chart.md)，[时序数据对接](send-time-series-data-from-log-service-to-grafana.md)[Grafana](send-time-series-data-from-log-service-to-grafana.md)。
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
