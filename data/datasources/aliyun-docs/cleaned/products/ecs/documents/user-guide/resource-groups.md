# 使用资源组进行ECS资源分组，实现多用户或多项目的资源分级管理-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/resource-groups

# 使用资源组管理ECS资源
资源组可以根据资源的用途、权限和归属等维度对您拥有的云资源进行分组，从而实现企业内部多用户、多项目的资源分级管理。每个云资源只能属于一个资源组，加入资源组不会改变云资源之间的关联关系。
更多资源组信息，请参见[什么是资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)。
## 支持的ECS资源
支持资源组的ECS资源包括实例、云盘、镜像、弹性网卡、安全组、快照、实例启动模板和密钥对。
## 使用说明
使用资源组管理ECS资源之前，您需要了解如下说明：
一个资源组可以包含不同地域的ECS资源。
例如：资源组A中可以包含华北2（北京）地域的实例和华东1（杭州）地域的实例。
同一个账号内不同资源组中，相同地域的资源可以进行关联。
例如：资源组A中华北2（北京）地域的实例可以加入到资源组B中华北2（北京）地域的VPC内。
资源组会继承RAM用户的全局权限。即如果您授权RAM用户管理所有的阿里云资源，则阿里云账号下所有的资源组都会在该RAM用户中显示出来。
使用资源组管理ECS资源的具体操作，请参见[使用资源组限制](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[RAM](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[用户管理指定的](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[ECS](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)[实例](../../../ram/documents/use-cases/use-a-resource-group-to-manage-an-ecs-instance.md)。
## 相关文档
您可以根据实际需要管理您的资源组，具体操作，请参见[管理资源组](https://help.aliyun.com/zh/resource-management/resource-group/user-guide/manage-resource-groups/)。
您也可以使用标签对ECS资源进行分类，实现资源的精细化管理。更多信息，请参见[标签](label-overview.md)。
您可以调用[JoinResourceGroup](../developer-reference/api-ecs-2014-05-26-joinresourcegroup.md)接口将一个ECS资源或者服务加入一个资源组。
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
