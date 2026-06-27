# ALB快速实现IPv6服务的负载均衡-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/getting-started/implement-load-balancing-for-ipv6-services

# ALB快速实现IPv6服务的负载均衡
应用型负载均衡ALB（Application Load Balancer）支持转发IPv6网络请求，本文指导您如何为双栈ALB实例开启IPv6挂载，即ALB实例同时支持挂载IPv4和IPv6的云服务器ECS（Elastic Compute Service），使IPv6网络的客户端请求通过ALB可以访问部署在后端的IPv4和IPv6服务。
## 场景示例
本文以下图场景为例。某公司希望ALB可以转发来自IPv6客户端的请求，以实现IPv6客户端使用公网正常访问VPC中的IPv4和IPv6服务。该公司需要创建具有IPv4和IPv6地址的ECS，同时需要在VPC中创建双栈ALB实例并创建具有IPv6挂载功能的服务器组。完成上述配置后，IPv6客户端的请求即可通过ALB访问部署在后端ECS上的IPv4和IPv6服务。
## 使用限制
双栈支持的地域，请参见[ALB](../user-guide/alb-instance-overview.md)[双栈支持的地域](../user-guide/alb-instance-overview.md)。
使用双栈功能，需要开通VPC可用区中交换机的IPv6功能。
双栈ALB实例支持将IPv4和IPv6的客户端流量转发至IPv4、IPv6的后端服务。详情请参见[ALB](../user-guide/alb-instance-overview.md)[实例概述](../user-guide/alb-instance-overview.md)。
不支持已有的IPv4实例升级为双栈实例，仅支持新建双栈实例。
IP协议版本为IPv4/v6双栈的服务器组，仅支持添加至双栈ALB实例的监听或转发规则中。
## 前提条件
您已在华东2（上海）地域创建了一个VPC1，并分别在可用区E和可用区G创建了一个交换机VSW1和VSW2，且VPC1已[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)[网段](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vpc#section-p31-wbx-mlj)、VSW1和VSW2均已[开通](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-qn2-ft9-1g2)[IPv6](https://help.aliyun.com/zh/ipv6-gateway/user-guide/enable-ipv6-for-a-vswitch-1#section-qn2-ft9-1g2)。VPC开通IPv6网段后，系统会为您默认创建一个IPv6网关。
如果计划将ALB部署在交换机VSW1和VSW2，需注意：[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器通信），如果IP不足会出现报错并且无法创建实例，请确保交换机VSW1和VSW2中已预留足够的可用IP；升级前的ALB实例不受该限制。
说明
为确保ALB升级实例各项弹性能力可用，建议您在ALB实例所在的每个交换机内预留至少8个IP地址。
为确保ALB升级实例与后端服务正常连通，如您的后端服务中存在访问策略（包括iptables或其他任何第三方安全策略软件），建议您提前放通ALB实例所属交换机网段。
您已经[注册域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)。
## 步骤一：创建并配置ECS实例
- 登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。
在左侧导航栏，单击交换机。
选择交换机的地域，本文选择华东2（上海）。
在交换机页面，找到目标交换机，然后在操作列选择添加云产品>ECS实例。
在云服务器ECS购买页面的自定义购买页签下，创建2台ECS实例，并将IPv4 ECS修改实例名称为ECS01，将IPv6 ECS修改实例名称为ECS02，两台ECS实例绑定的安全组均需要放行80端口。具体操作，请参见[自定义购买实例](../../../../ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。
单击查看本文ECS实例的配置
| ECS 实例名称 | 地域 | VPC 名称 | 交换机 | IP 版本 | 镜像 |
| --- | --- | --- | --- | --- | --- |
| ECS01 | 华东 2（上海） | VPC1 | 可用区 E 的 VSW1 | IPv4 | Alibaba Cloud Linux 3.2104 LTS 64 位 |
| ECS02 | 华东 2（上海） | VPC1 | 可用区 G 的 VSW2 | IPv6 说明 创建具有 IPv6 地址的实例时，需在 IPv6 处选中 免费分配 IPv6 地址 。 | Alibaba Cloud Linux 3.2104 LTS 64 位 |
远程登录ECS01和ECS02实例，具体操作，请参见[ECS](../../../../ecs/documents/user-guide/connect-to-instance.md)[远程连接操作指南](../../../../ecs/documents/user-guide/connect-to-instance.md)。
在ECS01中执行如下命令，部署Nginx服务。
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! this is ipv4 rs." > index.html
在ECS02中执行如下命令，部署Nginx服务。
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! this is ipv6 rs." > index.html
配置ECS02实例的IPv6地址。具体操作请参见[IPv6](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[通信](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
说明
如果您的ECS02实例镜像为Alibaba Cloud Linux 3.2104 LTS 64，并且在创建时已在IPv6处选中免费分配IPv6地址，可忽略此步骤。
远程登录VPC中的ECS02实例。
配置IPv6地址。
执行ip addr | grep inet6或者ifconfig | grep inet6命令。
如下所示，表示已成功配置IPv6地址，您可忽略此步骤。
[root@iZbpxxx fxe4Z ~]# ip addr | grep inet6 inet6 ::1/128 scope host inet6 2408:4005:xxx:xxx:7cd5:aa9c/128 scope global dynamic noprefixroute inet6 fe80::xxx:cc1c/64 scope link noprefixroute
如果未返回inet6相关内容，表示实例未开启IPv6服务，请先[开启](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[IPv6](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[服务](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
如果返回inet6相关内容，表示ECS02实例已成功开启IPv6服务并识别到IPv6地址，请继续[配置](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[IPv6](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)[地址](../../../../ecs/documents/user-guide/step-1-create-a-vpc-that-supports-ipv6-addressing-step-1-create-a-vpc-that-supports-ipv6-addressing.md)。
## 步骤二：ECS02配置IPv6安全组规则
您需要为ECS02实例配置IPv6安全组规则，使安全组入方向能够允许接受IPv6客户端发送的请求。
登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)。
在左侧导航栏，选择网络与安全>安全组。
在顶部菜单栏处，选择目标安全组的地域。本文选择华东2（上海）。
在安全组页面，找到目标安全组，在操作列单击管理规则。
单击安全组详情页面，然后在访问规则区域，单击入方向页签。
单击增加规则，在规则列表中根据以下信息配置IPv6安全组规则，然后单击提交。
| 参数 | 描述 |
| --- | --- |
| 授权策略 | 设置是否允许安全组的授权策略。本文选择 允许 。 |
| 优先级 | 设置安全组的优先级。优先级的数值越小，优先级越高。取值范围： 1~100 。 本文保持默认值 1 。 |
| 协议 | 允许入方向放行的安全组的协议类型。本文选择 所有 ICMP-IPv6 。 |
| 访问来源 | 输入授权的 IPv6 地址段。 本文输入 ::/0 ，表示授权所有 IPv6 地址。 说明 本文配置的授权对象仅为示例，您可以根据需要放行指定的 IPv6 网段。 |
| 访问目的(本实例) | 允许入方向放行的安全组的端口范围。 协议 选择 所有 ICMP-IPv6 时，端口范围的目的端口只能设置为 全部（-1/-1） 且不能修改。 |
| 描述 | 自定义描述信息。 |
## 步骤三：创建ALB实例
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在实例页面，单击创建应用型负载均衡。
在购买页面，完成以下配置，然后单击立即购买并根据控制台提示完成实例开通。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。
| 参数 | 描述 |
| --- | --- |
| 地域 | 选择实例所属的地域。本文选择 华东 2（上海） 。 |
| 实例网络类型 | 选择实例网络类型，系统会根据您的选择分配私网或公网服务地址。本文选择 公网 。 说明 实例网络类型 选择 公网 类型只作用于 IPv4，IPv6 默认是私网类型。本文使用 IPv6 的公网类型，需执行 [步骤](implement-load-balancing-for-ipv6-services.md) [4](implement-load-balancing-for-ipv6-services.md) 变更 IPv6 的网络类型为公网类型。 |
| VPC | 选择实例所属的 VPC。 说明 请确保该 VPC 开启了 IPv6 功能。 |
| 可用区 | 选择至少 2 个可用区。本文选择 上海 可用区 E ， 上海 可用区 G 。 分别在所选可用区内选择交换机。本文选择可用区 E 下的 VSW1 和可用区 G 下的 VSW2。 |
| 协议版本 | 选择实例的 IP 协议版本。本文选择 双栈 。 |
| 功能版本（实例费） | 选择实例的功能版本。本文选择 标准版 。 |
| 实例名称 | 输入自定义实例名称。 |
| 服务关联角色 | 首次创建应用型负载均衡实例时，需要单击 创建服务关联角色 ，创建一个名称为 AliyunServiceRoleForAlb 的服务关联角色。系统会为该角色添加名称为 AliyunServiceRolePolicyForAlb 的权限策略，授予 ALB 拥有访问其他云产品实例的权限。更多操作，请参见 [负载均衡系统权限策略参考](../../security-and-compliance/application-oriented-load-balancing-system-permission-policy-reference.md) 。 |
创建完公网双栈ALB实例后，本文需要使用公网IPv6地址，请执行以下步骤将ALB实例的IPv6地址变更为公网地址。更多信息，请参见[协议版本](../user-guide/change-the-network-type-of-an-alb-instance.md)。
返回实例页面，找到目标ALB实例，单击实例ID。
在实例详情页签的基本信息区域，找到网络类型，然后在IPv6：私网的右侧单击变更网络类型。
在变更网络类型对话框中单击确定变更。
变更成功后，您可以看到IPv6的网络类型变成了公网。
## 步骤四：创建服务器组
在左侧导航栏，选择应用型负载均衡 ALB>服务器组。
在服务器组页面，单击创建服务器组。
在创建服务器组对话框中，完成以下配置，然后单击创建。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建/删除服务器组](../user-guide/create-and-manage-a-server-group.md)。
| 参数 | 描述 |
| --- | --- |
| 服务器组类型 | 选择一种服务器组类型。本文选择 服务器类型 。 |
| 服务器组名称 | 输入自定义服务器组名称。 |
| VPC | 从 VPC 下拉列表中选择已创建的 VPC，只有该 VPC 下的服务器可以加入到该服务器组。 说明 确保您选择的 VPC 开启了 IPv6 功能，且与创建 ALB 实例时选择的 VPC 相同。 |
| 选择后端协议 | 选择一种后端协议。本文选择 HTTP 。 |
| 选择调度算法 | 选择一种调度算法。本文选择 加权轮询 。 |
| IP 协议版本 | 选择 IPv4/v6 双栈 。 |
| 会话保持 | 开启或关闭会话保持。本文保持默认值即不开启会话保持。 |
| 健康检查 | 开启或关闭健康检查。本文开启。 |
| 健康检查配置 | 开启健康检查后，您可以单击后面的 编辑 ，展开进行更多配置。 |
在服务器组页面，找到目标服务器组，然后单击目标服务器组ID。
单击后端服务器页签，然后单击添加后端服务器。
在添加后端服务器面板，选择已创建的ECS01和ECS02实例，在IP地址列选择ECS01实例的IPv4地址，选择ECS02实例的IPv6地址，然后单击下一步。
在配置端口和权重配置向导，设置ECS01和ECS02实例的端口和权重，然后单击确定。
本文ECS实例端口配置为80，权重为默认值100。
## 步骤五：配置监听
在实例页面，找到目标实例，单击实例ID。
单击监听页签，然后单击创建监听。
在配置监听配置向导，完成以下配置，然后单击下一步。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于配置监听的更多操作，请参见[添加](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)。
| 参数 | 描述 |
| --- | --- |
| 选择监听协议 | 选择监听的协议类型。本文选择 HTTP 。 |
| 监听端口 | 用来接收请求并向后端服务器进行请求转发的监听端口。本文输入 80 。 |
| 监听名称 | 输入自定义监听名称。 |
| 高级配置 | 本文保持默认，可单击 修改 进行设置。 |
在选择服务器组配置向导，选择服务器类型及服务器类型下的目标服务器组，查看后端服务器信息，然后单击下一步。
在配置审核配置向导，确认配置信息，然后单击提交。
单击知道了返回监听页签，查看目标监听的健康检查状态列为正常时，表示后端服务器ECS01和ECS02实例可以正常处理ALB实例转发的请求。
## 步骤六：设置域名解析
实际业务场景中，建议您使用自有域名，通过CNAME解析的方式将自有域名指向ALB实例域名。
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
## 步骤七：测试连通性
说明
测试连通性时，请确保您的客户端已支持IPv6功能，您可以在浏览器地址栏输入网址http://test-ipv6.com/测试您的客户端是否支持IPv6功能。
以任意一台可以访问IPv6客户端的终端为例，测试IPv6客户端与ECS01和ECS02服务器的连通性。
打开终端的cmd窗口。
多次执行以下命令，测试IPv6客户端是否可以通过ALB以轮询的方式访问IPv4 ECS以及IPv6 ECS。
curl -6 http://<域名> -v
如果收到如下所示的回复报文，则表示IPv6客户端可以访问IPv4 ECS。
C:\Users\w***g>curl -6 http://xxx.com -v * Rebuilt URL to: http://xxx.com/ * Trying 2408:xxx:d3:c2b:df22:bc09... * TCP_NODELAY set * Connected to xxx.com (2408:xxx:f22:bc09) port 80 (#0) > GET / HTTP/1.1 > Host: xxx.com > User-Agent: curl/7.55.1 > Accept: */* > < HTTP/1.1 200 OK < Date: Wed, 07 Sep 2022 06:52:47 GMT < Content-Type: text/html < Content-Length: 31 < Connection: keep-alive < Last-Modified: Wed, 07 Sep 2022 03:13:10 GMT < ETag: "63180c46-1f" < Accept-Ranges: bytes < Hello World ! this is ipv4 rs.
如果收到如下所示的回复报文，则表示IPv6客户端可以访问IPv6 ECS。
C:\Users\wxxx>curl -6 http://xxx.s.com -v * Rebuilt URL to: http://xxx.com/ * Trying 2408:40xxx:df22:bc09... * TCP_NODELAY set * Connected to xxx.s.com (2408:xxx:22:bc09) port 80 (#0) > GET / HTTP/1.1 > Host: xxx > User-Agent: curl/7.55.1 > Accept: */* > < HTTP/1.1 200 OK < Date: Wed, 07 Sep 2022 06:53:04 GMT < Content-Type: text/html < Content-Length: 31 < Connection: keep-alive < Last-Modified: Wed, 07 Sep 2022 03:13:50 GMT < ETag: "63180c6e-1f" < Accept-Ranges: bytes < Hello World ! this is ipv6 rs.
完成上述操作后，表明IPv6客户端可以通过ALB以轮询的方式访问VPC中部署的IPv4服务和IPv6服务。
## 释放资源
清理ECS、安全组等资源：
删除ECS01实例及其安全组：
登录[云服务器](https://ecs.console.aliyun.com/server)[ECS](https://ecs.console.aliyun.com/server)[实例控制台](https://ecs.console.aliyun.com/server)，顶部选择实例所属地域，单击ECS01实例右侧的，弹出的窗口中选择释放，立即释放实例并确认。
登录[云服务器](https://ecs.console.aliyun.com/securityGroup)[ECS](https://ecs.console.aliyun.com/securityGroup)[安全组控制台](https://ecs.console.aliyun.com/securityGroup)，顶部选择实例所属地域，勾选ECS01自定义安全组并单击删除，删除安全组。
参照上述步骤，删除ECS02实例及对应安全组资源。
删除域名解析记录：
删除域名解析记录，具体操作，请参见[删除域名解析记录](https://help.aliyun.com/zh/dns/delete-a-dns-record)。
清理ALB资源：
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。顶部选择实例所属地域，单击目标实例右侧的，弹出的窗口中选择释放并确认。
移除后端服务器，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
删除服务器组，具体操作，请参见[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
清理VPC资源：
登录[专有网络](https://vpc.console.aliyun.com/vpc)[VPC](https://vpc.console.aliyun.com/vpc)[控制台](https://vpc.console.aliyun.com/vpc)，顶部选择实例所属地域。
单击实例右侧删除，系统将校验是否存在未删除的云产品资源或关联资源。如有依赖资源时，您需要完全释放资源后，才可删除专有网络和交换机。
## 相关文档
了解ALB的应用场景、组成等信息，请参见[什么是应用型负载均衡](../product-overview/what-is-alb.md)[ALB](../product-overview/what-is-alb.md)。
了解ALB的功能特性，请参见[功能特性](../product-overview/functional-characteristics.md)。
了解ALB的配额及提升配额方式，请参见[配额与限制](../product-overview/quotas-and-limits.md)。
了解ALB支持的地域信息，请参见[ALB](../product-overview/supported-regions-and-zones.md)[支持的地域与可用区](../product-overview/supported-regions-and-zones.md)。
了解ALB付费方式、计费组成和定价等计费信息，请参见[ALB](../product-overview/billing-overview.md)[计费概述](../product-overview/billing-overview.md)。
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
