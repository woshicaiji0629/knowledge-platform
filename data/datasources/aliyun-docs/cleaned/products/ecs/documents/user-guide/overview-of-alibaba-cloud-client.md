# 阿里云客户端的优势和功能配置指引-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-of-alibaba-cloud-client

# 阿里云客户端概述
阿里云客户端（Alibaba Cloud Client）是一款桌面应用程序，通过集成的安全连接和凭证管理功能，解决在管理云上资源时，网络受限、操作繁琐和凭证安全难保障的痛点。
## 工具优势
统一资源管理：支持集中管理云服务器ECS、弹性容器实例ECI、轻量应用服务器SWAS、托管实例、容器服务ACK、对象存储OSS。
安全免密连接：通过私有网络连接云上实例，全程免输密码，既保障了连接安全又提升了运维效率。
安全端口转发：将云上实例的端口安全映射至本地进行访问，无需暴露公网或配置VPN，便于本地开发调试。
多账号切换：支持同时登录并管理多个云账号，可在不同身份间即时切换，无需重复登入登出。
## 核心功能
主要提供以下云产品的查看、查找、远程连接功能：
| 云产品 | 功能描述 |
| --- | --- |
| 云服务器 ECS | 分地域查看 ECS 实例、全局及本地域查找能力 支持通过以下方式连接实例： 通过 SSH 连接有公网 IP 的 Linux 实例 通过 RDP 连接有公网 IP 的 Windows 实例 通过会话管理连接实例（免公网、免密码） 通过端口转发连接（免公网连接到 SSH 或 RDP） 支持将实例登录信息（实例 ID、登录账号，SSH 密钥文件名及密码密文）保存至本地，实现后续免输入快速登录。 支持管理实例内部信息 管理实例系统内的用户 管理实例系统内的密钥 管理实例系统内的文件 |
| 弹性容器实例 ECI | 分地域查看弹性容器实例 查看容器组事件 远程连接容器组内的容器 |
| 轻量应用服务器 | 分地域查看轻量应用服务器实例 查看轻量服务器实例监控信息和实例属性 SSH 远程连接 Linux 实例 RDP 远程连接 Windows 实例 |
| 阿里云托管实例 | 分地域查看托管实例 查看托管实例属性 支持 SSH 连接与会话管理连接 支持通过端口转发连接 Windows 远程桌面 |
| 容器服务 ACK | 查看容器(ACK)集群 查看容器(ACK)集群的节点 查看容器(ACK)集群的容器组与容器 查看容器(ACK)集群的配置项与保密项 查看容器(ACK)集群的日志 远程连接容器组内的容器与节点 |
| 对象存储 OSS | 查看对象存储的 Bucket 列表 查看对象存储的文件列表 管理对象存在的文件 上传与下载目录 上传与下载文件 重命名与删除文件 查看图像文件 查看与编辑文本文件 修改文件访问权限 在云服务器(ECS)的文件管理器中使用对象存储 将 ECS 实例内文件上传到 OSS 下载 OSS 中的文件到 ECS 实例 |
| 混合云服务器 | 查看在其他公有云或私有云上的服务器列表 云服务器状态管理：启动/停止/重启实例 云服务器远程连接： 通过 SSH 与公网 IP 连接到 Linux 实例 通过 RDP 与公网 IP 连接到 Windows 实例 通过会话管理，免公网连接到云服务器 |
## 下载与安装
### 下载及安装指引
根据业务需求，下载并安装指定版本的阿里云客户端：
[Windows 版本](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/client/releases/win32/x64/alibaba-cloud-client-latest.exe)
[Mac x64 版本](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/client/releases/darwin/x64/alibaba-cloud-client-latest.dmg)
[Mac arm64 版本](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/client/releases/darwin/arm64/alibaba-cloud-client-latest.dmg)
### 配置指引
下载后需[在阿里云客户端配置登录身份凭证](add-one-or-more-accounts-to-alibaba-cloud-client.md)，用于管理该账号下的资源。
在阿里云客户端上查看和管理资源。
[通过阿里云客户端管理](use-alibaba-cloud-client-to-manage-ecs-instances.md)[ECS](use-alibaba-cloud-client-to-manage-ecs-instances.md)[实例](use-alibaba-cloud-client-to-manage-ecs-instances.md)
[通过阿里云客户端管理](use-alibaba-cloud-client-to-manage-elastic-container-instances.md)[ECI](use-alibaba-cloud-client-to-manage-elastic-container-instances.md)[容器实例](use-alibaba-cloud-client-to-manage-elastic-container-instances.md)
[通过阿里云客户端管理轻量应用服务器](use-alibaba-cloud-client-to-manage-simple-application-servers.md)
[通过阿里云客户端管理托管实例](use-alibaba-cloud-client-to-manage-managed-instances.md)
（可选）根据实际需要灵活[配置阿里云客户端](use-alibaba-cloud-client.md)（包括本地终端和SSH的系统设置）。
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
