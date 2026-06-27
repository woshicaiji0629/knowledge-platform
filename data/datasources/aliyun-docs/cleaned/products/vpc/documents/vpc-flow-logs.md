# VPC流日志-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-flow-logs

# VPC流日志
VPC流日志采集并记录弹性网卡的进出流量信息，可以监控网络性能、排查网络故障或优化流量成本。
## 工作原理
流日志支持3种粒度的流量信息采集：弹性网卡、交换机或VPC。如果为VPC或交换机创建流日志，则系统会采集VPC或交换机内所有关联弹性网卡的流量，包括创建流日志后新建的弹性网卡。
系统会在每个采集窗口（默认为10分钟）内先将流量信息聚合为流日志条目，再投递到SLS。
每条流日志条目会记录特定采集窗口中的特定五元组网络流，包含源/目IP地址、源/目端口、协议等信息，示例：
| eni-id | direction | srcaddr | srcport | protocol | dstaddr | dstport | ... |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eni-xxx | in | 10.0.0.1 | 53870 | 6 | 10.0.0.2 | 80 | ... |
| eni-xxx | out | 10.0.0.2 | 80 | 6 | 10.0.0.1 | 53870 | ... |
您可参考[流日志字段说明](vpc-flow-logs.md)了解所有字段及其含义。
您可根据实际使用场景，仅采集所需路径的流量，从而降低流日志的使用成本。可选路径：
通过IPv4网关访问公网的流量
通过NAT网关的流量
通过VPN网关的流量
通过转发路由器（TR）的流量
通过网关终端节点访问云服务的流量
通过边界路由器（VBR）访问专线的流量
通过专线网关（ECR）的流量
通过网关型负载均衡终端节点的流量
访问公网的流量
不支持采集公网 CLB 访问公网流量。
流日志的应用场景：
网络监控：了解VPC吞吐量和性能、VPC内资源的流量信息及变化趋势、排查网络故障、检查安全组或网络ACL生效情况。
优化网络流量成本：通过流日志分析网络传输情况，来优化网络流量费用。例如获取VPC发往其他地域的流量、发往特定公网地址的流量、流向本地IDC和其他云网络的流量，以及定位VPC中高流量的ECS实例。
网络安全分析：在出现突发事件时，通过出入流量信息分析异常IP或者调查入侵IP访问记录。
## 使用限制
首次使用流日志功能时，需要：
在[流日志页面](https://vpc.console.aliyun.com/flowlog/)单击立即开通。如果曾在公测期间创建过流日志实例，也需单击立即开通后才能重新查看和管理这些实例。
在[流日志页面](https://vpc.console.aliyun.com/flowlog/)单击立即授权，然后单击确认授权。该操作会自动创建1个RAM角色AliyunVPCLogArchiveRole和1个RAM策略AliyunVPCLogArchiveRolePolicy，VPC默认通过此角色和策略来访问日志服务，来保证将流日志写入日志服务中。
已在[日志服务产品页](https://www.aliyun.com/product/sls/)开通了日志服务。
开启流日志后，新建弹性网卡的首次采集可能存在时间延迟（通常＜10分钟）。
流日志不支持采集[组播](../../cen/documents/user-guide/multicast-overview.md)流量。
## 管理流日志
### 控制台
创建流日志
前往专有网络控制台[流日志页面](https://vpc.console.aliyun.com/flowlog/cn-hangzhou/flowlogs)，单击创建流日志。在创建流日志面板中进行配置：
采集配置：
地域：选择目标采集对象所在的地域。
资源类型和资源实例：可选采集粒度为专有网络、交换机、弹性网卡。选择专有网络或交换机时，系统会监控其内所有弹性网卡的流量。
流量类型：可选被访问控制允许或拒绝的流量，此处的访问控制包括安全组和网络ACL。
流量采集IP版本：可选仅采集IPv4或采集IPv4+IPv6双栈。当前支持IPv6的地域包括：华东1（杭州）、华东2（上海）、华北1（青岛）、华北2（北京）、华北5（呼和浩特）、华南1（深圳）、新加坡、美国（硅谷）、美国（弗吉尼亚）。
采样间隔（分钟）：聚合流量信息的采集窗口时间，可选1分钟、5分钟或10分钟。窗口越小，流日志生成越频繁和及时，有助于更快发现和定位问题。窗口越大时效性越低，但日志条目数也会下降从而节省费用成本。
例如1个保持长连接的TCP会话，窗口为1分钟时每小时产生60条日志；为10分钟时仅产生6条。
当VPC内存在多个流日志实例同时采集同一网卡流量时，将会以所有流日志实例中最小的采样间隔作为实际采集周期。
采样路径：可选择特定的采集场景来降低使用成本。选择前需要先取消默认的采集全部场景。
支持选择通过如下网元的流量：IPv4网关、NAT网关、VPN网关、转发路由器（TR）、网关终端节点、边界路由器（VBR）、专线网关（ECR）、网关型负载均衡节点（GWLB），以及访问公网的流量。
分析和投递配置：支持投递至日志服务和NIS流量分析器。投递至日志服务，仅支持在创建流日志时选择，且关闭后不支持重新开启。
投递至日志服务：
选择Project和Logstore：首次创建流日志时，为和其他数据隔离，建议新建 Project并新建 Logstore。当需要将多个流日志汇总到一处集中分析时，请选择同一个Logstore。
开启流日志分析报表功能：建议勾选。该功能会自动在流日志对应的LogStore上[创建索引](../../sls/documents/create-indexes.md)并[创建仪表盘](../../sls/documents/dashboard-overview.md)，以支持对流日志执行SQL与可视化分析。开启后SLS产品会[产生计费](../../sls/documents/billable-items.md)。
开启NIS流量分析：选择NIS流量分析器，进行流量分析。如果选择列表为空，需要先创建NIS流量分析器。确保创建或选择的NIS流量分析器的流量分析采样间隔需大于流日志采样间隔。
[支持将](https://help.aliyun.com/zh/nis/user-guide/traffic-analyzer/#92cb328627ics)[VPC](https://help.aliyun.com/zh/nis/user-guide/traffic-analyzer/#92cb328627ics)[流日志接入流量分析器的地域](https://help.aliyun.com/zh/nis/user-guide/traffic-analyzer/#92cb328627ics)。
成功创建流日志后，系统会自动启动流量信息采集，下一步可以[分析流日志](vpc-flow-logs.md)。
启动或停止流日志
前往专有网络控制台[流日志页面](https://vpc.console.aliyun.com/flowlog/cn-hangzhou/flowlogs)，在目标流日志的操作列单击启动或停止。
停止后，VPC不再收取流日志生成费，但SLS会针对已保存的流日志持续[计费](vpc-flow-logs.md)。
删除流日志
前往专有网络控制台[流日志页面](https://vpc.console.aliyun.com/flowlog/cn-hangzhou/flowlogs)，在目标流日志的操作列单击删除。
删除后，VPC不再收取流日志生成费，但SLS会针对已保存的流日志持续[计费](vpc-flow-logs.md)，需至日志服务控制台[删除对应的](../../sls/documents/manage-a-logstore.md)[Logstore](../../sls/documents/manage-a-logstore.md)才能停止全部费用。
### API
创建流日志前，请确保已开通流日志功能，且已在日志服务产品中创建了Project和Logstore：
调用[OpenFlowLogService](developer-reference/api-vpc-2016-04-28-openflowlogservice.md)开通流日志功能。
调用[CreateProject](../../sls/documents/developer-reference/api-sls-2020-12-30-createproject.md)创建Project，调用[CreateLogStore](../../sls/documents/developer-reference/api-sls-2020-12-30-createlogstore.md)创建Logstore。
确保满足上述条件后，您可以：
调用[CreateFlowLog](developer-reference/api-vpc-2016-04-28-createflowlog.md)创建流日志，可选调用[CreateIndex](../../sls/documents/developer-reference/api-sls-2020-12-30-createindex.md)创建索引。
调用[DeactiveFlowLog](developer-reference/api-vpc-2016-04-28-deactiveflowlog.md)停止流日志。
调用[ActiveFlowLog](developer-reference/api-vpc-2016-04-28-activeflowlog.md)启动流日志。
调用[DeleteFlowLog](developer-reference/api-vpc-2016-04-28-deleteflowlog.md)删除流日志。
### Terraform
Resources:[alicloud_log_project](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/log_project),[alicloud_log_store](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/log_store),[alicloud_vpc_flow_log](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/vpc_flow_log)# 指定创建流日志的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定Project的描述、Logstore和流日志的名称 variable "name" { default = "vpc-flowlog-example" } # 生成随机数，用于生成project名称 resource "random_uuid" "example" { } # 创建日志服务Project resource "alicloud_log_project" "example" { project_name = substr("tf-example-${replace(random_uuid.example.result, "-", "")}", 0, 16) description = var.name } # 创建日志服务Logstore resource "alicloud_log_store" "example" { project_name = alicloud_log_project.example.project_name logstore_name = var.name shard_count = 3 auto_split = true max_split_shard_count = 60 append_meta = true } # 创建VPC流日志 resource "alicloud_vpc_flow_log" "example" { flow_log_name = var.name log_store_name = alicloud_log_store.example.logstore_name description = var.name traffic_path = ["all"] # 采集所有场景 project_name = alicloud_log_project.example.project_name resource_type = "VPC" # 资源类型为VPC resource_id = "vpc-bp1ekmgzch0bo3hxXXXXXX" # VPC的ID aggregation_interval = "1" # 采集时间窗口为1分钟 traffic_type = "All" # 采集全部流量，无论访问控制允许还是拒绝 }
## 分析流日志
通过分析流日志，可以监控网络性能、排查网络故障、优化网络流量成本以及进行网络安全分析等。
### 控制台
自定义分析：通过Logstore日志库
前往专有网络控制台[流日志页面](https://vpc.console.aliyun.com/flowlog/cn-hangzhou/flowlogs)，在目标流日志的日志服务列单击Logstore的实例名称，进入Logstore的详情页面。在此页面可以：
查看原始日志获取流日志条目明细。
输入语句[查询分析流日志](../../sls/documents/quick-guide-to-query-and-analysis.md)。
Logstore 查询界面提供原始日志、统计图表和日志聚类三个标签页，支持设置查询时间范围。上方展示日志量的时序分布图，下方展示包含 srcaddr、dstaddr、protocol 等字段的查询结果表格。
通过预设模板分析：Flowlog日志中心
Flowlog日志中心预设了一组可视化模板，支持VPC的策略统计、弹性网卡流量统计以及网段间流量统计，帮助您快速分析VPC流日志。
前往[Flowlog](https://sls.console.aliyun.com/lognext/app/flowlog)[日志中心](https://sls.console.aliyun.com/lognext/app/flowlog)页面，在右上方单击添加。
在创建实例面板中，填入实例名称、已有流日志对应的Project和Logstore，单击确定。
实例创建成功后，单击Flowlog日志中心列表的实例ID。在Flowlog详情页面，可以查看并分析流日志的信息。
监控中心提供以下仪表盘和自定义查询功能：
概览：展示流日志的Accept和Reject趋势、进出流量趋势、每个VPC的总数据包数和总字节数、每个ENI的总数据包数和总字节数、来源IP和目标IP的地理分布。
策略统计：展示Accept趋势、Reject趋势、Accept次数统计（由五元组构成）、Reject次数统计（由五元组构成）等信息。五元组是由源IP、源端口、协议类型、目标IP和目标端口组成的集合。
Accept：安全组和网络ACL允许记录的流量。
Reject：安全组和网络ACL拒绝记录的流量。
ENI流量：展示弹性网卡入方向和出方向的流量信息。
ECS间流量：展示ECS实例之间的流量情况。
自定义查询：可以自行[查询与分析快速指引](../../sls/documents/quick-guide-to-query-and-analysis.md)。
开启域间分析（可选）：在Flowlog详情页面，单击网段设置，在网段设置页签，打开开启“域间分析”开关。
开启域间分析功能后，系统将自动创建数据加工任务，生成具有网段信息的VPC流日志，用于分析不同网段之间的流量情况。数据加工功能会[收取一定的费用](../../sls/documents/billable-items.md)。
日志服务已预设多个网段。当需要分析不同网段之间的流量情况时，只需一键开启域间分析功能即可。也可以根据自身需求自定义添加网段。
默认预设三种网段类型：私有网络（10.0.0.0/8、172.16.0.0/12、192.168.0.0/16，可根据实际情况调整）、阿里云部分云服务（100:64.0.0/10）和互联网（除以上网段外的其他网段）。每种网段均支持编辑和删除操作。
域间分析提供以下仪表盘和自定义查询功能：
域间流量：展示不同网段之间的流量情况。
ECS到区间流量：展示ECS实例到目标网段的流量情况。
威胁情报：展示源IP地址与目标IP地址的威胁情报信息。
自定义查询：可以自行[查询和分析具有网段信息的](../../sls/documents/quick-guide-to-query-and-analysis.md)[VPC](../../sls/documents/quick-guide-to-query-and-analysis.md)[流日志](../../sls/documents/quick-guide-to-query-and-analysis.md)。
### API
调用[GetLogsV2](../../sls/documents/developer-reference/api-sls-2020-12-30-getlogsv2.md)查询分析流日志。
## 使用示例
下面列举4个典型的使用示例，供参考。
## 分析公网访问ECS的来源IP
假设已经创建了1台向公网开放的、监听80端口的Web服务器，并通过安全组限制了源IP访问。
那么可以通过创建流日志，来查询访问80端口的来源IP，并统计访问被安全组允许或拒绝的情况。
创建流日志
资源实例选择Web服务器的弹性网卡。
流量类型选择全部流量。
投递配置选择投递至日志服务并开启流日志分析报表功能。
其他选项保持默认。
分析流日志
查询分析语句
过滤访问10.0.0.1:80端口的源IP，并显示每个IP被安全组允许和拒绝的次数：
dstaddr:10.0.0.1 AND dstport:80 | SELECT -- 过滤目的IP是10.0.0.1，目的地端口是80的日志 srcaddr, SUM(CASE WHEN action = 'ACCEPT' THEN 1 ELSE 0 END) AS accept_count, -- 每当ACCEPT（即被允许）时计1 SUM(CASE WHEN action = 'REJECT' THEN 1 ELSE 0 END) AS reject_count -- 每当REJECT（即被拒绝）时计1 FROM log GROUP BY srcaddr -- 按源IP地址分组 ORDER BY accept_count + reject_count DESC -- 按照“安全组允许+拒绝”的总次数倒序排列
效果预览
srcaddr列显示访问80端口的源IP，accept_count和reject_count列分别统计每个源IP被安全组允许和拒绝的流日志条目数，即在查询时间内：
访问80端口来源IP有5个，分别为120.26.XX.XX、121.43.XX.XX、154.212.XX.XX、176.65.XX.XX、198.235.XX.XX。
来自120.26.XX.XX的请求全部被允许，其他公网IP的请求全部被拒绝。
## 分析ECS互访流量
| 配置项 | 分析 VPC 内部的 ECS 互访流量 | 分析 VPC 之间的 ECS 互访流量 |
| --- | --- | --- |
| 示意图 |  |  |
| 示例说明 | 如图所示，假设已在 1 个 VPC 中部署了 3 台 ECS，且 ECS 之间有互访流量。 此时，可以使用流日志功能分析 ECS 之间互访的流量速率和变化趋势。 | 如图所示，假设已有两个位于不同地域的 VPC，每个 VPC 内均部署有多台 ECS 实例。两个 VPC 已通过对等连接实现内网互通，对等连接使用 CDT 按量计费。 最近发现，跨地域流量费用较以往突增，此时可以使用流日志定位高流量 ECS 实例，从而优化流量成本。 |
| 创建流日志配置 | 资源实例 选择 ECS1 的 弹性网卡 分析和投递配置 选择 投递至日志服务 ，并 开启流日志分析报表功能 其他选项保持默认 | 资源实例 选择 专有网络 VPC1 分析和投递配置 选择 投递至日志服务 ，并 开启流日志分析报表功能 其他选项保持默认 |
| 查询分析语句 | 统计 ECS1 和其他 ECS 之间的流量速率趋势： (srcaddr:10.0.0.1 AND dstaddr:10.0.0.*) OR (srcaddr:10.0.0.* AND dstaddr:10.0.0.1 ) | select --过滤 ECS1 和其他 ECS 之间的流量趋势 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将 Unix 时间戳转换为可读的时间格式 concat(srcaddr,'->', dstaddr) as src_to_dst, -- 拼接 IP 会话对，格式为“源 ip->目的 ip” sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间 1 分钟 group by time,srcaddr,dstaddr -- 根据时间、源 ip、目的 ip 分组 order by time asc -- 按时间升序 limit 100 -- 显示前 100 条结果 | 统计 2 个 VPC 之间的会话流量速率趋势： (srcaddr:10.0.* AND dstaddr:172.16.*) OR (srcaddr:172.16.* AND dstaddr:10.0.*) | select --过滤 2 个 VPC 之间的会话 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将 Unix 时间戳转换为可读的时间格式 concat(srcaddr,'->', dstaddr) as src_to_dst, -- 拼接 IP 会话对，格式为“源 ip->目的 ip” sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间 1 分钟 group by time,srcaddr,dstaddr -- 根据时间、源 ip、目的 ip 分组 order by time asc -- 按时间升序 limit 100 -- 显示前 100 条结果 |
| 效果预览 | 在查询分析结果页面，选择 统计图表 标签页，将图表类型设置为 面积图 。设置 x 轴字段为 time 、y 轴字段为 bandwidth 、聚合列为 src_to_dst ，格式化单位选择 bps,Kbps,Mbps(bit) 。 10.0.0.1 发送到 10.0.0.2 的流量速率最大，约为 1.4Mbps；10.0.0.1 发送到 10.0.0.3 的流量速率次之，约为 700Kbps；其他流量占比较小。 | 查询结果的可视化配置方式与场景二相同，选择 面积图 类型，设置聚合列为 src_to_dst 。 10.0.0.1 发送到 172.16.0.1 的流量为突增流量，约为 6Mbps。 |
## 分析公网NAT流量
如图，假设您在某地域拥有多台ECS，且都部署在同一个交换机中，这些ECS通过公网NAT网关的SNAT功能访问互联网。
近期发现NAT访问公网的流量突增，导致服务器响应变慢，此时您可以通过流日志，排查分析流量占比高的ECS。
创建流日志
资源实例选择公网NAT网关所在的交换机2。
投递配置选择投递至日志服务并开启流日志分析报表功能。
其他选项保持默认。
过滤特定流量路径的方法
在本示例场景中过滤特定路径的流量信息时，需要在查询语句限定不同的条件：
| 示意图 | 序号 | 过滤方法 |
| --- | --- | --- |
|  | ① | 过滤从 ECS 到 NAT 网关的流量： direction 为 in， srcaddr 为 ECS 私网 IP 地址 |
| ② | 过滤从 NAT 网关到公网的流量： direction 为 out， srcaddr 为 NAT 网关私网 IP 地址 |  |
| ③ | 过滤从公网到 NAT 网关的流量： direction 为 in， dstaddr 为 NAT 网关私网 IP 地址 |  |
| ④ | 过滤从 NAT 网关到 ECS 的流量： direction 为 out， dstaddr 是 ECS 私网 IP 地址 |  |
分析流日志
查询分析语句
在ECS到NAT网关的这段路径上，分析去往特定公网IP地址的流量：
direction: 'in' and srcaddr: 10.0.0.* and dstaddr: 120.26.XX.XX | select -- 过滤ECS访问特定公网IP地址的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, srcaddr, -- 将Unix时间戳转换为可读的时间格式 sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,srcaddr -- 以时间、源ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
其他常用语句
在NAT网关到ECS的这段路径上，筛选某一特定公网IP到所有ECS实例的入流量信息：
direction: 'out' and dstaddr: 10.0.0.* and srcaddr: 120.26.XX.XX | select -- 过滤ECS访问特定公网IP地址的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将Unix时间戳转换为可读的时间格式 dstaddr, sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,dstaddr -- 以时间、目的ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
在ECS到NAT网关的这段路径上，筛选ECS实例去往所有公网IP的出流量信息：
direction: 'in' and srcaddr: 10.0.0.* | select -- 过滤ECS访问所有公网IP的日志 date_format(from_unixtime(__time__ - __time__% 60), '%H:%i:%S') as time, -- 将Unix时间戳转换为可读的时间格式 concat(srcaddr,'->', dstaddr), -- 拼接IP会话对，格式为“源ip->目的ip” sum(bytes*8/60) as bandwidth -- 将字节转换为比特，并除以采集窗口时间1分钟 group by time,srcaddr,dstaddr -- 以时间、源ip分组 order by time asc -- 按时间升序 limit 100 -- 显示前100条结果
效果预览
查询结果的可视化配置方式与场景二类似，选择面积图类型，设置聚合列为srcaddr。
在ECS到NAT网关的这段路径上，10.0.0.1（ECS1）发送到公网IP地址120.26.XX.XX的流量速率最高，约12Kbps。
## 分析专线内流量占比
如图，某企业在阿里云某地域使用两个VPC部署不同业务，并通过高速通道物理专线+云企业网实现本地IDC接入阿里云。
现在IT部门准备使用流日志监控分析VPC中不同业务流量对物理专线资源的占用情况，为网络资源规划、改善网络性能提供指导。
创建流日志
创建2个流日志，集中投递到同1个logstore，每个流日志的关键配置如下：
资源实例分别选择专有网络VPC1和VPC2。
采样路径选择转发路由器（TR）。
投递配置选择投递至日志服务，2个流日志选择同1个logstore，并开启流日志分析报表功能。
其他选项保持默认。
分析流日志
查询分析语句
分析不同VPC流入本地IDC流量的占比情况：
action: ACCEPT and srcaddr: 192.168.* and dstaddr:10.1.* | WITH vpc1_traffic AS ( SELECT date_trunc('minute',__time__) AS minute, SUM(bytes*8/(case WHEN "end"-start=0 THEN 1 else "end"-start end)) AS total_vpc1_traffic FROM log WHERE srcaddr LIKE '192.168.20.%' GROUP BY date_trunc('minute',__time__) ), vpc2_traffic AS ( SELECT date_trunc('minute',__time__) AS minute, SUM(bytes*8/(case WHEN "end"-start=0 THEN 1 else "end"-start end)) AS total_vpc2_traffic FROM log WHERE srcaddr LIKE '192.168.10.%' GROUP BY date_trunc('minute',__time__) ) SELECT COALESCE(vpc1_traffic.minute, vpc2_traffic.minute) AS minute, (COALESCE(vpc1_traffic.total_vpc1_traffic, 0) * 100/ NULLIF((COALESCE(vpc1_traffic.total_vpc1_traffic, 0) + COALESCE(vpc2_traffic.total_vpc2_traffic, 0)), 0)) AS vpc1_percentage, (COALESCE(vpc2_traffic.total_vpc2_traffic, 0) * 100/ NULLIF((COALESCE(vpc1_traffic.total_vpc1_traffic, 0) + COALESCE(vpc2_traffic.total_vpc2_traffic, 0)), 0)) AS vpc2_percentage FROM vpc1_traffic FULL OUTER JOIN vpc2_traffic ON vpc1_traffic.minute = vpc2_traffic.minute ORDER BY minute
单击查看SQL语句详细说明。
过滤条件：
srcaddr：192.168.*，过滤源地址以192.168.*开头的日志。
dstaddr：10.1.*，过滤目的地址以10.1.*开头的日志。
action：ACCEPT，过滤action字段取值为ACCEPT的日志。
主查询
使用FULL OUTER JOIN将vpc1_traffic和vpc2_traffic的结果根据minute字段连接在一起。
计算每分钟内两个VPC流量的百分比：
vpc1_percentage表示VPC1的流量在总流量中的占比。
vpc2_percentage表示VPC2的流量在总流量中的占比。
查询结果按minute升序排序。
WITH子查询：
SQL语句中包含vpc1_traffic和vpc2_traffic两个子查询，以vpc1_traffic子查询为例进行说明：
使用date_trunc函数将Unix 时间戳（__time__字段）的精度降低为分钟，并命名为minute。
使用SUM函数得到某一分钟内总的流量速率，单位bit/s，并命名为total_vpc1_traffic。
过滤源地址为192.168.20.*（VPC1下的网段）的流量记录。
按照分钟进行分组。
效果预览
查询结果的可视化配置方式与场景二类似，选择面积图类型，展示不同 VPC 流量占比随时间的变化趋势。
在14:50-15:50这段时间内，VPC1流入本地IDC的流量占比较高。
## 更多信息
### 流日志字段说明
流日志条目字段信息说明如下：
如果某个字段不适用，则字段值显示为-。
| 字段 | 说明 |
| --- | --- |
| version | 流日志版本，当前所有的日志条目版本为 1 。 |
| account-id | 阿里云账号 ID。 |
| eni-id | 弹性网卡 ID。 |
| vm-id | 弹性网卡绑定的 ECS 云服务器 ID。 |
| vswitch-id | 弹性网卡所在交换机 ID。 |
| vpc-id | 弹性网卡所在专有网络 ID。 |
| type | 流量类型，取值为 IPv4 或 IPv6。 支持采集 IPv4/IPv6 双栈 流量的地域有： 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 5（呼和浩特） 、 华南 1（深圳） 、 新加坡 、 美国（硅谷） 、 美国（弗吉尼亚） 。 |
| protocol | 流量的 [IANA](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) [协议编号](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) 。 常见协议号举例：ICMP 为 1，TCP 为 6，UDP 为 17。 |
| srcaddr | 源 IP 地址。 |
| srcport | 源端口。 |
| dstaddr | 目的 IP 地址。 |
| dstport | 目的端口。 |
| direction | 流量方向： in：流入弹性网卡的流量。 out：流出弹性网卡流量。 |
| action | 安全组或网络 ACL 是否允许该访问： ACCEPT：允许。 REJECT：拒绝。 |
| packets | 数据包个数。 |
| bytes | 字节数。 |
| start | 在采集窗口内，收到第 1 个包的时间。格式为 Unix 时间戳。 |
| end | 对于长连接，是采集窗口结束的时间；对于短连接，是连接关闭的时间。格式为 Unix 时间戳。 |
| tcp-flags | TCP 标志位，以十进制表示，反映了 TCP 协议中的 SYN、ACK、FIN 等标志的组合。 采集窗口内 1 个流日志条目可能会对应多个 TCP 数据包，该值是所有相关数据包的标志位字段进行 按位或（bitwise OR） 运算后的结果。 例如，1 个 TCP 会话在某采集窗口内有两个数据包，分别带有 SYN（2）和 SYN-ACK（18）标志，则日志中记录的 TCP 标志位字段为 18（2 | 18 = 18）。 部分 TCP 标志位对应的十进制： FIN: 1 SYN: 2 RST: 4 PSH: 8 SYN-ACK: 18 URG: 32 关于 TCP 标志通用信息（例如 SYN、FIN、ACK、RST 等标志的含义），请参见 [RFC: 793](https://datatracker.ietf.org/doc/html/rfc793) 。 |
| log-status | 日志记录状态： OK：数据记录正常。 NODATA：采集窗口中没有传入或传出网络接口的网络流量，常见于备用系统、非业务高峰期或配置问题导致没有流量的场景。 SKIPDATA：采集窗口中跳过了一些流日志记录，常见于高流量环境或突发性流量高峰，导致内部系统过载，从而无法采集流量并跳过记录的场景。 |
| traffic_path | 流量发生的场景： 0 - 除下述场景外，采集到的流量。 1 - 通过同一 VPC 中其他资源的流量。 2 - 访问同 VPC 内 ECS 实例的私网流量。 3 - 通过弹性网卡的流量。 4 - 通过高可用虚拟 IP（HaVip）的流量。 5 - 访问同地域阿里云云服务的流量。 6 - 通过网关终端节点访问云服务的流量。 7 - 通过 NAT 网关的流量。 8 - 通过转发路由器（TR）的流量。 9 - 通过 VPN 网关的流量。 10 - 通过边界路由器（VBR）访问专线的流量。 11 - 通过 CEN 基础版访问同地域 VPC 的流量。 12 - 除 11、18、19、20 所列出场景外通过 CEN 基础版的流量，如通过 CEN 基础版访问跨地域云服务、通过 CEN 基础版访问云连接网 CCN 等场景的流量。 13 - 通过 IPv4 网关访问公网的流量。 14 - 通过 IPv6 网关访问公网的流量。 15 - 通过公网 IP 访问公网的流量。 17 - 通过 VPC 对等连接的流量。 18 - 通过 CEN 基础版访问跨地域 VPC 的流量。 19 - 通过 CEN 基础版访问同地域 VBR 的流量。 20 - 通过 CEN 基础版访问跨地域 VBR 的流量。 21 - 通过专线网关（ECR）的流量。 22 - 通过网关型负载均衡终端节点的流量。 |
如下是流日志条目示例：
数据记录正常且允许记录流量示例
本示例阿里云主账号ID为1210123456**，VPC流日志版本为1，在2024年7月12日17:10:20至17:11:20（1分钟内），弹性网卡eni-bp166tg9uk1ryf**允许出方向以下流量：
源地址和端口（172.31.16.139，1332）通过TCP协议（6表示TCP协议）向目的地址和端口（172.31.16.21，80）传输了10个数据包，数据包总大小为2048字节。日志记录状态为OK，无异常。
{ "account-id": "1210123456**", "action": "ACCEPT", "bytes": "2048", "direction": "out", "dstaddr": "172.31.16.21", "dstport": "80", "end": "1720775480", "eni-id": "eni-bp166tg9uk1ryf**", "log-status": "OK", "packets": "10", "protocol": "6", "srcaddr": "172.31.16.139", "srcport": "1332", "start": "1720775420", "tcp-flags": "22", "traffic_path": "-", "version": "-", "vm-id": "1", "vpc-id": "-", "vswitch-id": "vpc-bp1qf0c43jb3maz******" }
数据记录正常且拒绝记录流量示例
本示例阿里云主账号ID为1210123456******，VPC流日志版本为1，在2024年7月15日10:20:00至10:30:00（10分钟内），弹性网卡eni-bp1ftp5sm9oszt******拒绝入方向以下流量：
源地址和端口（172.31.16.139，1332）通过TCP协议（6表示TCP协议）向目的地址和端口（172.31.16.21，80）传输了20个数据包，数据包总大小为4208字节。日志记录状态为OK，无异常。
{ "account-id": "1210123456******", "action": "REJECT", "bytes": "4208", "direction": "in", "dstaddr": "172.31.16.21", "dstport": "80", "end": "1721010600", "eni-id": "eni-bp1ftp5sm9oszt******", "log-status": "OK", "packets": "20", "protocol": "6", "srcaddr": "172.31.16.139", "srcport": "1332", "start": "1721010000", "tcp-flags": "22", "traffic_path": "-", "version": "-", "vm-id": "1", "vpc-id": "-", "vswitch-id": "vpc-bp1qf0c43jb3maz******" }
无数据记录状态示例
本示例阿里云主账号ID为1210123456******，VPC流日志版本为1，在2024年7月15日10:52:20至10:55:20（3分钟内），弹性网卡eni-bp1j7mmp34jlve******在此时间段内没有流量数据记录（NODATA）。
{ "account-id": "1210123456******", "action": "-", "bytes": "-", "direction": "-", "dstaddr": "-", "dstport": "-", "end": "1721012120", "eni-id": "eni-bp1j7mmp34jlve******", "log-status": "NODATA", "packets": "-", "protocol": "-", "srcaddr": "-", "srcport": "-", "start": "1721011940", "tcp-flags": "-", "traffic_path": "-", "version": "-", "vm-id": "1", "vpc-id": "-", "vswitch-id": "vpc-bp1qf0c43jb3maz******" }
跳过的数据记录状态示例
本示例阿里云主账号ID为1210123456******，VPC流日志版本为1，在2024年7月12日16:20:30至16:23:30（3分钟内），弹性网卡eni-bp1dfm4xnlpruv******的数据记录被跳过（SKIPDATA）。
{ "account-id": "1210123456******", "action": "-", "bytes": "-", "direction": "-", "dstaddr": "-", "dstport": "-", "end": "1720772610", "eni-id": "eni-bp1dfm4xnlpruv******", "log-status": "SKIPDATA", "packets": "-", "protocol": "-", "srcaddr": "-", "srcport": "-", "start": "1720772430", "tcp-flags": "-", "traffic_path": "-", "version": "-", "vm-id": "1", "vpc-id": "-", "vswitch-id": "vpc-bp1qf0c43jb3maz******" }
### 计费说明
计费项
流日志的计费项由流日志生成费、日志服务的服务费、流量分析器的流量处理费和流量分析存储费组成。
流日志生成费：
计费周期与出账周期均为1小时。账单出账时间通常在当前计费周期结束后3~4小时左右，具体以系统实际出账时间为准。
流日志生成费按照每月每地域生成的日志量实行阶梯累积计费。每个阿里云账号（主账号）在每个地域每月拥有5 GB免费额度。
| 流日志生成量阶梯（每月） | 定价（ 元/GB ） |
| --- | --- |
| 0 TB~10 TB（含） | 2.5 |
| 10 TB~30 TB（含） | 1.25 |
| 30 TB~50 TB（含） | 0.5 |
| 大于 50 TB | 0.25 |
日志服务的服务费：流日志投递到SLS之后产生，由SLS产品计费。收取[写入和存储等费用](../../sls/documents/billing-overview.md)。
SLS提供2种计费模式：“按写入数据量计费”和“按使用功能计费”。在VPC控制台创建流日志并选择新建Logstore时，默认使用“按使用功能计费”模式。
流量分析器计费：流日志投递到流量分析器之后产生，由NIS产品计费。收取[流量分析处理费和流量分析存储费](https://help.aliyun.com/zh/nis/product-overview/billing-method-new-version)。
计费示例
示例1
假设您于2022年09月01日00:00:00在某地域启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递3 GB日志。
由于每个阿里云账号（主账号）每月有5 GB流日志生成费的免费额度，则当月流日志的总费用=日志服务的服务费。
示例2
假设您于2022年09月01日00:00:00在华东2（上海）启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递100 GB日志。
当月流日志的生成费=(100－5)×2.5=237.5元，当月流日志的总费用=237.5元＋日志服务的服务费
示例3
假设您于2022年09月01日00:00:00在华北2（北京）启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递60 TB日志。
流日志的生成费按照阶梯定价计费：
0至10 TB（含）：(10×1024－5)×2.5=25587.5元
10 TB至30 TB（含）：20×1024×1.25=25600元
30 TB至50 TB（含）：20×1024×0.5=10240元
大于50 TB：10×1024×0.25=2560元
当月流日志生成费合计：25587.5+25600+10240+2560=63987.5元，当月流日志的总费用=63987.5元＋日志服务的服务费
欠费与充值
欠费和续费说明
欠费后如果在延停权益额度内，您的服务将不会受到停止影响，实例会继续运行。
阿里云提供[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。
欠费后如果超出了延停权益额度，服务将自动停止。实例停止后，不能对VPC流日志实例进行任何操作，计费也将停止。
在实例停止后7天内[充值](https://help.aliyun.com/zh/document_detail/37107.html)补足欠费后，服务会自动开启，可以继续使用。
如果实例停止7天仍未补足欠款，VPC流日志实例会被自动释放。实例被释放后相关配置和数据将被删除，不可恢复。
### 支持的地域
公有云支持的地域
| 区域 | 支持流日志的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 中国香港 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
金融云支持的地域
| 区域 | 支持流日志的地域 |
| --- | --- |
| 亚太 | 华北 2 金融云（邀测） 、 华南 1 金融云 、 华东 2 金融云 |
政务云支持的地域
| 区域 | 支持流日志的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_flowlog_inst_nums_per_user | 用户支持创建的流日志实例的数量 | 10 个 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
### 常见问题
VPC流日志可以保存多长时间？
VPC流日志生成后会被自动投递至日志服务中，遵循日志服务产品的保存策略。
创建VPC流日志时如果勾选了开启流日志分析报表功能，则用于存储VPC流日志的Logstore的数据保存时长默认为7天。未勾选时，默认为300天。
可在日志服务控制台[查看现有](../../sls/documents/manage-a-logstore.md)[Logstore](../../sls/documents/manage-a-logstore.md)[的数据保存时间](../../sls/documents/manage-a-logstore.md)，并按需修改。
等保（信息安全等级保护）要求网络日志，如何查询？
阿里云 VPC 默认不记录网络日志。若需满足等保要求，[开启](vpc-flow-logs.md)[VPC](vpc-flow-logs.md)[流日志功能](vpc-flow-logs.md)即可记录并分析出入弹性网卡的流量信息，实现安全合规监控。
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
