# 设置Tair实例的配置参数-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/modify-the-values-of-parameters-for-an-instance

# 设置参数
云数据库 Tair（兼容 Redis）支持自定义部分参数的值，不同的引擎版本和架构支持的参数有所区别，本文为您介绍各参数的设置方法。
## 注意事项
若在设置实例参数时报错Parameter is not supported for current version，表示当前实例的小版本过低。您需要将实例升级至最新的小版本，具体操作请参见[升级小版本与代理版本](update-the-minor-version.md)。
云数据库 Tair（兼容 Redis）不支持直接调用命令设置参数，例如执行CONFIG SET TIMEOUT 60，返回OK是为了满足某些集成框架的需求，但实际不会生效，请您通过控制台或[ModifyInstanceConfig](../developer-reference/api-r-kvstore-2015-01-01-modifyinstanceconfig-redis.md)API接口设置参数。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，单击参数设置。
修改参数。
当前支持如下3种方式修改参数，关于参数和参数值的说明，请参见[Tair](parameter-support.md)[企业版参数列表](parameter-support.md)或[Redis](supported-parameters.md)[开源版参数列表](supported-parameters.md)。
警告
部分参数在提交修改后会自动重启实例（重启过程中实例会发生秒级闪断，请谨慎操作），详情请参见目标参数的重启生效列。
修改单个参数：
找到目标参数，单击其操作列的修改。
单击确定。
批量修改：
单击批量修改。
在目标参数的参数运行值列，修改参数。
完成修改后，单击页面下方的确认修改。
从文件导入：
若您希望将其他实例的参数配置应用至当前实例，您可以选择此方式。使用该功能前，您需要提前访问源实例的参数设置页面，单击页面右上方图标，下载源实例的参数配置文件。
说明
请将参数配置文件导入至同版本、同架构的实例中，否则部分参数将无法生效。例如query_cache_enabled参数仅在Tair（企业版）[内存型](../product-overview/dram-based-instances.md)中支持，若将该参数导入至其他系列或Redis开源版实例将无法生效。
单击从文件导入。
在批量导入面板，单击图标，上传目标文件。
在参数详情区域，确认并勾选待修改的参数。
说明
您可以开启只展示有变化参数开关，快速过滤与当前参数运行值不同的参数。
单击确认修改。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [DescribeParameters](../developer-reference/api-r-kvstore-2015-01-01-describeparameters-redis.md) | 查询实例的配置参数和运行参数。 |
| [ModifyInstanceConfig](../developer-reference/api-r-kvstore-2015-01-01-modifyinstanceconfig-redis.md) | 修改实例的参数配置。 |
## 常见问题
Q：怎么设置实例的Maxclients参数？
A：云数据库 Tair（兼容 Redis）不支持设置Maxclients参数，实例的最大连接数与实例规格有关，例如Tair内存型 4GB（tair.rdb.4g）实例的最大连接数为40000。您可以在[实例规格](../product-overview/overview-4.md)文档中找到各个规格的最大连接数信息。您可以通过[提升实例规格](change-the-configurations-of-an-instance.md)或[开启读写分离](enable-read-write-splitting.md)。提升实例的最大连接数。
## 相关文档
[常见参数调整案例](common-parameter-adjustment-cases.md)
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
