# 如何在负载均衡控制台上开通访问日志功能-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/enable-the-access-log-management-feature

# 开通访问日志功能
本文介绍如何在负载均衡控制台上开通访问日志功能，将CLB 7层访问日志采集到日志服务中。
## 前提条件
已创建CLB实例。具体操作，请参见[创建实例](../../slb/documents/classic-load-balancer/getting-started/create-a-clb-instance.md)。
已为CLB实例配置7层监听，即配置HTTP监听或HTTPS监听。具体操作，请参见[添加](../../slb/documents/classic-load-balancer/user-guide/add-an-http-listener-1.md)[HTTP](../../slb/documents/classic-load-balancer/user-guide/add-an-http-listener-1.md)[监听](../../slb/documents/classic-load-balancer/user-guide/add-an-http-listener-1.md)或[添加](../../slb/documents/classic-load-balancer/user-guide/add-an-https-listener-1.md)[HTTPS](../../slb/documents/classic-load-balancer/user-guide/add-an-https-listener-1.md)[监听](../../slb/documents/classic-load-balancer/user-guide/add-an-https-listener-1.md)。
在CLB实例所在地域，已创建日志服务Project和LogStore。具体操作，请参见[创建](getting-started.md)[Project](getting-started.md)[和](getting-started.md)[LogStore](getting-started.md)。
## 操作步骤
重要
如果您使用RAM用户开通访问日志功能，则需先为RAM用户授权。具体操作，请参见[RAM](common-operations-on-logs-of-alibaba-cloud-services.md)[用户授权](common-operations-on-logs-of-alibaba-cloud-services.md)。
登录[负载均衡控制台](https://slb.console.aliyun.com/slb)负载均衡控制台。
在页面左上角，选择地域。
在左侧导航栏，选择传统型负载均衡CLB>日志管理>访问日志。
根据页面提示，授权传统型负载均衡使用AliyunLogArchiveRole角色访问日志服务。
该操作仅在首次配置时需要，且需要由阿里云账号完成。
警告
请勿取消授权或删除AliyunLogArchiveRole角色，否则将导致日志无法正常推送到日志服务。
在访问日志（7层）页面，单击目标实例右侧的设置。
在日志设置页面，选择可用的项目Project和日志库LogStore，并单击确定。
配置完成后，日志服务默认为该LogStore创建索引。如果LogStore已有索引，则原有索引将被覆盖。
## 相关操作
| 操作 | 说明 |
| --- | --- |
| 查询访问日志 | 在 访问日志（7 层） 页面，找到目标实例，然后在 操作 列单击 查看日志 。具体操作，请参见 [查询访问日志](../../slb/documents/classic-load-balancer/user-guide/configure-access-logs.md) 。 |
| 关闭访问日志 | 在 访问日志（7 层） 页面，找到目标实例，然后在 操作 列单击 删除 。具体操作，请参见 [关闭访问日志](../../slb/documents/classic-load-balancer/user-guide/configure-access-logs.md) 。 重要 关闭访问日志功能，不会自动删除 Project 及已推送的日志。因此，当您关闭访问日志功能后，为避免后续产生不必要的费用，请在日志服务控制台上删除对应的 Project。具体操作，请参见 [管理](manage-a-project.md) [Project](manage-a-project.md) 。 |
## 后续步骤
将CLB 7层访问日志投递到日志服务后，您可以在日志服务中执行查询分析、下载、投递、加工日志，创建告警等操作。具体操作，请参见[云产品日志通用操作](common-operations-on-logs-of-alibaba-cloud-services.md)。
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
