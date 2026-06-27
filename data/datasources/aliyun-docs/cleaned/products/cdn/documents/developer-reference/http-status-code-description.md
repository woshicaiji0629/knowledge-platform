# HTTP状态码错误解析与处理方法-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/developer-reference/http-status-code-description

# HTTP状态码说明
本文为您介绍阿里云CDN产品响应的4xx、5xx系列状态码，提供相关状态码的说明和解决措施，方便您进行错误排查。
## 4XX状态码
4xx代码表示客户端响应错误。
### 400
原因：Bad Request
原因释义：错误请求
说明：表明客户端向源站发送了一个请求，由于请求本身的问题，该请求无法被理解或处理。
解决措施：请检查请求输入参数的合法性、正确性后重试。
### 401
原因：Unauthorized
原因释义：未授权
说明：表明客户端向源站发送请求时未包含正确的身份验证凭据，源站需要身份验证才能处理该请求。
解决措施：请携带正确的身份验证凭据或在源站为请求授权后重试。
### 403
原因：Forbidden
原因释义：禁止
说明：表示源站理解了客户端的请求，但由于权限不足，无法访问请求的资源，因此无法执行。
解决措施：请为客户端请求开启相应的权限后重试。
### 404
原因：Not Found
原因释义：未找到
说明：表示源站无法找到请求的资源。
解决措施：请修改正确的请求路径后重试或检查服务端URL路径是否对外暴露。
### 405
原因：Method Not Allowed
原因释义：方法不允许
说明：表示客户端使用的HTTP请求方法（如GET、POST、PUT等）对目标资源无效。
解决措施：请调整请求方法为源站支持的请求方法后重试。
### 406
原因：Not Acceptable
原因释义：不可接受
说明：表示所请求的资源不支持以符合客户端指定的内容协商标头的格式提供（例如，Accept-Charset或Accept-Language）。
解决措施：修改请求头字段为源站支持的类型后重试。
### 407
原因：Authentication Required
原因释义：需要身份验证
说明：表示客户端未提供通过代理源站访问请求资源所需的身份验证凭据。
解决措施：检查代理源站的身份验证是否过期，携带正确的代理源站签发的凭据后重试。
### 408
原因：Request Timeout
原因释义：请求超时
说明：表示源站未在合理的时间内收到完整的请求，并且不希望继续等待连接。
解决措施：建议尝试、适当延长源站处理时长或减小客户端请求包大小后重试。
### 409
原因：Conflict
原因释义：冲突
说明：表示由于与目标资源的当前状态冲突，请求无法完成。当多个客户端尝试编辑同一资源时，通常会在PUT请求的响应发生此错误。
解决措施：尝试刷新后重新提交信息，或者在源站中增加冲突处理机制候后重试。
### 410
原因：Gone
原因释义：已消失
说明：表示某个资源被有意永久删除时，源站会使用此状态码通知客户端该资源不再可用。
解决措施：客户端需要移除被永久删除资源的引用后重试。
### 411
原因：Length Required
原因释义：长度要求
说明：表示客户端未在请求头的Content-Length字段中指定请求主体的长度，而获取资源需要此信息。
解决措施：在客户端的请求头中携带Content-Length字段后重试；如无法估计长度时，可携带Transfer-Encoding: chunked字段定义分块传输编码。
### 412
原因：Precondition Failed
原因释义：先决条件不满足
说明：表示源站拒绝处理请求，因为资源不满足客户端指定的条件。
解决措施：请求携带正确的预置条件后重试。
### 413
原因：Payload Too Large
原因释义：有效负载太大
说明：表示源站拒绝处理请求，因为客户端发送的有效负载超出了源站可接受的大小限制。
解决措施：减少文件上传体积或提交数据大小后重试。
### 414
原因：URI Too Long
原因释义：URI太长
说明：表示源站拒绝处理请求，因为客户端提供的URI过长。
解决措施：缩短客户端请求URI长度或将长参数分为多次处理后在客户端汇总结果。
### 415
原因：Unsupported Media Type
原因释义：不支持的媒体类型
说明：表示源站拒绝处理请求，因为有效负载的格式不受支持。
解决措施：修改请求头中的Content-Type字段为服务端支持的格式后重试。
### 416
原因：Range Not Satisfiable
原因释义：范围不满足
说明：表示源站无法满足客户端请求头中Range字段指定的请求范围。
解决措施：检查请求头Range字段范围是否合法，修改Range范围后重新访问。
### 417
原因：Expectation Failed
原因释义：期望失败
说明：表示源站无法满足客户端请求头中Expect字段指定的要求。
解决措施：常见于测试场景，如果真实访问出现请禁用请求头中的Expect字段。
### 429
原因：Too Many Requests
原因释义：请求过多
说明：表示客户端在指定时间内发送了过多请求，具体时间由源站的速率限制规则决定。
解决措施：单位时间内请求次数超过了源站的限制，请过段时间重试，具体参考源站设置的重试间隔时长。
### 499
原因：Client Close Request
原因释义：客户端关闭请求
说明：当客户端在源站能够响应之前终止连接时，通常会发生此错误。这个状态码表示客户端主动关闭请求，所以客户端不会收到异常响应页面，因此无需定义错误码页面。
## 5XX状态码
### 500
原因：Internal Server Error
原因释义：内部服务错误
说明：表明您的源站存在问题，导致其无法满足请求。
解决措施：检查源站日志信息，查找具体错误后，再针对解决；也可以直接回退上一个正常的版本进行业务快速恢复。
### 502
原因：Bad Gateway
原因释义：网关错误
说明：表明阿里云CDN节点无法与您的源站建立连接。
解决措施：确定源站是否可用，其次检查源站防火墙规则是否对阿里云CDN节点放开。
### 503
原因：Service Temporarily Unavailable
原因释义：服务暂时不可用
说明：表明您的源站过载。
解决措施：检查源站负载情况，找到高负载应用进程后，使用相关工具排查高负载原因后对应解决。
### 504
原因：Gateway Timeout
原因释义：网关超时
说明：表明阿里云CDN节点无法与您的源站建立连接。
解决措施：检查源站状态是否可用或适当增加超时时间。
### 508
原因：Loop Detected
原因释义：检测到循环
说明：表明阿里云CDN节点收到的请求已经超出了循环进入阿里云CDN网络的上限次数。
解决措施：检查源站循环，确保循环有终止条件且能正常结束后重试。
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
