# 华为云MySQL数据库迁移到阿里云的步骤-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-mysql-databases-from-huawei-cloud-to-alibaba-cloud

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 华为云云数据库RDS MySQL迁移到阿里云RDS MySQL

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍华为云云数据库RDS MySQL迁移到阿里云云数据库RDS MySQL的注意事项及操作步骤。

## 前提条件

- 

- 

- 

- 

| 源端及目标端 | 要求 |  |
| --- | --- | --- |
| 源端 | [华为云云数据库](https://support.huaweicloud.com/rds/index.html) [RDS MySQL](https://support.huaweicloud.com/rds/index.html) [实例](https://support.huaweicloud.com/rds/index.html) | 已开通公网访问，并获取外网连接地址及端口。 已创建高权限账号。 |
| 目标端 | 阿里云云数据库 RDS MySQL 实例 | 已 [创建阿里云](products/rds/documents/apsaradb-rds-for-mysql/create-an-apsaradb-rds-for-mysql-instance-1.md) [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/create-an-apsaradb-rds-for-mysql-instance-1.md) [实例](products/rds/documents/apsaradb-rds-for-mysql/create-an-apsaradb-rds-for-mysql-instance-1.md) 。 已 [创建高权限账号](products/rds/documents/apsaradb-rds-for-mysql/create-an-account-on-an-apsaradb-rds-for-mysql-instance.md) 。 |


## 迁移限制

- 

结构迁移不支持event的迁移。

- 

对于MySQL的浮点型float和double，DTS通过round(column,precision)来读取该列的值，若列类型没有明确定义其精度，对于float，精度为38位，对于double类型，精度为308，请先确认DTS的迁移精度是否符合业务预期。

- 

如果使用了对象名映射功能后，依赖这个对象的其他对象可能迁移失败。

- 

增量迁移限制如下：

- 

源端的MySQL实例需要按照要求开启binlog。

- 

源库的binlog_format要为row。

- 

源MySQL如果为5.6及以上版本时，它的binlog_row_image必须为full。

- 

增量迁移过程中如果源MySQL实例出现因实例跨机迁移或跨机重建等导致的binlog文件ID乱序，可能导致增量迁移数据丢失。

说明

华为云云数据库RDS MySQL实例的参数修改，请参见[华为云云数据库](https://support.huaweicloud.com/rds/index.html)[RDS](https://support.huaweicloud.com/rds/index.html)[官方文档](https://support.huaweicloud.com/rds/index.html)。

## 注意事项

- 

如果源端实例配置了访问控制，请先将[DTS](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[服务器的](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[IP](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)[地址段](https://help.aliyun.com/zh/dts/user-guide/add-the-cidr-blocks-of-dts-servers-to-the-security-settings-of-on-premises-databases#concept-1340353)添加到源端的安全配置中，再配置数据迁移任务。

- 

对于七天之内的异常迁移任务，DTS会尝试自动恢复，可能会导致迁移任务的源端数据库数据覆盖目标实例数据库中写入的业务数据，迁移任务结束后务必将DTS访问目标实例账号的写权限用revoke命令回收掉。

## 操作步骤

- 

进入目标地域的迁移任务列表页面。

- 

登录[数据传输服务](https://dtsnew.console.aliyun.com/)[DTS](https://dtsnew.console.aliyun.com/)[控制台](https://dtsnew.console.aliyun.com/)。

- 

在左侧导航栏，单击数据迁移。

- 

在页面左上角，选择实例所属地域。

- 

单击创建任务，进入任务配置页面，配置源库及目标库信息。

| 库类别 | 参数 | 说明 |
| --- | --- | --- |
| 源库 | 数据库类型 | 源数据库类型，选择 MySQL 。 |
| 接入方式 | 源库实例接入 DTS 的方式，本示例选择 公网 IP 。 |  |
| 实例地区 | 公网接入，选择目标地域即可，本示例选择 华东 1 （杭州） 。 |  |
| 域名或 IP 地址 | 华为云云数据库 RDS MySQL 实例的 公网地址 。 |  |
| 端口 | 华为云云数据库 RDS MySQL 实例的 数据库端口 。 |  |
| 数据库账号 | 华为云云数据库 RDS MySQL 实例的 高权限账号 。 |  |
| 数据库密码 | 华为云云数据库 RDS MySQL 实例的高权限账号的密码。 |  |
| 目标库 | 数据库类型 | 目标实例的类型，选择 MySQL 。 |
| 接入方式 | 目标实例接入 DTS 的方式，本示例选择 云实例 。 |  |
| 实例地区 | RDS MySQL 实例所在的地域。 |  |
| 是否跨阿里云账号 | 选择 不跨账号 。 |  |
| RDS 实例 ID | RDS MySQL 实例的 ID。 |  |
| 数据库账号 | 目标实例的 高权限账号 。 |  |
| 数据库密码 | 目标实例的高权限账号对应的密码。 |  |
| 连接方式 | 根据数据库实际情况选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS MySQL 实例的 SSL 加密功能，详情请参见 [使用云端证书快速开启](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [链路加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |


- 

填写完毕后单击测试连接以进行下一步，在DTS服务器访问授权确定窗口中，再次单击测试连接以进行下一步。

- 

在配置任务对象及高级配置步骤，选择迁移类型。

说明

为保证迁移数据的一致性，建议选择结构迁移+全量数据迁移+增量数据迁移。

- 

勾在源库对象框中将想要迁移的数据库选中，单击，移动到已选择对象框。

- 

单击下一步高级配置，保持默认配置即可。

当源库和目标库账号满足要求时，可以将源库的账号（包含密码和权限）迁移至目标库。迁移数据库账号的注意事项及数据库账号所需权限等更多信息请参见[数据库账号所需权限](https://help.aliyun.com/zh/dts/user-guide/permissions-for-database-accounts-to-migrate-account-information#section-account-permissions)。

- 

单击下一步保存任务并预检查，等待预检查结束。

说明

如果检查失败，可以根据错误项的提示进行修复，然后重新启动任务。

- 

单击下一步购买，在购买页，勾选《数据传输（按量付费）服务条款》并单击购买并启动。

如果选择了增量迁移，那么进入增量迁移阶段后，源库的更新写入都会被DTS同步到目标RDS MySQL实例。迁移任务不会自动结束。如果您只是为了迁移，那么建议在增量迁移无延迟的状态时，源库停写几分钟，等待增量迁移再次进入无延迟状态后，停止掉迁移任务，直接将业务切换到目标RDS MySQL实例上即可。

说明

结构迁移和全量迁移任务暂不收费，增量迁移根据链路规格按小时收费。

- 

等待迁移任务完成即可。

[上一篇：百度智能云云数据库RDS MySQL迁移到阿里云](products/rds/documents/apsaradb-rds-for-mysql/migrate-mysql-databases-from-baidu-ai-cloud-to-alibaba-cloud.md)[下一篇：Microsoft Azure Database for MySQL数据库迁移到阿里云](products/rds/documents/apsaradb-rds-for-mysql/migrate-mysql-databases-from-microsoft-azure-to-alibaba-cloud.md)

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
