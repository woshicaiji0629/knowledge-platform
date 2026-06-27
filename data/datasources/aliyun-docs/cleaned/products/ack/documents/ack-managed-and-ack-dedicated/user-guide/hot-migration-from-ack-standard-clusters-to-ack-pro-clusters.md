# 热迁移ACK集群基础版至ACK集群Pro版-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/hot-migration-from-ack-standard-clusters-to-ack-pro-clusters

# 热迁移ACK集群基础版至ACK集群Pro版
您可以将ACK托管集群基础版动态热迁移至ACK托管集群Pro版。热迁移无需中断业务，不影响集群业务的正常运行，集群迁移成功后不支持回退。
ACK托管集群Pro版是在ACK托管集群基础版的基础上针对企业大规模生产环境，进一步增强了可靠性、安全性，并且提供可赔付的SLA的Kubernetes集群。
ACK托管集群基础版单账号最多支持2个集群，单集群最大仅支持10个节点，规模较小，不保证集群控制面可用性，多用于个人学习与测试。为提升集群规模以及保证控制面的高可用，建议进行集群迁移以享受ACK托管集群Pro版的功能和特性。详细差异对比，请参见[集群类型](ack-cluster-overview.md)。
## 注意事项
| 注意项 | 说明 |
| --- | --- |
| 计费说明 | ACK 托管集群基础版 迁移至 ACK 托管集群 Pro 版 后，将新增 [集群管理费用](../product-overview/cluster-management-fee.md) （由 ACK 收取），其他云资源计费保持不变。 |
| 集群版本 | 仅支持 1.18 及以上版本的集群。迁移后，集群版本不变。关于集群版本机制，请参见 [版本说明](support-for-kubernetes-versions.md) 。 集群迁移不支持回退，即不能将 ACK 托管集群 Pro 版 迁移为 ACK 托管集群基础版 。若集群迁移失败，系统会自动回滚。 迁移后，集群版本保持不变。如同时有迁移集群和升级集群版本的需求，建议先完成迁移，再 [升级集群版本](update-the-kubernetes-version-of-an-ack-cluster.md) 。 |
## 操作步骤
迁移集群的流程包括前置检查和集群迁移两部分。集群迁移前置检查通过后，基础版集群才会被开始迁移至Pro版。
如前置检查未通过，请根据提示跳转到对应的检查页面，查看检查未通过的具体原因。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，找到需要迁移的ACK基础版集群，然后在操作列下，单击更多>迁移至Pro版。
在对话框，仔细阅读相关注意事项，然后单击前置检查。
单击前置检查后，页面会跳转至容器智能运维平台控制台，单击执行迁移检查，然后根据界面提示操作，对您的集群进行迁移前置检查。如果检查未通过，可以在迁移检查页面查看详情并处理。
检查通过后，返回迁移对话框阅读注意事项，然后单击确定。
迁移成功完成后，集群列表页面中目标ACK托管集群基础版的集群规格将由基础版自动变更为Pro 版。
## 常见问题
### 迁移过程中ACK托管集群基础版中的业务是否受影响？
集群迁移过程中会休眠ACK托管集群基础版的控制面组件，但不影响正在运行的业务。
### 迁移流程大概需要多长时间？
集群迁移主要包括控制面休眠、etcd数据备份以及控制面组件启动三个阶段。整体流程预计耗时10～15分钟，其不可用时间预计持续5～10分钟。
### 集群迁移后，访问链路是否会变？
迁移后，API ServerSLB IP地址不会改变，通过KubeConfig访问集群时，集群地址不发生变化。
## 相关文档
如需升级迁移后的集群版本，请参见[升级集群](upgrade-clusters.md)。
在迁移至ACK托管集群Pro版后，需手动收敛集群节点的Worker Role权限，提升节点安全性。具体操作，请参见[手动收敛](manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[ACK](manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[托管版集群的](manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[Worker RAM](manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)[角色权限](manually-converges-the-worker-ram-role-permissions-of-the-ack-managed-version-cluster.md)。
如需迁移ACK专有集群，请参见[热迁移](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[专有集群至](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[ACK](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[托管集群](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[Pro](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)[版](hot-migration-from-ack-dedicated-clusters-to-ack-pro-clusters.md)。
在超大规模集群或突发高并发场景下，可启用[ACK Pro 预设控制面](ack-pro-provisioned-control-plane.md)，预先分配并固化控制面资源，保障控制面性能始终可预期。ACK Pro预设控制面包括Pro XL、Pro 2XL、Pro 4XL三个档位，通过API 请求并发数（seats）、Pod 调度速率（个/秒）、etcd 数据库大小（GB）指标定义控制面容量。
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
