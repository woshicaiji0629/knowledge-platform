# Redis开源版云原生版实例规格-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/product-overview/instance-types-of-cloud-native-community-edition-instances

# Redis开源版云原生版实例规格
本文介绍Redis开源版云原生实例的规格，包含内存容量、CPU性能、网络带宽、连接数、QPS参考值等信息。
## 实例规格
下表为单个分片的规格，集群架构、读写分离架构实例的整体性能为：分片规格性能 * 分片数。
说明
规格中的[ESSD](../../../ecs/documents/user-guide/essds.md)[云盘](../../../ecs/documents/user-guide/essds.md)仅用于系统运行（例如存储日志、备份临时文件、AOF文件等），不作为数据存储的介质。
关于集群架构直连模式与集群架构代理模式的差异，请参见[集群架构](cluster-master-replica-instances.md)。
集群架构的云原生实例支持自由调整分片节点的数量，更多信息请参见[调整集群分片数](../user-guide/adjust-the-number-of-cluster-shards.md)。
### 非集群架构（标准架构）的分片规格
非集群架构即为标准架构，以下规格适用于非集群架构的云原生实例。
说明
若标准架构开启读写分离，请参见下方[读写分离架构的分片规格](instance-types-of-cloud-native-community-edition-instances.md)。
| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 256 MB | redis.shard.micro.ce | 3 | 0.25 | 1 | 192 Mbps（24 MB/s） | 10,000 | 100,000 |
| 1 GB | redis.shard.small.2.ce | 3 | 1 | 5 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB | redis.shard.mid.2.ce | 3 | 2 | 10 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB | redis.shard.large.ce | 3 | 4 | 20 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | redis.shard.xlarge.ce | 3 | 8 | 40 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | redis.shard.2xlarge.ce | 3 | 16 | 80 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 24 GB | redis.shard.3xlarge.ce | 3 | 24 | 120 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 32 GB | redis.shard.4xlarge.ce | 3 | 32 | 160 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | redis.shard.8xlarge.ce | 3 | 64 | 320 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
### 集群架构直连模式的分片规格
以下规格适用于集群架构直连模式的云原生实例。
| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB | redis.shard.small.ce | 3 | 1 | 5 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB | redis.shard.mid.ce | 3 | 2 | 10 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB | redis.shard.large.ce | 3 | 4 | 20 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | redis.shard.xlarge.ce | 3 | 8 | 40 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | redis.shard.2xlarge.ce | 3 | 16 | 80 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 24 GB | redis.shard.3xlarge.ce | 3 | 24 | 120 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 32 GB | redis.shard.4xlarge.ce | 3 | 32 | 160 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | redis.shard.8xlarge.ce | 3 | 64 | 320 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
### 集群架构代理模式与读写分离架构的分片规格
以下规格适用于集群架构代理模式与读写分离架构的云原生实例。
| 规格名称 | 规格代码（API 使用） | CPU 核数 | 内存（GB） | ESSD 云盘（GB） | 带宽 | 最大连接数 | QPS 参考值 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 GB | redis.shard.with.proxy.small.ce | 3 | 1 | 5 | 384 Mbps（48 MB/s） | 10,000 | 100,000 |
| 2 GB | redis.shard.with.proxy.mid.ce | 3 | 2 | 10 | 768 Mbps（96 MB/s） | 10,000 | 100,000 |
| 4 GB | redis.shard.with.proxy.large.ce | 3 | 4 | 20 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 8 GB | redis.shard.with.proxy.xlarge.ce | 3 | 8 | 40 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 16 GB | redis.shard.with.proxy.2xlarge.ce | 3 | 16 | 80 | 768 Mbps（96 MB/s） | 20,000 | 100,000 |
| 24 GB | redis.shard.with.proxy.3xlarge.ce | 3 | 24 | 120 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 32 GB | redis.shard.with.proxy.4xlarge.ce | 3 | 32 | 160 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
| 64 GB | redis.shard.with.proxy.8xlarge.ce | 3 | 64 | 320 | 768 Mbps（96 MB/s） | 30,000 | 100,000 |
说明
集群架构代理模式与读写分离架构实例的最大连接数不直接与分片规格相关，具体计算规则参考[最大连接数说明](instance-types-of-cloud-native-community-edition-instances.md)。
## 性能说明
| 架构 | 性能说明 |
| --- | --- |
| [标准架构](standard-master-replica-instances.md) | 实例整体的性能与实例规格表中对应的性能一致。 |
| [集群架构直连模式](cluster-master-replica-instances.md) [集群架构代理模式](cluster-master-replica-instances.md) [读写分离功能](read-or-write-splitting-instances-1.md) | 实例整体的性能 = 分片规格的性能 * 分片数。 说明 集群架构代理模式实例的带宽上限为 20Gbps(2.5GB/s)，而最大连接数的计算规则取决于 Proxy 节点数，与分片数无关，上限为 50 万。 例如实例具备 4 个分片，分片的规格为 redis.shard.with.proxy.small.ce，每个分片的性能为： CPU 核数：2 工作核+1 后台核。 带宽：384 Mbps（48 MB/s）。 最大连接数：10,000。 QPS 参考值：100,000。 那么，该实例的整体性能即为： CPU 核数：12 核。 带宽：1,536 Mbps（192 MB/s）。 分片最大连接数为：40,000。 Proxy 最大连接数为：360,000（以该连接数为准）。 QPS 参考值：400,000。 |
## CPU核数说明
3个核心分为2工作核和1后台核。 工作核用于处理用户业务请求，后台核用于处理持久化、过期加速、性能分析、日志等非业务类任务。
## 带宽说明
上表中的带宽值是单个分片的带宽，集群架构、读写分离架构实例的总带宽为所有分片节点带宽的总和。
集群架构代理模式与读写分离架构的带宽上限为20Gbps(2.5GB/s)，达到该上限后，即使增加分片数量，带宽也不会提高。集群架构直连模式无整体带宽限制。
带宽分别应用于上行带宽和下行带宽，如果某规格的总带宽为192 Mbps（24 MB/s），则该规格实例的上下行带宽都是192 Mbps（24 MB/s）。
Tair和Redis开源版的带宽限制，是指分片节点的带宽，与网络连接类型无关。
更多关于带宽的常见问题请参见[带宽的常见问题](../user-guide/faq-about-bandwidth.md)。
## 最大连接数说明
代理模式：实例最大连接数的计算规则为：min(Proxy节点数*12万, 50万）。因此上限为50万，如业务连接数需求超过此限制，建议采用集群直连模式，连接数可随分片数量线性扩展。
| 分片数 | Proxy 节点数 | 最大连接数 |
| --- | --- | --- |
| 1 | 2 | 240,000 |
| 2 | 2 | 240,000 |
| 3 | 3 | 360,000 |
| 4 | 3 | 360,000 |
| 5~6 | 3 | 360,000 |
| 7~8 | 4 | 480,000 |
| ≥9 | ≥5 | 500,000（上限） |
直连模式：若单分片最大连接数的上限为10,000，实例最大连接数的上限为：分片数 * 10,000。
## 常见问题
Redis开源版不同规格实例在运行速度、性能上有区别吗？
除256MB、1GB的Redis开源版实例的带宽低于768Mbps（96MB/s），2 GB及以上Redis开源版实例在CPU、带宽上都是相同的，仅内存容量不同。
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
