# 转换ECS实例的公网带宽计费方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/change-the-billing-method-for-network-usage-1

# 转换固定公网IP的带宽计费方式
对于使用固定公网IP的ECS实例，如果当前带宽计费方式不满足需求，您可以将公网带宽的计费方式由按固定带宽计费转换为按使用流量计费，或者由按使用流量计费转换为按固定带宽计费。
说明
如您使用的是弹性公网IP（EIP），且需要转换计费方式，请参见[转换计费方式](../../eip/documents/switch-billing-methods.md)。
## 固定公网IP的带宽计费方式
按固定带宽：按您指定的带宽值收费。使用过程中，实际的出网带宽不会超过指定的带宽值。适用于对网络带宽要求比较稳定的业务场景。
按使用流量：一种后付费方式，按实际使用的流量计费。此时设置的带宽值为出网带宽峰值，以防突然爆发的流量产生较高费用。适用于对网络带宽需求变化较大的业务场景。
重要
按使用流量计费模式的出入带宽峰值都是带宽上限，不作为业务承诺指标。当出现资源争抢时，带宽峰值可能会受到限制。如果您的业务需要带宽的保障，请使用按固定带宽计费模式。
中国香港地域下的BGP精品（多线）不支持按使用流量计费。
## 按固定带宽转按使用流量
以下操作指导您如何在ECS控制台将实例的公网带宽计费模式由按固定带宽计费转换为按使用流量计费。您也可以通过调用[ModifyInstanceNetworkSpec](developer-reference/api-ecs-2014-05-26-modifyinstancenetworkspec.md)API的方式进行转换。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到待转换的实例，并进入实例详情页面，在全部操作中选择升降配 >更改带宽。
重要
对于包年包月的ECS实例，如果您操作过带宽临时升级，并选择将公网带宽的计费方式从按固定带宽转换为按使用流量，那么所有已生效和未生效的带宽临时升级订单都将被取消并退款。
在高流量使用场景中，公网带宽采用按使用流量方式计费可能会增加您的网络流量费用。建议您预先进行预算评估，以确保该计费方式符合您的预算计划。关于如何选择公网带宽计费方式，请参见[公网带宽计费](public-bandwidth.md)。
在弹出的更改带宽对话框中，操作方式选择更改带宽，带宽计费方式选择按使用流量 (CDT)，并设置流量带宽峰值。
仔细阅读页面下方的服务协议和服务等级协议内容，如无问题，选中我已阅读并同意Cloud Data Transfer服务协议，然后单击立即更改。转换完成后，新配置立即生效。
说明
阿里云也为您提供了[在实例列表页执行批量操作](user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)的功能，选中多个待转换的实例后，进行批量转换操作。
## 按使用流量转按固定带宽
以下操作指导您如何在ECS控制台将实例的公网带宽计费模式由按使用流量计费转换为按固定带宽计费。您也可以通过调用[ModifyInstanceNetworkSpec](developer-reference/api-ecs-2014-05-26-modifyinstancenetworkspec.md)API的方式进行转换。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
找到待转换的实例，并进入实例详情页面，在全部操作中选择升降配 >更改带宽。
重要
对于包年包月的ECS实例，如果您操作过带宽临时升级，并选择将公网带宽的计费方式从按固定带宽转换为按使用流量，那么所有已生效和未生效的带宽临时升级订单都将被取消并退款。
在高流量使用场景中，公网带宽采用按使用流量方式计费可能会增加您的网络流量费用。建议您预先进行预算评估，以确保该计费方式符合您的预算计划。关于如何选择公网带宽计费方式，请参见[公网带宽计费](public-bandwidth.md)。
在弹出的更改带宽对话框中，操作方式选择更改带宽，带宽计费方式选择按固定带宽，并设置固定带宽值。
仔细阅读页面下方的产品服务协议和服务等级协议内容，单击立即更改。转换完成后，新配置立即生效。
说明
阿里云也为您提供了[在实例列表页执行批量操作](user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)的功能，选中多个待转换的实例后，进行批量转换操作。
## 相关文档
计费方式转换后，系统将按照新的计费方式来计算公网带宽的费用。更多信息，请参见[公网带宽计费](public-bandwidth.md)。
根据新的计费方式，您可能需要调整带宽限制或配额。
[修改固定公网带宽](user-guide/modify-the-bandwidth-configurations.md)
[按量付费实例修改带宽](user-guide/modify-the-bandwidth-configurations-of-pay-as-you-go-instances.md)
[包年包月实例临时升级固定公网带宽（连续时间段）](user-guide/temporary-bandwidth-upgrade.md)
[包年包月实例临时升级固定公网带宽（周期性）](user-guide/temporary-upgrade-bandwidth-on-a-daily-basis.md)
如果您希望更加灵活地管理公网IP，如支持在ECS实例上的弹性插拔等，可以将[固定公网](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[转为弹性公网](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)[IP](user-guide/convert-the-public-ip-address-of-an-instance-in-a-vpc-to-an-eip.md)。
重要
如果固定公网IP转换为EIP后，再将EIP的计费方式由按量付费转换为包年包月，可能会存在一定差价，请您谨慎操作。更多信息，请参见[计费](billing-faq.md)[FAQ](billing-faq.md)。
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
