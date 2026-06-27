# 通过多种方式精确查找并选择ECS镜像-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/find-an-image

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

# 查找镜像

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在创建云服务器ECS实例时，需要从海量的镜像中选择并定位一个合适的镜像。阿里云支持通过控制台、镜像目录或API的方式精确查找镜像。

## 购买ECS时快速查找镜像

- 

单击[ECS](https://ecs-buy.aliyun.com)[控制台-自定义购买](https://ecs-buy.aliyun.com)

- 

在镜像区域单击页签快速选择或使用搜索功能，查找目标镜像。

若需全局搜索精细查找目标镜像，可单击图标，在弹窗中[使用镜像目录查找镜像](products/ecs/documents/user-guide/find-an-image.md)。

- 

配置ECS实例其他属性，按照界面指引创建ECS实例。

## 在镜像页面查找镜像

镜像页面适用于已下单的云市场镜像、已创建的自定义镜像、被共享的镜像、社区镜像及公共镜像的查找。

云市场镜像页签仅展示已下单的云市场镜像，若需查看选购云市场镜像，需前往[云市场](https://market.aliyun.com/products/)搜索。

- 

单击进入[ECS](https://ecs.console.aliyun.com/image)[控制台-镜像](https://ecs.console.aliyun.com/image)，在页面左侧顶部选择目标资源组和地域。

- 

根据业务需要选择镜像类型并查找目标镜像。

自定义镜像页签下支持以[镜像族系](products/ecs/documents/user-guide/overview-37.md)的方式分类查看镜像，对于需要保证操作系统版本一致性的场景，建议开启镜像族系视图。

## 使用镜像目录查找镜像

镜像目录支持对全量镜像按镜像归属和使用频率等因素进行分类、智能化搜索、更细颗粒度的筛选和过滤等功能，相较于镜像页面提供更丰富的分类和筛选，适合在不确定具体镜像时进行探索和比较。

镜像目录会将符合ECS镜像标准化规范的镜像标识为[标准镜像](products/ecs/documents/user-guide/find-an-image.md)。

操作步骤

- 

访问[ECS](https://ecs.console.aliyun.com/imageCatalog/region/cn-hangzhou)[控制台-镜像目录](https://ecs.console.aliyun.com/imageCatalog/region/cn-hangzhou)。在页面左侧顶部，选择目标资源组和地域。

- 

在镜像目录页面，根据业务需要选择镜像目录的分类并查找目标镜像。可在镜像目录页面的筛选条件区域，勾选过滤条件，匹配出符合条件的镜像。

快速启动镜像是阿里云官方筛选后推荐给用户的常用镜像，来源于公共镜像和市场镜像；私有镜像是归属当前用户的镜像，包含个人制作的自定义镜像和他人共享的镜像。

- 

搜索或筛选完成后，可以单击右侧查看其他类型筛选结果，查看除当前分类展示的符合条件的镜像外，其他分类搜索到的镜像。

## 使用API查找镜像

可以调用API接口[DescribeImages - 查询镜像资源](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeimages.md)查找账户下的自定义镜像、阿里云提供的公共镜像、云市场镜像以及其他阿里云账户主动共享给当前账户的共享镜像。

## 常见问题

什么是标准镜像？

当Linux镜像同时满足以下条件时会被定义为标准镜像：

重要

标准镜像中不包含CVE等安全漏洞的评估。因此，建议在使用任何阿里云平台的推荐镜像之前进行全面的安全评估和漏洞扫描，并及时更新和修复可能存在的安全漏洞。您也可以根据自身需求和安全要求，自行选择其他安全性更高的镜像或采取其他安全措施来保护系统和数据的安全。可以在[镜像概述](products/ecs/documents/user-guide/image-overview.md)页面查看更多镜像的权责说明。

- 

安装了阿里云版cloud-init：用于实例初始化。

- 

内核支持CONFIG_FW_CFG_SYSFS特性：用于实例元数据传递。

- 

网络配置为DHCP：确保基于该镜像创建的实例能自动获取IP地址。

- 

安装了Virtio驱动：提供高性能的I/O。

- 

安装了growpart工具：支持实例启动时自动扩容根分区。

- 

使用UUID配置fstab和grub：避免因磁盘顺序变化导致启动失败。

为什么镜像控制台找不到想要的镜像？

请按以下步骤排查：

- 

地域： 确保在控制台选择的地域是镜像所在的地域。

- 

镜像类型：检查是否在正确的镜像类型页签下查找。

- 

权限设置： 确认当前操作的 RAM 用户或角色具有ecs:DescribeImages权限。

- 

镜像状态： 确保镜像状态为Available。

- 

若为共享镜像，请与共享方确认：

- 

镜像是否已成功共享给当前阿里云账号。

- 

共享操作是否与当前选择的地域一致。

- 

若需查看未购买的云市场镜像，需前往[云市场](https://market.aliyun.com/products/)搜索。

- 

若为新建资源，可能存在 1-5 分钟的索引延迟，请稍后刷新重试。

## 相关文档

查找到满足要求的镜像后，可以使用镜像进行以下相关操作：

- 

[使用自定义镜像创建实例](products/ecs/documents/user-guide/create-an-ecs-instance-by-using-a-custom-image.md)

- 

[使用社区镜像创建实例](products/ecs/documents/user-guide/create-an-instance-using-community-image.md)

- 

[共享镜像](products/ecs/documents/user-guide/shared-images.md)

- 

[复制自定义镜像](products/ecs/documents/user-guide/copy-an-image.md)

- 

[导出自定义镜像](products/ecs/documents/user-guide/export-a-custom-image.md)

- 

[修改镜像的属性和标签](products/ecs/documents/user-guide/modify-the-attributes-of-a-custom-image.md)

- 

[删除自定义镜像](products/ecs/documents/user-guide/delete-a-custom-image.md)

[上一篇：图说镜像](products/ecs/documents/user-guide/tew-mirror.md)[下一篇：镜像类型](products/ecs/documents/user-guide/image-types.md)

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
