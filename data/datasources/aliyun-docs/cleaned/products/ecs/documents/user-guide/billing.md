# 突发性能实例计费组成与CPU积分额外费用-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/billing

# 突发性能实例计费
突发性能实例通过消耗CPU积分来维持运行性能，可以在业务平峰期积累CPU积分余额，用于在业务高峰期提高运行性能，从而节约成本。但如果实例消耗了预支CPU积分或超额CPU积分，可能产生额外费用，因此突发性能实例费用分为实例购买费用和额外费用。
## 实例购买费用
购买突发性能实例时支持按量付费、包年包月、抢占式实例等计费方式。不同计费方式的区别，请参见[计费方式概述](../overview-of-billing-methods.md)。详细的实例规格定价，请参见[详细价格总览](https://www.aliyun.com/price/product#/ecs/detail)。
如果实例计费方式为按量付费，您可以购买预留实例券抵扣实例的按量账单，更多信息，请参见[预留实例券概述](overview-6.md)。但是，如果预留实例券的实例规格为t5，存在以下限制：
- 仅支持购买可用区级预留实例券。
- 购买后不支持拆分和合并预留实例券。
## 额外费用
突发实例的性能模式会影响实例计费，规则如下：
说明购买或使用突发性能实例时，您可以选择是否打开无性能约束模式。关于无性能约束模式下CPU积分的消耗规则，请参见[无性能约束模式](burst-performance-instance-overview.md)。
- 性能约束模式：仅需支付实例购买费用，使用实例时不产生额外费用。
- 无性能约束模式：在支付实例购买费用的基础上，部分情况下还需要支付额外费用。收取费用情况说明如下：
- 如果实例将预支CPU积分消耗完毕后，继续消耗了超额CPU积分。超额CPU积分按小时出账单并收取费用。
- 如果实例消耗了预支CPU积分，并在预支CPU积分恢复完毕前停止（节省停机模式）、变配或释放实例，或者切换到性能约束模式，则会一次性收取预支CPU积分的费用。
在无性能约束模式下，不同地域及实例类型消耗CPU积分所收取的额外费用标准如下表所示。
| 地域 | Windows 实例（元/积分） | Linux 实例（元/积分） |
| --- | --- | --- |
| 中国内地地域 | 0.005 | 0.005 |
| 非中国内地地域 | 0.01 | 0.005 |
额外收费情况示例如下：
- 示例一：地域为中国内地，实例类型为Linux实例，预支CPU积分消耗完毕继续消耗了100个超额CPU积分。则收取的额外费用=100*0.005=0.5元。
- 示例二：地域为非中国内地，实例类型为Windows实例，消耗了200个预支CPU积分，并在预支CPU积分恢复到100个时切换为性能约束模式，则收取的额外费用=100*0.01=1元。
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
