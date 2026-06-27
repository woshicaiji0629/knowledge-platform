# 【停售/下线】2023年01月31日起RDS PostgreSQL部分基础系列通用规格停止售卖-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/some-general-purpose-instance-types-are-no-longer-available-for-purchase

# 【停售/下线】2023年01月31日起RDS PostgreSQL部分基础系列通用规格停止售卖
因RDS PostgreSQL产品架构演进调整，阿里云于2023年01月31日起，将停止售卖部分基础系列通用型规格。
## 背景信息
随着RDS PostgreSQL产品架构的演进，计划于2023年01月31日起，逐步停止售卖部分基础系列通用规格，推荐购买已推出的全新[通用型](primary-apsaradb-rds-for-postgresql-instance-types.md)规格，为您提供更好的弹性能力以及更高的实例性能，增强实例的创建、变配速度。
## 停售规格及停售时间
| 系列 | 版本 | 规格族 | 规格代码 | CPU 和内存 | 停售时间 |
| --- | --- | --- | --- | --- | --- |
| 基础系列 | 15、14、13、12、11、10 | 通用型 | pg.n2.small.1 | 1 核 2GB | 2023 年 01 月 31 日 |
| pg.n2.medium.1 | 2 核 4GB | 2023 年 09 月 15 日 |  |  |  |
| pg.n4.medium.1 | 2 核 8GB |  |  |  |  |
| pg.n2.large.1 | 4 核 8GB |  |  |  |  |
| pg.n4.large.1 | 4 核 16GB |  |  |  |  |
| pg.n2.xlarge.1 | 8 核 16GB |  |  |  |  |
| pg.n4.xlarge.1 | 8 核 32GB |  |  |  |  |
| pg.n2.2xlarge.1 | 16 核 32GB |  |  |  |  |
| pg.n4.2xlarge.1 | 16 核 64GB |  |  |  |  |
| pg.n8.2xlarge.1 | 16 核 128GB |  |  |  |  |
| pg.n4.4xlarge.1 | 32 核 128GB |  |  |  |  |
| pg.n8.4xlarge.1 | 32 核 256GB |  |  |  |  |
| pg.n4.8xlarge.1 | 64 核 256GB | 2023 年 01 月 31 日 |  |  |  |
| pg.n8.8xlarge.1 | 64 核 512GB | 2023 年 01 月 31 日 |  |  |  |
## 影响及建议
| 分类 | 影响 | 建议 |
| --- | --- | --- |
| 已有实例 | [变更实例规格](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 时，不能选购已停售的规格。 [变更实例规格](change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md) 时，需要进行 SLR 授权。 说明 SRL 授权的更多信息，请参见 [【产品/功能变更】2022](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [年](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [10](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [月](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [10](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [日起创建](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [RDS PostgreSQL](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [实例需](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [SLR](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) [授权](slr-authorization-is-required-to-create-an-apsaradb-rds-for-postgresql-instance-from-october-10-2022.md) 。 [实例回收站](manage-apsaradb-rds-for-postgresql-instances-in-the-recycle-bin.md) 重建实例时，不支持选择本次停售的规格。 已购实例的其他服务不受影响。 例如： 仍旧支持除变更规格外的其他变更配置行为（变更磁盘类型、存储空间等）。 [升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md) 时，仍支持选择本次停售的规格。 对于以下情况的用户，将会显示本次停售的规格以支持存量实例的运维： 存在只读实例的用户 存在磁盘加密实例的用户 所在可用区目前无法购买新实例的客户 | 变更实例规格时，推荐购买其他在售规格，请以实际变配页为准。 说明 如果您使用 [OpenAPI](../api-create-an-instance.md) 或者 [Terraform](babelfish-for-apsaradb-rds-for-postgresql.md) 变更实例规格，建议您将实例规格相关参数调整为其他在售规格，以避免老规格停售后，变更配置失败。 |
| 新购实例 | 已停售规格，不再支持新购。 | 新购实例时，推荐购买其他在售规格。更多规格信息，请参见 [RDS PostgreSQL](primary-apsaradb-rds-for-postgresql-instance-types.md) [主实例规格列表](primary-apsaradb-rds-for-postgresql-instance-types.md) 。 说明 如果您使用 [OpenAPI](../api-create-an-instance.md) 或者 [Terraform](babelfish-for-apsaradb-rds-for-postgresql.md) 创建实例，建议您将实例规格相关参数调整为其他在售规格，以避免老规格停售后，实例创建失败。 |
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
