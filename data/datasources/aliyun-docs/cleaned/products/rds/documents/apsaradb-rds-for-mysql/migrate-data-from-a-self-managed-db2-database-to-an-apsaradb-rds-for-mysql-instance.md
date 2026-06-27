# 如何将自建的Db2迁移至RDSMySQL-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance

# 从自建Db2迁移至RDS MySQL
本文介绍如何使用数据传输服务DTS（Data Transmission Service），将自建的Db2数据库迁移至RDS MySQL或RDS MySQL Serverless实例。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成Db2数据库的迁移。
## 前提条件
Db2数据库版本为9.7~11.5版本。
说明
DTS也支持迁移7.3、7.4版本的Db2数据库至RDS MySQL，配置方式与Db2数据库迁移至RDS MySQL类似，您可参考本文介绍的迁移任务配置方式进行配置。
RDS MySQL的存储空间须大于Db2数据库占用的存储空间。
## 注意事项
不支持DDL操作的同步。
如果待迁移数据库名称不符合阿里云RDS的定义规范，您需要在配置迁移任务之前在阿里云RDS MySQL中创建数据库。
说明
关于阿里云RDS的定义规范和创建数据库的操作方法，请参见[创建数据库](create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。
DTS在执行全量数据迁移时将占用源库和目标库一定的读写资源，可能会导致数据库的负载上升，在数据库性能较差、规格较低或业务量较大的情况下（例如源库有大量慢SQL、存在无主键表或目标库存在死锁等），可能会加重数据库压力，甚至导致数据库服务不可用。因此您需要在执行数据迁移前评估源库和目标库的性能，同时建议您在业务低峰期执行数据迁移（例如源库和目标库的CPU负载在30%以下）。
对于迁移失败的任务，DTS会触发自动恢复。在将业务切换至目标实例前，请务必先结束或释放该任务，避免该任务被自动恢复后，源端数据覆盖目标实例的数据。
由于DTS基于Db2的CDC复制技术，将Db2数据库的增量更新数据同步到目标库中，但是CDC复制技术自身具有限制，请参见[CDC](https://www.ibm.com/support/knowledgecenter/SSTRGZ_11.4.0/com.ibm.swg.im.iis.db.repl.sqlrepl.doc/topics/iiyrssubdatarestrict.html)[复制技术所支持数据类型的限制](https://www.ibm.com/support/knowledgecenter/SSTRGZ_11.4.0/com.ibm.swg.im.iis.db.repl.sqlrepl.doc/topics/iiyrssubdatarestrict.html)。
## 费用说明
| 迁移类型 | 链路配置费用 | 公网流量费用 |
| --- | --- | --- |
| 结构迁移和全量数据迁移 | 不收费。 | 当目标库的 接入方式 为 公网 IP 时收取公网流量费用。更多信息，请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |
| 增量数据迁移 | 收费，详情请参见 [计费概述](https://help.aliyun.com/zh/dts/product-overview/billing-overview#concept-261679) 。 |  |
## 迁移类型说明
结构迁移
DTS将迁移对象的结构定义迁移到目标实例，目前DTS支持结构迁移的对象为表、索引和外键。
全量数据迁移
DTS会将Db2数据库迁移对象的存量数据，全部迁移到目标RDS MySQL数据库中。
增量数据迁移
在全量迁移的基础上，DTS将Db2数据库的增量更新数据同步到目标RDS MySQL中。通过增量数据迁移可以实现在自建应用不停服的情况下，平滑地完成Db2数据库的迁移。
## 数据库账号的权限要求
| 数据库 | 结构迁移 | 全量迁移 | 增量迁移 |
| --- | --- | --- | --- |
| Db2 数据库 | CONNECT、SELECT 权限 | CONNECT、SELECT 权限 | DBADM 权限 |
| RDS MySQL 或 RDS MySQL Serverless 实例 | 读写权限 | 读写权限 | 读写权限 |
数据库账号创建及授权方法：
Db2数据库请参见[创建用户](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_11.1.0/com.ibm.db2.luw.qb.server.doc/doc/t0006742.html#t0006742)和[权限概述](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_11.1.0/com.ibm.db2.luw.admin.sec.doc/doc/c0055206.html)。
RDS MySQL或RDS MySQL Serverless请参见[创建账号](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)和[修改账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
## 数据迁移流程
为解决对象间的依赖，提高迁移成功率，DTS对Db2数据库结构和数据的迁移流程如下：
执行表结构和索引的迁移。
执行全量数据迁移。
执行外键的结构迁移。
执行增量数据迁移。
## 增量数据迁移前准备工作
在配置增量数据迁移任务之前，您还需要打开Db2数据库的归档日志，详情请参见[主日志归档方法](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_10.5.0/com.ibm.db2.luw.admin.config.doc/doc/r0011448.html)和[辅助日志归档方法](https://www.ibm.com/support/knowledgecenter/zh/SSEPGG_10.5.0/com.ibm.db2.luw.admin.config.doc/doc/r0011449.html)。
说明
如您只需要全量数据迁移，可跳过本步骤。
## 操作步骤
登录[数据传输控制台](https://dts.console.aliyun.com/)。
说明
若数据传输控制台自动跳转至数据管理DMS控制台，您可以在右下角的中单击，返回至旧版数据传输控制台。
在左侧导航栏，单击数据迁移。
在迁移任务列表页面顶部，选择迁移的目标实例所属地域。
单击页面右上角的创建迁移任务。
配置迁移任务的源库及目标库信息。
| 类别 | 配置 | 说明 |
| --- | --- | --- |
| 无 | 任务名称 | DTS 会自动生成一个任务名称，建议配置具有业务意义的名称（无唯一性要求），便于后续识别。 |
| 源库信息 | 实例类型 | 根据源库的部署位置进行选择，本文以 有公网 IP 的自建数据库 为例介绍配置流程。 说明 当自建数据库为其他实例类型时，您还需要执行相应的准备工作，详情请参见 [准备工作](https://help.aliyun.com/zh/dts/user-guide/preparations/) 。 |
| 实例地区 | 当实例类型选择为 有公网 IP 的自建数据库 时， 实例地区 无需设置。 说明 如果您的 Db2 数据库具备白名单安全设置，您需要在 实例地区 配置项后，单击 获取 DTS IP 段 来获取到 DTS 服务器的 IP 地址，并将获取到的 IP 地址加入 Db2 数据库的白名单安全设置中。 |  |
| 数据库类型 | 选择 DB2 。 |  |
| 主机名或 IP 地址 | 填入 Db2 数据库的访问地址，本案例中填入公网地址。 |  |
| 端口 | 填入 Db2 数据库的服务端口，默认为 50000 。 说明 本案例中，该服务端口须开放至公网。 |  |
| 数据库名称 | 填入待迁移的数据库名。 |  |
| 数据库账号 | 填入 Db2 的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入 Db2 数据库账号的密码。 说明 源库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的源库信息是否正确。源库信息填写正确则提示 测试通过 ，如提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的源库信息。 |  |
| 目标库信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例地区 | 选择目标 RDS 实例所属地域。 |  |
| RDS 实例 ID | 选择目标 RDS 实例 ID。 |  |
| 数据库账号 | 填入目标 RDS 实例的数据库账号，权限要求请参见 [数据库账号的权限要求](migrate-data-from-a-self-managed-db2-database-to-an-apsaradb-rds-for-mysql-instance.md) 。 |  |
| 数据库密码 | 填入该数据库账号的密码。 说明 目标库信息填写完毕后，您可以单击 数据库密码 后的 测试连接 来验证填入的目标库信息是否正确。目标库信息填写正确则提示 测试通过 ，如提示 测试失败 ，单击 测试失败 后的 诊断 ，根据提示调整填写的目标库信息。 |  |
| 连接方式 | 根据需求选择 非加密连接 或 SSL 安全连接 。如果设置为 SSL 安全连接 ，您需要提前开启 RDS 实例的 SSL 加密功能，详情请参见 [设置](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md) 。 |  |
配置完成后，单击页面右下角的授权白名单并进入下一步。
说明
此步骤会将DTS服务器的IP地址自动添加到目标RDS实例的白名单中，用于保障DTS服务器能够正常连接目标RDS实例。
选择迁移对象及迁移类型。
| 配置 | 说明 |
| --- | --- |
| 迁移类型 | 如果只需要进行全量迁移，在迁移类型选择时勾选 结构迁移 和 全量数据迁移 。 如果需要进行不停机迁移，在迁移类型选择时勾选 结构迁移 、 全量数据迁移 和 增量数据迁移 。 说明 如果未勾选 增量数据迁移 ，为保障数据一致性，数据迁移期间请勿在 Db2 数据库中写入新的数据。 |
| 迁移对象 | 在 迁移对象 框中单击待迁移的对象，然后单击 图标将其移动到 已选择对象 框。 说明 迁移对象选择的粒度可以为库、表、列三个粒度。 默认情况下，迁移完成后，迁移对象名跟 Db2 数据库一致。如果您需要迁移对象在目标 RDS 实例上名称不同，那么需要使用 DTS 提供的对象名映射功能。使用方法请参见 [库表列映射](https://help.aliyun.com/zh/dts/user-guide/object-name-mapping#concept-610481) 。 如果使用了对象名映射功能，可能会导致依赖这个对象的其他对象迁移失败。 |
| 映射名称更改 | 如需更改迁移对象在目标实例中的名称，请使用对象名映射功能，详情请参见 [库表列映射](https://help.aliyun.com/zh/dts/user-guide/object-name-mapping#concept-610481) 。 |
| 源、目标库无法连接重试时间 | 默认重试 12 小时，您也可以自定义重试时间。如果 DTS 在设置的时间内重新连接上源、目标库，迁移任务将自动恢复。否则，迁移任务将失败。 说明 由于连接重试期间，DTS 将收取任务运行费用，建议您根据业务需要自定义重试时间，或者在源和目标库实例释放后尽快释放 DTS 实例。 |
上述配置完成后，单击页面右下角的预检查并启动。
说明
在迁移任务正式启动之前，会先进行预检查。只有预检查通过后，才能成功启动迁移任务。
如果预检查失败，单击具体检查项后的，查看失败详情。
您可以根据提示修复后重新进行预检查。
如无需修复告警检测项，您也可以选择确认屏蔽、忽略告警项并重新进行预检查，跳过告警检测项重新进行预检查。
预检查通过后，单击下一步。
在购买配置确认页面，选择链路规格并选中数据传输（按量付费）服务条款。
单击购买并启动，迁移任务正式开始。
全量数据迁移
请勿手动结束迁移任务，否则可能导致数据不完整。您只需等待迁移任务完成即可，迁移任务会自动结束。
增量数据迁移
迁移任务不会自动结束，您需要手动结束迁移任务。
说明
请选择合适的时间手动结束迁移任务，例如业务低峰期或准备将业务切换至目标实例时。
观察迁移任务的进度变更为增量迁移，并显示为无延迟时，将源库停写几分钟，此时增量迁移可能会显示延迟的时间。
等待迁移任务的增量迁移再次进入无延迟后，手动结束迁移任务。
将业务切换至RDS MySQL。
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
