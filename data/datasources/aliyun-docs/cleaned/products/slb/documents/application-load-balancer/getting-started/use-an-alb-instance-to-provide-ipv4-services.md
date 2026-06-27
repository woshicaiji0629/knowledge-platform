# ALB快速实现IPv4服务的负载均衡-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/getting-started/use-an-alb-instance-to-provide-ipv4-services

# ALB快速实现IPv4服务的负载均衡
阿里云应用型负载均衡ALB支持HTTP、HTTPS和QUIC协议，专门面向网络应用层。本文介绍如何快速创建一个IPv4版本的ALB实例，并将来自IPv4客户端的访问请求转发至后端服务器。
## 前提条件
您已在华东2（上海）地域创建了一个专有网络VPC1，并分别在可用区E和可用区G创建了一个交换机VSW1和VSW2。具体操作，请参见[创建专有网络和交换机](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)。
如果计划将ALB部署在交换机VSW1和VSW2，需注意：[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器通信），如果IP不足会出现报错并且无法创建实例，请确保交换机VSW1和VSW2中已预留足够的可用IP；升级前的ALB实例不受该限制。
说明
为确保ALB升级实例各项弹性能力可用，建议您在ALB实例所在的每个交换机内预留至少8个IP地址。
为确保ALB升级实例与后端服务正常连通，如您的后端服务中存在访问策略（包括iptables或其他任何第三方安全策略软件），建议您提前放通ALB实例所属交换机网段。
您已分别在VSW1和VSW2创建ECS01和ECS02实例，且ECS01和ECS02实例中部署了应用服务。
关于创建ECS实例，请参见[自定义购买实例](../../../../ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。
本文ECS01和ECS02部署测试应用示例如下：
ECS01服务部署命令
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS01." > index.html
ECS02服务部署命令
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS02." > index.html
您已经注册域名并完成备案。具体操作，请参见[注册阿里云域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)、[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案流程](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)。
本文VPC实例的相关配置如下所示，仅供参考。
单击查看本文VPC的配置
| 配置 | 说明 |
| --- | --- |
| 名称 | VPC1 |
| 地域 | 华东 2（上海） |
| IPv4 网段 | 192.168.0.0/16 |
| 交换机 | 名称 ：VSW1 可用区 ：可用区 E IPv4 网段 ：192.168.5.0/24 |
| 名称 ：VSW2 可用区 ：可用区 G IPv4 网段 ：192.168.6.0/24 |  |
本文ECS实例的相关配置如下所示，仅供参考。
单击查看本文ECS的配置
| 名称 | 地域 | 所属 VPC | 所属可用区及交换机 | ECS 配置 |
| --- | --- | --- | --- | --- |
| ECS01 | 华东 2（上海） | VPC1 | 可用区 E | VSW1 | 实例规格：ecs.e-c1m1.large CPU&内存：2 核（vCPU）2 GiB 镜像：Alibaba Cloud Linux 3.2104 LTS 64 位 |
| ECS02 | 可用区 G | VSW2 |  |  |  |
## 步骤一：创建ALB实例
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在实例页面，单击创建应用型负载均衡。
在应用型负载均衡（按量付费）购买页面，根据需要配置实例。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。
| 配置 | 说明 |
| --- | --- |
| 地域 | 选择实例所属的地域。本文选择 华东 2（上海） 。 |
| 实例网络类型 | 选择实例网络类型，系统会根据您的选择分配私网或公网服务地址。本文选择 公网 。 |
| VPC | 选择实例所属的 VPC。 |
| 可用区 | 至少选择 2 个可用区。本文选择 上海 可用区 E 及该可用区下的交换机 VSW1， 上海 可用区 G 及该可用区下的交换机 VSW2。 |
| 协议版本 | 选择实例的协议版本。本文选择 IPv4 。 |
| 功能版本（实例费） | 选择实例的功能版本，本文选择 标准版 。 |
| 实例名称 | 输入自定义实例名称。 |
| 服务关联角色 | 首次创建应用型负载均衡实例时，需要单击 创建服务关联角色 ，创建一个名称为 AliyunServiceRoleForAlb 的服务关联角色。系统会为该角色添加名称为 AliyunServiceRolePolicyForAlb 的权限策略，授予 ALB 拥有访问其他云产品实例的权限。更多操作，请参见 [负载均衡系统权限策略参考](../../security-and-compliance/application-oriented-load-balancing-system-permission-policy-reference.md) 。 |
单击立即购买，根据控制台提示完成实例开通。
返回实例页面，选择对应的地域即可看到新建的实例。
## 步骤二：创建服务器组
在左侧导航栏，选择应用型负载均衡ALB>服务器组。
在服务器组页面，单击创建服务器组。
在创建服务器组对话框配置服务器组相关的参数，然后单击创建。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建/删除服务器组](../user-guide/create-and-manage-a-server-group.md)。
| 参数 | 描述 |
| --- | --- |
| 服务器组类型 | 选择一种服务器组类型：本文选择 服务器类型 。 |
| 服务器组名称 | 输入服务器组名称。 |
| VPC | 从 VPC 下拉列表中选择 ECS 实例所属的 VPC。 说明 确保您选择的 VPC 与创建 ALB 实例时选择的 VPC 相同。 |
| 选择后端协议 | 选择一种后端协议，本文选择 HTTP 。 |
| 选择调度算法 | 选择一种调度算法，本文选择 加权轮询 。 |
| 开启会话保持 | 开启或关闭会话保持。本文保持默认值即不开启会话保持。 |
| 后端长连接 | 开启或关闭后端长连接。本文保持默认开启。 |
| 健康检查 | 开启或关闭健康检查。本文开启。 |
| 健康检查配置 | 开启健康检查后，您可以单击后面的 编辑 ，展开进行更多配置。 |
在服务器组创建成功对话框单击添加后端服务器。
在后端服务器页签单击添加后端服务器。
在添加后端服务器面板，选择已创建的ECS01和ECS02实例，然后单击下一步。
在配置端口和权重配置向导，为已添加的服务器设置端口和权重，然后单击确定。
本文ECS实例端口配置为80，权重为默认值100。
## 步骤三：配置监听
在左侧导航栏，选择应用型负载均衡ALB>实例，单击实例ID。
单击监听页签，然后单击创建监听。
在配置监听配置向导页面，完成以下配置，然后单击下一步。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于配置监听的更多操作，请参见[添加](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)。
| 参数 | 描述 |
| --- | --- |
| 选择监听协议 | 选择监听的协议类型。本文选择 HTTP 。 |
| 监听端口 | 用来接收请求并向后端服务器进行请求转发的监听端口。本文输入 80 。 |
| 监听名称 | 输入自定义监听名称。 |
| 高级配置 | 本文保持默认，可单击 修改 进行设置。 |
在选择服务器组配置向导，选择服务器类型及服务器类型下的目标服务器组，查看后端服务器信息，然后单击下一步。
在配置审核配置向导页面，确认监听配置信息，然后单击提交。
单击知道了返回监听页签，查看目标监听的健康检查状态列为正常时，表示后端服务器ECS01和ECS02实例可以正常处理ALB实例转发的请求。
## 步骤四：设置域名解析
实际业务场景中，建议您使用自有域名，通过CNAME解析的方式将自有域名指向ALB实例域名。
重要
[负载均衡域名已升级](../../product-overview/alb-and-nlb-domain-name-upgrade-announcement.md)，不支持直接使用ALB提供的DNS域名进行访问。
在左侧导航栏，选择应用型负载均衡ALB>实例
在实例页面，复制已创建的ALB实例的DNS名称。
执行以下步骤添加CNAME解析记录。
说明
对于非阿里云注册域名，需先将域名添加到云解析控制台，才可以进行域名解析设置。具体操作，请参见[域名管理](https://help.aliyun.com/zh/dns/domain-management#topic-2035895)。如果您是阿里云注册的域名，请直接执行以下步骤。
登录[域名解析控制台](https://dns.console.aliyun.com/#/dns/domainList)。
在权威域名解析页面，找到目标域名，在操作列单击解析设置。
在解析设置页面，单击添加记录。
在添加记录面板，配置以下信息完成CNAME解析配置，然后单击确定。
| 配置 | 说明 |
| --- | --- |
| 记录类型 | 在下拉列表中选择 CNAME 。 |
| 主机记录 | 您的域名的前缀。本文输入 @ 。 说明 创建域名为根域名时，主机记录为 @ 。 |
| 解析请求来源 | 选择默认。 |
| 记录值 | 输入域名对应的 CNAME 地址，即您复制的 ALB 实例的 DNS 名称。 |
| TTL | 全称 Time To Live，表示 DNS 记录在 DNS 服务器上的缓存时间，本文使用默认值。 |
## 步骤五：测试连通性
测试客户端与ECS01和ECS02服务器之间的连通性。本文以任意一台可以访问公网的客户端为例。
在浏览器中输入域名，例如http://<域名>。多次刷新页面，您可以观察到客户端请求在ECS01和ECS02服务器之间转换。
浏览器页面显示Hello World ! This is ECS01.，表明请求已被转发至 ECS01 服务器。
Hello World ! This is ECS02.
完成上述操作后，表明客户端可以通过ALB以轮询的方式访问不同的后端服务。
## 释放资源
清理ECS、安全组等资源：
删除ECS01实例及其安全组：
登录[云服务器](https://ecs.console.aliyun.com/server)[ECS](https://ecs.console.aliyun.com/server)[实例控制台](https://ecs.console.aliyun.com/server)，顶部选择实例所属地域，单击ECS01实例右侧的，弹出的窗口中选择释放，立即释放实例并确认。
登录[云服务器](https://ecs.console.aliyun.com/securityGroup)[ECS](https://ecs.console.aliyun.com/securityGroup)[安全组控制台](https://ecs.console.aliyun.com/securityGroup)，顶部选择实例所属地域，勾选ECS01自定义安全组并单击删除，删除安全组。
参照上述步骤，删除ECS02实例及对应安全组资源。
删除域名解析记录
删除域名解析记录，具体操作，请参见[删除域名解析记录](https://help.aliyun.com/zh/dns/delete-a-dns-record)。
清理ALB资源：
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。顶部选择实例所属地域，单击实例右侧的，弹出的窗口中选择释放并确认。
移除后端服务器，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
删除服务器组，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
清理VPC资源：
登录[专有网络](https://vpc.console.aliyun.com/vpc)[VPC](https://vpc.console.aliyun.com/vpc)[控制台](https://vpc.console.aliyun.com/vpc)，顶部选择实例所属地域。
单击实例右侧删除，系统将校验是否存在未删除的云产品资源或关联资源。如有依赖资源时，您需要完全释放资源后，才可删除专有网络和交换机。
## 相关文档
了解ALB的应用场景、组成等信息，请参见[什么是应用型负载均衡](../product-overview/what-is-alb.md)[ALB](../product-overview/what-is-alb.md)。
了解ALB的功能特性，请参见[功能特性](../product-overview/functional-characteristics.md)。
了解ALB支持的地域信息，请参见[ALB](../product-overview/supported-regions-and-zones.md)[支持的地域与可用区](../product-overview/supported-regions-and-zones.md)。
了解ALB的配额及提升配额方式，请参见[配额与限制](../product-overview/quotas-and-limits.md)。
了解ALB计费文档，请参见[ALB](../../alb-billing.md)[产品计费](../../alb-billing.md)。
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
