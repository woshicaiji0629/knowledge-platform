# 使用自定义镜像或共享的自定义镜像创建ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/create-an-ecs-instance-by-using-a-custom-image

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

# 使用自定义镜像或共享镜像创建实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

为实现应用环境的批量部署或服务器的快速复制，可使用自定义或共享镜像直接创建ECS实例，以此简化配置流程，确保环境一致性并提高运维效率。

## 地域限制

待创建实例的地域必须与镜像所在地域一致。

## 操作步骤

## 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/image)[控制台-镜像](https://ecs.console.aliyun.com/image)，在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在自定义镜像或共享镜像页签找到待使用的自定义镜像，在操作列中，单击创建实例。

- 

在自定义购买页，系统将自动填充地域与镜像信息，根据界面提示完成其他[配置项](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)后单击确认下单。

## CLI

在通过[RunInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createinstance.md)创建实例时，可通过配置ImageId为对应自定义镜像的ID。命令示例如下：

执行该命令后，会创建一台使用自定义镜像（ID为m-bp1******pi）的实例。aliyun ecs RunInstances \ --region cn-hangzhou \ --RegionId 'cn-hangzhou' \ --ImageId 'm-bp1******pi' \ --InstanceType 'ecs.g7.large' \ --VSwitchId 'vsw-bp1******trg' \ --SecurityGroupId 'sg-bp1******dgl' \ --SystemDisk.Size 40 \ --SystemDisk.Category cloud_essd \

## API

在通过[RunInstances](products/ecs/documents/developer-reference/api-ecs-2014-05-26-runinstances.md)或[CreateInstance](products/ecs/documents/developer-reference/api-ecs-2014-05-26-createinstance.md)创建实例时，可配置ImageId为需要使用的自定义镜像的ID。

## 后续操作

- 

若创建实例时增加了数据盘的大小，实例创建成功后，必须登录ECS实例扩容分区和文件系统才能使新增的容量生效。[Linux](products/ecs/documents/user-guide/resize-linux-cloud-disks.md)[实例指引](products/ecs/documents/user-guide/resize-linux-cloud-disks.md)、[Windows](products/ecs/documents/user-guide/resize-windows-cloud-disks.md)[实例指引](products/ecs/documents/user-guide/resize-windows-cloud-disks.md)。

增加了系统盘大小，系统盘会自动扩容，若自动扩容失败，需手动扩容分区和文件系统使新增的容量生效。[Linux](products/ecs/documents/user-guide/resize-linux-cloud-disks.md)[实例指引](products/ecs/documents/user-guide/resize-linux-cloud-disks.md)、[Windows](products/ecs/documents/user-guide/resize-windows-cloud-disks.md)[实例指引](products/ecs/documents/user-guide/resize-windows-cloud-disks.md)。

- 

若创建实例时，手动添加了新数据盘，实例创建成功后，必须先[初始化](products/ecs/documents/user-guide/initialize-a-data-disk.md)该新数据盘才能正常使用。

## 计费说明

基于付费商业镜像制作的镜像创建ECS实例时会产生[额外费用](products/ecs/documents/images.md)。

## 常见问题

自定义镜像不在当前账号或地域中，如何处理？

| 场景 | 解决方法 |
| --- | --- |
| 自定义镜像在本地设备上 | 将本地镜像 [导入](products/ecs/documents/user-guide/import-an-image.md) 为阿里云自定义镜像。 |
| 自定义镜像在其他地域 | 将自定义镜像 [复制](products/ecs/documents/user-guide/copy-an-image.md) 到需要创建实例的地域。 |
| 自定义镜像在其他阿里云账号 | 将自定义镜像 [共享](products/ecs/documents/user-guide/share-a-custom-image.md) 给需要创建实例的账号。 |


为什么创建ECS实例时看不到某些镜像（包括自定义镜像）？

- 

镜像与实例规格的特性不匹配：支持NVMe的实例规格只能选择支持NVMe的镜像，因此请确保镜像已安装NVMe驱动，并将镜像的NVMe驱动属性[修改](products/ecs/documents/user-guide/modify-the-attributes-of-a-custom-image.md)为支持，该镜像才会显示在镜像列表中；仅支持UEFI启动模式的实例规格只能选择UEFI版本的镜像，若为自定义镜像可更换镜像启动模式解决。

- 

操作系统与实例规格处理器不兼容：部分实例规格（如8代实例）对支持的操作系统有限制。

- 

[AMD](products/ecs/documents/compatibility-between-amd-instance-types-and-operating-systems.md)[实例规格与操作系统兼容性说明](products/ecs/documents/compatibility-between-amd-instance-types-and-operating-systems.md)

- 

[Intel](products/ecs/documents/intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](products/ecs/documents/intel-instance-specifications-and-operating-system-compatibility.md)

- 

[倚天处理器实例兼容的操作系统](products/ecs/documents/user-guide/the-migration-process.md)

- 

Windows操作系统版本对CPU核数和内存大小有限制：使用Windows镜像时，实例规格内存需大于等于1 GiB。内存低于1 GiB的实例只能选择Linux镜像。

- 

Red Hat镜像只能匹配经过红帽官方认证的实例规格。

- 

部分裸金属、本地SSD型等实例对操作系统的驱动程序、内核有限制：需选择与实例规格处理器匹配的镜像。

更多详情，请参见[为什么创建](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[ECS](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[实例时看不到某些镜像？](products/ecs/documents/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)

[上一篇：自定义购买实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)[下一篇：使用社区镜像创建实例](products/ecs/documents/user-guide/create-an-instance-using-community-image.md)

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
