# 开通或关闭RDS PostgreSQL外网地址-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/apply-for-or-release-a-public-endpoint-on-an-apsaradb-rds-for-postgresql-instance

# 为RDS PostgreSQL实例开通外网地址
RDS默认提供内网地址，仅允许同VPC下的实例（ECS等阿里云实例）内网访问，如果您的业务部署在其他VPC或本地机器上，则需要开通外网地址，您的业务可以通过外网地址访问RDS实例。
## 内网地址和外网地址
| 地址类型 | 说明 |
| --- | --- |
| 内网地址 | 默认提供内网地址，无需申请，无法释放，可以切换网络类型。 如果您的应用部署在 ECS 实例，且该 ECS 实例与 RDS 实例在同一 VPC 下，则 RDS 实例与 ECS 实例可以通过内网互通，无需申请外网地址。 通过内网访问 RDS 实例时，安全性高，而且可以实现 RDS 的最佳性能。 |
| 外网地址 | 外网地址需要手动申请，不需要时也可以释放。 无法通过内网访问 RDS 实例时，您需要申请外网地址。具体场景如下： ECS 实例访问 RDS 实例，且 ECS 实例与 RDS 实例位于不同 VPC 下。 阿里云以外的设备访问 RDS 实例。 重要 申请外网地址和后续产生的公网流量暂不收费。 外网地址会降低实例的安全性，请谨慎使用。 为了获得更快的传输速率和更高的安全性，建议您将应用迁移到与您的 RDS 实例在同一地域且网络类型相同的 ECS 实例，然后使用内网地址。 |
## 开通或关闭外网地址
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏单击数据库连接。
您可以执行申请或释放操作：
如果未申请外网地址，可以单击开通外网地址。
如果已申请外网地址，可以单击关闭外网地址。
警告
开通外网地址时，默认会勾选将0.0.0.0/0加入白名单，0.0.0.0/0表示允许任何IP访问RDS实例，只建议在测试时使用，请勿在线上业务实例中设置IP白名单为0.0.0.0/0。
在弹出的对话框中，单击确定。
## 相关文档
开通外网地址后，您需要将客户端或应用程序所在机器的公网IP添加到RDS实例的白名单中，才能通过外网访问RDS实例。更多信息，请参见[设置白名单](configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance-1.md)。
您可以通过pgAdmin客户端、PostgreSQL命令行工具、应用程序等方式连接RDS实例。更多信息，请参见[连接](connect-to-an-apsaradb-rds-for-postgresql-instance.md)[PostgreSQL](connect-to-an-apsaradb-rds-for-postgresql-instance.md)[实例](connect-to-an-apsaradb-rds-for-postgresql-instance.md)。
您可以通过API开通或释放外网地址。
| API | 描述 |
| --- | --- |
| [AllocateInstancePublicConnection](api-rds-2014-08-15-allocateinstancepublicconnection-postgresql.md) | 开通实例的外网地址 |
| [ReleaseInstancePublicConnection](api-rds-2014-08-15-releaseinstancepublicconnection-postgresql.md) | 关闭实例的外网地址 |
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
