# 修改专有网络VPC或交换机解决跨网络连接问题-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/change-the-vpc-or-vswitch-of-an-instance

# 修改专有网络VPC或交换机
云数据库Tair（兼容 Redis）实例支持修改专有网络或交换机，例如您可以将实例的专有网络调整为目标ECS实例所属的专有网络，实现与ECS实例间的互连。
## 前提条件
若经典版集群架构实例开通了[直连地址](enable-the-direct-connection-mode.md)，请临时释放直连地址，待修改专有网络VPC后再重新启用。
但云原生版集群架构直连模式实例不支持修改VPC。
若实例已开启[专有网络免密访问](enable-password-free-access.md)，请临时关闭该功能。
若存在正在运行的[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)数据迁移或同步任务，请临时暂停任务，否则将提示错误。
## 适用场景
| 操作 | 场景示例 |
| --- | --- |
| 修改专有网络 | 解决客户端与实例因专有网络不同导致无法连接的问题。 例如，业务所属的 ECS 部署在专有网络 A，而 云数据库 Tair（兼容 Redis） 实例在专有网络 B，您可以将实例切换至专有网络 A，即可解决因专有网络不同导致的连接问题。 |
| 修改交换机 | 将云资源根据业务分类并规划 IP 地址的分配，便于集中管理云资源和 IP 白名单。 例如，需要将数据库业务相关的云资源（例如 ECS、 云数据库 Tair（兼容 Redis） 实例等）统一划入相同的交换机中，自动分配相同网段的地址。 |
## 影响
切换过程中会有30秒闪断，请在业务低峰期操作并确保应用程序具有重连机制。
切换专有网络或交换机会造成虚拟IP地址（Virtual IP address）的变更，如果应用程序使用虚拟IP地址连接实例，会因为虚拟IP地址的变更导致连接失败。
说明
切换专有网络或交换机不会引起实例连接地址的变化（例如r-hp3bpn39cs1vu****.redis.hangzhou.rds.aliyuncs.com），推荐应用程序使用连接地址连接实例。
VIP的变更会短暂影响到[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)的使用，变更结束后会自动恢复正常。
切换完成后，请及时清理客户端的缓存 ，否则可能出现只能读取数据，无法写入数据的情况。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在基本信息区域框，单击专有网络ID后的修改。
说明
如果仅需要修改交换机，您也可以单击交换机ID后的修改。
在右侧弹出的面板中，选择要切换的目标专有网络和交换机。
说明
如果下拉框中没有可选的专有网络或交换机，请先创建专有网络和交换机。具体操作，请参见[创建和管理专有网络](../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)和[创建和管理交换机](../../../vpc/documents/user-guide/create-and-manage-vswitch.md)。
单击确定。
警告
切换过程中会有30秒闪断，请在业务低峰期操作并确保应用程序具有重连机制。
阅读对话框的提示，单击确定。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [SwitchNetwork](../developer-reference/api-r-kvstore-2015-01-01-switchnetwork-redis.md) | 切换实例的专有网络 VPC 或交换机。 |
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
