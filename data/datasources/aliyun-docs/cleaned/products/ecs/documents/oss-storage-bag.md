# OSS标准-本地冗余存储包在快照存储费用中的应用-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/oss-storage-bag

# OSS资源包
快照数据独立存储在对象存储OSS中，按容量和存储时长收取费用。您可以购买OSS提供的标准-本地冗余存储包（简称OSS资源包）进行抵扣，相比按量付费更划算。OSS资源包在有效期内会自动抵扣标准快照存储费用，若OSS资源包到期或额度全部抵扣完后，则自动恢复按量付费。
## 使用限制
购买资源包之前，请您了解如下使用限制，以便正确购买抵扣快照存储费用的资源包。
仅标准-本地冗余存储包类型的OSS资源包可以用来抵扣标准快照的存储费用，其他类型的资源包不支持抵扣。
OSS资源包仅支持抵扣标准快照存储费用，不支持抵扣归档快照存储费用和复制快照流量费用。
同地域、同类型的OSS资源包在同一时段内只能购买一次，不支持叠加购买。
说明
如果您需要更高规格或更长周期的资源包，可以升级或续费资源包。更多信息，请参见[续费或升级](oss-storage-bag.md)。
OSS资源包仅支持抵扣当前阿里云账号下产生的费用，不支持跨账号抵扣。
OSS指定地域的OSS资源包仅支持抵扣同地域的快照存储费用，中国内地通用OSS资源包支持跨地域抵扣快照存储费用。更多信息，请参见[资源包](../../oss/documents/resource-plan.md)。
OSS资源包仅支持抵扣购买资源包后产生的费用，不支持抵扣资源包购买前产生的费用。
说明
对于购买资源包前产生的欠费，您只能通过充值抵消欠款。为阿里云账号充值的具体步骤，请参见[为阿里云账号充值](https://help.aliyun.com/zh/document_detail/324650.html#task-2020864)。
## 购买资源包
说明
以下操作以在ECS控制台入口购买OSS资源包为例，关于在OSS控制台购买资源包的具体操作请参见[资源包购买指南](../../oss/documents/purchase-resource-plans.md)。
购买OSS资源包前，建议您先评估以下内容以便购买合适的资源包。
确认您快照所在的地域，快照和OSS资源包必须位于同一地域才能抵扣。
预估您的快照容量，确定购买的OSS资源包规格。
如何根据快照容量评估购买的OSS资源包规格？
示例1：假设您在华北2（北京）地域已经有100 GB的标准快照，则购买多大容量的OSS资源包合适？
您可以在华北2（北京）地域购买100 GB的OSS资源包，购买后每小时开始抵扣100 GB快照的存储费用。
示例2：假设您在华北2（北京）地域计划为容量为100 GB的云盘周期性创建云盘快照备份数据，则购买多大容量的OSS资源包合适？
建议您根据云盘后续的备份情况（多久备份一次、快照保留多长时间等因素）来预估可能产生的快照容量，然后再评估需要购买多大容量的OSS资源包，避免产生资源浪费。例如您计划每天凌晨对云盘创建一份快照（容量为0.5 GB），快照保留时间6个月，则6个月内产生的快照容量为90 GB。因此，您可以在创建快照前购买容量为100 GB、时长为6个月的OSS资源包，这样可以完全抵扣快照的存储费用。
进入[ECS](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[控制台](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[OSS](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)[资源包购买入口](https://ecs.console.aliyun.com/snapshot/region/cn-hangzhou)，单击立即购买。
跳转至OSS控制台资源包购买页，选择购买参数，并按照页面指引完成购买。
商品类型选择OSS资源包。
资源包类型选择标准 - 本地冗余存储。
选择OSS资源包的地域。
说明
指定地域的资源包只能抵扣指定地域的费用，中国内地通用的资源包可以跨地域抵扣中国内地各地域的存储费用，请您根据业务需求合理选择。关于中国内地通用资源包支持抵扣的中国内地地域，请参见[资源包](../../oss/documents/resource-plan.md)。
选择OSS资源包的规格和购买时长。
OSS资源包根据规格和购买时长进行计费。您可以访问[资源包定价详情](https://www.aliyun.com/price/product?spm=5176.8064714.694085.pricedetail2222.308e14ceu4kW4A#/oss/detail)，在包年包月-资费详情页签下查看标准-本地冗余存储包的价格，实际费用以购买页显示为准。
## 抵扣规则
### 抵扣方式
购买OSS资源包后，您无需手动使用OSS资源包，系统将自动抵扣同地域内标准快照的存储容量费用。OSS资源包的抵扣方式为总量恒定型，即在有效期内每小时都以固定额度（容量规格）抵扣快照存储容量费用。关于总量恒定型的更多说明，请参见[资源包](../../oss/documents/resource-plan.md)。
例如您在华北2（北京）地域购买了时长为1年、容量规格为100 GB的OSS资源包，则1年内每小时都可以抵扣华北2（北京）地域下100 GB的标准快照存储容量费用。当1年内该地域的某一小时快照存储容量超出100 GB时，则OSS资源包将抵扣其中100 GB的容量费用，超出部分按量付费。
### 抵扣顺序
OSS资源包 > 按量付费
说明
如果在当前地域同时购买了[存储容量单位包](storage-capacity-units-1.md)[SCU](storage-capacity-units-1.md)，则抵扣顺序为：OSS资源包 > 存储容量单位包SCU > 按量付费。
### 抵扣示例
示例一：假设您购买了华北2（北京）地域、规格为10 TB、购买时长1年的OSS资源包，则1年内华北2（北京）地域快照容量在10 TiB之内的部分均会优先通过资源包抵扣，超出部分自动按量付费。
示例二：假设您购买了中国内地通用、规格为10 TB、购买时长1年的OSS资源包，则1年内中国内地地域快照容量在10 TiB之内的部分均会优先通过资源包抵扣，超出部分自动按量付费。
## 续费或升级
### 续费
为了确保您的优惠不会中断，建议您对已经购买的尚未到期的OSS资源包提前进行续费操作。您可以选择手动续费，也可以设置自动续费，以防忘记手动操作而导致优惠中断。具体操作，请参见[资源包续费指南](../../oss/documents/renew-resource-plans.md)。
如果OSS资源包到期未续费，快照存储费用将默认采用按量付费。您也可以在OSS资源包过期后选择重新购买，以继续享受优惠。
### 升级
如果您需要更高规格的OSS资源包，可以对当前资源包进行升级。具体操作，请参见[资源包升级指南](../../oss/documents/upgrade-resource-plans.md)。
## 退款
OSS资源包支持线上[自助退款](https://usercenter2.aliyun.com/refund/refund)。具体操作，请参见[资源包退款指南](../../oss/documents/refund-resource-plans.md)。关于退订规则的更多信息，请参见[退订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#b475cd1055o92)。
## 过期
OSS资源包超出有效期后，无法继续抵扣快照存储费用，也无法进行续费、升级等操作。
如果您不希望继续使用OSS资源包，资源包到期后，快照存储费用将默认采用按量付费。
如果您希望继续使用享有更高折扣优惠的资源包，您可以选择重新购买OSS资源包。
## 查看资源包使用情况
您可以在阿里云费用与成本中心的明细账单中，查看OSS资源包对快照的抵扣情况，判断购买的OSS资源包是否有效降低快照的使用成本。具体操作，请参见[资源包使用明细](../../oss/documents/view-the-usage-details-of-a-resource-plan.md)。
## 相关文档
有关快照更多的计费信息，请参见[快照计费](snapshots-1.md)。
有关OSS资源包的更多的计费信息，请参见[OSS](../../oss/documents/storage-fees.md)[存储费用](../../oss/documents/storage-fees.md)。
[为什么购买了](user-guide/snapshot-faq.md)[OSS](user-guide/snapshot-faq.md)[资源包，快照还在计费？](user-guide/snapshot-faq.md)
您可以在[OSS](https://oss.console.aliyun.com/package)[资源包列表](https://oss.console.aliyun.com/package)或调用API接口[DescribeSnapshotPackage](developer-reference/api-ecs-2014-05-26-describesnapshotpackage.md)查询已购买的OSS资源包。
使用OSS资源包的一些常见问题，请参见[资源包](../../oss/documents/package-faq.md)。
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
