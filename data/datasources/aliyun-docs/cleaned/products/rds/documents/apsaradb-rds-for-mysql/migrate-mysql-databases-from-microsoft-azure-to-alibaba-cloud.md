# Azure Database for MySQL数据库迁移到阿里云-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-mysql-databases-from-microsoft-azure-to-alibaba-cloud

# Azure Database for MySQL数据库迁移到阿里云
本文介绍Microsoft Azure Database for MySQL数据库迁移到阿里云云数据库RDS MySQL的注意事项及操作步骤。
## 前提条件
| 源端及目标端 | 要求 |  |
| --- | --- | --- |
| 源端 | [Microsoft Azure Database for MySQL](https://docs.azure.cn/zh-cn/mysql/) [实例](https://docs.azure.cn/zh-cn/mysql/) | 已开通公网访问，并获取外网连接地址及端口。 已创建高权限账号。 如果源端实例配置了访问控制，请先在源端安全配置中 [添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) ，再配置数据迁移任务。 |
| 目标端 | 阿里云云数据库 RDS MySQL 实例 | 已 [创建阿里云](create-an-apsaradb-rds-for-mysql-instance-1.md) [RDS MySQL](create-an-apsaradb-rds-for-mysql-instance-1.md) [实例](create-an-apsaradb-rds-for-mysql-instance-1.md) 。 已 [创建高权限账号](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md) 。 阿里云 RDS MySQL 的存储空间须 大于 Azure Database for MySQL 已使用的存储空间。 |
## 注意事项
结构迁移不支持event的迁移。
DTS在执行全量数据迁移时将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升，在数据库性能较差、规格较低或业务量较大的情况下（例如源库有大量慢SQL、存在无主键表或目标库存在死锁等），可能会加重数据库压力，甚至导致数据库服务不可用。因此您需要在执行数据迁移前评估源库和目标库的性能，同时建议您在业务低峰期执行数据迁移（例如源库和目标库的CPU负载在30%以下）。
如果源库中待迁移的表没有主键或唯一约束，且所有字段没有唯一性，可能会导致目标数据库中出现重复数据。
对于数据类型为FLOAT或DOUBLE的列，DTS会通过ROUND(COLUMN,PRECISION)来读取该列的值。如果没有明确定义其精度，DTS对FLOAT的迁移精度为38位，对DOUBLE的迁移精度为308位，请确认迁移精度是否符合业务预期。
DTS会自动地在阿里云RDS MySQL中创建数据库，如果待迁移的数据库名称不符合阿里云RDS的定义规范，您需要在配置迁移任务之前在阿里云RDS MySQL中创建数据库。
说明
关于阿里云RDS的定义规范和创建数据库的操作方法，请参见[创建数据库](create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。
对于迁移失败的任务，DTS会触发自动恢复。在您将业务切换至目标实例前，请务必先结束或释放该任务，避免该任务被自动恢复后，导致源端数据覆盖目标实例的数据。
DTS会尝试恢复七天之内迁移失败任务。因此业务切换至目标实例前，请务必结束或释放该任务，或者将DTS访问目标实例账号的写权限用revoke命令回收掉。避免该任务被自动恢复后，源端数据覆盖目标实例的数据。
如果使用了对象名映射功能后，依赖这个对象的其他对象可能迁移失败。
建议源和目标库的MySQL版本保持一致，以保障兼容性。
## 费用说明
| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 当目标库的 接入方式 为 公网 IP 时收取公网流量费用。更多信息，请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |
## 操作步骤
进入目标地域的迁移任务列表页面。
登录[数据传输服务](https://dtsnew.console.aliyun.com/)[DTS](https://dtsnew.console.aliyun.com/)[控制台](https://dtsnew.console.aliyun.com/)。
在左侧导航栏，单击数据迁移。
在页面左上角，选择实例所属地域。
单击创建任务，进入任务配置页面。
配置源库及目标库信息。
| 库类别 | 参数 | 说明 |
| --- | --- | --- |
| 源库 | 数据库类型 | 源数据库类型，选择 MySQL 。 |
| 接入方式 | 源库实例接入 DTS 的方式，本示例选择 公网 IP 。 |  |
| 实例地区 | 公网接入，选择任意地区即可，本示例选择 华东 1 （杭州） 。 如果您的实例配置了访问控制，则请先为 DTS 服务开放访问权限后，再配置数据迁移任务。DTS 服务的 IP 地址段信息，请参见 [添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) [地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353) 。 |  |
| 域名或 IP 地址 | Microsoft Azure Database for MySQL 数据库的服务器名称。 |  |
| 端口 | Microsoft Azure Database for MySQL 数据库的服务端口（需开放至公网），默认为 3306 。 |  |
| 数据库账号 | Microsoft Azure Database for MySQL 数据库的高权限账号。 |  |
| 数据库密码 | Microsoft Azure Database for MySQL 数据库的高权限账号的密码。 |  |
| 目标库 | 数据库类型 | 目标实例的类型，选择 MySQL 。 |
| 接入方式 | 目标实例接入 DTS 的方式，选择 云实例 。 |  |
| 实例地区 | 目标实例所在的地域。 |  |
| 是否跨阿里云账号 | 选择 不跨账号 。 |  |
| RDS 实例 ID | 对应地域下的实例 ID，这里选择想要迁移到的目标实例的 ID。 |  |
| 数据库账号 | 目标 RDS 实例的高权限账号。 |  |
| 数据库密码 | 目标 RDS 实例的高权限账号对应的密码。 |  |
| 连接方式 | 支持 非加密连接 和 SSL 安全连接 两种连接方式，选择 SSL 安全加密连接会显著增加阿里云 RDS MySQL 实例的 CPU 消耗。 |  |
配置完成后，单击页面下方的测试连接以进行下一步。
请确保已将弹跳框中的DTS服务器IP地址加入到Azure平台的MySQL数据库的白名单安全设置中，然后单击测试连接。
重要
[添加](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[服务器](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)[地址白名单](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases)可能会存在安全风险，一旦使用本产品代表您已理解和确认其中可能存在的安全风险，并且需要您做好基本的安全防护，包括但不限于加强账号密码强度防范、限制各网段开放的端口号、内部各API使用鉴权方式通信、定期检查并限制不需要的网段。
在配置任务对象及高级配置步骤，选择迁移类型。
说明
为保证迁移数据的一致性，建议选择库表结构迁移+全量数据迁移+增量数据迁移。
在源库对象框中将想要迁移的数据库选中，单击，移动到已选择对象框。
单击下一步高级配置，保持默认配置即可。
单击下一步保存任务并预检查，等待预检查结束。
说明
如果检查失败，可以根据错误项的提示进行修复，然后重新启动任务。
单击下一步购买，在购买页，勾选《数据传输（按量付费）服务条款》并单击购买并启动。
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
