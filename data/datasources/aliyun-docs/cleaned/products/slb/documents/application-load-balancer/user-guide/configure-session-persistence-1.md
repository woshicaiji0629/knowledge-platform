# 配置会话保持-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/configure-session-persistence-1

# 配置会话保持
部分应用业务场景下需要保持用户会话的状态，例如购物车中的商品、登录信息、用户偏好设置、游戏应用等场景，如果用户的请求被分发到不同的服务器，那么会话状态就会丢失从而导致用户体验问题。当您开启了ALB会话保持功能后，可以使来自同一客户端的请求被转发到同一台后端服务器上，从而确保用户的体验和数据的一致性。
## 背景信息
默认情况下，ALB会将每个客户端请求分别分发至不同的后端服务器上。[开启会话保持](configure-session-persistence-1.md)后，同一客户端的请求会被转发至同一台后端服务器上，方便后端服务器维护状态信息及向客户端提供持续体验。
未开启会话保持：同一客户端的请求通过ALB可能会被分发至不同的后端服务器，在某些场景下，如登录后端服务器获取交互信息等场景，客户端的请求可能需重新登录后端服务器。
开启会话保持：同一客户端的请求通过ALB被分配至同一台后端服务器，而非分配至不同的后端服务器，在某些场景下，如登录后端服务器获取交互信息等场景，避免了客户端的请求需要重新登录后端服务器。
ALB开启会话保持后，需要选择Cookie的处理方式，有植入Cookie和重写Cookie两种处理方式。
植入Cookie：客户端第一次访问时，ALB会在返回请求中植入Cookie（即ALB插入SERVERID和SERVERCORSID两个cookie；SERVERCORSID是以SERVERID为基础，且加入了samesite=None这个属性），下次客户端携带此Cookie访问，负载均衡服务会将请求定向转发给之前记录到的后端服务器上。
说明
会话保持植入Cookie方式自带SameSite=None，无需用户配置，可以有效解决ALB转发规则中跨域（CORS）场景下浏览器无法保存Cookie的问题。
重写Cookie：当ALB发现用户自定义了Cookie，将会对原来的Cookie进行重写，下次客户端携带新的Cookie访问，ALB会将请求定向转发给之前记录的后端服务器。
## 使用限制
服务器组类型为函数计算类型时，您无需配置会话保持。更多操作，请参见[创建/删除服务器组](create-and-manage-a-server-group.md)。
## 前提条件
您已经创建了一个处于运行中状态的公网ALB实例。具体操作，请参见[创建和管理](create-and-manage-alb-instances.md)[ALB](create-and-manage-alb-instances.md)[实例](create-and-manage-alb-instances.md)。
您已经创建了服务器类型或IP类型的服务器组。具体操作，请参见[创建/删除服务器组](create-and-manage-a-server-group.md)。
您已经创建了后端服务器ECS01和ECS02，用于接收请求。ECS01和ECS02中部署了不同的后端服务，访问时需要有不同展示，例如访问ECS01时返回"Hello World ! This is ECS01."，返回ECS02时返回"Hello World ! This is ECS02."。注意安全组需要对相应服务端口放行。
您已将后端服务器ECS01与ECS02添加到服务器组中。具体操作，请参见[添加/移除后端服务器](create-and-manage-a-server-group.md)。
您已经为该实例配置了监听。具体操作，请参见[添加](../../add-an-http-listener.md)[HTTP](../../add-an-http-listener.md)[监听](../../add-an-http-listener.md)、[添加](add-an-https-listener.md)[HTTPS](add-an-https-listener.md)[监听](add-an-https-listener.md)或[添加](add-a-quic-listener.md)[QUIC](add-a-quic-listener.md)[监听](add-a-quic-listener.md)。
## 步骤一：配置会话保持
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏处，选择后端服务器组所属的地域。
在左侧导航栏，选择应用型负载均衡 ALB>服务器组。
在服务器组页面，找到目标服务器组，在操作列单击编辑基本信息。
在编辑基本信息对话框中，开启会话保持。
打开会话保持开关并选择Cookie处理方式。
选择植入Cookie，输入会话保持超时时间，然后单击保存。
超时时间不宜设置过长（建议短连接场景设置为60~300秒），否则同一客户端的请求会持续路由到同一台后端服务器，可能导致负载不均衡。
选择重写Cookie，输入Cookie名称，然后单击保存。
本文示例将Cookie名称设置为BACKEND_SERVER，该名称仅为示例，您可以自定义该名称。
## （可选）步骤二：后端服务器配置Cookie
当服务器组开启会话保持，并且选择的Cookie处理方式为重写Cookie时，才需要在后端服务器中配置对应的Cookie。
远程登录ECS。具体操作，请参见[ECS](../../../../ecs/documents/user-guide/connect-to-instance.md)[远程连接操作指南](../../../../ecs/documents/user-guide/connect-to-instance.md)。
根据不同的Web服务器配置Cookie。
说明
不同的Web服务器对应的Cookie设置方法不同，以下列举常见Web服务器的设置方法，请您根据实际情况选择，如果您使用的Web服务器不在以下列表中，请您查阅对应的官方文档获取配置方法。
## Nginx
此处以CentOS 7.9操作系统、Nginx 1.20.1 版本配置为例介绍。具体请以您实际使用的环境为准。
修改Nginx服务配置文件并保存，修改点可参考下方说明。执行nginx -t命令查看配置文件所在路径，默认通常为/etc/nginx/nginx.conf，具体请以实际环境为准。
http { # ... server { listen 80; # BACKEND_SERVER是您配置重写Cookie时输入的Cookie名称；value您可使用自定义字符串。 add_header Set-Cookie "BACKEND_SERVER=value"; # ... } }
执行以下命令重新加载Nginx的配置文件。
sudo nginx -s reload
## Apache
此处以CentOS 7.9操作系统、Apache 2.4.6版本配置为例介绍。具体请以您实际使用的环境为准。
修改Apache服务配置文件并保存，修改点可参考下方说明。默认通常为/etc/httpd/conf/httpd.conf，具体请以实际环境为准。
# ... Listen 80 # BACKEND_SERVER是您配置重写Cookie时输入的Cookie名称；value您可使用自定义字符串。 Header always set Set-Cookie "BACKEND_SERVER=value" # ...
执行以下命令，重新加载Apache的配置文件，使以上改动生效。
sudo systemctl reload httpd.service
参考以上步骤，修改服务器组中其余后端服务器的配置。
## 步骤三：测试会话保持的有效性
登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏选择地域。找到目标ALB实例，复制其对应的DNS名称。
在浏览器中输入DNS名称，可访问某个服务器，多次刷新页面仍然访问相同服务器。
例如您第一次访问的是ECS01，则后续几次刷新后均是访问ECS01。
如果多次刷新页面后在ECS01与ECS02之间切换，则会话保持配置不生效，请您检查配置是否有误再重新测试。
## 相关文档
如果配置过程中遇到问题，您可参考[ALB](../support/faq-about-alb.md)[常见问题](../support/faq-about-alb.md)进行定位处理。
如果遇到健康检查异常问题，您可参考[ALB](../support/how-do-i-troubleshoot-health-check-errors.md)[健康检查异常排查方法](../support/how-do-i-troubleshoot-health-check-errors.md)。
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
