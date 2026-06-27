# ALB健康检查-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/alb-health-check

# ALB健康检查
ALB支持通过健康检查持续监控后端服务器的运行状况，自动屏蔽异常服务器，确保业务可用性。
用户可以为每个服务器组独立配置健康检查。每个服务器组默认开启健康检查。
开启健康检查后，ALB会持续监控服务器组中所有后端服务器的运行状况，并自动将请求路由至健康检查正常的服务器。后端服务器需连续通过指定次数（健康阈值）的健康检查才会被判定为正常，以避免网络抖动导致的误判。
当某台后端服务器健康检查出现异常时，ALB会自动将新的请求分发到其他健康检查正常的后端服务器。
当该服务器恢复正常运行时，ALB会将其自动恢复到负载均衡服务中。
健康检查为短连接，完成健康检查后连接将关闭。
如果同一个服务器组中仅包含健康检查异常的服务器，ALB仍会尝试根据调度算法将请求路由至这些服务器，而不考虑这些服务器的运行状况，以最大可能避免业务受损。
说明
如果后端服务器权重设置为0，该服务器不会参与健康检查。
ALB通过特定IP地址与后端服务器通信和健康检查，请确保后端服务器未屏蔽这些地址（包括iptables或安全策略软件）：
[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)使用所在交换机网段的私网地址（Local IP）通信，可在实例详情页查看。
升级前的ALB实例使用内网地址段100.64.0.0/10与后端服务器通信。
## 创建健康检查
## 控制台
前往ALB控制台的[健康检查](https://slb.console.aliyun.com/alb/cn-hangzhou/health-check-templates)页面。
在顶部菜单栏选择目标地域后，单击创建健康检查。完成以下配置，然后单击创建。
健康检查名称：输入健康检查名称。
协议：选择健康检查协议。
HTTP：通过发送HEAD或GET请求检查服务器应用是否健康。
HTTPS：通过发送HEAD或GET请求检查服务器应用是否健康。标准版和WAF增强版ALB实例支持，基础版不支持。
TCP：通过发送SYN握手报文检测服务器端口是否存活。
gRPC：通过发送POST或GET请求检查服务器应用是否健康。
健康检查方法：仅在健康检查协议为HTTP、HTTPS或gRPC时可配置。
HEAD（HTTP/HTTPS默认）：请确保后端服务器支持HEAD请求。不支持时可改用GET。
POST（gRPC默认）：请确保后端服务器支持POST请求。不支持时可改用GET。
GET：响应报文超过8KB会被截断，但不影响健康检查结果判定。
健康检查HTTP协议版本：支持HTTP1.0或HTTP1.1。仅在健康检查协议为HTTP或HTTPS时可配置。
端口：健康检查探测端口。默认为空，表示使用后端服务器端口。取值范围1~65535，仅支持填写一个端口号。
路径：健康检查探测路径，如/health，建议指向静态页面。不填时默认探测根路径（/）。仅在健康检查协议为HTTP、HTTPS或gRPC时可配置。
域名：健康检查域名。默认使用后端服务器内网IP。仅在健康检查协议为HTTP、HTTPS或gRPC时可配置。
健康状态返回码：仅当探测请求返回指定状态码时判定为健康。仅在健康检查协议为HTTP、HTTPS或gRPC时可配置。
HTTP/HTTPS协议：可选http_2xx、http_3xx、http_4xx、http_5xx。默认选择http_2xx和http_3xx。
gRPC协议：状态码范围0~99，最多支持20个范围值，多个值用半角逗号（,）隔开。
警告
将4XX或5XX纳入健康状态码可能导致故障实例无法被及时剔除。建议优先确保后端服务返回正确的2XX或3XX状态码。
健康检查响应超时时间：后端服务器在指定时间内未返回正确响应，则判定为健康检查失败。取值范围1~300秒，默认5秒。
健康检查间隔时间：两次健康检查的时间间隔。取值范围1~50秒，默认2秒。
健康检查健康阈值：连续成功指定次数后判定为健康。取值范围2~10，默认3次。
健康检查不健康阈值：连续失败指定次数后判定为不健康。取值范围2~10，默认3次。
标签及资源组：
标签键和标签值：以键值对形式标记健康检查，便于筛选管理。
选择资源组：选择健康检查归属的[资源组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/create-a-resource-group#task-xpl-kjm-4fb)。
健康检查创建完成后，可以在创建服务器组时，在健康检查配置中选择已创建的健康检查。
支持在[创建服务器组](create-and-manage-a-server-group.md)时配置健康检查，并选中将新的配置保存为健康检查，方便下次快速复制使用。
## API
调用[CreateHealthCheckTemplate](../developer-reference/api-alb-2020-06-16-createhealthchecktemplate.md)创建健康检查模板。
调用[ApplyHealthCheckTemplateToServerGroup](../developer-reference/api-alb-2020-06-16-applyhealthchecktemplatetoservergroup.md)将健康检查模板应用到服务器组。
## 编辑健康检查
警告
关闭健康检查后，ALB不再检查后端服务器，一旦某台后端服务器发生故障，则无法实现访问流量自动切换至其他正常的后端服务器。
如延长健康检查的间隔时间，后端服务器出现故障时，ALB发现故障后端服务器的时间也会变长。
## 控制台
前往ALB控制台的[健康检查](https://slb.console.aliyun.com/alb/cn-hangzhou/health-check-templates)页面。
找到目标健康检查，在操作列单击编辑。
在编辑健康检查对话框中，修改健康检查参数配置，然后单击保存。
也可以[在服务器组页面编辑健康检查](create-and-manage-a-server-group.md)。
## API
调用[UpdateHealthCheckTemplateAttribute](../developer-reference/api-alb-2020-06-16-updatehealthchecktemplateattribute.md)更新健康检查模板的属性。
## 查看健康检查状态
若ALB实例已配置监听且服务器组已开启健康检查，可以在监听页签查看后端服务器的健康检查状态。
## 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/slbs)页面。
找到目标ALB实例，单击实例ID。
单击监听页签，在监听列表的健康检查状态列查看后端服务器的健康检查状态。
## API
调用[GetListenerHealthStatus](../developer-reference/api-alb-2020-06-16-getlistenerhealthstatus.md)查询监听的健康检查状态。
## 删除健康检查
## 控制台
前往ALB控制台的[健康检查](https://slb.console.aliyun.com/alb/cn-hangzhou/health-check-templates)页面。
找到目标健康检查，在操作列单击删除。
在弹出的删除对话框中，确认提示信息，然后单击确定。
## API
调用[DeleteHealthCheckTemplates](../developer-reference/api-alb-2020-06-16-deletehealthchecktemplates.md)删除健康检查模板。
## 应用于生产环境
创建专用健康检查端点：推荐创建专用接口（如/health），始终返回 HTTP 200 状态码。避免使用业务路径，业务路径可能因权限校验或资源不存在返回 4XX。
健康检查失败时优先修复后端服务：排查并修复后端服务问题，使健康检查路径返回正确的 2XX 或 3XX 状态码，而非放宽状态码判定条件。
合理配置健康检查参数：默认配置适用于大多数场景。如果后端服务启动较慢，可适当增大健康检查间隔或不健康阈值；如果网络延迟较高，可适当增大响应超时时间。
使用 curl 命令模拟健康检查：排查健康检查问题时，可参考以下命令模拟 ALB 的健康检查行为，根据实际配置替换方法（HEAD/GET）、域名、IP和端口：
curl -Iv -X HEAD --http1.0 -H "Host: your-domain.com" http://backend_ip:port/health_path
## 计费
健康检查不产生额外费用。ALB实例的计费规则请参见[ALB](../product-overview/alb-billing-rules.md)[计费说明](../product-overview/alb-billing-rules.md)。
## 配额
一个地域最多支持50个健康检查模板，不支持提升。
## 相关文档
[健康检查常见问题](../support/faq-about-alb.md)
[健康检查异常排查方法](../support/how-do-i-troubleshoot-health-check-errors.md)
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
