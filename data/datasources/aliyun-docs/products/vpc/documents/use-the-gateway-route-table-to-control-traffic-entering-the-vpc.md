# 使用网关路由表控制进入VPC的流量-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/use-the-gateway-route-table-to-control-traffic-entering-the-vpc

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 使用网关路由表控制进入VPC的流量

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以使用IPv4网关/IPv6网关结合网关路由表，将公网入方向流量转发至安全设备进行深度检测与过滤，防止恶意攻击和未经授权的访问，实现安全防护。本文以IPv4网关与网关路由表结合使用，控制进入VPC的流量为例。

## 场景示例

部分企业会在VPC内部署第三方安全设备（由独立厂商提供的网络安全硬件或软件解决方案，例如防火墙，入侵检测系统等），用于公网入方向的流量清洗。通过修改网关路由表的系统路由条目，将其与IPv4网关绑定，可以将公网入方向流量转发安全设备进行检测，控制进入VPC的流量。

## 前提条件

- 

已在华东2（上海）地域创建了一个专有网络VPC，并在其中配置了两台ECS实例，分别命名为ECS-A和ECS-B。

- 

已创建2个[自定义路由表](products/vpc/documents/network-traffic-management-using-custom-routing-tables.md)，分别与交换机1、交换机2绑定。

## 操作步骤

### 步骤一：创建IPv4网关并绑定网关路由表

- 

创建并激活IPv4网关

- 

登录[IPv4](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)[网关控制台](https://vpc.console.aliyun.com/ipv4/cn-hangzhou/ipv4s)，顶部菜单栏选择VPC所在地域，本文为华东2（上海）。

- 

单击创建IPv4网关，选择对应的VPC，并单击创建。在创建IPv4网关页面，根据需要选择资源组并配置标签，然后在专有网络下拉框中选择目标VPC。

- 

选择ECS-A所在交换机绑定的路由表，单击激活。

- 

激活时，系统会为您选择的交换机路由表添加一条0.0.0.0/0的默认路由指向IPv4网关，使得路由表关联的交换机具备公网访问能力。如果当前路由表已经存在目标网段为0.0.0.0/0的默认路由，则无法再添加IPv4网关的默认路由。

- 

在激活IPv4网关之前，VPC内的网络流量不会受到影响。但在激活过程中，可能会因流量路径切换导致短暂的网络中断。

在选择路由表区域，勾选需要关联的自定义路由表（建议选择自定义路由表而非主路由表），然后单击激活。

- 

完成IPv4网关激活与交换机路由表配置。

创建完成后，确认IPv4网关状态显示为可用，表示IPv4网关已成功激活并配置路由表。

- 

创建网关路由表

- 

登录[路由表控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)，顶部菜单栏选择IPv4网关所在地域，本文为华东2（上海）。

- 

单击创建路由表，选择对应的VPC，绑定对象类型选择边界网关，配置路由表名称并单击确定。

- 

绑定网关路由表

- 

在网关路由表详情页，绑定边界网关。

在弹出的对话框中选中状态为可绑定的目标IPv4网关，单击确定。

- 

绑定完成后，确认边界网关状态为可用。绑定完成后，在已绑定的边界网关页签下，边界网关的状态显示为可用，表示绑定成功。

### 步骤二：配置安全设备

重要

本方案将ECS-A模拟为安全设备，需要配置IP流量转发。如果您使用第三方安全设备，您需要按照自身业务实际情况联系第三方安全设备提供商协助部署。

本方案配置以Alibaba Cloud Linux 3.2104 64位操作系统为例。

登录ECS-A，执行以下命令配置IP流量转发。

永久启用# 永久启用IP转发（写入配置文件） echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf # 立即生效 sysctl -p

实例重启后失效# 临时启用IP转发（重启后失效） sysctl -w net.ipv4.ip_forward=1

### 步骤三：配置路由

- 

配置自定义路由表，路由出方向流量

- 

在路由表页面，找到ECS-B所在交换机绑定的自定义路由表，单击路由表ID。

- 

找到路由条目列表>自定义路由条目页签，单击添加路由条目，将目标网段设置为0.0.0.0/0，将下一跳类型设置为ECS实例，在ECS实例下拉框中选择ECS-A。

- 

配置网关路由表，路由入方向流量

- 

在路由表页面，找到已创建的网关路由表，单击路由表ID。

- 

找到路由条目列表>系统路由条目页签，可以查看到系统路由条目。系统默认添加以交换机网段为目标网段的系统路由。

- 

编辑目标网段指向交换机2的路由条目，将下一跳设置为ECS-A（安全设备）。单击系统路由条目对应的编辑操作，在编辑路由表条目弹窗中，将下一跳类型设置为ECS实例，在ECS实例下拉框中选择ECS-A。

- 

配置完成后，系统路由条目将转化为自定义路由条目。确认路由条目状态为可用。

在路由条目列表页面单击自定义路由条目页签，可查看到路由条目的目标网段（如10.0.1.0/24）及下一跳（ECS实例）等详细信息。

### 结果验证

注意检查[网络](products/vpc/documents/network-acl-overview.md)[ACL](products/vpc/documents/network-acl-overview.md)与[安全组概述](products/ecs/documents/user-guide/overview-44.md)的配置，避免VPC内的ECS测试连通性时受到影响。

验证公网入向流量访问

浏览器访问ECS-B公网IPhttp://<ECS-B 弹性公网IP>。

页面返回This is ECS–B!，表示请求已成功路由至 ECS-B 实例。

验证公网入向流量流经ECS-A

登录ECS-A，执行tcpdump dst host <ECS-B 私网IP>，抓取目的地为ECS-B的流量。

浏览器访问ECS-B公网IP，查看ECS-A抓包结果。

[root@ECS-A ~]# tcpdump dst host 10.0.1.221 dropped privs to tcpdump tcpdump: verbose output suppressed, use -v or -vv for full protocol decode listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes 17:33:36.662426 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [S], seq 884222365, w 17:33:36.662445 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [S], seq 884222365, w 17:33:36.662818 IP 140.2xxx.xxx.37526 > 10.0.1.221.http: Flags [S], seq 3020843667, 17:33:36.662823 IP 140.2xxx.xxx.37526 > 10.0.1.221.http: Flags [S], seq 3020843667, 17:33:36.676731 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [.], ack 1519927262, 17:33:36.676737 IP 140.2xxx.xxx.19404 > 10.0.1.221.http: Flags [.], ack 1, win 2058

## 更多操作

### 管控IPv6流量

IPv4网关是VPC边界上的公网IPv4流量控制组件。如果需要控制进入VPC的IPv6流量，您需要使用[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)[网关](https://help.aliyun.com/zh/ipv6-gateway/product-overview/what-is-an-ipv6-gateway/)，将其与网关路由表绑定，控制进入VPC的IPv6流量。

系统为开通了IPv6网段的VPC自动创建IPv6 网关，确保已为ECS的IPv6地址开通IPv6公网带宽，[实现](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[VPC](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[中的](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[ECS](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[与](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)[互联网互通](https://help.aliyun.com/zh/ipv6-gateway/getting-started/allow-an-ecs-instance-in-a-vpc-to-communicate-with-external-ipv6-clients-over-the-internet#section-hh0-5ut-dru)。

- 

创建网关路由表并与IPv6网关绑定。

- 

登录[路由表控制台](https://vpc.console.aliyun.com/vpc/cn-hangzhou/route-tables)，顶部菜单栏选择IPv6网关所在地域。

- 

单击创建路由表，选择对应的VPC，绑定对象类型选择边界网关，配置路由表名称并单击确定。

- 

在网关路由表详情页，单击已绑定的边界网关>绑定边界网关，选择IPv6网关并绑定。

- 

配置网关路由表，路由入方向流量。

- 

进入路由条目列表>系统路由条目页签，可以查看到系统路由条目。系统默认添加以交换机网段为目标网段的系统路由。

- 

编辑目标网段指向交换机2的IPv6路由条目，将下一跳设置为ECS-A（安全设备）。

### 调整公网入方向路由

您可以通过调整网关路由表的系统路由条目，调整公网入方向路由。

IPv4/IPv6路由的下一跳支持修改为ECS实例、弹性网卡、网关型负载均衡终端节点和路由目标组。

- 

网关路由表仅允许修改系统路由，不支持创建自定义路由条目。

- 

网关路由表编辑系统路由信息并成功保存后，将会转化为自定义路由条目；删除后可转化为系统路由条目。

- 

编辑网关路由表的系统路由条目时，下一跳类型的说明与建议如下：

- 

ECS实例/弹性网卡：交换机内部指定实例或网卡可被访问。常用于公网流量安全引流到特定ECS实例或弹性网卡。如果需要更换ECS实例或弹性网卡，需要先删除路由条目再重新编辑系统路由信息，无法直接替换。

- 

[网关型负载均衡终端节点](products/slb/documents/gateway-based-load-balancing-gwlb/getting-started/gwlb-quickly-implements-load-balancing-for-ipv4-services.md)：交换机内部指定终端节点可被访问。用于网关型负载均衡GWLB场景的第三方安全设备公网流量引流。

支持修改下一跳为网关型负载均衡终端节点的地域，请参见[网关型负载均衡](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)[GWLB](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)[支持的地域](products/slb/documents/gateway-based-load-balancing-gwlb/product-overview/regions-and-zones-supported-by-gwlb.md)。

- 

[路由目标组](products/vpc/documents/route-target-group.md)：支持通过主备模式配置两个下一跳实例，系统将自动检测实例的健康状态，当实例异常时，自动实现可用区级别的容灾切换，缩短故障恢复时间（RTO）。

### 解绑网关路由表

将网关路由表和IPv4/IPv6网关解除绑定，解绑后边界网关将不具备网关路由的能力。

- 

在路由表页面，找到目标网关路由表，单击路由表的ID。

- 

单击已绑定的边界网关页签，找到目标边界网关，在操作列单击解绑。

- 

在弹出的对话框中，单击确定。

### 删除网关路由表

如果网关路由表绑定了边界网关，您需要先解绑边界网关后再删除网关路由表。

- 

在路由表页面，找到目标网关路由表，然后在操作列单击删除。

- 

在删除路由表对话框，单击确定。

## 相关文档

- 

您可以查看[IPv4](products/vpc/documents/ipv4-gateway-overview.md)[网关](products/vpc/documents/ipv4-gateway-overview.md)，了解IPv4网关使用指引与相关限制。

- 

您可以通过调用以下API来管理网关路由表：

- 

[绑定网关路由表和网关](products/vpc/documents/developer-reference/api-vpc-2016-04-28-associateroutetablewithgateway.md)

- 

[解绑网关路由表和网关](products/vpc/documents/developer-reference/api-vpc-2016-04-28-dissociateroutetablefromgateway.md)

- 

[修改网关路由表的下一跳类型和下一跳](products/vpc/documents/developer-reference/api-vpc-2016-04-28-updategatewayroutetableentryattribute.md)

- 

[查询网关路由表列表信息](products/vpc/documents/developer-reference/api-vpc-2016-04-28-listgatewayroutetableentries.md)

[上一篇：路由表](products/vpc/documents/vpc-route-table.md)[下一篇：路由目标组](products/vpc/documents/route-target-group.md)

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
