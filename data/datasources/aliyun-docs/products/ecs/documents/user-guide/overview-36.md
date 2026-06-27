# 自定义镜像概述-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-36

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

# 自定义镜像概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

自定义镜像是您使用实例或快照创建的镜像，或是您从本地导入的镜像。通过对已经部署好应用的实例创建自定义镜像，您可以以此来快速创建更多包含相同配置的实例，免除重复配置。

## 自定义镜像生命周期

当您成功创建或成功导入自定义镜像后，镜像的状态为可用。此时，您可以使用该镜像创建实例，也可以将其共享给其他阿里云账号使用，或复制该镜像到其他地域使用，或导出该镜像到OSS存储空间（OSS Bucket）。不再需要该镜像时，您可以将其删除。

说明只有自定义镜像的创建者可以对镜像进行共享、复制和删除等操作。

自定义镜像的生命周期如下图所示。

## 相关操作

自定义镜像支持的相关功能操作如下表所示。

- 

- 

- 

- 

| 操作 | 说明 | 相关文档 |
| --- | --- | --- |
| 创建镜像 | 您可以通过已有实例或快照创建自定义镜像，以便快速复制系统环境，免除重复配置。您还可以使用镜像定义工具 Packer 创建自定义镜像。 | [使用实例创建自定义镜像](products/ecs/documents/user-guide/create-a-custom-image-from-an-instance.md) [使用快照创建自定义镜像](products/ecs/documents/user-guide/create-a-custom-image-from-a-snapshot-1.md) [使用](products/ecs/documents/user-guide/use-packer-to-create-a-custom-image.md) [Packer](products/ecs/documents/user-guide/use-packer-to-create-a-custom-image.md) [创建自定义镜像](products/ecs/documents/user-guide/use-packer-to-create-a-custom-image.md) [使用](products/ecs/documents/user-guide/use-packer-to-create-and-import-an-on-premises-image.md) [Packer](products/ecs/documents/user-guide/use-packer-to-create-and-import-an-on-premises-image.md) [创建并导入本地镜像](products/ecs/documents/user-guide/use-packer-to-create-and-import-an-on-premises-image.md) |
| 导入镜像 | 您可以从本地导入自定义镜像。 | [导入镜像流程](products/ecs/documents/user-guide/import-an-image.md) |
| 更新镜像 | 运维编排服务 OOS 为更新自定义镜像的场景提供了公共模版。您只需选择一个源镜像，输入更新镜像所需的云助手脚本等必要参数，就可以创建随机或定时的运维任务，一键更新自定义镜像。 | [更新自定义镜像](products/ecs/documents/user-guide/update-a-custom-image.md) |
| 复制镜像 | 您需要在其他地域使用该镜像时，可以复制该镜像到目标地域。复制后的镜像独立存在，拥有唯一的镜像 ID。 | [复制自定义镜像](products/ecs/documents/user-guide/copy-an-image.md) |
| 共享镜像 | 创建自定义镜像后，您可以将镜像共享给其他阿里云账号使用。该账号可以使用您共享的自定义镜像，快速创建运行同一镜像环境的 ECS 实例。 | [共享自定义镜像](products/ecs/documents/user-guide/share-a-custom-image.md) |
| 导出镜像 | 创建自定义镜像后，您可以导出镜像到 OSS 存储空间（OSS Bucket），并下载到本地使用。 | [导出自定义镜像](products/ecs/documents/user-guide/export-a-custom-image.md) |
| 修改镜像信息 | 为了方便您管理自定义镜像，您可以根据需要修改自定义镜像的名称和描述。 | [修改镜像的属性和标签](products/ecs/documents/user-guide/modify-the-attributes-of-a-custom-image.md) |
| 删除镜像 | 当您不再需要一个自定义镜像，可以将其删除。 | [删除自定义镜像](products/ecs/documents/user-guide/delete-a-custom-image.md) |


[上一篇：Alibaba Cloud Linux 3 预装NVIDIA GPU驱动镜像](products/ecs/documents/user-guide/alibaba-cloud-linux-3-with-pre-installed-nvidia-gpu-drivers.md)[下一篇：共享镜像](products/ecs/documents/user-guide/shared-image.md)

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
