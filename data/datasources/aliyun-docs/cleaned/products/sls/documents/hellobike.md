# 哈啰出行迁移日志至日志服务替代KafkaESClickHouse并降本30%-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/hellobike

# 哈啰出行
哈啰出行通过把日志数据迁移到日志服务，替代原有的Kafka、ES、ClickHouse，累积节省成本30%，同时满足了稳定性、扩展性以及日志查询与分析的需求。
## 公司简介
哈啰出行是本地出行及生活服务平台，致力于应用数字技术的红利，为人们提供更便捷的出行以及更好的普惠生活服务。更多信息，请参见[哈啰出行](https://www.hello-inc.com/)。
## 业务场景
哈啰出行为用户提供哈啰单车、哈啰助力车分时租赁的服务。共享单车服务致力于解决最后一公里的出行难题。哈啰出行以技术创新赋能智能终端，推动运维高效执行与自营管理体系相结合，依托搭载定位芯片的智能锁，辅以后台智能规划调度、运维人员智能端口精细化运营。哈啰单车累积注册4亿多用户，入驻400多座城市，累积骑行237亿公里。依托于智能锁，赋能了在线的实时调度。单车数据、APP数据无缝打通，因而催生了数据的实时采集、分析、存储需求。
## 业务痛点
哈啰出行原有架构是将数据采集到Kafka，然后将日志写入ELK做查询，同时写入ClickHouse做分析。由于每天增量数据在TB级别，对ES稳定性压力比较大。当查询数据操作，会影响ES的写入延时。由于写入量大，查询基本处于不可用状态。因此，当天数据采用单副本，隔天再生成多副本。这种方式对数据的可靠性带来很大的挑战。此外，自建Kafka、ES、ClickHouse成本较高，急需降低成本。
## 解决方案
日志服务为哈啰出行提供了TB级别日志的实时采集、弹性扩容、实时查询的能力。
实时采集
日志服务原生支持Kafka协议。哈啰出行的各个客户端只需把Kafka的地址设置成日志服务的Kafka协议地址即实现了无缝迁移。
弹性扩容
日志服务采用Shard模型，当流量发生上涨时，可以手动分裂Shard，实现写入带宽的扩容，也可以设置成自动分裂，当流量达到上限时，自动扩容出新的Shard。
查询与分析
日志服务同时提供了查询和分析能力。在查询方面，日志服务支持关键字检索、数值范围查询、JSON字段的递归查询、多条件组合查询。在分析方面，日志服务支持以SQL 92语法分析日志，秒级分析数百亿条日志。SQL语法支持200多种函数，以及支持join计算，可与OSS、MySQL数据源做关联分析。
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
