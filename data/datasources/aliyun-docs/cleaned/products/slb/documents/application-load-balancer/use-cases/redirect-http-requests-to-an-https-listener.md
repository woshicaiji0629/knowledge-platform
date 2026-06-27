# 使用ALB将HTTP访问重定向至HTTPS-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/use-cases/redirect-http-requests-to-an-https-listener

# 使用ALB将HTTP访问重定向至HTTPS
HTTPS是加密数据传输协议，安全性高。当您需要进行HTTPS安全改造时，您可以使用应用型负载均衡ALB将HTTP访问重定向至HTTPS，让用户在无感知的情况下将HTTP访问重定向至HTTPS。
## 功能简介
ALB提供HTTP到HTTPS的重定向功能。通过配置监听转发规则，将HTTP协议的请求重定向到HTTPS，从而确保数据传输加密，防止中间人攻击和数据泄露，帮助用户构建符合现代安全标准的网络架构。
### 关键特性
灵活配置：支持自定义重定向规则，可以基于路径、HTTP标头等参数设置特定的重定向策略，满足复杂应用场景的需求。
状态码设置：支持选择不同的HTTP状态码进行重定向，如301（永久重定向）或302（临时重定向）。
性能优化：将重定向逻辑转移到负载均衡层，后端服务器无需处理重定向逻辑，专注于核心业务处理，提升整体效率。
### 应用场景
HTTPS安全改造：将现有网站或应用程序从HTTP改造为HTTPS，提升用户和服务器之间通信的安全性。
域名更改/站点迁移：当网站迁移到新的域名时，使用重定向可以保持用户访问的连续性，避免流量损失。
基于HTTP标头重定向：根据HTTP标头信息（如语言、设备类型等），将用户请求重定向至不同的HTTPS应用，实现个性化服务。
## 场景示例
某企业在阿里云华东1（杭州）地域购买的ALB实例部署了业务并对外提供服务。企业希望在域名保持不变的情况下，将HTTP协议切换为HTTPS协议，以实现数据加密，并提升用户体验的流畅性与多样性。
## 前提条件
已[创建公网](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)（基础版、标准版和WAF增强版均支持）。
已为ALB实例[创建服务器组](../user-guide/create-and-manage-a-server-group.md)（后端协议为HTTP）。
已在ALB实例的服务器组中分别添加ECS01和ECS02实例，并在ECS01和ECS02中均部署了应用服务。
本文以Alibaba Cloud Linux 3操作系统为例，并使用Nginx配置HTTP 80服务。
参考示例：ECS01部署测试服务
yum install -y nginx systemctl start nginx.service cd /usr/share/nginx/html/ echo "Hello World ! This is ECS01." > index.html
已为ALB实例[创建](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)。
已[注册自有域名](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)并完成[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，且通过自有域名[为](../user-guide/configure-cname-resolution-for-alb.md)[ALB](../user-guide/configure-cname-resolution-for-alb.md)[配置](../user-guide/configure-cname-resolution-for-alb.md)[CNAME](../user-guide/configure-cname-resolution-for-alb.md)[解析](../user-guide/configure-cname-resolution-for-alb.md)。
已[创建并申请证书](https://help.aliyun.com/zh/ssl-certificate/product-overview/get-started-with-ssl-certificates-service)或者上传第三方证书到SSL证书服务并绑定自有域名。
## 操作步骤
本文通过以下两种方式介绍通过ALB实现HTTP访问重定向至HTTPS，您可以按需配置：
HTTP端口所有请求重定向至HTTPS：无条件地将所有到达ALB的HTTP请求重定向到HTTPS，适用于强制要求所有访问都使用HTTPS的场景，例如全站启用HTTPS或统一安全策略。
基于HTTP标头重定向至HTTPS：基于HTTP请求头（如语言、设备类型等）进行条件判断，只有满足特定条件的请求才会被重定向。适用于需按条件区分跳转目标的场景，例如，可以根据用户语言偏好重定向到不同的语言版本网站，或者根据设备类型（手机、平板、PC）或浏览器版本，将请求重定向到移动端或桌面端的HTTPS版本。
## HTTP端口所有请求均重定向至HTTPS
### 步骤一：配置HTTPS监听
在[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)顶部菜单栏选择ALB实例所属地域。
在ALB实例页面，单击目标实例ID。
在监听页签，单击创建监听。
在负载均衡业务配置向导页面，完成以下配置，然后单击下一步。
此处仅列出和本文强相关的配置项，[HTTPS](../user-guide/add-an-https-listener.md)[监听其他参数配置](../user-guide/add-an-https-listener.md)可保持默认值或根据实际情况修改。
在配置监听配置向导，选择监听协议为HTTPS，监听端口为443，然后单击下一步。
在配置SSL证书配置向导，选择已创建好的服务器证书。然后单击下一步。
在选择服务器组配置向导，选择已创建好的服务器组，并查看后端服务器信息，然后单击下一步。
在配置审核配置向导页面，确认配置信息，单击提交。
### 步骤二：配置监听转发规则
在监听页签，找到已创建的HTTP监听，然后在操作列单击查看/编辑转发规则。
在转发规则页签，单击插入新规则。
在插入转发规则区域，配置下表参数，然后单击确定。
此处仅列出和本文强相关的配置项，[转发规则其他参数配置](../user-guide/manage-forwarding-rules-for-a-listener.md)可保持默认值或根据实际情况修改。
| 参数 | 说明 |
| --- | --- |
| 转发条件 | 选择 路径 并输入 /* 。 |
| 转发动作 | 选择 重定向至 。 协议 ：本示例选择 HTTPS 。 端口 ：输入您已创建的 HTTPS 协议监听端口。本文输入 443 。 状态码 ：本示例保持默认值 301 。 |
### 步骤三：结果验证
以任意一台可以访问公网的终端为例，测试访问ALB的HTTP请求是否能够重定向至HTTPS。
打开终端的命令行窗口。
执行curl -v -L http://<自有域名>。
如下图所示，收到状态码301，表示访问ALB的请求重定向至HTTPS，应答服务器为ECS01。
重复执行命令，应答服务器变为ECS02。
## 基于HTTP标头重定向至HTTPS
本文以HTTP标头Accept-Language是zh-CN,zh的HTTP请求重定向至HTTPS为例。
### 步骤一：配置HTTPS监听
在[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)顶部菜单栏选择ALB实例所属地域。
在ALB实例页面，单击目标实例ID。
在监听页签，单击创建监听。
在负载均衡业务配置向导页面，完成以下配置，然后单击下一步。
此处仅列出和本文强相关的配置项，[HTTPS](../user-guide/add-an-https-listener.md)[监听其他参数配置](../user-guide/add-an-https-listener.md)可保持默认值或根据实际情况修改。
在配置监听配置向导，选择监听协议为HTTPS，监听端口为443，然后单击下一步。
在配置SSL证书配置向导，选择已创建好的服务器证书。然后单击下一步。
在选择服务器组配置向导，选择已创建好的服务器组，并查看后端服务器信息，然后单击下一步。
在配置审核配置向导页面，确认配置信息，单击提交。
### 步骤二：配置监听转发规则
在监听页签，找到已创建的HTTP监听，然后在操作列单击查看/编辑转发规则。
在转发规则页签，单击插入新规则。
在插入转发规则区域，配置下表参数，然后单击确定。
此处仅列出和本文强相关的配置项，[转发规则其他参数配置](../user-guide/manage-forwarding-rules-for-a-listener.md)可保持默认值或根据实际情况修改。
| 参数 | 说明 |
| --- | --- |
| 转发条件 | 选择 HTTP 标头 。 键是 ：本示例输入 Accept-Language 。 值是 ：本示例输入 zh-CN,zh 。 |
| 转发动作 | 选择 重定向至 。 协议 ：本示例选择 HTTPS 。 域名 ：输入您的自有域名。 端口 ：输入您已创建的 HTTPS 协议监听端口。本文输入 443 。 状态码 ：本示例选择 302 。 |
### 步骤三：结果验证
以任意一台可以访问公网的终端为例，测试访问ALB的HTTP请求是否能够重定向至HTTPS。
打开终端的命令行窗口。
执行curl -v -L -H "Accept-Language: zh-CN,zh" http://<自有域名>.
如下图所示，收到状态码302，表示访问ALB的请求重定向至HTTPS，应答服务器为ECS01。
重复执行命令，应答服务器变为ECS02。
## 重定向状态码说明
ALB重定向状态码默认为301，您可以根据业务需求选择其他重定向状态码。ALB支持的重定向状态码及说明如下：
| 状态码 | 说明 |
| --- | --- |
| 301 | 永久移动。请求的资源已被永久移动至新的 URL，建议客户端的请求都使用新的 URL 代替。 |
| 302 | 临时移动。请求的资源只是临时被移动，客户端应继续使用原有 URL 访问。 |
| 303 | 与 302 类似表示资源的临时移动，无论原始请求方法是什么，要求客户端在重定向后使用 GET 方法发起请求。 |
| 307 | 与 302 类似表示资源的临时移动，但客户端必须保持原请求方法（如 POST 请求重定向后仍为 POST，不允许 POST 转为 GET）。 |
| 308 | 与 301 类似表示资源的永久移动，客户端必须保持原请求方法（如 POST 请求重定向后仍为 POST，不允许 POST 转为 GET）。 |
关于状态码说明的更多信息请参见[HTTP/1.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.4)[标准（RFC 7231）](https://www.rfc-editor.org/rfc/rfc7231#section-6.4)。
## 相关文档
若您的业务有更高的安全需求，您可以进一步了解ALB的以下功能：
[配置全链路](end-to-end-data-transfer-over-https.md)[HTTPS](end-to-end-data-transfer-over-https.md)[访问实现加密通信](end-to-end-data-transfer-over-https.md)：ALB提供全链路HTTPS加密功能，可以实现客户端到ALB、ALB到后端服务器之间的全链路加密通信，提升敏感业务的安全性。
[使用](configure-mutual-authentication-on-an-https-listener.md)[ALB](configure-mutual-authentication-on-an-https-listener.md)[部署](configure-mutual-authentication-on-an-https-listener.md)[HTTPS](configure-mutual-authentication-on-an-https-listener.md)[业务（双向认证）](configure-mutual-authentication-on-an-https-listener.md)：ALB提供HTTPS双向认证功能，在客户端与服务端建立连接之前，双方需进行身份验证。仅在双方均成功通过认证后，方可建立安全通信通道进行数据传输，从而确保只有授权的客户端能够访问接入，有效降低中间人攻击和未授权访问等安全风险。
了解更多关于监听的转发条件以及转发动作，请参见[配置监听转发规则](../user-guide/manage-forwarding-rules-for-a-listener.md)。
通过ALB监听转发规则还可以实现以下场景需求：
[使用](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[ALB](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[流量镜像功能实现仿真压测](use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)：通过ALB提供的流量镜像功能可以实现在线流量仿真，将在线流量镜像到测试环境的后端服务器，同时ALB自动丢弃镜像后端服务器返回的响应数据，保证镜像后端服务器的测试业务不会影响到线上业务。
[使用](use-alb-to-implement-canary-releases.md)[ALB](use-alb-to-implement-canary-releases.md)[实现灰度发布](use-alb-to-implement-canary-releases.md)：通过配置基于特定条件或不同服务器组流量权重的监听转发规则，将部分请求转发至新版本应用，逐步验证新版本稳定性，实现灰度发布。
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
