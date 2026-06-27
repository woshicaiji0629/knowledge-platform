# 为实例申请公网连接地址以开启公网访问-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/apply-for-a-public-endpoint-for-an-apsaradb-for-redis-instance

# 申请公网连接地址
默认情况下，云数据库 Tair（兼容 Redis）实例仅提供专有网络连接地址，如需从本地通过公网连接实例，请先申请实例的公网连接地址。
## 注意事项
云原生版集群架构直连模式实例不支持申请公网地址。
为保障安全性，若实例已开启专有网络免密访问，通过公网地址连接实例仍需密码验证。
申请公网地址不会对实例造成影响，但会降低实例的安全性，请谨慎使用。
## 连接地址的网络类型
| 连接地址的网络类型 | 说明 |
| --- | --- |
| 专有网络 | [专有网络](../../../vpc/documents/what-is-vpc.md) [VPC](../../../vpc/documents/what-is-vpc.md) （Virtual Private Cloud）是您自己独有的云上私有网络，不同的专有网络之间二层逻辑隔离，拥有较高的安全性和性能。 实例默认提供专有网络连接地址，通过专有网络连接实例可以获取更高的安全性和性能。 |
| 公网 | 由于通过公网连接实例存在一定的安全风险，实例默认未提供公网连接地址。如果您的客户端属于以下情形，您可以申请公网连接地址，通过公网连接实例： 客户端所属的设备（例如 [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) [实例](../../../ecs/documents/user-guide/what-is-ecs.md) ）与实例不在同一专有网络。 客户端所属的设备与实例不在同一地域。 客户端为阿里云以外的设备（例如本地设备）。 说明 为了获得更快的传输速率和更高的安全性，建议您将应用迁移到与您的实例在同一地域且网络类型相同的 ECS 实例，然后使用专有网络地址。 公网与专有网络会共享该实例的带宽与连接数。例如该实例的带宽为 96 MB/s，若专有网络已使用 70 MB/s，则公网最多可使用 26 MB/s 的带宽。 |
## 费用
申请公网地址和后续产生的公网流量暂不收费。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在连接信息区域框，单击公网访问对应的申请连接地址。
说明
若连接信息区域未显示专有网络或公网连接地址，请先根据提示[设置](../getting-started/step-2-configure-whitelists.md)[IP](../getting-started/step-2-configure-whitelists.md)[白名单](../getting-started/step-2-configure-whitelists.md)。
若没有申请连接地址按钮或该按钮为灰色，表示该实例为云原生版集群架构直连模式实例，不支持申请公网地址。
在右侧弹出的面板中，设置连接地址和端口。
| 配置 | 说明 |
| --- | --- |
| 连接地址 | 目前仅支持修改连接地址的前缀（前缀默认为实例 ID）。 自定义前缀需由小写英文字母和数字组成，以小写字母开头，长度为 8~40 个字符。 |
| 端口 | 可在修改连接地址的同时，修改端口，范围为 1024~65535。 |
单击确定。
申请操作完成后，连接信息区域框中将展示公网连接地址。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [AllocateInstancePublicConnection](../developer-reference/api-r-kvstore-2015-01-01-allocateinstancepublicconnection-redis.md) | 为实例申请公网连接地址。 |
## 常见问题
### 申请公网地址收费吗？
申请公网地址和后续产生的公网流量暂不收费。
### 为什么没有申请公网地址的操作入口？
没有申请公网地址的操作入口，有两个原因：
如果连接信息区域，也不显示专有网络连接地址，说明还未配置实例的白名单，请先配置白名单。具体操作请参见[设置白名单](../getting-started/step-2-configure-whitelists.md)。
若实例为云原生版集群架构直连模式，则不支持申请公网，无法通过公网连接实例，请通过专有网络连接实例。
说明
确认实例是否为云原生集群架构直连模式，请参见[怎样知道实例是否为云原生集群架构直连模式？](view-endpoints.md)。
如果应用所在的ECS实例与实例不在同一VPC，或您的应用不在阿里云上，您可以考虑使用云原生集群架构代理模式。由于云原生集群架构直连模式不能直接变配为代理模式，您可以通过的恢复实例功能完成迁移变配，将源实例的备份数据恢复至新实例中，在页面选择为代理模式，具体操作请参见[从备份集恢复至新实例](restore-data-from-a-backup-set-to-a-new-instance.md)。
警告
变配云原生版实例的集群架构后，需根据所使用的模式对连接代码进行适当修改，否则可能会无法连接，请谨慎操作。
### 公网访问是否支持免密登录？
仅专有网络支持免密访问。公网访问不支持免密登录，仍需要密码验证。
### 报错Current engine version does not support operations，怎么办？
当前引擎的小版本过低，不支持此操作，请升级小版本后重试，更多信息请参见[升级小版本与代理版本](update-the-minor-version.md)。
## 后续步骤
[使用公网地址连接实例](use-a-public-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)
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
