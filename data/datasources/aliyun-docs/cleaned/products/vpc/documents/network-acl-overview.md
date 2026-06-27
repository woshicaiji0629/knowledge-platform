# 网络ACL-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/network-acl-overview

# 网络ACL
您可以创建网络ACL并将其与交换机绑定，通过配置网络ACL规则，精确控制出入交换机的流量。
## 工作原理
### 作用范围
网络ACL仅对绑定交换机内的弹性网卡生效。
网络ACL会控制依赖弹性网卡实现网络通信的云资源的流量，例如ECS、ECI、NLB等实例。
由于RDS、CLB等实例不依赖弹性网卡，流量不会被网络ACL控制。RDS实例的访问控制由其[白名单](../../rds/documents/apsaradb-rds-for-mysql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mysql-instance.md)实现，CLB实例通过[访问控制策略](../../slb/documents/classic-load-balancer/user-guide/access-control.md)实现。网络ACL不会控制绑定了[网卡可见模式](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)[EIP](../../eip/documents/associate-an-eip-with-a-secondary-eni-1.md)的辅助弹性网卡的流量。
通过私网连接PrivateLink的方式访问云服务时，流量经过终端节点网卡，会受网络ACL规则管控。
### 规则生效机制
每条规则有生效顺序，系统将从生效顺序为1的规则开始，根据IP版本、协议类型、源/目的地址及端口范围，依次判断流量是否匹配。流量匹配到首条规则后，执行指定的允许/拒绝策略。
针对入方向规则和出方向规则，端口范围始终匹配流量的目的端口。入方向规则仅支持配置源地址，出方向规则仅支持配置目的地址。单条规则不支持同时配置源地址和目的地址。网络ACL在拒绝流量时采用drop操作，发起端不会收到任何响应，表现为请求超时或者无法建立连接。
网络ACL规则是无状态的。当配置入方向规则来允许特定流量进入交换机时，响应流量不会被自动允许，您必须创建允许响应流量返回客户端临时端口的出方向规则。当客户端向服务器发起请求时，会从临时端口范围中随机选择一个端口，接收服务器的响应。
为了保证各种类型的客户端都能正常访问您的服务，您可以设置1024-65535的临时端口范围。
不同类型的客户端的临时端口范围
| 客户端 | 临时端口范围 |
| --- | --- |
| Linux | 32768/61000 |
| Windows Server 2003 | 1025/5000 |
| Windows Server 2008 及更高版本 | 49152/65535 |
| NAT 网关 | 1024/65535 |
示例配置中，存在两条源/目的地址范围有重叠的自定义规则。当IP为192.168.0.1的客户端通过HTTPS协议访问子网内的服务时，流量会首先匹配到生效顺序为1的规则，因此被拒绝；而当IP为192.168.1.1的客户端访问时，流量按顺序匹配到生效顺序为2的规则，因此被允许，且响应流量按照生效顺序为1的出方向规则发送回客户端的临时端口。
当服务需开放大量端口，但部分端口需要拒绝访问时，您需要确保拒绝规则的优先级高于允许规则。
### 与安全组的区别
| 对比项 | 网络 ACL | 安全组 |
| --- | --- | --- |
| 作用范围 | 根据网络 ACL 规则控制出入交换机的流量。 | ECS 实例级别的访问控制方式。ECS 实例关联的多个安全组的规则将按固定的策略排序，共同决定是否放行实例出入站的流量。 |
| 返回数据流状态 | 无状态：返回数据流必须被规则明确允许。 | 有状态：返回数据流会被自动允许，不受任何规则的影响。 |
| 规则匹配顺序 | 按照规则生效顺序，依次判断流量是否匹配。 | 先按照优先级排序：优先级相同时，授权策略为拒绝的规则排在授权策略为允许的规则之前。 排序完成后，依次匹配已排序好的规则。 |
| 与 ECS 实例的关联关系 | 每个交换机仅允许绑定一个网络 ACL。 | 一个 ECS 实例可加入多个安全组。 |
| 规则地址配置 | 入方向规则仅支持配置源地址，出方向规则仅支持配置目的地址。单条规则不支持同时配置源地址和目的地址。 | 入方向规则配置授权对象（源地址），出方向规则配置授权对象（目的地址）。 |
## 创建/删除网络ACL
您可以创建网络ACL，并将其与交换机关联，来控制出入交换机的流量。
当您为仅有IPv4网段的VPC创建网络ACL时，系统默认在入方向和出方向添加以下规则：
云服务规则：允许使用阿里云的私网域名解析服务与ECS元数据服务。优先级固定最高，无法修改和删除。
1、阿里云默认DNS服务器IP为100.100.2.136、100.100.2.138，用于解析内网域名。2、MetaServer的IP为100.100.100.200，提供了ECS实例必需的元数据服务，确保实例正常运行。
自定义规则：允许所有IPv4流量，以确保创建网络ACL后不会影响同一VPC内不同交换机之间的私网互通。您可以配置自定义规则，精确控制进出交换机的流量。
系统规则：用于拒绝未匹配其他规则的IPv4流量。优先级固定最低，无法修改和删除。
如果ACL所属的VPC开启了IPv6，入方向和出方向将再添加允许所有IPv6流量的自定义规则、拒绝所有IPv6流量的系统规则。
网络ACL仅允许绑定所属VPC内的交换机，每个交换机仅允许绑定一个网络ACL。
### 控制台
创建网络ACL
前往[专有网络控制台-网络](https://vpc.console.aliyun.com/nacl/cn-hangzhou/nacls)[ACL](https://vpc.console.aliyun.com/nacl/cn-hangzhou/nacls)，在页面上方选择目标地域后，单击创建网络ACL。
配置所属专有网络，需选择计划与网络ACL关联的交换机所属的VPC。
关联交换机
单击实例ID或操作列的管理，进入已绑定资源页签，单击关联交换机，选择一个或多个目标交换机并确定关联。关联的交换机将按照网络ACL规则控制出入交换机的流量。如需解除控制，您可以在该页签下，单击目标交换机操作列的解绑。
您也可以在目标交换机详情页的网络ACL参数项，绑定、更换或解绑网络ACL。
删除网络ACL
需先确保已解除与交换机的关联。在目标网络ACL的操作列，单击删除。
### API
调用[CreateNetworkAcl](developer-reference/api-vpc-2016-04-28-createnetworkacl.md)创建网络ACL。
调用[AssociateNetworkAcl](developer-reference/api-vpc-2016-04-28-associatenetworkacl.md)绑定网络ACL与交换机。
调用[UnassociateNetworkAcl](developer-reference/api-vpc-2016-04-28-unassociatenetworkacl.md)解除网络ACL与交换机的绑定。
调用[DeleteNetworkAcl](developer-reference/api-vpc-2016-04-28-deletenetworkacl.md)删除网络ACL。
### Terraform
与控制台逻辑不同，Terraform仅支持将网络ACL与一个交换机关联。Resources：[alicloud_network_acl](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/network_acl)# 指定网络ACL的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定VPC ID variable "vpc_id" { default = "vpc-bp1k******" # 修改为VPC的实际ID } # 指定交换机ID variable "vswitch_id" { default = "vsw-bp1y******" # 修改为交换机的实际ID } # 创建网络ACL并关联交换机 resource "alicloud_network_acl" "example_network_acl" { vpc_id = var.vpc_id # 指定网络ACL所属VPC network_acl_name = "example_network_acl_name" resources { resource_id = var.vswitch_id # 指定网络ACL关联的交换机 resource_type = "VSwitch" } }
## 配置网络ACL规则
创建网络ACL后，系统将默认添加允许/拒绝所有流量的网络ACL规则。
您可以配置自定义规则，精确控制特定流量进出交换机。基于协议类型、IP版本、源地址/目的地址、端口范围匹配到网络ACL规则后，系统将对流量执行指定策略，允许/拒绝对应的流量。
协议类型为TCP(6)/UDP(17)时，可以调整端口范围。取值范围为0~65535，设置格式为起始端口/终止端口，但不能设置为-1/-1（表示不限制端口）。选择其他协议类型时，端口范围无法设置，默认为-1/-1。
仅网络 ACL 所属 VPC 开启 IPv6 时，您可以添加 IPv6 类型的出入方向规则。
添加/修改/删除网络ACL规则后，会自动应用到与网络ACL绑定的交换机。
您可以将常用 IP 地址段统一管理在[前缀列表](vpc-prefix-lists.md)中，在网络 ACL 规则中引用。修改前缀列表后，网络 ACL 规则会自动同步更新。
前缀列表的最大条目数（而非实际包含的条目数），会占用网络 ACL 规则的配额。您可尝试通过调低最大条目数、合并相邻IP段、清理无用条目等方式来降低配额超限风险。
前缀列表是地域级资源，仅限创建地域内使用，不可跨地域引用或共享。一个前缀列表不能同时包含 IPv4 和 IPv6 CIDR地址块。
常用端口列表
| 端口 | 服务 | 说明 |
| --- | --- | --- |
| 21 | FTP | FTP 服务所开放的端口，用于上传、下载文件。 |
| 22 | SSH | SSH 端口，用于通过命令行模式或远程连接软件（例如 PuTTY、Xshell、SecureCRT 等）连接 Linux 实例。 |
| 23 | Telnet | Telnet 端口，用于 Telnet 远程登录 ECS 实例。 |
| 25 | SMTP | SMTP 服务所开放的端口，用于发送邮件。 |
| 53 | DNS | 用于域名解析服务器（Domain Name Server，简称 DNS）协议。 |
| 80 | HTTP | 用于 HTTP 服务提供访问功能，例如，IIS、Apache、Nginx 等服务。 |
| 110 | POP3 | 用于 POP3 协议，POP3 是电子邮件接收的协议。 |
| 143 | IMAP | 用于 IMAP（Internet Message Access Protocol）协议，IMAP 是用于接收电子邮件的协议。 |
| 443 | HTTPS | 用于 HTTPS 服务提供访问功能。HTTPS 是一种能提供加密和通过安全端口传输的协议。 |
| 1433 | SQL Server | SQL Server 的 TCP 端口，用于供 SQL Server 对外提供服务。 |
| 1434 | SQL Server | SQL Server 的 UDP 端口，用于获取 SQL Server 使用的 TCP/IP 端口号和 IP 地址等信息。 |
| 1521 | Oracle | Oracle 通信端口，ECS 实例上部署了 Oracle SQL 需要放行的端口。 |
| 3306 | MySQL | MySQL 数据库对外提供服务的端口。 |
| 3389 | Windows Server Remote Desktop Services | Windows Server Remote Desktop Services（远程桌面服务）端口，可以通过这个端口使用软件连接 Windows 实例。 |
| 8080 | 代理端口 | 与 80 端口类似，8080 端口通常用于提供 WWW 代理服务，用于实现网页浏览。如果您使用了 8080 端口，当访问网站或使用代理服务器时，需要在 IP 地址后面加上冒号和 8080（例如： IP 地址:8080 ）。在安装 Apache Tomcat 服务后，默认的服务端口为 8080。 |
| 137、138、139 | NetBIOS 协议 | NetBIOS 协议常被用于 Windows 文件、打印机共享和 Samba。 UDP 端口 137 和 138 通常用于网上邻居传输文件时的通信。 通过端口 139，连接试图获取 NetBIOS/SMB 服务。 |
1、配置[DHCP](dhcp-option-set-and-dns-hostname.md)[选项集](dhcp-option-set-and-dns-hostname.md)后，您需要添加放行指定DNS服务器的出入方向规则。未添加规则，可能会造成域名解析异常。2、使用负载均衡时，您需要在出入方向规则中添加允许监听端口接收到的请求转发至后端服务器、健康检查端口的请求发送至后端服务器的规则。
### 控制台
在目标网络ACL的入方向规则/出方向规则页签，您可参考以下步骤，来配置自定义规则。
由于网络ACL规则是无状态的，当您设置入方向规则来允许特定流量进入交换机时，需要设置相应的出方向规则。
添加规则
手动配置：在目标网络ACL的入方向规则/出方向规则页签，单击管理入方向规则/管理出方向规则。
单击添加IPv4规则/添加IPv6规则，逐条配置。
如果您需要对多个IP地址段进行统一的访问控制，您可以选择快速添加规则，通过优先级来设置插入规则的位置。
将常用 IP 地址段统一管理在前缀列表后，可单击添加IPv4规则/添加IPv6规则，选择IP版本为VPC前缀列表，配置源地址/目的地址为前缀列表。
批量导入：如需批量添加不同策略的规则，您可以使用提供的模板，批量导入规则。
模板中列出的所有配置项均需填写，缺少配置项的规则将无法导入。
不支持引用前缀列表。
成功导入的规则将在原有规则的基础上顺序添加，不会覆盖原有规则。
调整规则顺序
单击管理入方向规则/管理出方向规则，上下拖动规则来调整生效顺序。
删除规则
在目标网络ACL规则的操作列单击删除。
### API
调用[UpdateNetworkAclEntries](developer-reference/api-vpc-2016-04-28-updatenetworkaclentries.md)更新网络ACL规则。与控制台逻辑不同的是，该API将对ACL规则进行全量更新。如果只传入新增规则，将会删除原有规则，仅保留新传入的规则。因此，增加规则时必须传入所有需要保留的规则。
调用[CopyNetworkAclEntries](developer-reference/api-vpc-2016-04-28-copynetworkaclentries.md)将网络ACL的规则完整复制到另一个网络ACL。为保证所有规则都能被目标网络ACL正确地识别和接收，您需确保两个网络ACL所属的VPC均只有IPv4网段或均开启了IPv6。未开启IPv6的VPC中的网络ACL无法配置IPv6类型的规则，若将规则完整复制到已开启IPv6的VPC的网络ACL时，系统不会自动添加允许所有IPv6流量的自定义规则，可能影响IPv6通信。
### Terraform
本示例分别在入方向和出方向添加了拒绝规则，您应根据实际的访问控制策略调整规则配置。
Resources：[alicloud_network_acl](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/network_acl)# 指定网络ACL的地域 provider "alicloud" { region = "cn-hangzhou" } # 指定VPC ID variable "vpc_id" { default = "vpc-bp1k******" # 修改为VPC的实际ID } # 指定交换机ID variable "vswitch_id" { default = "vsw-bp1y******" # 修改为交换机的实际ID } # 创建网络ACL并绑定交换机 resource "alicloud_network_acl" "example_network_acl" { vpc_id = var.vpc_id # 指定网络ACL所属VPC network_acl_name = "example_network_acl_name" resources { resource_id = var.vswitch_id # 指定网络ACL关联的交换机 resource_type = "VSwitch" } ingress_acl_entries { # 指定入方向规则 network_acl_entry_name = "example-ingress" protocol = "tcp" # 协议类型 source_cidr_ip = "10.0.0.0/24" # 源地址 port = "20/80" # 端口范围 policy = "drop" # 策略 } egress_acl_entries { # 指定出方向规则 network_acl_entry_name = "example-egress" protocol = "tcp" destination_cidr_ip = "10.0.0.0/24" # 目的地址 port = "20/80" # 端口范围 policy = "drop" # 策略 } }
## 网络ACL规则配置示例
### 限制不同交换机下ECS的互通
同一VPC内的不同交换机之间默认私网互通，如需限制不同交换机下的资源互通，您可以使用网络ACL拒绝特定IP的访问。
如图，您可以为交换机1绑定的网络ACL配置出入方向规则，禁止交换机1中的实例与ECS06互通。
### 仅允许特定IP访问云上服务
使用高速通道实现线下IDC与VPC互通后，线下IDC中的所有资源都可以访问云上服务。您可以使用网络ACL仅允许特定IP访问，拒绝其他访问。
如图，您可以为交换机绑定的网络ACL配置出入方向规则，仅允许云下服务器1和云下服务器2访问交换机内的实例。
## 更多信息
### 计费说明
网络ACL功能不收费。
### 支持的地域
公有云支持的地域
| 区域 | 支持网络 ACL 的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） 、 马来西亚（柔佛州） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 法国（巴黎） 、 美国（硅谷） 、 美国（弗吉尼亚） 、 墨西哥 |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
金融云支持的地域
| 区域 | 支持网络 ACL 的地域 |
| --- | --- |
| 亚太 | 华南 1 金融云 、 华东 2 金融云 、 华北 2 金融云（邀测） |
政务云支持的地域
| 区域 | 支持网络 ACL 的地域 |
| --- | --- |
| 亚太 | 华北 2 阿里政务云 1 |
### 配额
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| vpc_quota_nacl_ingress_entry | 单个网络 ACL 支持创建的入方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 | 前往 [配额管理页面](https://vpc.console.aliyun.com/quota) 或 [配额中心](https://quotas.console.aliyun.com/products/vpc/quotas?query=peer) 申请提升配额。 |
| vpc_quota_nacl_egress_entry | 单个网络 ACL 支持创建的出方向规则数量 网络 ACL 所属 VPC 开启了 IPv6 时，支持创建的 IPv4/IPv6 入方向规则，默认均为 20 条。 | 20 条 |  |
| nacl_quota_vpc_create_count | 单个 VPC 支持创建的网络 ACL 数量 | 20 个 |  |
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
