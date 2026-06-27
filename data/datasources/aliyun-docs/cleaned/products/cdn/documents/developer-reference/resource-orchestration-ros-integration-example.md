# 通过编写资源编排ROS添加加速域名-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/resource-orchestration-ros-integration-example

# 资源编排ROS集成示例
使用资源编排服务ROS调用CDN。本文为您介绍如何编写一个资源编排的模板，自动化添加一个CDN的加速域名。
### 支持资源列表
资源编排服务ROS（Resource Orchestration Service）是阿里云提供的一项简化云计算资源管理的服务。开发者和管理员可以编写模板，在模板中定义所需的阿里云资源（例如：ECS 实例、RDS 数据库实例）、资源间的依赖关系等。ROS 的编排引擎将根据模板自动完成所有资源的创建和配置，实现自动化部署及运维。更多详情，请参见[什么是资源编排服务](https://help.aliyun.com/zh/ros/product-overview/what-is-ros)。
支持使用资源编排服务ROS调用CDN。编排的部分资源包括普通资源和数据资源。
普通资源：
[ALIYUN::CDN::Domain](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domain)：用于添加加速域名。
[ALIYUN::CDN::DomainConfig](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domainconfig)：用于批量配置域名。
数据资源：
[DATASOURCE::CDN::Domains](https://help.aliyun.com/zh/ros/developer-reference/datasource-cdn-domains)：用于查询已创建加速域名的基础信息
## 权限说明
在本案例中，需要添加一个加速域名。默认情况下资源编排直接使用当前登录控制台的用户凭证，要求当前用户必须具备以下权限：
AliyunCDNFullAccess: 管理CDN资源的权限。
阿里云账号拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维。请根据业务的实际情况按需分配权限后进行接口调用。RAM用户需具备操作CDN资源的权限。具体操作，请参见[CDN](../security-and-compliance/cdn.md)[系统权限策略参考](../security-and-compliance/cdn.md)。
### 操作步骤
## 操作步骤
登录[资源编排](https://rosnext.console.aliyun.com/cn-shanghai/stacks)[ROS](https://rosnext.console.aliyun.com/cn-shanghai/stacks)[控制台](https://rosnext.console.aliyun.com/cn-shanghai/stacks)，单击顶部导航栏地域下拉框，选择您需要的地域。
单击左侧菜单栏中的资源栈，选择创建资源栈>使用ROS。
指定模板：选中选择已有模板。
模板录入方式：选中输入模板。
模板内容选择ROS，并输入代码。
添加加速域名的语法、说明及示例，请参见[ALIYUN::CDN::Domain](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domain)。
YAML格式
ROSTemplateFormatVersion: '2015-09-01' Parameters: CdnType: AllowedValues: - video - download - web - liveStream Description: 'The business type. Valid values: web, download, video, livestream, and httpsdelivery. web: acceleration of images and small files download. download: acceleration of large file downloads. video: live streaming acceleration. httpsdelivery: SSL acceleration for HTTPS.' Type: String CheckUrl: Description: The validation of the origin. Type: String DomainName: Description: The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com. Type: String ResourceGroupId: Description: The ID of the resource group. If this is left blank, the system automatically fills in the ID of the default resource group. Type: String Scope: Description: 'Valid values: domestic, overseas, and global. Default value: domestic. The setting is supported for users outside mainland China, users in mainland China of level 3 or above.' Type: String Sources: Description: The list of origin URLs. Type: String Tags: Description: Tags to attach to instance. Max support 20 tags to add during create instance. Each tag with two properties Key and Value, and Key is required. MaxLength: 20 Type: Json TopLevelDomain: Description: The top-level domain, which can only be configured by users on the whitelist. Type: String Resources: Domain: Properties: CdnType: Ref: CdnType CheckUrl: Ref: CheckUrl DomainName: Ref: DomainName ResourceGroupId: Ref: ResourceGroupId Scope: Ref: Scope Sources: Ref: Sources Tags: Ref: Tags TopLevelDomain: Ref: TopLevelDomain Type: ALIYUN::CDN::Domain Outputs: Cname: Description: The CNAME generated for the CDN domain.You must add a CNAME record with your DNS provider to map the CDN domain name to the CNAME. Value: Fn::GetAtt: - Domain - Cname DomainName: Description: The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com. Value: Fn::GetAtt: - Domain - DomainName
JSON格式
{ "ROSTemplateFormatVersion": "2015-09-01", "Parameters": { "CheckUrl": { "Type": "String", "Description": "The validation of the origin." }, "ResourceGroupId": { "Type": "String", "Description": "The ID of the resource group. If this is left blank, the system automatically fills in the ID of the default resource group." }, "Scope": { "Type": "String", "Description": "Valid values: domestic, overseas, and global. Default value: domestic. The setting is supported for users outside mainland China, users in mainland China of level 3 or above." }, "DomainName": { "Type": "String", "Description": "The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com." }, "CdnType": { "Type": "String", "Description": "The business type. Valid values: web, download, video, livestream, and httpsdelivery. web: acceleration of images and small files download. download: acceleration of large file downloads. video: live streaming acceleration. httpsdelivery: SSL acceleration for HTTPS.", "AllowedValues": [ "video", "download", "web", "liveStream" ] }, "TopLevelDomain": { "Type": "String", "Description": "The top-level domain, which can only be configured by users on the whitelist." }, "Sources": { "Type": "String", "Description": "The list of origin URLs." }, "Tags": { "Type": "Json", "Description": "Tags to attach to instance. Max support 20 tags to add during create instance. Each tag with two properties Key and Value, and Key is required.", "MaxLength": 20 } }, "Resources": { "Domain": { "Type": "ALIYUN::CDN::Domain", "Properties": { "CheckUrl": { "Ref": "CheckUrl" }, "ResourceGroupId": { "Ref": "ResourceGroupId" }, "Scope": { "Ref": "Scope" }, "DomainName": { "Ref": "DomainName" }, "CdnType": { "Ref": "CdnType" }, "TopLevelDomain": { "Ref": "TopLevelDomain" }, "Sources": { "Ref": "Sources" }, "Tags": { "Ref": "Tags" } } } }, "Outputs": { "DomainName": { "Description": "The CDN domain name. Wildcard domain names that start with periods (.) are supported. For example, .example.com.", "Value": { "Fn::GetAtt": [ "Domain", "DomainName" ] } }, "Cname": { "Description": "The CNAME generated for the CDN domain.You must add a CNAME record with your DNS provider to map the CDN domain name to the CNAME.", "Value": { "Fn::GetAtt": [ "Domain", "Cname" ] } } } }
单击下一步，执行操作栈。
在配置参数页面配置参数，单击创建。
输出结果。
资源栈的状态显示为创建成功，状态描述为Stack CREATE completed successfully，表示资源栈已成功创建。
创建完成后，您可以通过OpenAPI、SDK或者在CDN控制台，可以查看到。
在CDN控制台的域名管理页面中，可以看到新添加的加速域名，其状态显示为正常运行，CNAME状态为已配置。
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
