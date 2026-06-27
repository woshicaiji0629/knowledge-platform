# 如何使用ALB实现gRPC协议的负载均衡-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/use-cases/enable-load-balancing-for-grpc-services

# 使用ALB实现gRPC协议的负载均衡
gRPC是一种高性能、开源的远程过程调用框架，当您使用gRPC进行后端服务通信时，您可使用应用型负载均衡ALB（Application Load Balancer）实现gRPC协议的负载均衡，统一流量入口。gRPC基于HTTP/2协议进行通信，目前ALB仅支持前端加密（通过HTTPS监听）和后端明文（服务器组后端协议为gRPC）的形态。
## 背景信息
gRPC是一种高性能、开源的远程过程调用框架，它使用Protocol Buffers作为接口定义语言（IDL）和基于HTTP/2协议进行通信。
gRPC用于构建分布式系统中的服务通信。它解决了不同服务之间的跨语言通信问题，并提供了IDL和自动生成的代码，使得开发人员可以方便地定义和调用远程服务。同时，gRPC具有高性能、低延迟和高效的数据传输，通过采用二进制编码和HTTP/2的多路复用特性，提供了快速、可靠的远程调用体验。
gRPC适用于微服务架构、跨语言通信、大规模分布式系统等场景。特别是在需要高性能和低延迟的场景下，gRPC具有较高的性能表现。它还支持多种调用方式，如简单调用、流式请求和响应、双向流等，可以灵活地满足不同业务需求。
关于gRPC的更多信息，可参考[gRPC](https://grpc.io/docs/)[官方文档](https://grpc.io/docs/)。
## 场景示例
某公司在华东1（杭州）地域的专有网络VPC（Virtual Private Cloud）内部署了gRPC服务，在VPC中创建了ALB实例和支持gRPC协议的后端服务器组，ALB配置了HTTPS监听并打开HTTP2.0开关，同时后端服务器组配置了gRPC协议的健康检查。
客户端需要通过ALB实例来访问VPC中部署的gRPC服务。
## 前提条件
已创建ALB实例。具体操作，请参见[创建和管理](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。
已准备后端服务器，并在服务器中部署了gRPC服务。关于gRPC服务部署方法，可参考[gRPC](https://grpc.io/docs/)[官方文档](https://grpc.io/docs/)。
已经注册域名并完成备案。具体操作，请参见[注册阿里云域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)、[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案流程](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)。
已购买证书或者上传第三方证书到SSL证书服务并绑定域名。关于创建证书，请参见[使用正式证书为](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)[Web](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)[站点开启](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)[HTTPS](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)[访问](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)。
## 步骤一：创建服务器组并添加后端服务器
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏处，选择所属的地域。
在左侧导航栏，选择应用型负载均衡 ALB>服务器组。
在服务器组页面，单击创建服务器组。
在创建服务器组对话框中，完成以下配置。完成后单击创建。
此处仅列出和本文强相关的配置项，其他未列出的配置项可使用默认值或自行配置。
| 配置 | 说明 |
| --- | --- |
| 服务器组类型 | 选择一种服务器组类型。本文选择 服务器类型 。 |
| VPC | 从 VPC 下拉列表中选择 ALB 所属的 VPC，只有该 VPC 下的服务器可以加入到该服务器组。 |
| 选择后端协议 | 本文选择 gRPC 。 |
| 健康检查 | 本文选择开启健康检查。 |
| 健康检查配置 | 单击 编辑 ，修改健康检查配置信息： 健康检查协议 ：本文选择 gRPC 。 健康检查方法 ：本文选择 POST 。 健康状态返回码 ：选择健康检查正常的状态码，需要与后端 gRPC 服务配置一致。本文示例为 12 。 |
在服务器组页面找到目标服务器组，单击其实例ID。
单击后端服务器页签，然后单击添加后端服务器。
在添加后端服务器面板，选择已创建的ECS实例，然后单击下一步。
在配置端口和权重配置向导，设置ECS的端口和权重，然后单击确定。
说明
此处ECS配置的端口必须要与实际部署的gRPC服务设置的端口保持一致。同时注意安全组规则需要放行相关端口。
## 步骤二：配置HTTPS监听
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在左侧导航栏，选择实例。
在实例页面，找到目标实例，然后在操作列单击创建监听。
在配置监听页面配置以下信息，其他参数可保持默认值或根据实际情况修改。完成后单击下一步。
| 配置 | 说明 |
| --- | --- |
| 选择监听协议 | 选择 HTTPS 。 |
| 监听端口 | 本文配置端口 443。 |
说明
服务器组设置后端协议为gRPC时，监听协议类型只支持HTTPS。
gRPC基于HTTP/2协议进行通信，服务器组设置后端协议为gRPC时，HTTPS监听必须开启HTTP2.0。ALB默认启用该功能，需要确保启用HTTP2.0功能为已开启，请勿关闭。
在配置SSL证书页面配置以下信息，其他参数可保持默认值或根据实际情况修改。完成后单击下一步。
| 配置 | 说明 |
| --- | --- |
| 选择服务器证书 | 选择准备的 SSL 证书。 |
在选择服务器组页面配置以下信息，其他参数可保持默认值或根据实际情况修改。完成后单击下一步。
| 配置 | 说明 |
| --- | --- |
| 选择服务器组 | 选择此前已创建好的 gRPC 服务器组。 |
在配置审核页面，检查配置参数是否有误，无误的话单击提交，等待监听创建完成。
## 步骤三：配置域名解析
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
## 步骤四：验证连通性
完成上述操作后，客户端可以通过ALB访问部署了gRPC服务的后端服务器，以下内容为您展示如何测试客户端和gRPC服务之间的连通性。
说明
浏览器无法直接访问gRPC服务。建议您通过grpcurl工具之类的测试工具验证访问。
在客户端中执行grpcurl -insecure -v <域名>:<监听端口> <gRPC服务名称>/<方法>命令尝试访问ECS中的gRPC服务。
如果收到类似以下所示的回复报文，则表示客户端可以通过ALB访问部署了gRPC服务的后端服务器ECS。
[root@iZbp1xxx.0Z ~]# grpcurl -insecure -v xxx.com:443 helloworld.Greeter/SayHello Resolved method descriptor: rpc SayHello ( .helloworld.HelloRequest ) returns ( .helloworld.HelloReply ); Request metadata to send: (empty) Response headers received: accept-encoding: identity,gzip content-type: application/grpc date: Mon, 04 Jul 2022 08:53:01 GMT grpc-accept-encoding: identity,deflate,gzip vary: Accept-Encoding Response contents: { "message": "remoteip:47.xxx.xxx.195 x-forwarded-for:47.xxx.xxx.xx5 user-agent:grpcurl/v1.8.0 grpc-go/1.30.0 hostname:iZbp12xxx0kZ server addr:192.168.1.239 " } Response trailers received: (empty) Sent 0 requests and received 1 response
## 相关文档
HTTPS监听详细配置参数及注意事项，可参考[添加](../user-guide/add-an-https-listener.md)[HTTPS](../user-guide/add-an-https-listener.md)[监听](../user-guide/add-an-https-listener.md)。
服务器组详细配置参数及注意事项，可参考[创建和管理服务器组](../user-guide/create-and-manage-a-server-group.md)。
健康检查详细配置参数及注意事项，可参考[ALB](../user-guide/alb-health-check.md)[健康检查](../user-guide/alb-health-check.md)。
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
