# 为什么创建ECS实例时看不到某些镜像？-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances

# 为什么创建ECS实例时看不到某些镜像？
本文主要介绍创建ECS实例时看不到某些镜像（包括自定义镜像）的可能原因和解决办法。
## 问题描述
创建ECS实例在选择镜像时，选不到部分镜像（包括自定义镜像）。
## 可能原因和解决方案
以下情况，均可能导致上述问题。
### 镜像的操作系统和实例规格的处理器不是官方兼容
部分ECS实例规格，比如8代ECS实例，对支持的操作系统有限制。
具体限制如下：
[AMD](compatibility-between-amd-instance-types-and-operating-systems.md)[实例规格与操作系统兼容性说明](compatibility-between-amd-instance-types-and-operating-systems.md)
[Intel](intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](intel-instance-specifications-and-operating-system-compatibility.md)
[倚天处理器实例兼容的操作系统](user-guide/the-migration-process.md)
解决方案：
如果对操作系统或实例规格没有特殊要求，选择兼容的镜像操作系统或实例规格。
如果必须选择该镜像和实例规格，您可以在购买页申请放开限制。
支持放开限制的实例：
AMD实例：ecs.c8ae、ecs.g8ae、ecs.r8ae、ecs.c8a、ecs.g8a、ecs.r8a、ecs.hpc8a、ecs.g9a、ecs.c9a、ecs.r9a、ecs.g9ae、ecs.c9ae、ecs.r9ae、ecs.u2a
Intel实例：ecs.g8i、ecs.c8i、ecs.r8i、ecs.hfg8i、ecs.hfc8i、ecs.hfr8i、ecs.g8ise、ecs.c9i、ecs.g9i、ecs.r9i、ecs.u2i
申请方式如下：
在实例购买页面，镜像类型选择自定义镜像，单击检查操作链接。
勾选申请放开限制的勾选框。
首次勾选并单击确定后，需等待约1分钟再刷新镜像列表。
重要
申请放开限制对全地域生效，且生效后不支持再取消。
单击确定，等待一段时间后刷新即可。
### 镜像和实例规格的特性不匹配
| 常见的不匹配原因 | 解决方案 |
| --- | --- |
| 镜像和实例规格的 NVMe 属性不匹配 选择了支持 NVMe 的实例规格，就只能选择支持 NVMe 的镜像（即镜像中包含了 NVMe 驱动且已支持 NVMe 属性）。 | 若目标镜像为自定义镜像，且业务需通过 NVMe 提升存储性能或实现云盘多重挂载。请确保该镜像安装了 NVMe 驱动，且已将镜像的属性 NVMe 驱动 设置为 支持 。更多信息，请参见 [如何为已有自定义镜像安装](adapt-linux-custom-images-to-nvme-based-system-disks.md) [NVMe](adapt-linux-custom-images-to-nvme-based-system-disks.md) [驱动？](adapt-linux-custom-images-to-nvme-based-system-disks.md) 。 说明 关于 NVMe 的更多介绍，请参见 [NVMe](user-guide/nvme-protocol.md) [协议概述](user-guide/nvme-protocol.md) 。 您可以通过 API 接口查询实例规格（ [DescribeInstanceTypes](developer-reference/api-ecs-2014-05-26-describeinstancetypes.md) ）和镜像（ [DescribeImages](developer-reference/api-ecs-2014-05-26-describeimages.md) ）是否支持 NVMe（字段为 NvmeSupport ）。 |
| 镜像和所选实例规格的启动模式不匹配 例如您选择了仅支持 UEFI 启动模式的安全增强型实例规格，则仅能选择 UEFI 版本的镜像。 | 若目标镜像为自定义镜像，可更换镜像的启动模式使之与目标实例匹配。具体操作，请参见 [实例启动模式](user-guide/instance-startup-mode.md) 。 |
### Windows操作系统版本对CPU核数和内存大小有限制
选择与操作系统匹配的实例规格，具体可查看[Windows 和 Windows Server 版本的内存限制](https://learn.microsoft.com/windows/win32/memory/memory-limits-for-windows-releases)。
重要
使用Windows操作系统创建ECS实例时，需要确保实例规格内存大于等于1 GiB。内存低于1 GiB的ECS实例（例如0.5 GB）只能选择Linux镜像或者Windows Server Version 2004镜像（原厂已停止维护）。
### Red Hat操作系统只能匹配经过红帽官方认证的实例规格
选择已通过红帽官方认证的实例规格，具体可查看[Red Hat](instance-families-supported-by-red-hat-images.md)[镜像支持哪些实例规格族？](instance-families-supported-by-red-hat-images.md)
### 部分裸金属、本地型SSD等实例对操作系统的驱动程序、内核有限制
如果对镜像有要求，请选择与操作系统匹配的实例规格。
如果对实例规格有要求，请选择与实例规格处理器匹配的镜像。
[本地](compatibility-between-i4-instance-types-with-operating-systems.md)[SSD](compatibility-between-i4-instance-types-with-operating-systems.md)[型](compatibility-between-i4-instance-types-with-operating-systems.md)[i4](compatibility-between-i4-instance-types-with-operating-systems.md)[实例规格与操作系统兼容性说明](compatibility-between-i4-instance-types-with-operating-systems.md)
[通用型弹性裸金属服务器实例规格族](user-guide/elastic-bare-metal-server-overview.md)[ebmg7a](user-guide/elastic-bare-metal-server-overview.md)
[计算型弹性裸金属服务器实例规格族](user-guide/elastic-bare-metal-server-overview.md)[ebmc7a](user-guide/elastic-bare-metal-server-overview.md)
[内存型弹性裸金属服务器实例规格族](user-guide/elastic-bare-metal-server-overview.md)[ebmr7a](user-guide/elastic-bare-metal-server-overview.md)
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
