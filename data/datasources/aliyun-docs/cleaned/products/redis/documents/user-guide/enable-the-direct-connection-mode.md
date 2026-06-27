# 开通实例直连访问-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-the-direct-connection-mode

# 开通直连访问
经典版集群架构的云数据库 Tair（兼容 Redis）实例默认提供代理（Proxy）连接方式，若您希望该实例能兼容原生Redis Cluster协议，您可以参考本文开通直连访问模式，并在客户端中连接直连地址。您可以通过该地址绕过代理节点，像连接原生Redis集群一样连接云数据库 Tair（兼容 Redis）集群实例。
## 前提条件
重要
本功能公测中，如需使用请填写[表单](https://page.aliyun.com/form/act213201526/index.htm)申请使用。
实例需满足下述条件：
实例架构为集群架构。
部署模式为经典。
说明
云原生集群架构直连模式默认提供直连地址，无需额外开通。
云原生集群架构代理模式不支持开通直连模式。
兼容Redis版本为5.0，且[升级至最新小版本](update-the-minor-version.md)。
实例的TLS（SSL）加密功能需处于关闭状态，详情请参见[TLS](enable-tls-encryption.md)[加密](enable-tls-encryption.md)。
实例所属的交换机需具备充足的可分配的IP地址数，详情请参见[查询实例所属交换机可分配的](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)[IP](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)[地址数](obtain-the-number-of-available-ip-addresses-in-the-vswitch-to-which-an-apsaradb-for-redis-instance-is-connected.md)。
说明
例如实例的分片数为8，申请直连地址会为每个分片的主节点分配一个IP地址，同时直连地址本身需占用一个IP地址，那么实例所属的交换机中可分配的IP地址须大于等于9。
## 连接方式的对比
直连模式：通过直连地址，客户端可以绕过代理服务器，直接访问后端的数据节点，相比代理模式，直连模式节约了通过代理处理请求的时间，可以在一定程度上提高服务的响应速度。
代理模式：通过实例提供的代理连接地址，客户端的请求由代理节点转发至数据节点，更多信息请参见[Tair Proxy](../product-overview/features-of-proxy-nodes.md)[特性说明](../product-overview/features-of-proxy-nodes.md)。
## 注意事项
由于绕过了代理节点，连接性能有一定的下降，Redis开源版集群实例中单个分片的最大连接数为10,000；Tair（企业版）集群实例中单个分片的最大连接数为30,000。更多规格信息，请参见[实例规格](../product-overview/overview-4.md)。
如果存在数据倾斜，即某个分片被大量访问，其他分片基本处于空闲状态，可能引起该分片的连接数被耗尽，新的连接建立请求被拒绝，从而影响实例整体性能。
说明
数据倾斜通常由热点Key或大Key引起，排查方法，请参见[Top Key](use-the-real-time-key-statistics-feature.md)[统计](use-the-real-time-key-statistics-feature.md)和[离线全量](offline-key-analysis.md)[Key](offline-key-analysis.md)[分析](offline-key-analysis.md)。
开通直连地址后，将无法执行[升级大版本](upgrade-the-major-version-1.md)与[更换实例所属的可用区](migrate-an-instance-across-zones.md)操作，如需执行请先释放[直连地址](release-a-private-endpoint-from-an-apsaradb-for-redis-instance.md)。
开通直连地址后，集群实例在变配时，单次仅支持变配分片数或分片规格，更多信息请参见[分布式集群实例变配方案](../support/why-do-i-fail-to-change-the-configurations-of-a-cluster-instance-that-use-local-disks.md)。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在连接信息区域，单击直连右侧的申请连接地址。
在右侧弹出的面板中，设置连接地址和端口。
| 配置 | 说明 |
| --- | --- |
| 连接地址 | 目前仅支持修改连接地址的前缀（前缀默认为实例 ID）。 自定义前缀需由小写英文字母和数字组成，以小写字母开头，长度为 8~40 个字符。 |
| 端口 | 可在修改连接地址的同时，修改端口，范围为 1024~65535。 |
单击确定。
使用直连地址的连接示例请参见[使用直连模式连接实例](use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)。
## 常见问题
我的实例类型满足前提条件的要求，为什么找不到申请直连地址按钮？
答：请尝试将实例的小版本升级到最新，详情请参见[升级小版本与代理版本](update-the-minor-version.md)。
开通直连访问前是否需要停止业务？
答：不需要，开通直连访问不会导致服务中断。
直连模式和代理模式的连接地址是否可以同时使用？
答：经典版集群架构可以同时使用直连模式和代理模式，云原生版集群架构不支持同时使用，只能单独使用直连模式或代理模式。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [AllocateDirectConnection](../developer-reference/api-r-kvstore-2015-01-01-allocatedirectconnection-redis.md) | 申请集群实例的直连地址。 |
| [ReleaseDirectConnection](../developer-reference/api-r-kvstore-2015-01-01-releasedirectconnection-redis.md) | 释放集群实例的直连地址。 |
## 相关文档
[释放直连地址](release-a-private-endpoint-from-an-apsaradb-for-redis-instance.md)（可选）
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
