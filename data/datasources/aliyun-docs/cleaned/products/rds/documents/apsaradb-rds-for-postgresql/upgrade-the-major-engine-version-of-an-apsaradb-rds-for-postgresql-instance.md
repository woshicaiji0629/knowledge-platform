# 大版本升级方案对比与选择-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance

# RDS PostgreSQL大版本升级
随着PostgreSQL社区对低版本（如9.4、10等）实例的停止维护，继续使用低版本实例将存在风险，如果您需要将低版本的RDS PostgreSQL实例升级到更高版本，或者希望使用高版本的新特性，建议您进行大版本升级操作。
## 方案简介
PostgreSQL社区定期发布大版本，带来功能和性能提升。较低版本将逐渐不再受支持，存在性能和安全风险。为了让您享受新版本的提升，同时降低升级风险，RDS PostgreSQL支持大版本升级功能。
RDS PostgreSQL的大版本升级功能可以在升级后保留原实例的设置，例如，白名单、参数设置、插件（新版本不支持的插件和参数除外）。此外，[加密](../overview.md)[RDS PostgreSQL](../overview.md)[实例](../overview.md)升级大版本后仍为加密实例，且加密密钥将保持不变。
| 升级方案 | 本地升级 | 蓝绿部署 | 零停机 | [使用](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md) [DTS](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md) [迁移数据](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md) |  |
| --- | --- | --- | --- | --- | --- |
| 割接 | 不割接 |  |  |  |  |
| 适用场景 | 期望升级后的实例与原实例一致。并可以接受升级期间实例只读。 | 期望保留原实例，并可以接受升级期间实例只读。 | 升级演练。 应用双跑。 | 业务不接受长时间停机。 | 业务不接受长时间停机。 实例中数据库数量不多。 |
| 实现原理 | 使用 pg_upgrade 将原实例升级到目标版本。同时，保留所有元信息。 | 恢复到一个新实例，并使用 pg_upgrade 将其升级至目标版本。同时，自动切换原连接地址到新实例。 | 恢复到一个新实例，并使用 pg_upgrade 将其升级至目标版本。 | 使用 pg_upgrade 将原实例升级到目标版本。同时，通过原生逻辑复制进行增量更新。 | 手动创建新 RDS PostgreSQL 实例，并使用异步逻辑复制进行数据迁移。 |
| 方案优点 | 原实例配置和账单信息完全保留。 | 自动切换连接地址的能力。 可基于原实例进行回滚。 | 提供独立环境进行升级验证，对原实例无影响。 | 支持切换前验证高版本实例。 支持主动切换。 支持带只读实例升级。 原实例配置和账单信息完全保留。 | 产品级解决方案。 具备数据校验能力。 |
| 方案缺点 | 不支持基于旧实例的回滚。 | 不继承原实例的账单信息。 | 无。 | 缺乏数据校验能力和反向数据链路。 逻辑复制存在多项限制，例如表必须包含主键。 Sequence 对象的数量影响切换所需的时间。 | 一个数据库一个迁移任务。 需手动切换连接地址。 |
| 原实例只读时间 | 通常为分钟级。 | 通常为分钟级。 | 无。 | 通常为秒级。 | 通常为秒级。 |
| 费用 | 无升级费用。 | 新建实例按量付费。 | 新建实例按量付费。 | 无升级费用。 | 新建 RDS 实例的费用。 DTS 实例费用。 |
重要
对于本地升级模式，如果在升级过程中实例未达推荐规格，系统将自动尝试使用推荐规格进行升级。这将导致分钟级的只读状态，并额外出现一次秒级闪断。建议升级前，处理[大版本升级检查报告](introduction-to-the-check-report-of-a-major-engine-version-upgrade-for-an-apsaradb-rds-for-postgresql-instance.md)中关于实例规格的告警。
## 大版本升级
### 方式一：[通过本地升级模式升级大版本](upgrade-major-engine-version-in-local-upgrade-mode.md)
### 方式二：[通过蓝绿部署模式升级大版本](upgrade-major-engine-version-in-blue-green-deployment-mode.md)
### 方式三：[通过零停机模式升级大版本](upgrade-major-engine-version-in-zero-downtime-mode.md)
### 方式四：通过DTS迁移数据的方式升级
如果通过以上三种方式无法升级，或者期望升级时进行数据校验，您可以通过DTS迁移数据的方式进行升级。
[创建新实例](create-an-apsaradb-rds-for-postgresql-instance-1.md)。
[数据迁移至新实例](../apsaradb-rds-for-mysql/migrate-data-between-apsaradb-rds-for-mysql-instances.md)。
[释放原实例](release-or-unsubscribe-from-an-apsaradb-rds-for-postgresql-instance.md)
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
