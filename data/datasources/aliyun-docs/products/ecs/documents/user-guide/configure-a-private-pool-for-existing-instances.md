# 如何为已有实例设置私有池-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/configure-a-private-pool-for-existing-instances

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 为已有实例设置私有池

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以为已有实例设置私有池，让已有实例使用私有池以充分利用私有池的容量，或者空出私有池的容量以保障创建新的实例。

## 背景信息

设置私有池功能的应用示例包括但不限于：

- 

已经使用私有池创建了实例，在整体库存紧张时希望储备更多实例。您可以设置已有实例不使用私有池，然后再使用私有池保障创建新的实例。

- 

购买容量预定后，暂时不需要创建实例，希望已有实例直接使用容量预定的关联私有池。您可以为这些实例手动指定私有池ID，避免私有池容量闲置而浪费成本。

- 

您需要释放当前持有的实例再购买，临时希望购买容量预定预留资源，但由于当前库存不足导致容量预定购买失败。您可以设置实例的私有池匹配方式为开放，则当前持有的实例也被视为可匹配的资源，可以成功购买容量预定。

## 操作步骤

重要

仅支持为按量付费实例设置私有池。

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标实例ID进入实例详情页，单击全部操作展开所有操作面板，然后搜索并单击设置私有池。

- 

在设置私有池对话框中，选择私有资源池类型。

- 

手动指定私有池ID：设置私有资源池类型为指定（Target），并手动指定一个专用或开放私有池的ID，即对应弹性保障或立即生效容量预定的ID。

- 

手动绑定标签匹配开放私有池：设置私有资源池类型为开放（Open），并为实例绑定与弹性保障或容量预定相同的标签，即可使用对应的开放私有池。在实例已经通过标签匹配了开放私有池时，如果需要通过[编辑实例标签](products/ecs/documents/user-guide/edit-the-tags-of-an-instance.md)触发重新匹配，实例必须启用节省停机模式或者手动停止并启动实例，直接重启实例不会触发重新匹配。

说明

如果同时指定了开放私有池的ID并为实例绑定了标签，则使用指定ID的开放私有池。例如，指定了开放私有池A的ID，同时绑定了与开放私有池B相同的标签，则使用开放私有池A。

- 

自动选择开放私有池：设置私有资源池类型为开放（Open）。系统会自动选择一个无标签的开放私有池。

- 

不使用私有池：设置私有资源池类型为不使用（None）。不使用任何私有池，仅使用公共池。

重要

以下两个场景，可能导致实例从私有池中移除。系统补充私有池容量如遇到库存不足，私有池容量将被缩减，请谨慎操作。

场景1：从指定（Target）模式改为开放（Open）模式。

场景2：从指定（Target）模式或者开放（Open）模式，改为不使用（None）模式。

- 

单击确定。

## 后续步骤

为已有实例设置私有池后，您可以前往私有资源池页签查看私有池和实例的关联情况。具体操作，请参见[在私有池查看预留的资源](products/ecs/documents/user-guide/view-a-private-pool.md)。

[上一篇：使用私有池容量创建实例](products/ecs/documents/user-guide/use-a-private-pool-to-create-instances.md)[下一篇：使用云监控查看私有池容量](products/ecs/documents/user-guide/use-cloudmonitor-to-view-private-pools.md)

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
