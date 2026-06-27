# 修改Tair实例的同步模式为半同步-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/modify-the-synchronization-mode-of-a-persistent-memory-optimized-instance

# 修改Tair（企业版）实例的同步模式
Tair（企业版）实例的默认同步模式为异步，若业务场景对数据持久化要求较高，您可以在控制台将其同步模式修改为半同步。该模式会增加写的延迟，大约为百微秒（us）~数毫秒（ms），适用于对数据一致性要求高，可以接受牺牲写性能的场景。
## 前提条件
实例需满足以下条件：
内存型（兼容Redis 6.0及以上）：小版本为24.8.0.0及以上。
磁盘型：小版本为2.5.2及以上。
说明
低版本实例可在升级小版本后使用该功能，更多信息请参见[升级小版本与代理版本](update-the-minor-version.md)。
## 同步模式概述
原生Redis采用的主备节点同步模式为异步（Async），即当客户端发起更新请求时，主节点（Master）完成操作后会立即响应客户端，同时主节点向备节点（Replica）同步数据。当主节点不可用时引发高可用（High Availability）切换，而此时主备节点可能会存在数据不一致的情况。
半同步（Semisync）即客户端发起的更新在主节点执行完成后，主节点会将日志同步到备节点，待备节点确认接收后才返回信息给客户端，保证高可用切换后数据不丢失（RPO为0）。
下图为异步和半同步的流程图：
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在基本信息的右侧，单击变更同步模式。
在右侧弹出的面板中，完成下述配置。
| 配置 | 说明 |
| --- | --- |
| 同步模式 | 支持如下选项： 半同步 ：主节点将更新操作复制至备节点后，才返回信息给客户端。 重要 当备实例不可用或者主备实例间出现网络异常时，半同步会退化为异步。 异步 （默认）：使用异步复制。 |
| 退化阈值 | 仅 半同步 支持配置该参数，单位为 ms，取值范围为 10~60000，默认为 500。 当同步延迟超出该阈值时， 同步模式 会自动转为 异步 ，当同步延迟消除后， 同步模式 会自动转换为 半同步 。 |
单击确定。
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
