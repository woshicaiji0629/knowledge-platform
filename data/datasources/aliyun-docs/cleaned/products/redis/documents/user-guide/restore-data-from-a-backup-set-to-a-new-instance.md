# 使用备份集克隆新实例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/restore-data-from-a-backup-set-to-a-new-instance

# 从备份集恢复至新实例
在误删除数据、快速部署业务等场景中，您可以随时基于指定的备份集克隆出新的云数据库 Tair（兼容 Redis）实例，新实例中的数据与指定备份集中的数据一致。
## 注意事项
在克隆实例时，您可以创建与源实例不同分片数或不同架构的新实例，但是您必须确保新实例的总内存规格大于备份集的大小，否则会导致恢复失败。
在克隆过程中，请勿对源实例进行变配操作，否则会导致克隆失败。
## 费用说明
执行本操作将创建一个新的实例并产生相关费用，更多信息，请参见[计费项](../product-overview/billable-items.md)。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，单击备份与恢复。
找到目标备份集，单击右侧操作列的恢复。
说明
若实例为经典版集群架构，请选择目标备份集的所有子分片备份集，例如2分片的集群实例，需勾选r-bp1vhgd6dzgu89****-db-0和r-bp1vhgd6dzgu89****-db-1备份集，再单击左上方的恢复。
在弹出的对话框中，阅读提示并单击确定。
在克隆实例页，按需完成对应设置，具体请以控制台为准。
阅读服务协议，单击立即购买。
支付成功后等待1~5分钟，即可在控制台看到新创建的实例。
## 后续步骤
新实例创建成功后，您可能需要进行如下操作：
设置新实例的白名单，更多信息请参见[设置](configure-whitelists.md)[IP](configure-whitelists.md)[白名单](configure-whitelists.md)。
若创建实例时未设置密码，请设置新实例的账户密码，更多信息请参见[修改或重置密码](change-or-reset-the-password.md)。若已设置请忽略。
在控制台的实例详情页，获取新实例的连接地址，连接至新实例执行数据验证，验证无误后可在业务程序侧使用新实例的连接地址，完成业务恢复。
说明
克隆成功后，若您不再需要源实例，您可以释放源实例来节约资源，具体操作，请参见[退款说明](../product-overview/refunds.md)。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [CreateInstance](../developer-reference/api-r-kvstore-2015-01-01-createinstance-redis.md) | 创建一个新实例，并将选定的源实例备份集恢复至新实例中。 |
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
