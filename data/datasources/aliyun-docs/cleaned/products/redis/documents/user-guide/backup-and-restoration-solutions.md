# 数据持久化与备份恢复体系-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/backup-and-restoration-solutions

# 备份与恢复
备份（内存中数据的持久化）是指定期将内存中的数据存储到磁盘中。如遇到业务异常造成的数据丢失或错误，能够利用备份文件恢复数据。为满足各类场景下对备份与恢复的需求，实例提供RDB、AOF和Tair-Binlog持久化策略。
## 持久化策略
### RDB
RDB持久化是指周期性地为引擎中保存的数据创建快照，生成RDB文件，保存到磁盘中，实现数据的持久化。RDB文件占用空间小，便于移动，非常适合用于备份或迁移指定时间点的数据。
开源Redis在生成RDB文件时会可能会带来操作阻塞，阻塞时间取决于实例的数据总量。而云数据库 Tair（兼容 Redis）实例对此优化并实现了“无阻塞备份”，使实例的备份不影响客户端请求。
云数据库 Tair（兼容 Redis）的RDB持久化策略默认每天备份一次，您可以根据业务需求修改自动备份策略，也可以手动发起临时的备份。
### AOF
AOF持久化是指以日志的形式记录所有的写入类操作（例如SET）。当AOF文件过大时，实例会自动执行AOF Rewrite，重组AOF文件，降低其占用的存储空间。
云数据库 Tair（兼容 Redis）的AOF持久化策略为AOF_FSYNC_EVERYSEC，每秒异步将AOF缓冲区中的命令写入磁盘。此策略能相对降低AOF开启对实例的性能影响。
### Tair-Binlog
Tair（企业版）内存型不仅支持上述两种持久化策略，还优化了基于AOF（Append-only-file）的持久化机制，实现AOF增量归档，避免了AOF Rewrite对服务性能的影响，同时完整保留了每一次写操作与其时间戳，可以将实例整体或指定Key的数据恢复至某个秒级的时间点（PITR，point-in-time recovery）。更多信息，请参见[通过数据闪回按时间点恢复数据](use-data-flashback-to-restore-data-by-point-in-time.md)。
## 备份恢复方案
云数据库 Tair（兼容 Redis）实例基于RDB持久化、AOF持久化和AOF增量归档，实现数据的备份与恢复。
| 类别 | 实施方案 | 说明 |
| --- | --- | --- |
| 数据备份 | [自动或手动备份](automatic-or-manual-backup.md) | 支持数据持久化，实例会按照默认的策略自动备份数据（基于 RDB），您可以根据业务需求修改自动备份策略，也可以手动发起临时的备份。 |
| [下载备份文件](download-a-backup-file.md) | 备份文件支持保留 7~730 天，如果需要更长时间的备份存档（例如监管或信息安全需要），您可以将备份文件下载到本地进行存储。 |  |
| 数据恢复 | [从备份集恢复至新实例](restore-data-from-a-backup-set-to-a-new-instance.md) | 支持从指定的备份集创建新实例，新实例中的数据将和该备份集中的数据一致，可用于数据恢复、快速部署业务或数据验证等场景。 |
| [通过数据闪回按时间点恢复数据](use-data-flashback-to-restore-data-by-point-in-time.md) | 开启数据闪回功能（基于 AOF）后，在备份文件的保存期内，您可以恢复指定时间点（精确到秒级）的数据，可最大限度地避免误操作带来的数据损失，或者在频繁回档的业务场景中快速完成数据切换。 说明 该功能仅 Tair（企业版） [内存型](../product-overview/dram-based-instances.md) 支持。 |  |
## 备份的数据保护
防篡改：云数据库 Tair（兼容 Redis）RDB备份数据和Tair-Binlog数据都存储在OSS中，都具备WORM（write once read many）不可篡改特性。
防恶意/误删除：
手动删除：仅允许删除手动备份的数据，不允许删除自动备份的数据。
自动过期删除：当备份数据到期后将自动被删除。但不允许关闭自动备份功能，每周至少需进行1次[自动备份](automatic-or-manual-backup.md)，且每份自动备份数据需保留7天及以上。因此自动备份数据无法完全删除。
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
