# 为包年包月实例手动续费与管理自动续费-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/renewal

# 续费实例
为避免实例到期后停机，对您的服务造成影响，请及时完成续费或开通自动续费。续费功能仅适用于包年包月云数据库 Tair（兼容 Redis）实例，按量付费实例不需要续费，您只需要保证账户可用余额充足即可。
云数据库 Tair（兼容 Redis）支持两种续费方式：
自动续费（推荐）
为避免因忘记手动续费导致资源被自动释放，建议您开通自动续费。
开通后，实例会在每次到期前自动续费，请您务必保证账户可用余额充足，若在到期前7天仍未自动扣款成功，系统将通过短信或者邮件进行提醒。
说明
若因账户余额不足导致自动续费失败（即实例到期），实例不会再尝试自动续费，此时您必须在实例自动释放前手动续费。
手动续费
在使用实例的过程中（截止实例释放前），您可以随时手动续费。
## 开通自动续费
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在实例状态区域框，单击自动续费右侧的开关。
在右侧弹出的自动续费面板中，打开自动续费开关，阅读提示信息并选择自动续费的时长。
说明
开通自动续费后，系统将以选择的续费时长进行续费。例如您选择了自动续费时长为3个月，那么每次自动续费时会缴纳3个月的费用。
单击开通自动续费。
### 如何调整自动续费周期或关闭自动续费？
访问[自动续费管理](https://usercenter2.aliyun.com/renew/auto)页面。
在实例ID文档框中搜索目标实例ID。
找到目标实例，在右侧操作列下，单击修改自动续费或恢复手动续费。
## 手动续费实例
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域。
在目标实例的操作列，单击续费。
在跳转到的续费页面，选择续费时长。
阅读服务协议，单击立即购买。
根据提示完成支付流程。
## 常见问题
Q：续费时报错Specified network type does not support this operation？
A：可能是实例未释放经典网络连接地址，该实例仍存在相关限制。请释放经典网络连接地址后重试。更多信息请参见[【通知】云数据库 Tair（兼容 Redis）下线经典网络](notice-apsaradb-for-redis-instances-deployed-in-classic-network-discontinued.md)。
## 相关API
| API | 说明 |
| --- | --- |
| [RenewInstance](../developer-reference/api-r-kvstore-2015-01-01-renewinstance-redis.md) | 为实例续费。 |
| [ModifyInstanceAutoRenewalAttribute](../developer-reference/api-r-kvstore-2015-01-01-modifyinstanceautorenewalattribute-redis.md) | 调用该 API 可以开启或关闭实例的自动续费功能。 |
| [DescribeInstanceAutoRenewalAttribute](../developer-reference/api-r-kvstore-2015-01-01-describeinstanceautorenewalattribute-redis.md) | 调用该 API 可以查看实例的自动续费详情。 |
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
