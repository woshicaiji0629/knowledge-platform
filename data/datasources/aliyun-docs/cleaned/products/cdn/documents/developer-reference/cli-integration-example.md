# 使用阿里云CLI管理CDN操作示例-CDN-阿里云-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/developer-reference/cli-integration-example

# CLI集成示例
阿里云CLI（Alibaba Cloud Command Line Interface）是基于OpenAPI Explorer构建的通用命令行工具，您可以通过阿里云CLI实现自动化管理和维护CDN。本文将为您介绍使用阿里云CLI调用CDN的操作步骤和示例。
## 前置概念
阅读本文前，若您还不了解阿里云CLI，请参见[什么是阿里云 CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
## 安装阿里云CLI
使用阿里云CLI前，您需要先安装阿里云CLI。阿里云CLI为用户提供了Windows、Linux和macOS三种操作系统下的安装服务，请根据您使用设备的操作系统选择对应的安装服务。
Windows：[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows)。
Linux：[安装/更新 CLI](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)。
macOS：[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos)。
您也可使用阿里云提供的云命令行[Cloud Shell](https://shell.aliyun.com/)调试阿里云CLI命令。关于云命令行的更多信息，请参阅[什么是云命令行](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)。
## 配置阿里云CLI
重要
阿里云账号（主账号）拥有所有产品API的管理和访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维。
使用阿里云CLI之前，您需要在阿里云CLI中配置身份凭证、地域ID等信息。阿里云CLI支持多种身份凭证，详情请参见[配置与管理身份凭证](https://help.aliyun.com/zh/cli/configure-credentials/#30ab0f9c3eovm)。本文操作以AK类型凭证为例，具体操作步骤如下：
您需要创建一个RAM用户并授予相应操作权限。具体操作，请参见[创建](../../../ram/documents/create-a-ram-user-1.md)[RAM](../../../ram/documents/create-a-ram-user-1.md)[用户](../../../ram/documents/create-a-ram-user-1.md)及[管理](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
重要
本示例需要您为RAM用户授予AliyunCDNReadOnlyAccess权限策略。您也可以按需选择AliyunCDNFullAccess权限（具有查询、修改CDN域名的完全控制权限）或进行自定义策略，更多信息请参见[CDN](../security-and-compliance/custom-policies-for-dcdn.md)[自定义权限策略参考](../security-and-compliance/custom-policies-for-dcdn.md)。
创建RAM用户并授权后，您需要创建RAM用户对应的AccessKey，并记录AccessKey ID和AccessKey Secret，以便后续配置身份凭证使用。具体操作，请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
您需要获取并记录可用的地域ID，以便后续配置身份凭证使用。阿里云CLI将使用您指定的地域发起API调用，可用地域请参见[请求结构](https://help.aliyun.com/zh/hbase/developer-reference/request-structure)。
说明
使用阿里云CLI过程中您可使用--region选项指定地域发起命令调用，该选项在使用时将忽略默认身份凭证配置及环境变量设置中的地域信息。详情请参见[命令行选项](https://help.aliyun.com/zh/cli/command-line-options)。
使用RAM用户的AccessKey配置AK类型凭证，配置文件命名为AkProfile。具体操作，请参见[服务接入点](api-cdn-2018-05-10-endpoint.md)。
## 生成CLI命令示例
登录[CDN API](https://api.aliyun.com/api/Cdn/2018-05-10/AddCdnDomain)[调试列表](https://api.aliyun.com/api/Cdn/2018-05-10/AddCdnDomain)。
在API调试界面左侧搜索框中可搜索您需要使用的API。在参数配置中根据API文档信息填写参数，单击参数配置右侧的CLI示例页签即可生成携带参数的命令示例。
单击按钮，可唤出云命令行[Cloud Shell](https://shell.aliyun.com/)并在其中快速完成命令调试。
单击按钮，将CLI示例复制到剪贴板中，可粘贴至本地Shell工具中运行。
复制CLI示例到本地Shell工具中进行调试时请注意参数格式。关于阿里云CLI命令参数使用格式的详细信息，请参见[理解命令行参数](https://help.aliyun.com/zh/cli/understanding-command-line-parameters)。
OpenAPI门户生成示例中会默认添加--region选项，复制命令到本地调用时阿里云CLI将忽略默认身份凭证配置及环境变量设置中的地域信息，优先使用指定的地域调用命令，您可根据需要对该选项进行删除或保留。
## 调用API
### 命令结构
阿里云CLI的通用命令行结构如下。更多详情，请参见[生成并调用命令](https://help.aliyun.com/zh/cli/sample-commands#1640a5c2c077i)。
aliyun <command> <subcommand> [options and parameters]
### 常用命令选项
在阿里云CLI中，您可根据需要使用命令行选项，用来修改命令的默认行为或为命令提供额外功能。常用命令行选项如下：
--profile<profileName>：使用--profile选项并指定有效配置名称profileName后，阿里云CLI将忽略默认身份凭证配置及环境变量设置，优先使用指定的配置进行命令调用。
--help：在需要获取帮助的命令层级处键入--help选项，即可获取该命令的帮助信息。更多详情，请参见[获取帮助信息](https://help.aliyun.com/zh/cli/use-the-help-command)。
更多详细信息，请参见[命令行选项](https://help.aliyun.com/zh/cli/command-line-options)。
### 调用示例
以下示例将为您展示如何使用阿里云CLI调用CDN中的DescribeUserDomains命令，查询用户名下所有的域名与状态。DescribeUserDomains命令的详细介绍，请参见[DescribeUserDomains](api-cdn-2018-05-10-describeuserdomains.md)。
执行命令。
aliyun cdn DescribeUserDomains --DomainName mxxxio.top
输出结果。
{ "Domains": { "PageData": [ { "CdnType": "web", "Cname": "mxxx.xxxp.w.kunlunq.com", "Coverage": "domestic", "Description": "", "DomainId": 201xxx553, "DomainName": "mjlxxxao.top", "DomainStatus": "online", "GlobalResourcePlan": "off", "GmtCreated": "2024-08-27T06:29:36Z", "GmtModified": "2024-08-27T06:34:04Z", "ResourceGroupId": "rg-acfmwpdflelaoai", "Sandbox": "", "Sources": { "Source": [ { "Content": "183.xxx.xxx.88.cn-hangzhou.sae.aliyuncs.com", "Port": 80, "Priority": "20", "Type": "domain", "Weight": "10" } ] } } ] }, "PageNumber": 1, "PageSize": 20, "RequestId": "E4EBD2BF-5EB0-4044-9B97-xxxxxx", "TotalCount": 1 } } ] }, "SslProtocol": "off" } ] }, "PageNumber": 1, "PageSize": 20, "RequestId": "34C9E61F-02A0-5EB5-BBCB-16B531ABB9E0", "TotalCount": 1 }
说明
如果调用CDNAPI后返回错误，您需要根据返回的错误码提示检查传入的请求参数及其取值是否正确。
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
