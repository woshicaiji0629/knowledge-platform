# 自定义权限策略的配置方法与场景示例-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/security-and-compliance/custom-policies-for-dcdn

# CDN自定义权限策略参考
如果系统权限策略不能满足您的要求，您可以创建自定义权限策略实现最小授权。使用自定义权限策略有助于实现权限的精细化管控，是提升资源访问安全的有效手段。本文介绍CDN使用自定义权限策略的场景和策略示例。
## 什么是自定义权限策略
在基于RAM的访问控制体系中，自定义权限策略是指在系统权限策略之外，您可以自主创建、更新和删除的权限策略。自定义权限策略的版本更新需由您来维护。
创建自定义权限策略后，需为RAM用户、用户组或RAM角色绑定权限策略，这些RAM身份才能获得权限策略中指定的访问权限。
已创建的权限策略支持删除，但删除前需确保该策略未被引用。如果该权限策略已被引用，您需要在该权限策略的引用记录中移除授权。
自定义权限策略支持版本控制，您可以按照RAM规定的版本管理机制来管理您创建的自定义权限策略版本。
## 操作文档
[创建自定义权限策略](../../../ram/documents/create-a-custom-policy.md)
[修改自定义权限策略内容和备注](../../../ram/documents/modify-the-document-and-description-of-a-custom-policy.md)
[删除自定义权限策略](../../../ram/documents/delete-a-custom-policy.md)
[管理权限策略引用记录](../../../ram/documents/manage-policy-references.md)
[管理自定义权限策略版本](../../../ram/documents/manage-custom-policy-versions.md)
## 常见自定义权限策略场景及示例
示例1：刷新预热权限
该权限策略通过授予RAM用户刷新和预热接口的权限，使被授权的RAM用户拥有刷新预热功能的权限，可进行刷新预热配置。
{ "Version": "1", "Statement": [ { "Action": [ "cdn:PushObjectCache", "cdn:RefreshObjectCaches", "cdn:DescribeRefreshTasks", "cdn:DescribeRefreshQuota" ], "Resource": "acs:cdn:*:*:*", "Effect": "Allow" } ] }
示例2：限制RAM用户修改计费模式
{ "Statement": [ { "Action": "cdn:*", "Resource": "*", "Effect": "Allow" }, { "Action": [ "cdn:OpenCdnService", "cdn:ModifyCdnService" ], "Resource": "*", "Effect": "Deny" }, { "Action": "ram:CreateServiceLinkedRole", "Resource": "*", "Effect": "Allow", "Condition": { "StringEquals": { "ram:ServiceName": [ "cdn-waf.cdn.aliyuncs.com", "cdn-ddos.cdn.aliyuncs.com" ] } } } ], "Version": "1" }
## 授权信息参考
使用自定义权限策略，您需要了解业务的权限管控需求，并了解CDN的授权信息。详细内容请参见[授权信息](../developer-reference/api-cdn-2018-05-10-ram.md)。
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
