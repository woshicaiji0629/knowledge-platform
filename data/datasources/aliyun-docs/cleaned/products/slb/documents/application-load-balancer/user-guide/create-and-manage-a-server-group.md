# 创建和管理服务器组-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/create-and-manage-a-server-group

# 创建和管理服务器组
ALB服务器组用于将客户端请求路由至一个或多个后端服务器。使用ALB时，用户需要创建服务器组并添加后端服务器来接收转发的请求。
## 配置选型
创建服务器组前，建议根据业务需求确定以下关键配置。服务器组类型创建后不可修改，请根据后端服务的实际部署方式选择。
### 选择服务器组类型
| 服务器组类型 | 支持的后端服务类型 | 说明 | 相关文档 |
| --- | --- | --- | --- |
| 服务器类型 | ECS、ENI、ECI 实例 | 后端服务器需与服务器组属于同一 VPC。 | [ALB](../getting-started/use-an-alb-instance-to-provide-ipv4-services.md) [快速实现](../getting-started/use-an-alb-instance-to-provide-ipv4-services.md) [IPv4](../getting-started/use-an-alb-instance-to-provide-ipv4-services.md) [服务的负载均衡](../getting-started/use-an-alb-instance-to-provide-ipv4-services.md) [ALB](../getting-started/implement-load-balancing-for-ipv6-services.md) [快速实现](../getting-started/implement-load-balancing-for-ipv6-services.md) [IPv6](../getting-started/implement-load-balancing-for-ipv6-services.md) [服务的负载均衡](../getting-started/implement-load-balancing-for-ipv6-services.md) |
| IP 类型 | IP 地址 | 开启远端 IP：当后端服务器不在服务器组所属 VPC 内时使用，例如其他 VPC 或本地 IDC 中的 IP 地址。支持 10.0.0.0/8、100.64.0.0/10、172.16.0.0/12、192.168.0.0/16 网段。 未开启远端 IP：仅支持当前服务器组所在 VPC 网段内的 IP 地址。 | [使用](../use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) [ALB](../use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) [挂载跨地域](../use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) [VPC](../use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) [内的服务器](../use-cases/specify-an-ecs-instance-in-a-vpc-as-a-backend-server-of-alb-in-a-different-region.md) [使用](../use-cases/specify-an-on-premises-server-as-a-backend-server-of-alb.md) [ALB](../use-cases/specify-an-on-premises-server-as-a-backend-server-of-alb.md) [挂载同地域](../use-cases/specify-an-on-premises-server-as-a-backend-server-of-alb.md) [IDC](../use-cases/specify-an-on-premises-server-as-a-backend-server-of-alb.md) [服务器](../use-cases/specify-an-on-premises-server-as-a-backend-server-of-alb.md) |
| 函数计算类型 | 函数计算 | 需开通函数计算服务，且与 ALB 实例属于同一地域。 | [ALB](../use-cases/specify-a-function-from-function-compute-as-a-backend-server-of-alb.md) [添加函数计算](../use-cases/specify-a-function-from-function-compute-as-a-backend-server-of-alb.md) [FC](../use-cases/specify-a-function-from-function-compute-as-a-backend-server-of-alb.md) [作为后端服务](../use-cases/specify-a-function-from-function-compute-as-a-backend-server-of-alb.md) |
重要
ALB实例的后端服务器被释放或私有IP地址被修改后，ALB不会联动更新后端服务器。建议在释放后端服务器或修改其私有IP地址时，先在ALB服务器组中移除该后端服务器，确保不影响业务。
### 选择后端协议与调度算法
| 后端协议 | 适用场景 |
| --- | --- |
| HTTP（默认） | 大多数 Web 应用场景。适用于 HTTP、HTTPS 和 QUIC 监听。 |
| HTTPS | ALB 到后端服务器之间需要加密通信。适用于 HTTPS 和 HTTP 监听。 |
| gRPC | 后端服务使用 gRPC 协议。需搭配 HTTPS 监听且启用 HTTP2.0。 |
| 调度算法 | 适用场景 |
| --- | --- |
| 加权轮询 | 通用场景。按权重比例均匀分配请求。轮询调度以每次请求为粒度进行分配，而非基于用户。 |
| 加权最小连接数 | 长连接或请求处理时间差异较大的场景。综合权重和实时连接数，优先分配给负载较低的服务器。 |
| 一致性哈希 | 需要请求亲和性的场景（如缓存命中优化）。根据源 IP 或 URL 参数将相同特征的请求固定到同一后端。 |
详细算法逻辑参见[负载均衡调度算法介绍](../../product-overview/introduction-to-load-balancing-scheduling-algorithm.md)。
各监听协议与后端协议、健康检查协议的完整适配关系如下：
| 监听协议 | 支持的后端协议 | 支持的服务器组类型 | 支持的健康检查协议 |
| --- | --- | --- | --- |
| HTTP | HTTP、HTTPS | 服务器类型、IP 类型、函数计算类型 函数计算类型服务器组无需配置后端协议和健康检查协议。 | HTTP、HTTPS、TCP、gRPC 基础版 ALB 实例不支持 HTTPS 健康检查协议。 |
| HTTPS | HTTP、HTTPS、gRPC gRPC 需搭配 HTTPS 监听且启用 HTTP2.0。 基础版 ALB 实例的 HTTPS 监听仅支持 HTTP 和 gRPC 后端协议。 |  |  |
| QUIC | HTTP |  |  |
## 创建/删除服务器组
### 创建服务器组
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。
在顶部菜单栏选择目标地域后，单击创建服务器组。完成以下配置，然后单击创建。
服务器组类型：根据后端服务的部署方式选择。
服务器类型：以ECS、ENI、ECI实例作为后端服务器，需与服务器组属于同一VPC。
IP类型：以IP地址作为后端服务器。支持VPC内IP地址；开启远端IP后，还可添加其他VPC或本地IDC中的IP地址。
函数计算类型：以函数计算作为后端服务，需开通函数计算服务且与ALB实例属于同一地域。
服务器组名称：输入服务器组的自定义名称。
VPC：服务器组所属的VPC。仅该VPC内的后端服务器可以加入此服务器组。
IP类型服务器组开启远端IP时，后端服务器不限于该VPC内，但须从该VPC网络可达。函数计算类型的服务器组无需配置该参数。
选择后端协议：选择ALB与后端服务器之间的通信协议。
HTTP（默认）：适用于HTTP、HTTPS和QUIC监听。ALB与后端服务器之间使用HTTP通信。
HTTPS：适用于HTTPS和HTTP监听。ALB与后端服务器之间使用HTTPS加密通信。
gRPC：适用于HTTPS监听。ALB与后端服务器之间使用gRPC协议通信。
基础版ALB实例的HTTPS监听仅支持HTTP和gRPC后端协议。函数计算类型的服务器组无需配置该参数。
选择调度算法：选择请求分配策略。
加权轮询：按权重比例分配请求，权重越高的后端服务器分配到的请求越多。
加权最小连接数：综合权重和实时连接数分配请求。权重相同时，当前连接数越少的后端服务器优先分配。
一致性哈希：根据哈希因子将相同特征的请求调度到相同的后端服务器。
选择哈希因子：
源IP：按客户端源IP地址哈希。
URL参数：按指定的URL参数值哈希。需输入指定URL参数。
指定URL参数填写请求URL中的查询参数名称（Query Parameter Name），例如userid、sessionid等。ALB将根据该参数的值进行哈希计算，将相同参数值的请求调度到同一台后端服务器。
例如，指定URL参数填写userid后，URL中包含?userid=123的请求将始终调度到同一台后端服务器。该方式适用于需要会话保持的场景，例如购物车会话绑定或缓存命中率优化。
建议服务器组中添加2台及以上后端服务器，以充分发挥哈希分发的效果。
函数计算类型的服务器组无需配置该参数。
标签及资源组：可选。用于对服务器组进行分类管理。
标签键和标签值：以键值对形式标记服务器组。
选择资源组：服务器组归属的资源组，默认为默认资源组。
后端长连接：默认开启。开启后，ALB与后端服务器之间维持TCP长连接，新请求优先复用已有连接，避免重复建连，降低延迟并减轻后端服务器压力。
函数计算类型的服务器组无需配置该参数。
健康检查：默认开启。用于检测后端服务器的可用性。
函数计算类型的服务器组默认关闭健康检查。开启后，健康检查探测次数将计为函数计算的请求并产生[费用](../../../../fc/documents/product-overview/billing-overview-of-fc.md)。
健康检查配置：单击右侧编辑展开配置，参数说明请参见[ALB](alb-health-check.md)[健康检查](alb-health-check.md)。
选择并加载健康检查：选择一个已有的健康检查并加载配置。
用户可以创建健康检查，不与服务器组及监听关联，方便下次复用。一个服务器组只支持配置一个健康检查。
### 删除服务器组
仅支持删除未被监听转发规则关联的服务器组。删除不影响后端服务器。
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列选择>删除并确定。
### API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)创建服务器组。
调用[DeleteServerGroup](../developer-reference/api-alb-2020-06-16-deleteservergroup.md)删除指定服务器组。
## 添加/移除后端服务器
添加后端服务器前，请确保服务器上已部署业务应用。
重要
ALB通过特定IP地址与后端服务器通信和健康检查，请确保后端服务器未屏蔽这些地址（包括iptables或安全策略软件）：
[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)使用所在交换机网段的私网地址（Local IP）通信，可在实例详情页查看。
升级前的ALB实例使用内网地址段100.64.0.0/10与后端服务器通信。
请确保后端服务器的配置不会导致转发路径形成[环路](../support/alb-exception-status-code-description.md)。
### 添加后端服务器
### 服务器类型
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑后端服务器。
在后端服务器页签，单击添加后端服务器。在添加后端服务器面板，完成服务器的添加，单击下一步。
添加云服务器ECS
选择服务器类型为云服务器ECS/弹性网卡ENI，勾选目标ECS。
如果没有可用的ECS，可以在服务器列表右上方单击购买云服务器。
添加弹性网卡ENI
选择服务器类型为云服务器ECS/弹性网卡ENI，打开高级模式开关。
单击目标ECS实例ID左侧的图标，勾选目标ENI。
如需添加弹性网卡ENI，请确保目标ENI已绑定至ECS，参考[绑定辅助弹性网卡](../../../../ecs/documents/user-guide/bind-an-eni.md)。
添加弹性容器实例ECI
选择服务器类型为弹性容器实例ECI，勾选目标ECI。
如果没有可用的ECI，可以在服务器列表右上方单击购买弹性容器实例。
在配置端口和权重配置向导页面，设置所添加服务器的端口和权重，然后单击确定。
端口：后端服务器实际提供服务的端口。
权重：按权重比例分配流量。取值范围0~100，默认100。
例如：服务器组中有三台服务器，其权重分别设置为100、50和50。请求将按照比例2:1:1进行分发，即这三台服务器分别接收到的请求占比为50%、25%和25%。
说明
开启会话保持时，可能导致后端服务器的请求分配不均匀。
权重设为0时，该服务器不再接受新请求。
健康检查异常的服务器不参与流量分配，请求按剩余正常服务器的权重比例分配。
若所有服务器均异常，ALB仍会按权重尝试分配流量，以最大可能避免业务中断。
批量操作：
勾选服务器后，可在底部使用设置相同端口、设置相同权重或批量移除。
鼠标悬浮至端口或权重输入框右侧，可选择向下复制、向上复制或全部复制，将当前值快速复制到其他服务器。
单击列表头端口或权重右侧的重置，可清除所有服务器的端口或将权重恢复为默认值。
### 函数计算类型
支持FC 2.0和FC 3.0。ALB与函数计算之间通过阿里云内部网络安全通信。
使用前需先开通函数计算服务。2024年8月27日之后注册并完成实名认证的阿里云账号无需开通，可直接使用。
使用限制
[ALB](../product-overview/supported-regions-and-zones.md)[挂载函数计算支持的地域](../product-overview/supported-regions-and-zones.md)。
ALB实例和函数须属于同一地域。
一个函数计算类型服务器组仅支持添加一个函数。
函数计算2.0请求处理程序类型为处理事件请求时，需配置HTTP触发器才能关联ALB。
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑后端服务器。
在后端服务器页签，单击设置函数计算。在添加后端服务器面板，选择以下任意方式完成配置，然后单击确定。
通过选择资源
函数名称：选择已创建的函数。如果没有可用的函数，可创建新的函数，参考[新建函数](../../../../fc/documents/user-guide/function-instance-1.md)。
版本或别名：选择指定版本或指定别名。新创建的函数默认只有一个LATEST版本。
通过ARN配置
ARN：输入目标函数的ARN。可在函数计算控制台的函数详情页面[获取函数](../../../../fc/documents/user-guide/creating-an-event-function.md)[ARN](../../../../fc/documents/user-guide/creating-an-event-function.md)。
### IP类型
未开启远端IP时，仅支持添加当前VPC网段内的IP地址；开启远端IP后，还可添加其他VPC或本地IDC中的IP地址。
说明
自北京时间2025年2月25日00:00:00起，对于新建实例默认使用升级后的ALB，已创建的ALB实例不受影响（提交自助申请创建的实例除外）。具体可参考[应用型负载均衡](../../product-overview/alb.md)[ALB](../../product-overview/alb.md)[实例升级公告](../../product-overview/alb.md)。
使用限制
警告
升级前的ALB实例不支持通过IP类型服务器组挂载同一个VPC内的ALB、NLB或CLB实例。如果需要挂载同VPC下的该类资源，请确保使用ALB升级实例，否则可能会导致服务异常。
升级后
后端服务器限制
只支持挂载私网IP地址，不支持挂载公网IP地址。
IP协议版本为IPv4/v6双栈时，仅支持添加当前服务器组所在VPC网段内的IPv6地址，不支持启用远端IP。
ALB与后端服务器间的转发配置限制
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在指定的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。详情请参见[转发路由器工作原理](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
升级前
后端服务器限制
[升级前](../product-overview/supported-regions-and-zones.md)[ALB](../product-overview/supported-regions-and-zones.md)[实例挂载远端](../product-overview/supported-regions-and-zones.md)[IP](../product-overview/supported-regions-and-zones.md)[支持的地域](../product-overview/supported-regions-and-zones.md)。
跨地域挂载的后端服务器仅支持IP类型。
只支持挂载私网IP地址，不支持挂载公网IP地址。
不支持挂载同一个VPC内的ALB、NLB或CLB实例。
ALB与后端服务器间的转发配置限制
支持通过企业版转发路由器或高速通道实现远端IP转发，不支持基础版转发路由器。
如果使用企业版转发路由器，请注意：企业版转发路由器会在用户指定的可用区的交换机实例上创建弹性网卡ENI（Elastic Network Interface），作为VPC实例向企业版转发路由器发送流量的入口。创建VPC实例时，请确保在企业版转发路由器支持的可用区中创建至少一个交换机实例，以便将VPC实例连接至企业版转发路由器。更多信息，请参见[企业版转发路由器支持的地域和可用区](../../../../cen/documents/product-overview/how-transit-routers-work.md)。
一张云企业网中，一个地域只能有一个VPC内的一个或多个ALB实现跨地域挂载服务器。
无法实现同一个地域多个VPC内的ALB使用同一个转发路由器访问后端服务。
无法实现同一个地域多个VPC内的ALB使用多个转发路由器访问同一个后端服务。
ALB与后端服务器的流量仅支持通过系统路由表转发，暂不支持通过VPC自定义路由表转发。
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑后端服务器。
在后端服务器页签，单击添加IP。在添加后端服务器面板，输入后端服务器的IP地址，然后单击下一步。
开启远端IP时，支持输入以下私网网段的IP地址：10.0.0.0/8、100.64.0.0/10、172.16.0.0/12、192.168.0.0/16。
未开启远端IP时，仅支持当前VPC网段内的IP地址。
如需添加多个后端服务器，可单击添加IP地址。
在配置端口和权重配置向导页面，设置端口和权重，然后单击确定。
端口：后端服务器实际提供服务的端口。
权重：按权重比例分配流量。取值范围0~100，默认100。
例如：服务器组中有三台服务器，其权重分别设置为100、50和50。请求将按照比例2:1:1进行分发，即这三台服务器分别接收到的请求占比为50%、25%和25%。
说明
开启会话保持时，可能导致后端服务器的请求分配不均匀。
权重设为0时，该服务器不再接受新请求。
健康检查异常的服务器不参与流量分配，请求按剩余正常服务器的权重比例分配。
若所有服务器均异常，ALB仍会按权重尝试分配流量，以最大可能避免业务中断。
批量操作：
勾选服务器后，可在底部使用设置相同端口、设置相同权重或批量移除。
鼠标悬浮至端口或权重输入框右侧，可选择向下复制、向上复制或全部复制，将当前值快速复制到其他服务器。
单击列表头端口或权重右侧的重置，可清除所有服务器的端口或将权重恢复为默认值。
### 移除后端服务器
移除后，该服务器将不再处理转发请求。
警告
直接移除可能造成业务中断，建议先将权重设置为0再移除。
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑后端服务器。
在后端服务器页签下，找到目标后端服务器，在操作列单击移除并确定。
### API
调用[AddServersToServerGroup](../developer-reference/api-alb-2020-06-16-addserverstoservergroup.md)向服务器组添加后端服务器。
调用[RemoveServersFromServerGroup](../developer-reference/api-alb-2020-06-16-removeserversfromservergroup.md)移除服务器组中的后端服务器。
## 会话保持
当同一客户端的多次请求需要由同一台后端服务器处理时（如购物车、登录态保持等场景），可以开启会话保持。
会话保持：默认关闭。开启后，ALB将来自同一客户端的请求分发到同一台后端服务器。
函数计算类型的服务器组无需配置该参数。仅服务器类型和IP类型的服务器组支持。关闭跨AZ负载均衡时，不支持开启会话保持。
## 控制台
在创建或编辑服务器组时，开启会话保持，选择Cookie处理方式：
Cookie处理方式：
植入Cookie：ALB自动生成Cookie（SERVERID）并植入响应，后续携带该Cookie的请求将转发至同一后端服务器。会话保持超时时间取值范围1~86400秒。
重写Cookie：ALB重写用户自定义的Cookie值。需输入Cookie名称。
## API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)或[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)时，通过StickySessionConfig配置会话保持。
更多信息，请参见[配置会话保持](configure-session-persistence-1.md)。
## 后端服务器平滑上下线
### 慢启动
新添加的后端服务器可能因缓存未预热、连接池未建立等原因无法立即承受正常流量。开启慢启动后，ALB会在指定时间内逐步增加分配给新服务器的请求量，避免突增流量对未就绪服务器造成压力。
仅当调度算法为加权轮询时支持。仅标准版和WAF增强版的ALB实例支持，基础版ALB实例不支持。函数计算类型的服务器组无需配置该参数。
### 控制台
在创建或编辑服务器组时，开启慢启动，设置慢启动持续时间（取值范围30~900秒，默认30秒），到期后恢复正常分配。
### API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)或[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)时，通过SlowStartConfig配置慢启动。
说明
慢启动运行机制：
服务器组内健康检查正常的已有后端服务器不会自动进入慢启动模式。为空的服务器组首次添加的后端服务器也不会进入慢启动模式；仅当至少有一个健康检查正常的后端服务器未处于慢启动状态时，新添加的后端服务器才会进入慢启动模式。
删除处于慢启动模式的后端服务器，该服务器退出慢启动模式。再次添加同一后端时，健康检查正常后重新进入慢启动模式。
处于慢启动模式的后端服务器健康检查异常时退出慢启动模式，健康检查恢复正常后重新进入慢启动模式。
健康检查开启时，后端服务器健康检查正常后慢启动生效；健康检查关闭时，慢启动立即生效。
更多信息，请参见[配置慢启动](smooth-business-start-through-alb-slow-start.md)。
### 连接优雅中断
当后端服务器被移除或健康检查异常时，默认情况下现有连接仅在客户端主动断开或会话到期时才中断。开启连接优雅中断后，现有连接可在超时时间内继续完成传输，到期后主动断开，保障业务平稳下线。
仅标准版和WAF增强版的ALB实例支持，基础版ALB实例不支持。函数计算类型的服务器组无需配置该参数。
### 控制台
在创建或编辑服务器组时，开启连接优雅中断，设置连接优雅中断超时时间（取值范围0~900秒，0表示立即中断，默认300秒）。
### API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)或[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)时，通过ConnectionDrainConfig配置连接优雅中断。
更多信息，请参见[配置连接优雅中断](smooth-transition-of-alb-request-by-connection-graceful-interrupt.md)。
## 降低跨可用区时延
默认情况下，ALB在同地域跨可用区的后端服务器之间分配流量。当用户的业务对延迟敏感且各可用区内的后端服务器资源充足时，可以关闭跨AZ负载均衡，使流量仅在同可用区内的后端服务器之间分配，降低跨区网络时延。
仅标准版、WAF增强版ALB实例支持关闭，基础版ALB不支持。开启远端IP的IP类型服务器组，不支持关闭跨AZ负载均衡。关闭跨AZ负载均衡时，不支持开启会话保持。函数计算类型的服务器组无需配置该参数。
## 控制台
在创建或编辑服务器组时，关闭跨AZ负载均衡。
## API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)或[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)时，将CrossZoneEnabled设为false关闭跨可用区负载均衡（默认为true）。
更多信息，请参见[关闭跨](disable-cross-zone-forwarding-to-reduce-request-latency.md)[AZ](disable-cross-zone-forwarding-to-reduce-request-latency.md)[负载均衡](disable-cross-zone-forwarding-to-reduce-request-latency.md)。
## 添加IPv6后端服务器
当用户需要在服务器组中挂载IPv6类型的后端服务器时，可以将IP协议版本设置为IPv4/v6双栈。
仅服务器类型和IP类型的服务器组支持。
需要服务器组所属VPC已[开启](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)[功能](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#task-2198980)。
IP协议版本为IPv4/v6双栈的服务器组，仅支持添加至双栈ALB实例的监听转发规则中。
IP类型服务器组还要求ALB实例为[升级实例](../../product-overview/alb.md)，且仅支持当前VPC网段内的IPv6地址，不支持启用远端IP。
## 控制台
在创建服务器组时，将IP协议版本设置为IPv4/v6双栈。
## API
调用[CreateServerGroup](../developer-reference/api-alb-2020-06-16-createservergroup.md)时，将Ipv6Enabled设为true，即IP协议版本为IPv4/v6双栈。
## 编辑健康检查
修改服务器组的健康检查配置。
警告
关闭健康检查后，ALB无法检测后端服务器故障，流量不会自动切换至正常服务器。
延长健康检查间隔会增加ALB发现故障服务器的时间。
## 控制台
前往ALB控制台的[服务器组](https://slb.console.aliyun.com/alb/cn-hangzhou/server-groups)页面。找到目标服务器组，在操作列单击编辑健康检查。
在弹出的编辑健康检查对话框中，根据需要开启或关闭健康检查。开启时，单击健康检查配置右侧的编辑修改参数。
## API
调用[UpdateServerGroupAttribute](../developer-reference/api-alb-2020-06-16-updateservergroupattribute.md)更新服务器组的健康检查配置。
## 计费说明
服务器组本身不产生费用，但[ALB](../product-overview/alb-billing-rules.md)[实例](../product-overview/alb-billing-rules.md)和添加到服务器组中的后端服务器会按各自产品的计费规则收费。
## 配额
| 配额名称 | 描述 | 默认值 | 最大支持提升至 | 是否支持申请 |
| --- | --- | --- | --- | --- |
| alb_quota_loadbalancer_servers_num_basic_edition | 一个基础版 ALB 实例可添加的后端服务器数 | 200 个 | 400 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_servers_num_basic_edition) |
| alb_quota_loadbalancer_servers_num_standard_edition | 一个标准版 ALB 实例可添加的后端服务器数 | 1000 个 | 1500 个 |  |
| alb_quota_loadbalancer_servers_num_standardwithwaf_edition | 一个 WAF 增强版 ALB 实例可添加的后端服务器数 | 1000 个 | 1500 个 |  |
| alb_quota_server_added_num | 同一个后端服务器（IP）可被添加到 ALB 服务器组的次数 | 200 次 | 300 次 |  |
| alb_quota_servergroup_attached_num | 同一个服务器组可被关联 ALB 监听转发规则的次数 | 50 次 | 100 次 |  |
| alb_quota_server_groups_weight | 转发规则转发至服务器组时，单个服务器组可配置的权重上限 | 100 | 10000 | 联系商务经理 |
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
