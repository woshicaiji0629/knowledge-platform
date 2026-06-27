# 升级SSD云盘至ESSD云盘-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/upgrade-from-standard-ssds-to-essds

# 升级SSD云盘至ESSD云盘
相较于SSD云盘，ESSD PL1云盘基于新一代分布式块存储架构，具备更高的IOPS、更高的吞吐量和更稳定的I/O性能，并且在大部分地域中两者费用相同。您可以通过控制台将存储类型从SSD云盘升级到ESSD PL1云盘，享受更高的性价比。
## 前提条件
实例的状态为运行中。
实例的存储类型为SSD云盘。
## 云盘性能对比
ESSD PL1云盘和SSD云盘的费用相近但性能差别较大，具体请参见下表。
| 性能类别 | ESSD 云盘（PL1） | SSD 云盘 |
| --- | --- | --- |
| 单盘最大容量（GiB） | 20~64000 | 6000 |
| 最大 IOPS | 50000 | 25000 |
| 最大吞吐量（MB/s） | 350 | 300 |
| 单盘 IOPS 性能计算公式 | min{1800+50*容量, 50000} | min{1800+30*容量, 25000} |
| 单盘吞吐量性能计算公式（MB/s） | min{120+0.5*容量, 350} | min{120+0.5*容量, 300} |
| 单路随机写平均时延（ms） | 0.2 | 0.5~2 |
## 费用
升级包含如下费用：
备份费用：为保证数据安全，系统会为实例做一次临时全量备份，保留7天时间，该备份可能会产生备份费用。更多信息，请参见[备份费用](../apsaradb-rds-for-mysql/billable-items-and-pricing-for-the-backup-storage-of-an-apsaradb-rds-for-mysql-instance.md)。
ESSD云盘费用：根据实例所在地域的不同，升级存储类型可能会产生一定的费用，您可以在变配时看到费用信息。
## 影响
升级存储类型会出现约30秒的闪断，请在业务低峰期进行变配，并确保您的应用有自动重连机制。
实例升级存储类型期间无法对该实例执行升降配、版本升级、跨可用区迁移等实例级别的操作。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息区域，单击存储类型右侧的升级存储类型。
说明
如果没有找到升级存储类型，请确认是否本文的前提条件中的要求。如果符合前提条件要求，仍未找到按钮，说明该地域没有ESSD资源。
在变配实例页签，选中服务条款，单击右下角的去支付并完成支付。
此时实例状态会变更为升降配中，等待实例状态恢复成运行中即表示升级完成。
## 常见问题
Q：变更配置时，是否会影响线上业务？
A：请参见[影响](../apsaradb-rds-for-mysql/upgrade-the-storage-type-of-an-apsaradb-rds-for-mysql-instance-from-standard-ssds-to-essds.md)。
Q：变更存储类型后，实例的地址会变化吗？
A：实例的连接地址（如rm-bpxxxxx.mysql.rds.aliyuncs.com）不会变化，但是对应的IP地址可能会变化。建议在应用程序中使用连接地址，而不是IP地址。
## 相关API
| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec](../api-change-instance-configuration.md) | 变更 RDS 实例配置。 |
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
