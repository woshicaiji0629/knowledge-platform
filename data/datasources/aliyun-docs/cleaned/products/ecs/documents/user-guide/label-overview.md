# 使用标签对云服务器ECS资源进行分类以精细化管理资源-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/label-overview

# 使用标签对云服务器ECS资源进行分类和管理
随着云资源增加，管理难度也在增加，您可能无法批量管理云资源的成本和监控。为了实现资源的精细化管理，您可以使用标签对资源进行分类标记。标签是重要的分组工具，可以帮助您在人员、财务和物品管理方面进行横向管理。
更多标签信息，请参见[什么是标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)。
## 应用场景
随着您创建的云服务器ECS数量的增加，利用标签进行资源分组管理和分类有利于搜索和批量操作。标签的常见场景包括：
管理应用发布流程
资源溯源，基于标签分组检索和管理资源
搭配系统运维管理、资源编排、弹性伸缩和云助手等实现基于标签自动化分组运维
基于标签管理成本和分账
设计资源或角色访问控制
本文将详细介绍以下两个场景，更多应用场景，请参见[什么是标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)。
## 场景一：优化云服务器资源管理或使用标签进行自动化运维
您可以为不同环境（如生产环境和测试环境）、操作系统（如Windows和Linux）或客户端平台（如iOS和Android）绑定不同的标签。例如，为测试环境涉及的所有ECS实例绑定一个类似Test:Server-Windows的标签键值对，以便在维护中快速筛选相关实例。
批量操作示例：
更换镜像部署应用
升级补丁
添加安全组规则控制网络访问
更多信息，请参见[使用标签获取](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)[实例并将其加入到对应标签的安全组](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)。
通过系统运维管理批量启动、停止或重启ECS实例
以批量启动ECS为例，具体操作，请参见[使用](https://help.aliyun.com/zh/resource-management/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time-1)[OOS](https://help.aliyun.com/zh/resource-management/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time-1)[批量启动带指定标签的](https://help.aliyun.com/zh/resource-management/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time-1)[ECS](https://help.aliyun.com/zh/resource-management/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time-1)[实例](https://help.aliyun.com/zh/resource-management/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time-1)。
通过云助手在多台ECS实例上运行运维脚本
以在指定标签的ECS实例上执行云助手命令为例，具体操作，请参见[使用标签控制云助手命令的执行](control-the-executions-of-cloud-assistant-commands-based-on-tags.md)。
### 场景二：团队和项目管理
在团队或项目管理中，您可以添加以群组、项目或部门为维度的标签（如CostCenter:aliyun），然后实现分组、在费用中心基于标签实现分账管理，或者交叉授权等目的。
更多信息，请参见：
[使用标签实现实例型云服务分账](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-tags-to-allocate-costs-for-instance-based-services)
[查看和导出实例型云服务的分账账单](https://help.aliyun.com/zh/resource-management/tag/use-cases/view-and-export-the-split-bills-of-instance-based-services)
[使用标签查找资源](https://help.aliyun.com/zh/resource-management/tag/user-guide/use-tags-to-query-cloud-resources)
[使用标签对](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)[ECS](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)[实例进行分组授权](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)
## 使用说明
标签都由一对键值对（Key-Value）组成，资源的任一标签的标签键（Key）必须唯一。
重要
使用标签前，您需要了解标签的使用限制及配额，请参见[什么是标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview#section-fln-n74-2dh)。
支持绑定标签的ECS资源
ECS实例
云盘
预留实例券
块存储
快照
快照一致性组
自动快照策略
镜像
镜像组件
镜像模板
安全组
弹性网卡
专有宿主机
SSH密钥对
实例启动模板
专有宿主机组
弹性保障
容量预定服务
存储容量单位包
云助手命令
云助手命令执行或文件下发结果
云助手托管实例
云助手托管实例激活码
## 创建并绑定标签
在创建标签前，请参见[标签设计的原则](https://help.aliyun.com/zh/resource-management/tag/use-cases/best-practices-for-tag-design#section-svt-g2c-pri)以了解相关背景和示例。创建或绑定标签的具体操作如下：
重要
一个资源绑定标签的上限为20个。如果超出上限，您需要解绑部分标签后再继续绑定新标签。
访问[ECS](https://ecs.console.aliyun.com/tags/region)[控制台-标签](https://ecs.console.aliyun.com/tags/region)。
在页面左侧顶部，选择目标资源所在的资源组和地域。
在自定义标签页签下，单击创建自定义标签。
在创建自定义标签页面中，完成以下操作。
创建自定义标签时必须同时绑定资源。如果需要仅创建标签，并规划标签键和标签值，请使用预置标签。更多信息，请参见[创建标签](https://help.aliyun.com/zh/resource-management/tag/user-guide/create-a-tag#task-2115168)。
创建新标签。
参数说明如下所示：
| 参数 | 是否必选 | 说明 |
| --- | --- | --- |
| 标签键 | 是 | 输入新标签键或选择已有标签键。 输入新标签键时，最多支持 128 个字符，不能以 aliyun 或 acs: 开头，不能包含 http:// 和 https:// 。 选择已有标签键时，支持模糊搜索。 |
| 标签值 | 否 | 输入新标签值。 输入新标签值时，最多支持 128 个字符，不能包含 http:// 和 https:// 。 说明 标签中同一标签键可对应不同标签值。因此，选择已有标签键，输入新标签值也可创建新标签。 |
单击下一步。
配置相关参数绑定资源。
参数说明如下所示：
| 参数 | 说明 | 示例 |
| --- | --- | --- |
| 资源选择方式 | 资源选择支持以下两种方式： 资源列表选择 ：您可以在资源列表中选择需要绑定的一个或多个资源。 输入多个资源 ID ：您可以在 输入资源 ID 区域的输入框中输入资源 ID。 说明 多个资源 ID 请分行输入，或使用半角逗号（,）分隔。 单次请求最多可以绑定 20 个标签。 | 输入多个资源 ID |
| 产品 | 选择产品的资源类型。例如，云服务器 ECS 的实例、云盘、快照等资源。 | 云服务器:实例 |
| 输入资源 ID | 输入对应云服务器 ECS 实例的实例 ID。 | i-bp12d03u8usvakpo**** |
单击确定。
（可选）查看绑定的资源列表。
在标签创建和绑定成功后，您可以在自定义标签列表上方单击图标，然后找到已成功绑定的标签，单击对应操作列的查看资源，查看绑定的资源列表。
## 解绑或删除标签
如果标签不再适用，您可以将该标签从目标资源上解绑。下面以资源类型为云服务器：实例、该资源绑定的标签为ECS:Documentation（标签键为ECS，标签值为Documentation）为例，介绍资源解绑标签的操作方法。
重要
单次最多可以解绑20个标签。
解绑标签后，如果标签绑定的资源数量为零，则该标签将在24小时内被自动删除。
在自定义标签页签下，选择资源类型为实例。
在标签列表中找到待解绑的标签ECS:Documentation，以如下任一方式进入资源列表页面。
方式一：单击ECS标签键后，在Documentation标签值对应的操作列，单击查看资源。
方式二：在ECS标签键对应的操作列，单击查看资源。
在资源列表页签下，解绑一个或多个资源。
单个解绑：选择一个待解绑的资源，单击对应操作列的解绑资源。
批量解绑：选中多个待解绑资源，单击解绑当前标签或解绑标签。
在弹出的解绑资源对话框中，单击确定。
资源解绑标签成功后，在资源列表页面，单击图标后，您可以查看到资源对应的标签已解绑。
## 标签最佳实践
您可以使用标签来精细化管理资源，常见用法及对应操作如下：
查找或导出资源
使用标签编辑器编辑资源的标签以及导出资源信息，具体操作，请参见[标签编辑器](https://help.aliyun.com/zh/resource-management/tag-editor/)。
精确查找和模糊搜索目标标签下的云资源，具体操作，请参见[使用标签查找资源](https://help.aliyun.com/zh/resource-management/tag/user-guide/use-tags-to-query-cloud-resources)。
使用标签控制资源访问
使用标签对ECS实例进行分组并授权，以满足RAM用户只能查看和操作被授权资源的需求。具体操作，请参见[使用标签对](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)[ECS](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)[实例进行分组授权](../../../ram/documents/use-cases/use-tags-to-grant-access-to-ecs-instances-by-group.md)。
通过RAM的自定义策略指定授权的标签，利用标签限制RAM用户只能查看和管理指定的ECS实例。具体操作，请参见[使用标签限制](../../../ram/documents/use-cases/use-tags-to-control-access-to-ecs-resources-1.md)[RAM](../../../ram/documents/use-cases/use-tags-to-control-access-to-ecs-resources-1.md)[用户管理指定的](../../../ram/documents/use-cases/use-tags-to-control-access-to-ecs-resources-1.md)[ECS](../../../ram/documents/use-cases/use-tags-to-control-access-to-ecs-resources-1.md)[实例](../../../ram/documents/use-cases/use-tags-to-control-access-to-ecs-resources-1.md)。
使用标签进行自动化运维
在OOS中批量启动带指定标签的多台ECS实例。具体操作，请参见[使用](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time)[OOS](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time)[批量启动带指定标签的](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time)[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time)[实例](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-start-multiple-ecs-instances-with-specific-tags-at-a-time)。
使用OOS提供的公共任务模板创建执行，为ECS实例下的云盘、弹性网卡、弹性公网IP、快照和自定义镜像批量继承ECS实例的标签。具体操作，请参见[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-enable-resources-of-the-ecs-instances-to-inherit-tags-at-a-time)[实例下的云盘、弹性网卡、弹性公网](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-enable-resources-of-the-ecs-instances-to-inherit-tags-at-a-time)[IP、快照和自定义镜像批量继承](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-enable-resources-of-the-ecs-instances-to-inherit-tags-at-a-time)[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-enable-resources-of-the-ecs-instances-to-inherit-tags-at-a-time)[实例的标签](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-oos-to-enable-resources-of-the-ecs-instances-to-inherit-tags-at-a-time)。
使用OOS提供的公共任务模板创建执行，根据指定标签获取ECS实例，并把获取到的ECS实例加入到绑定了同一标签的安全组中。具体操作，请参见[使用标签获取](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)[实例并将其加入到对应标签的安全组](https://help.aliyun.com/zh/resource-management/tag/use-cases/query-ecs-instances-based-on-tags-and-add-ecs-instances-to-security-groups-with-same-tags)。
为多台ECS实例绑定相同标签，然后通过云监控的智能标签同步功能，将它们自动添加至同一个应用分组，实现自动化分组监控。具体操作，请参见[使用标签将](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-tags-to-enable-ecs-instances-to-be-automatically-added-to-cloudmonitor-application-groups-1)[ECS](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-tags-to-enable-ecs-instances-to-be-automatically-added-to-cloudmonitor-application-groups-1)[实例自动加入云监控应用分组](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-tags-to-enable-ecs-instances-to-be-automatically-added-to-cloudmonitor-application-groups-1)。
在指定标签的ECS实例上批量执行云助手命令或通过云助手上传文件。具体操作，请参见[使用标签控制云助手的命令执行](https://help.aliyun.com/zh/resource-management/tag/use-cases/use-tags-to-control-the-running-of-cloud-assistant-commands)。
## 相关文档
您还可以通过资源组根据资源的用途、权限和归属等维度对您拥有的云资源进行分组，从而实现企业内部多用户、多项目的资源分级管理。更多信息，请参见[什么是资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)或[资源组](resource-groups.md)。
调用接口[创建并绑定标签](../developer-reference/api-ecs-2014-05-26-tagresources.md)。
调用接口[查询资源已经绑定的标签列表](../developer-reference/api-ecs-2014-05-26-listtagresources.md)。
调用接口[为指定资源列表统一解绑标签](../developer-reference/api-ecs-2014-05-26-untagresources.md)。
调用接口[将一个](../developer-reference/api-ecs-2014-05-26-joinresourcegroup.md)[ECS](../developer-reference/api-ecs-2014-05-26-joinresourcegroup.md)[资源或者服务加入一个资源组](../developer-reference/api-ecs-2014-05-26-joinresourcegroup.md)。
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
