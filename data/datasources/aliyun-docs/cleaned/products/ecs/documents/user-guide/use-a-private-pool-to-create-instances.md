# 使用私有池容量创建ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/use-a-private-pool-to-create-instances

# 使用私有池容量创建ECS实例
购买资源预定后，阿里云以私有池的方式预留属性一致的资源，使用私有池容量创建实例时可以确保创建成功。本文介绍如何使用私有池容量创建ECS实例。
重要
释放预留的裸金属实例时，其占用的私有池容量需要较长时间才能恢复可用。在此期间，使用该部分容量创建新实例可能会失败。请合理规划实例的释放时间和频率。
## 前提条件
私有池处于预定生效中状态。
私有池有可用容量。查看私有池容量使用情况的具体操作，请参见[在私有池查看预留的资源](view-a-private-pool.md)。
## 操作步骤
## 控制台方式
本操作主要说明私有池相关的配置项，关于其他配置项的说明，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。
通过控制台使用私有池容量创建实例有以下两个入口。
在实例页面，单击创建实例。
在资源预定页面，单击预定生效中的资源预定操作列的购买实例。
完成基础配置。
在自定义购买页面，需要注意下表中的配置项。
| 配置项 | 说明 |
| --- | --- |
| 付费类型 | 如果资源预定的类型为弹性保障、立即生效容量预定或节省计划容量预定，使用其私有池容量时，付费模式设置为 按量付费 。 如果资源预定的类型为包年包月容量预定，使用其私有池容量时，付费模式设置为 包年包月 。 |
| 地域 | 在购买资源预定时，需要选择地域，因此创建实例时必须选择相同的地域。 |
| 网络及可用区 | 在购买资源预定时，需要选择网络及可用区，因此创建实例时必须选择相同的网络及可用区。 |
| 实例 | 在购买资源预定时，需要选择实例规格，因此创建实例时必须选择相同的实例规格。 |
| 镜像 | 如果资源预定的类型为立即生效容量预定，使用其私有池容量时，必须选择相同类型的操作系统（Linux 或 Windows）。 |
完成存储、带宽和安全组、管理设置配置，然后单击高级选项（选填）。
在高级选项（选填）配置中，完成其他配置项，然后在私有池类型区域，您可以设置是否使用私有池容量以及使用方式。设置方法如下所示：
指定私有池ID：设置私有池类型为指定，并指定一个私有池的ID（私有池的ID和对应资源预定的ID相同）。通过这种方式选择私有池时，如果该私有池没有可用容量，则实例创建失败。
说明
专用私有池和开放私有池仅支持通过指定私有池ID使用。
自动选择开放私有池：设置私有池类型为开放，系统会自动选择一个这类开放私有池，如果这类开放私有池都没有可用容量，则尝试使用公共池容量。
说明
仅开放私有池支持自动选择使用，专用私有池不支持该方式。
不使用私有池容量：设置私有池类型为不使用。不使用任何私有池容量，仅使用公共池容量。
检查所选配置，阅读相关协议。如无疑问，确认创建实例并按提示完成支付。
## OpenAPI方式
使用[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)创建ECS实例时，通过PrivatePoolOptions.MatchCriteria参数设置实例的私有池类型。
Open：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量，则使用公共池资源启动。该模式下无需设置PrivatePoolOptions.Id参数。
Target：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。该模式下必须指定私有池 ID，即PrivatePoolOptions.Id参数为必填项。
None：不使用模式。实例启动将不使用私有池容量。
## 后续步骤
使用私有池容量创建实例时确保创建成功，您可以前往私有资源池页签查看私有池和实例的关联情况。具体操作，请参见[在私有池查看预留的资源](view-a-private-pool.md)。
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
