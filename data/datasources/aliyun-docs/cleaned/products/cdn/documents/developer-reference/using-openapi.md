# CDN集成概览-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/using-openapi

# 集成概览
本文为您介绍使用阿里云CDNOpenAPI的基本信息。
## OpenAPI介绍
为了能够让开发者快速高效地学习和使用云产品OpenAPI，阿里云为用户提供OpenAPI网站。它是一款集OpenAPI智能搜索、文档、在线调试、SDK获取、CodeSample、调用出错诊断、调用统计为一体的产品。您可以在OpenAPI门户中调用阿里云各云产品开放的OpenAPI，查看OpenAPI请求和返回结果。此外，OpenAPI门户会自动生成相应的SDK调用示例，帮助您快速使用阿里云产品。更多信息，请参见[什么是](https://help.aliyun.com/zh/openapi/what-is-openapi)[OpenAPI](https://help.aliyun.com/zh/openapi/what-is-openapi)。
### 版本说明
| 版本号 | 说明 |
| --- | --- |
| [2018-05-10](https://next.api.aliyun.com/document/Cdn/2018-05-10/overview) | 推荐使用。 |
### 在线调试
CDN在OpenAPI门户提供API调试等功能。在调用前，您需要了解CDN提供的版本、接入点说明、集成方式等信息。
以AddCdnDomain（添加域名）接口为例，在 OpenAPI 门户左侧导航栏选择域名管理>添加/删除域名>添加域名 AddCdnDomain，在中间参数配置区域填写必填参数CdnType（加速域名的业务类型）、DomainName（需要接入CDN的加速域名）、Sources（回源地址列表），以及可选参数ResourceGroupId、CheckUrl、Scope、TopLevelDomain等，然后单击发起调用。调用前需注意：需先开通 CDN 服务；加速域名必须完成备案；每次只能添加一个域名；每个用户最多添加 50 个域名；单个用户调用频率限制为 30 次/秒。
### 调试入口
调试API入口为：[CDN API](https://api.aliyun.com/api/Cdn/2018-05-10/AddCdnDomain)[调试入口](https://api.aliyun.com/api/Cdn/2018-05-10/AddCdnDomain)。
### 接入点说明
根据相关资源所在地域，选择对应的服务接入点地址，以获得最低延迟。例如华东2（上海）的CDN公网接入地址为cn-shanghai.aliyuncs.com。
更多信息，请参见[CDN](api-cdn-2018-05-10-endpoint.md)[服务接入点](api-cdn-2018-05-10-endpoint.md)。
### 用户身份
您阿里云账号登录OpenAPI网站后，默认使用您的阿里云账号进行在线OpenAPI调试。由于阿里云账号拥有所有API的访问权限，存在较高的风险。强烈建议您创建并使用RAM用户进行API访问或日常运维。请根据业务的实际情况按需分配权限后进行接口调用。RAM用户需具备操作CDN资源的权限。具体操作，请参见[使用](../security-and-compliance/identity-management-and-access-control-1.md)[RAM](../security-and-compliance/identity-management-and-access-control-1.md)[进行访问控制](../security-and-compliance/identity-management-and-access-control-1.md)。
| 用户身份 | 支持情况 |
| --- | --- |
| [阿里云账号](https://help.aliyun.com/zh/openapi/identity#3948d68066ppy) | 支持 |
| [RAM 用户](https://help.aliyun.com/zh/openapi/identity#265242420egiy) （推荐） | 支持 |
| [RAM](https://help.aliyun.com/zh/openapi/identity#5b7a31e066wma) [角色](https://help.aliyun.com/zh/openapi/identity#5b7a31e066wma) （推荐） | 支持 |
### 更多信息
[身份、凭据与授权](https://help.aliyun.com/zh/openapi/identity-credentials-and-authorization)
[流量控制与配额管理](https://help.aliyun.com/zh/openapi/throttling-and-quota-management)
## 集成方式
CDN产品提供SDK、CLI等多种集成方式，您可以根据业务的实际需要进行选择。
| 调用方式 | 支持情况 |
| --- | --- |
| [阿里云](using-openapi.md) [SDK](using-openapi.md) （推荐） | 支持 |
| [阿里云](using-openapi.md) [CLI](using-openapi.md) | 支持 |
| [Terraform](using-openapi.md) | 支持 |
| [资源编排](using-openapi.md) [ROS](using-openapi.md) | 支持 |
| [自定义封装](using-openapi.md) [API](using-openapi.md) [调用](using-openapi.md) | 支持 |
### 阿里云SDK
阿里云为开发者提供了多种编程语言（Java、C#、Go、Py thon、Node.js/TypeScript、PHP、C++ 等）的SDK。开发者只需要集成SDK，通过SDK暴露的方法直接调用OpenAPI 。SDK统一封装了签名逻辑、超时机制、重试机制，并根据文档返回结构化Response对象，易于开发。更多关于阿里云SDK的介绍，请参见[阿里云](https://help.aliyun.com/zh/sdk/product-overview/alibaba-cloud-sdk)[SDK](https://help.aliyun.com/zh/sdk/product-overview/alibaba-cloud-sdk)。
支持在OpenAPI通过阿里云SDK调用CDN。支持语言及依赖安装方法请参见[CDN_SDK](https://next.api.aliyun.com/api-tools/sdk/Cdn?version=2018-05-10&language=java-async-tea)[中心](https://next.api.aliyun.com/api-tools/sdk/Cdn?version=2018-05-10&language=java-async-tea)。
### 阿里云CLI
支持使用阿里云CLI调用CDN。更多信息，请参见[使用阿里云](https://help.aliyun.com/zh/cli/sample-commands)[CLI](https://help.aliyun.com/zh/cli/sample-commands)。
阿里云命令行工具可以帮您在使用命令行终端时，使用aliyun命令与阿里云服务进行交互，管理云服务资源。有关阿里云CLI的更多详细信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
### Terraform
Terraform 是一种开源工具，用于安全高效地预览，配置和管理云基础架构和资源。它与阿里云的资源编排服务的运行机制类似，通过将模板转化为内部数据后完成 OpenAPI 调用。更多详情，请参见[了解阿里云](https://help.aliyun.com/zh/terraform/what-is-terraform)[Terraform](https://help.aliyun.com/zh/terraform/what-is-terraform)。
快速使用Terraform编排CDN，请参见[Terraform](terraform-integration-example.md)[集成示例](terraform-integration-example.md)。
支持使用Terraform管理CDN的资源，支持常规资源和数据资源清单的部分如下。
| 资源类型 | 资源 | 说明 |
| --- | --- | --- |
| Resources | [alicloud_cdn_domain_config](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cdn_domain_config) | 提供 CDN 域配置资源。 |
| [alicloud_cdn_domain_new](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cdn_domain_new) | 提供 CDN 与资源及域名。 |  |
| [alicloud_cdn_fc_trigger](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cdn_fc_trigger) | 提供了 CDN FC 的触发器资源。 |  |
| [alicloud_cdn_real_time_log_delivery](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/cdn_real_time_log_delivery) | 提供了 CDN 实时日志传递资源。 |  |
| Date Sources | [alicloud_cdn_blocked_regions](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cdn_blocked_regions) | 提供 CDN 阻塞区域。 |
| [alicloud_cdn_ip_info](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cdn_ip_info) | 提供了验证 IP 是否为 CDN 节点的功能。 |  |
| [alicloud_cdn_real_time_log_deliveries](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cdn_real_time_log_deliveries) | 提供当前阿里云用户的 CDN 实时日志交付功能。 |  |
| [alicloud_cdn_service](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/data-sources/cdn_service) | 提供自动启用 CDN 服务。 |  |
### 资源编排ROS
资源编排服务ROS（Resource Orchestration Service）是阿里云提供的一项简化云计算资源管理的服务。开发者和管理员可以编写模板，在模板中定义所需的阿里云资源（例如：ECS 实例、RDS 数据库实例）、资源间的依赖关系等。ROS 的编排引擎将根据模板自动完成所有资源的创建和配置，实现自动化部署及运维。更多详情，请参见[什么是资源编排服务](https://help.aliyun.com/zh/ros/product-overview/what-is-ros)。
快速使用资源编排ROS编排CDN，请参见[资源编排](resource-orchestration-ros-integration-example.md)[ROS](resource-orchestration-ros-integration-example.md)[集成示例](resource-orchestration-ros-integration-example.md)。
支持使用资源编排服务ROS调用CDN。编排的部分资源包括普通资源和数据资源。
普通资源：
[ALIYUN::CDN::Domain](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domain)：用于添加加速域名。
[ALIYUN::CDN::DomainConfig](https://help.aliyun.com/zh/ros/developer-reference/aliyun-cdn-domainconfig)：用于批量配置域名。
数据资源：
[DATASOURCE::CDN::Domains](https://help.aliyun.com/zh/ros/developer-reference/datasource-cdn-domains)：用于查询已创建加速域名的基础信息。
### 自定义封装API调用
原生HTTP调用需要您自己实现签名算法，并构建自定义请求，发起HTTP调用。有关签名机制的更多详细信息，请参见文档[API](api-cdn-2018-05-10-overview.md)[概览](api-cdn-2018-05-10-overview.md)和[V3](https://help.aliyun.com/zh/sdk/product-overview/v3-request-structure-and-signature)[版本请求体&签名机制](https://help.aliyun.com/zh/sdk/product-overview/v3-request-structure-and-signature)。
## 注意事项
如果调用API后返回错误，您需要根据返回的错误码提示检查传入的请求参数及其取值是否正确，更多信息请参见[错误码中心](https://api.aliyun.com/document/Cdn/2018-05-10/errorCode)。
您也可以记录下调用返回的RequestID或SDK报错信息，通过[阿里云](https://next.api.aliyun.com/troubleshoot)[OpenAPI](https://next.api.aliyun.com/troubleshoot)[诊断平台](https://next.api.aliyun.com/troubleshoot)进行自助诊断。
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
