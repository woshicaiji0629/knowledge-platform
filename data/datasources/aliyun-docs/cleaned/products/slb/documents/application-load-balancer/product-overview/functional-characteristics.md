# 功能特性-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/product-overview/functional-characteristics

# 功能特性
ALB功能版本：
基础版：提供应用型负载均衡的基本功能，可支持基于域名、URL、HTTP Header等路由转发。
标准版：在基础版之上，支持更多功能特性，增强了转发、安全、监控和连接管理等能力。
WAF增强版：在标准版之上，集成Web应用防火墙（[WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/product-overview/what-is-waf.md)），为Web业务提供应用层安全防护。
扩展版：基于灵活的“服务扩展”能力，提供身份认证、基于内容的路由等核心流量治理功能，并新增多模型代理、负载感知路由、Token限速等AI原生特性，打造面向AI及传统应用的一体化智能流量入口。
ALB的[实例性能指标](what-is-alb.md)与功能版本无关。[ALB](../../product-overview/alb.md)[升级实例](../../product-overview/alb.md)支持通过[安全组](../user-guide/add-an-alb-instance-to-a-security-group.md)或[访问控制策略组（ACL）](../user-guide/network-acls.md)管理流量，而升级前的实例仅支持ACL。如需使用安全组，请[新建实例](../user-guide/create-and-manage-alb-instances.md)或联系商务经理对存量实例进行升级。
| 功能 | 基础版 | 标准版 | WAF 增强版 | 扩展版 |
| --- | --- | --- | --- | --- |
| 监听协议 |  |  |  |  |
| HTTP/1.1 协议 | 支持 | 支持 | 支持 | 支持 |
| HTTP/2 协议 | 支持 | 支持 | 支持 | 支持 |
| HTTP/3 协议 | 支持 | 支持 | 支持 | 暂不支持 |
| QUIC 协议 | 支持 | 支持 | 支持 | 暂不支持 |
| WEBSOCKET 协议 | 支持 | 支持 | 支持 | 支持 |
| 转发规则 |  |  |  |  |
| 基于域名或路径匹配 | 支持 | 支持 | 支持 | 支持 |
| 基于 HTTP Header 匹配 | 支持 | 支持 | 支持 | 支持 |
| 基于查询字符串匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 基于 Cookie 匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 基于 HTTP 请求方法匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 基于源 IP 匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 基于 AI 模型匹配 | 不支持 | 不支持 | 不支持 | 支持 |
| 基于响应中的状态码匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 基于响应中的 Header 匹配 | 不支持 | 支持 | 支持 | 暂不支持 |
| 转发至 | 支持 | 支持 | 支持 | 支持 |
| 重定向 | 支持 | 支持 | 支持 | 支持 |
| 重写或返回固定响应 | 不支持 | 支持 | 支持 | 支持 |
| 写入 Header 或删除 Header | 不支持 | 支持 | 支持 | 支持 |
| 容错回退 | 不支持 | 不支持 | 不支持 | 支持 |
| 流量镜像 | 不支持 | 支持 | 支持 | 暂不支持 |
| QPS 限速 | 不支持 | 支持 | 支持 | 暂不支持 |
| CORS 跨域 | 不支持 | 支持 | 支持 | 暂不支持 |
| 可编程脚本 AScript | 不支持 | 支持 | 支持 | 不支持 |
| 服务扩展 |  |  |  |  |
| 组件库 | 不支持 | 不支持 | 不支持 | 支持 |
| 插件/外部调用 | 不支持 | 不支持 | 不支持 | 支持 |
| 后端服务类型 |  |  |  |  |
| 服务器类型、IP 类型、函数计算类型 | 支持 | 支持 | 支持 | 支持 |
| DNS 域名类型 | 不支持 | 不支持 | 不支持 | 支持 |
| AI 服务类型 | 不支持 | 不支持 | 不支持 | 支持 |
| 后端服务协议 |  |  |  |  |
| HTTP | 支持 | 支持 | 支持 | 支持 |
| HTTPS | 不支持 | 支持 | 支持 | 支持 |
| GRPC | 支持 | 支持 | 支持 | 暂不支持 |
| 安全 |  |  |  |  |
| 访问控制黑白名单 | 支持 | 支持 | 支持 | 不支持 |
| 安全组 | 支持 | 支持 | 支持 | 暂不支持 |
| TLS 加密算法套件选择 | 支持 | 支持 | 支持 | 暂不支持 |
| SNI 多证书支持 | 支持 | 支持 | 支持 | 支持 |
| RSA&ECC 双证书 | 支持 | 支持 | 支持 | 支持 |
| ECC 证书 | 支持 | 支持 | 支持 | 支持 |
| 国密 SM2 证书 | 不支持 | 支持 | 支持 | 暂不支持 |
| 全链路 HTTPS | 不支持 | 支持 | 支持 | 支持 |
| 双向认证 | 不支持 | 支持 | 支持 | 暂不支持 |
| 自定义 TLS 安全策略 | 不支持 | 支持 | 支持 | 暂不支持 |
| TLS 1.3 协议支持 | 支持 | 支持 | 支持 | 支持 |
| 健康检查 | 支持 | 支持 | 支持 | 支持 |
| 身份管理 | 不支持 | 不支持 | 不支持 | 支持 |
| 监控统计 |  |  |  |  |
| 访问日志 | 支持 | 支持 | 支持 | 支持 |
| 操作日志 | 支持 | 支持 | 支持 | 支持 |
| 基础监控项 | 支持 | 支持 | 支持 | 支持 |
| 链路追踪 | 不支持 | 支持 | 支持 | 暂不支持 |
| 高级特性 |  |  |  |  |
| ALB Ingress Controller（集成 ACK、ACS 等） | 不支持 | 支持 | 支持 | 暂不支持 |
| Web 应用安全防护（WAF） | 不支持 （可 [升级为](../use-cases/enable-waf-protection-for-alb.md) [WAF](../use-cases/enable-waf-protection-for-alb.md) [增强版](../use-cases/enable-waf-protection-for-alb.md) ） | 不支持 （可 [升级为](../use-cases/enable-waf-protection-for-alb.md) [WAF](../use-cases/enable-waf-protection-for-alb.md) [增强版](../use-cases/enable-waf-protection-for-alb.md) ） | 支持 | 暂不支持 |
| 开启全球加速 GA | 支持 | 支持 | 支持 | 暂不支持 |
| 查找真实客户端源 IP | 不支持 | 支持 | 支持 | 暂不支持 |
| 会话保持 | 支持 | 支持 | 支持 | 暂不支持 |
| 后端长连接 | 支持 | 支持 | 支持 | 支持 |
| 实例克隆 | 支持 | 支持 | 支持 | 暂不支持 |
| 慢启动 | 不支持 | 支持 | 支持 | 暂不支持 |
| 连接优雅中断 | 不支持 | 支持 | 支持 | 暂不支持 |
| 关闭跨 AZ 负载均衡 | 不支持 | 支持 | 支持 | 暂不支持 |
| 资源预留 | 不支持 | 支持 | 支持 | 暂不支持 |
| AI 代理 | 不支持 | 不支持 | 不支持 | 支持 |
| Token 限速 | 不支持 | 不支持 | 不支持 | 支持 |
| 入站/出站身份认证 | 不支持 | 不支持 | 不支持 | 支持 |
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
