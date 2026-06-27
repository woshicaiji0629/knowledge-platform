# DuckDB分析加速-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration

# DuckDB分析加速
当您在RDS PostgreSQL上进行复杂查询并期望快速获得结果时，可以使用分析加速引擎rds_duckdb。该引擎基于DuckDB构建，提供列存表与向量化执行能力，无需修改原始SQL即可显著提升复杂分析查询的执行速度。
## 功能简介
RDS PostgreSQL默认使用行存格式存储数据，行存适合在线事务处理（OLTP）场景的高频点查与更新，但在分析（OLAP）场景下需要扫描大量数据时性能受限。rds_duckdb插件在RDS PostgreSQL中集成了DuckDB分析引擎，通过以下能力加速复杂查询：
列存格式：将数据按列组织存储，对于只涉及部分列的聚合、统计类查询，只需读取相关列，大幅减少I/O开销。
向量化执行：以批量数据为单位进行计算，充分利用CPU的SIMD指令与缓存局部性，相比传统的逐行执行（火山模型）有数倍至数十倍的性能提升。
无侵入使用：原始SQL语句无需任何修改，业务可平滑迁移至加速链路。
## 适用场景
复杂报表与即席查询（Ad-hoc Query），涉及多表JOIN、GROUP BY、聚合计算。
数据分析与统计场景，单表数据量较大且查询只涉及部分列。
HTAP混合负载场景，希望在同一份数据上同时支持在线事务与分析查询。
## 开启方式
在正式使用分析加速能力前，请先完成实例配置。RDS PostgreSQL提供以下两种方式，您可以根据业务负载特征进行选择：
| 开启方式 | 资源模式 | 推荐场景 | 操作文档 |
| --- | --- | --- | --- |
| 主实例开启分析加速 | PostgreSQL 与 DuckDB 共享主实例资源，部署简单、成本较低。 | TP 负载较轻或允许 AP 查询占用部分主实例资源的业务，希望快速验证加速效果。 | [主实例开启](enable-duckdb-for-the-master-instance.md) [AP](enable-duckdb-for-the-master-instance.md) [加速](enable-duckdb-for-the-master-instance.md) |
| DuckDB 分析实例 | 独立部署 DuckDB 分析实例，与主实例进行数据同步，AP 与 TP 负载在物理资源上完全隔离。 | 对在线业务延迟敏感的核心业务，需要保障 TP 稳定性，同时承载大规模 AP 分析查询。 | [DuckDB](add-a-duckdb-read-only-instance.md) [分析实例](add-a-duckdb-read-only-instance.md) |
说明
如果您不确定如何选择，建议优先采用DuckDB分析实例方式，将分析负载与在线事务隔离，避免AP查询影响核心业务的性能与稳定性。
## 使用方法
成功开启HTAP加速功能后，您可以通过rds_duckdb插件创建列存表、导入数据并执行查询。详细的语法说明、表管理操作、查询使用方式，请参见[AP](how-to-use-duckdb-to-speed-up-queries.md)[加速引擎（rds_duckdb）](how-to-use-duckdb-to-speed-up-queries.md)。
## 性能测试
如果您希望量化评估rds_duckdb对复杂查询的加速效果，可以参考标准TPC-H测试方案。该方案包含完整的测试数据准备、查询执行步骤与结果对比，详情请参见[AP](duckdb-performance-test.md)[加速引擎（rds_duckdb）性能测试](duckdb-performance-test.md)。
## 免费体验
如果您希望快速体验rds_duckdb的核心功能，可以使用免费体验入口，无需购买额外资源即可完成简单的AP加速查询验证。详情请参见[免费体验](free-experience-duckdb.md)[RDS PostgreSQL AP](free-experience-duckdb.md)[加速引擎（rds_duckdb）](free-experience-duckdb.md)。
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
