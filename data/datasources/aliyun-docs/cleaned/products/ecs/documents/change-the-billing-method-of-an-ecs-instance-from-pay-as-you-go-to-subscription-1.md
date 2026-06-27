# 将按量付费ECS转为包年包月-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1

# 按量付费转包年包月
创建一台按量付费ECS实例后，您可以将ECS实例的计费方式转为包年包月，提前预留资源，同时享受更大的价格优惠。
## 前提条件
实例非[已停售的实例规格](user-guide/retired-instance-types.md)或抢占式实例。
若有未支付的订单，须先支付或作废未支付的订单。
未若为实例设置了自动释放时间，须先[关闭自动释放设置](user-guide/release-an-instance.md)。
实例处于运行中或已停止状态，若实例处于节省停机模式需先启动实例。
若ECS实例处于上述状态时下单成功，但是在支付完成前变更了实例状态，会导致支付和转换失败。需在还原下单时实例状态，并前往订单中心重新支付该订单。
## 操作步骤
## 控制台
前往[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面左侧顶部，选择目标资源所在的资源组和地域。
找到待转换的ECS实例，单击实例ID进入实例详情页，在全部操作中，选择按量付费转包年包月。
在页面中，完成计费转换相关的设置：
设置购买时长。
选择是否将实例上挂载的按量付费的数据盘转换为包年包月云盘。
设置是否开启自动续费。
选中《云服务器 ECS 服务条款》。
单击确认订单，并按页面提示完成支付。
阿里云也提供了[在实例列表页执行批量操作](user-guide/batch-operation-of-ecs-instances-through-the-ecs-console.md)的功能，支持单次最多批量转换20台实例，批量转换时仅支持设置相同的购买时长。
## API
通过API接口[ModifyInstanceChargeType](api-modifyinstancechargetype.md)将按量付费ECS实例转换为包年包月的ECS实例。
## 转换影响
转换完成后，除ECS实例规格、实例系统盘、镜像软件许可证会转为包年包月计费方式外，还会对实例产生如下影响：
若实例转换前开通了公网带宽或绑定了弹性公网IP，转换后公网带宽或弹性公网IP的计费方式不会发生变更，可能仍然会产生按量付费费用。需注意关注账号余额状态，避免欠费停机影响资源使用。若希望将网络资源转换为包年包月计费方式，可以参见以下途径：
[转换固定公网](change-the-billing-method-for-network-usage-1.md)[IP](change-the-billing-method-for-network-usage-1.md)[的带宽计费方式](change-the-billing-method-for-network-usage-1.md)将公网带宽转换为包年包月付费。
若实例绑定了按量付费的弹性公网IP，可以参考[转换弹性公网](../../eip/documents/switch-billing-methods.md)[IP](../../eip/documents/switch-billing-methods.md)[计费方式](../../eip/documents/switch-billing-methods.md)将弹性公网IP转换为包年包月付费。
若按量付费实例挂载了数据盘，且在转换时未勾选转换，转换后仍为按量付费的计费方式。后续可以在需要时单独进行[转换云盘计费方式](switch-the-billing-method-of-a-disk.md)。
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
