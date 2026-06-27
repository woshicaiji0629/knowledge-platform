# 图形化桌面客户端管理OSS资源-ossbrowser 2.0-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/developer-reference/ossbrowser-2-0-overview

# ossbrowser 2.0概述
ossbrowser 2.0是一款用于管理OSS的免费图形化桌面客户端。该客户端支持Windows、macOS和Linux操作系统，提供直观的图形用户界面，使您能够高效地执行各种操作，包括文件的上传、下载和删除。由于其本地部署特性，ossbrowser 2.0可在您的设备上直接运行，确保操作的流畅性。
说明
ossbrowser 2.0作为旧版ossbrowser的升级版本，目前暂未开源。有关各版本的更新详情，请参见[版本发布记录](version-release-record.md)。
## 使用限制
ossbrowser 2.0暂时尚未适配专有云、金融云以及政务云等其他非公共云环境。如果您是非公共云的用户请使用[图形化管理工具](graphical-management-tools-ossbrowser-1-0.md)[ossbrowser 1.0](graphical-management-tools-ossbrowser-1-0.md)。
在公网环境下上传或下载超过10 GB的大文件时，容易因网络状况不稳定而导致传输失败。如果您处于非内网环境，并且需要传输超过10 GB的大文件，建议您使用[命令行工具](ossutil-overview.md)[ossutil 2.0](ossutil-overview.md)。
## 操作视频
请观看以下视频快速了解如何使用ossbrowser 2.0。
## 功能优势
提供直观简洁的界面交互，方便对Bucket进行管理。
支持批量文件或目录的上传与下载操作（文件总大小10 GB以内），还可进行在线预览和编辑。
通过不同角色对不同资源的授权访问，进一步保障OSS资源的安全。
## 适用环境
重要
Windows系统仅支持Windows 7及以上版本包括Windows Server。
Linux x64发行版本众多，需要安装图形界面依赖文件，因此不推荐使用。建议您在Windows或macOS上使用ossbrowser 2.0。
| 操作系统 | 系统架构 | 安装包类型 | 安装教程 |
| --- | --- | --- | --- |
| Windows | x86-64 | nsis | [Windows](installing-the-ossbrowser-2-0.md) [系统](installing-the-ossbrowser-2-0.md) |
| macOS | x86-64 | dmg | [macOS](installing-the-ossbrowser-2-0.md) [系统](installing-the-ossbrowser-2-0.md) |
| arm64 | dmg |  |  |
| Linux | x86-64 | AppImage | [Linux](installing-the-ossbrowser-2-0.md) [系统](installing-the-ossbrowser-2-0.md) |
## 计费说明
ossbrowser软件本身免费，但通过ossbrowser执行相关操作时，其计费方式与在控制台操作相同，都会遵循OSS计费逻辑收取相应费用。例如：
本地环境中上传下载文件：在本地环境中使用ossbrowser上传和下载文件时，涉及PUT类[请求费用](../api-operation-calling-fees.md)，GET类的[请求费用](../api-operation-calling-fees.md)和下行[流量费用](../traffic-fees.md)。上传文件到OSS后需要根据文件存储类型收取[存储费用](../storage-fees.md)。
内网环境中上传下载文件：在阿里云内网环境中，使用ossbrowser上传和下载文件，只涉及PUT和GET类[请求费用](../api-operation-calling-fees.md)以及文件[存储费用](../storage-fees.md)。无流量费用。例如可以通过创建ECS实例，并在其上安装ossbrowser后实现在阿里云内网中上传和下载文件。
此外，如果您的业务需要在中国内地与海外地域之间传输数据，使用内外网可能无法满足预期的传输效率。建议开启传输加速服务来提升数据上传下载速度。使用传输加速服务会产生[传输加速费用](../transfer-acceleration-fees.md)。有关OSS更多增值相关费用，请参见[增值计费项](../value-added-billing-item.md)。
## 后续步骤
如需在Windows、macOS及Linux系统中安装ossbrowser 2.0，请参见[安装](installing-the-ossbrowser-2-0.md)[ossbrowser 2.0](installing-the-ossbrowser-2-0.md)。若您已完成ossbrowser 2.0的安装，但在登录环节遇到问题，可参阅[登录](login-to-ossbrowser-2-0.md)[ossbrowser 2.0](login-to-ossbrowser-2-0.md)。
## 相关文档
[登录](login-to-ossbrowser-2-0.md)[ossbrowser 2.0](login-to-ossbrowser-2-0.md)
[常用操作](commonly-used-function-of-ossbrowser2-0.md)
[文件授权](document-authorization-using-ossbrowser2-0.md)
[新版本下载](download-the-latest-minor-version-of-ossbrowser2-0.md)
[常见问题](common-problems.md)
[版本发布记录](version-release-record.md)
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
