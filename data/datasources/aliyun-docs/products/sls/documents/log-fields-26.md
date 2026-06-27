# 传统型负载均衡CLB 7层访问日志字段说明-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/log-fields-26

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 日志字段详情

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍负载均衡7层访问日志的字段详情。

| 字段 | 说明 |
| --- | --- |
| body_bytes_sent | 发送给客户端的 http body 的字节数。 |
| client_ip | 请求客户端 IP 地址。 |
| client_port | 请求客户端端口。 |
| host | 优先从请求参数中获取 host，如果获取不到则从 host header 取值，如果还是获取不到则以处理请求的后端服务器 IP 地址作为 host。 |
| http_host | 请求报文 host header 的内容。 |
| http_referer | 负载均衡收到的请求报文中 HTTP 的 referer header 的内容。 |
| http_user_agent | 负载均衡收到的请求报文中 http_user_agent header 的内容。 |
| http_x_forwarded_for | 负载均衡收到的请求报文中 x-forwarded-for header 的内容。 |
| http_x_real_ip | 客户端真实的 IP 地址。 |
| read_request_time | 负载均衡读取请求的时间，单位：毫秒。 |
| request_length | 请求报文的长度，包括 startline、http header 和 http body。 |
| request_method | 请求报文的方法。 |
| request_time | 负载均衡收到第一个请求报文的时间到 SLB 返回应答之间的间隔时间，单位：秒。 |
| request_uri | 负载均衡收到的请求报文的 URI。 |
| scheme | 请求的 scheme，包括 http、https。 |
| server_protocol | 负载均衡收到的 HTTP 协议的版本，例如 HTTP/1.0 或 HTTP/1.1。 |
| slb_vport | 负载均衡的监听端口。 |
| slbid | 负载均衡实例 ID。 |
| ssl_cipher | 建立 SSL 连接使用的密码，例如 ECDHE-RSA-AES128-GCM-SHA256 等。 |
| ssl_protocol | 建立 SSL 连接使用的协议，例如 TLSv1.2。 |
| status | 负载均衡应答报文的状态。 |
| tcpinfo_rtt | 客户端 TCP 连接时间，单位：微秒。 |
| time | 日志记录时间。 |
| upstream_addr | 后端服务器的 IP 地址和端口。 |
| upstream_response_time | 从与后端建立连接开始到接受完数据然后关闭连接为止的时间，单位：秒。 |
| upstream_status | 负载均衡收到的后端服务器的响应状态码。 |
| vip_addr | 虚拟 IP 地址。 |
| write_response_time | 负载均衡写的响应时间，单位：毫秒。 |


[上一篇：开通访问日志功能](products/sls/documents/enable-the-access-log-management-feature.md)[下一篇：传统型负载均衡CLB 4层秒级监控指标](products/sls/documents/layer-4-monitoring-metrics-for-clb-usage-notes.md)

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
