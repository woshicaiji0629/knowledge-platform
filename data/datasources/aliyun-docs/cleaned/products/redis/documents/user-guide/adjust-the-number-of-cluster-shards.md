# 调整集群实例的分片数-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/adjust-the-number-of-cluster-shards

# 调整集群分片数
当业务的数据规模或读写流量增长时，可以通过增加集群实例的分片数来水平扩展性能。
## 准备工作
确认集群部署模式：云原生版与经典版集群的变配流程、业务影响和限制完全不同。操作前，请登录控制台，在实例的基本信息页面确认您的实例部署模式。
选择业务低峰期：云原生版集群变配可能引发响应延迟波动，经典版集群变配会产生连接闪断。为避免影响业务，建议在业务低峰期执行操作。
了解费用：
按量付费实例：增删分片数后，会按新规格计费。
包年包月实例：增加分片需支付新增分片的费用；删除分片，会自动退款。具体的费用说明和退款说明，请参见[变配说明](../product-overview/configuration-changes.md)。
## 操作步骤
## 云原生版集群
在原实例上直接增加或删除分片，然后自动进行数据重平衡。
影响
增加分片无连接闪断、无只读状态，平滑扩容。
删除分片会强制断开其上的连接，可能会造成部分连接闪断，请确保您的应用具备重连机制。
可能引发响应延迟的波动，建议在业务低峰期进行。
限制
除代理模式实例在删除分片时支持选择可维护时间内执行外，其余场景均立即执行。操作提交后，实例状态将变为变配中。
实例的分片数最少为2个，最多为256个。单次操作最多可增加或删除64个分片。
操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在实例信息页面的分片信息区域，根据需求执行操作：
增加分片
单击增加分片，在弹出的对话框中设置要增加的分片数量，然后单击去支付并完成支付流程。
说明
新增分片的规格与现有分片保持一致，不支持调整。
增加分片时，为保证数据重平衡效率，建议单次增加的分片数不少于当前总分片数的1/6（向上取整）。例如：
当前实例为8分片，建议增加分片数不少于2个（8/6≈1.33，向上取整为2）。
当前实例为64分片，建议增加分片数不少于11个
删除分片
警告
删除分片会降低实例的总容量和性能，请谨慎操作。
单击批量删除或目标分片右侧的删除。
在确认对话框中单击确定。分片将立即被删除，其数据会自动迁移至其他分片。
## 经典版集群
创建一个具有新分片数的新实例，将数据从原实例完整迁移至新实例，然后在指定时间将业务连接切换至新实例。
### 影响
连接闪断：实例切换时会出现1~2次30秒内的连接闪断，应用需具备重连机制。
服务只读：通常会出现1分钟内的只读状态。在写入量大的场景下，只读时间可能增加。
版本升级：变配时，系统会将实例的小版本升级至最新。
限制
若实例开启了直连地址，则无法调整分片数。更多信息，请参见[经典版集群实例变配方案](../support/why-do-i-fail-to-change-the-configurations-of-a-cluster-instance-that-use-local-disks.md)。
操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在实例详情页右上角，单击规格调整。在下拉菜单中：
包年包月实例：选择规格升配或规格降配。
按量付费实例：选择规格升降配。
在变配页面，调整分片数量，然后单击立即购买。
重要
在切换时间配置项，强烈推荐选择[可维护时间段](set-a-maintenance-window.md)执行切换，以减少对业务高峰期的影响。在任务执行前，您随时可以在任务中心修改计划的执行时间。
根据页面提示完成支付流程。
## 验证结果
提交变配任务后，实例状态将变为变配中。您可以在控制台的[任务中心](https://kvstore.console.aliyun.com/Redis/jobCenter)页面跟踪任务进度。任务完成后，返回实例详情页，确认分片信息区域的分片数量已更新为目标值。
## 常见问题
Q：增加或删除实例的分片数，数据会重分布吗？
A：会。当实例分片数发生变化时，系统会自动进行数据重平衡以保证数据均匀分布，此过程无需人工干预，重分布的过程中不影响业务正常访问。
Q：删除分片，数据会丢失吗？
A：不会。被删除分片上的数据会自动迁移并重新分布到实例的其余分片中。
Q：删除分片，会退款吗？
A：对于包年包月实例，删除分片产生的费用差额会自动退款。具体说明，请参见[变更配置费用说明](../product-overview/configuration-changes.md)。
Q：经典版实例能转换为云原生版实例吗？
A：可以。转换后可享受无感扩缩容等更优的管控体验。操作详情请参见[转为云原生部署模式](change-to-the-cloud-native-deployment-mode.md)。
## 相关操作与参考
### 相关操作
如需调整单个分片的内存或性能规格，请参见[升降实例规格](change-the-instance-specification.md)。
### API参考
| API 接口 | 说明 |
| --- | --- |
| [AddShardingNode](../developer-reference/api-r-kvstore-2015-01-01-addshardingnode-redis.md) | 增加 云原生 版集群实例的分片。 |
| [DeleteShardingNode](../developer-reference/api-r-kvstore-2015-01-01-deleteshardingnode-redis.md) | 删除 云原生 版集群实例的分片。 |
| [ModifyInstanceSpec](../developer-reference/api-r-kvstore-2015-01-01-modifyinstancespec-redis.md) | 调整 经典 版集群实例的分片数或规格。 |
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
