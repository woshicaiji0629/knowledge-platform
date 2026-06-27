# 发布和使用社区镜像-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-12

# 社区镜像
社区镜像是一种完全公开的镜像。您可以将制作好的自定义镜像发布为社区镜像供他人使用，也可以获取并使用他人发布的社区镜像。
## 概述
社区镜像由以下三方共同参与：
其中：
阿里云：仅提供平台支撑，社区镜像由镜像提供者发布并负责。
镜像提供者：制作自定义镜像并发布为社区镜像，供他人使用。
镜像使用者：通过社区镜像可以获取更丰富的镜像种类。
## 发布社区镜像
您可以将可用状态的自定义镜像发布为社区镜像。
重要
仅通过认证的企业客户可以通过[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请使用社区镜像发布功能。
### 注意事项
在您发布社区镜像前，请先了解以下注意事项：
加密镜像不允许发布为社区镜像。
社区镜像完全公开，在镜像所属地域下，所有的阿里云账号均可使用。
社区镜像不支持共享、导出与复制。
### 发布规范
重要
社区镜像提供方在发布社区镜像时需要设置镜像名称和镜像描述，且镜像名称和镜像描述需遵循以下规范，方便镜像使用者选购社区镜像。
发布规范说明如下：
镜像名称
建议包含操作系统类型、内核版本、架构、发布时间（发布为社区镜像的时间）、镜像版本（可选），例如ubuntu20.04_kernel4.18_x86_64_20230101_v1.0。
镜像描述
建议提供镜像的详细描述，以便镜像使用者更清晰地选择并使用所发布的社区镜像。描述信息包括但不限于以下内容：
| 包含的内容 | 说明 | 描述示例 |
| --- | --- | --- |
| 迭代版本号 | 每次迭代都应标明对应的版本号，以便区分不同版本之间的变化。 | Ubuntu 20.04 LTS |
| 功能变更 | 详细描述每个迭代版本中添加、修改或删除的功能。说明新功能的作用、用途和效果，以及旧功能的改进或调整情况。 | 新增了图形界面工具包，使用户能够更方便地进行图形化操作。 更新了软件包管理器，增强了软件的安装和更新功能。 优化了网络设置，提升了网络连接的稳定性和速度。 增加了自动化部署脚本，简化了镜像的部署流程。 |
| 缺陷修复 | 列出已修复的错误或缺陷，并描述修复后的效果和影响范围。 | 修复了在特定硬件环境下出现的内核崩溃问题。 解决了某些情况下系统重启后无法正常加载驱动程序的缺陷。 |
| 性能优化 | 指明针对性能进行的优化措施和结果，例如加速启动时间、减少资源占用等。 | 优化了系统启动时间，缩短了开机等待时间。 降低了系统资源占用率，提高了整体性能表现。 |
| 安全增强 | 说明针对潜在安全风险或漏洞所做的补丁和改进措施。 | 升级了内核版本，修复了已知的安全漏洞。 强化了身份验证和权限管理，提高了系统的安全性。 |
| 依赖项更新 | 如果迭代版本中有更新依赖项或库的情况，需要说明更新的内容和原因。 | 更新了软件源列表，包含最新的软件包和库版本。 |
| 兼容性说明 | 如果迭代版本中存在与之前版本不兼容的情况，需要明确说明并提供相应的解决方案。 | 请注意，该版本不再支持 32 位系统，仅支持 64 位系统。 |
安全确认
检查并确认镜像名称与镜像描述无敏感词、镜像不包含木马病毒、漏洞、弱口令等违规信息。
镜像检测
发布社区镜像会触发[镜像检测](detect-custom-images-and-repair.md)，然后通过[系统标签](label-overview.md)将检测到的系统版本、系统架构、内核版本等信息透出，从而完善镜像信息。
### 操作步骤
进入镜像功能页面。
登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)。
在左侧导航栏，选择实例与镜像>镜像。
在顶部菜单栏左上角处，选择地域。
在自定义镜像页签，找到待发布为社区镜像的可用自定义镜像，然后在操作列选择>发布为社区镜像。
在发布为社区镜像对话框，完成社区镜像的发布。
发布成功后，您可以在镜像页面，单击社区镜像页签，查看已发布的社区镜像信息。
## 使用社区镜像创建ECS实例
您可以使用社区镜像快速部署与业务需求匹配的操作系统、应用程序和数据的ECS实例。具体操作，请参见[使用社区镜像创建实例](create-an-instance-using-community-image.md)。
## 下架社区镜像
当您需要更新已发布的社区镜像版本或者不再维护社区镜像时，可以将当前已发布的社区镜像下架。
说明
已发布的社区镜像一旦下架，将不再对其他所有的阿里云账号公开。如果镜像已共享至其他阿里云账号，共享关系会继续保持。
社区镜像下架后，已使用社区镜像创建的ECS实例将无法重新初始化云盘。
进入镜像功能页面。
登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)。
在左侧导航栏，选择实例与镜像>镜像。
在顶部菜单栏左上角处，选择地域。
在自定义镜像页签，找到已发布为社区镜像的自定义镜像，然后在操作列选择>下架社区镜像。
在下架社区镜像对话框，确认镜像信息，然后单击确定。
系统提示镜像***已从社区镜像下架表示镜像下架成功。
## 相关文档
社区镜像本质上是自定义镜像公开共享的镜像。如果该自定义镜像的最终来源为付费镜像，则使用社区镜像创建ECS实例时会收取镜像License费用。更多信息，请参见[镜像计费](../images.md)。
使用社区镜像创建ECS实例后，如果当前使用的社区镜像不能满足业务需求，您可以为ECS实例更换新的操作系统。具体操作，请参见[更换操作系统（更换系统盘）](replace-the-operating-system-of-an-instance.md)。
有关社区镜像的镜像族系说明，请参见[镜像族系概述](overview-37.md)。
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
