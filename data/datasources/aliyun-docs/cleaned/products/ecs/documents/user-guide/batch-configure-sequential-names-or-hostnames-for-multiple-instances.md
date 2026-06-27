# 批量设置有序的实例名称或主机名称-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/batch-configure-sequential-names-or-hostnames-for-multiple-instances

# 批量设置有序的实例名称或主机名称
在批量创建多台ECS实例时，默认会生成相同的实例名称和主机名称。为了便于区分每台ECS实例或批量分类和管理您的ECS实例，您可以在创建多台ECS实例时，按照排序规则（指定排序或自动排序）来自定义设置实例名称或主机名称，以规范命名、排序和分类ECS实例，有效提高管理效率。
## 指定排序ECS实例名称或主机名
当您批量创建ECS实例时，可以为您的ECS实例配置指定数值排序的实例名称或主机名称。
### 指定排序
指定排序是一种将实例名称和主机名称按照固定参数格式命名，然后通过参数中的有序数值自动排序来生成实例名称和主机名称的方式，因此，该有序数值是多台ECS实例的实例名称或者主机名称的区别部分。
您只需要在创建ECS实例时，直接在实例名称或主机名称中输入指定排序的参数，即可自动通过有序数值变更配置多台ECS实例的实例名称或主机名。指定排序的参数格式为name_prefix[begin_number,bits]name_suffix，参数说明和参数示例如下。
指定排序参数说明
| 字段名称 | 配置说明 | 示例 |
| --- | --- | --- |
| name_prefix | 指定实例名称或主机名称的前缀。 说明 在有序命名规则中，前缀是必选项，否则当作普通名称处理。 | k8s-node- |
| [begin_number,bits] | 指定实例名称或者主机名称的有序数值。设置后，实例名称或者主机名称的数值会依次递增。 begin_number：有序数值的起始值，取值支持[0,999999]，默认值为 0 。 bits：有序数值所占的位数，取值支持[1,6]，默认值为 6 。 重要 [begin_number,bits] 字段中不能有空格。 当指定的 begin_number 位数大于 bits 的取值时， bits 会默认取值为 6 。 相同前后缀的实例名称或主机名称最大支持 999999 台 ECS 实例。超过部分的 ECS 实例都使用 999999 。 假如 [begin_number,bits] 设置为 [] 或者 [,] ，则 begin_number 将会从 0 开始取值， bits 会默认取值为 6 。 假如 [begin_number,bits] 只设置了 begin_number ，例如 [99] 或 [99,] ，则 bits 会默认取值为 6 。 | [0,6] |
| name_suffix | 指定实例名称或主机名称的后缀。 | -ecshost |
指定排序参数示例
| 输入参数示例 | 生成名称（以 3 台 ECS 实例为例） |
| --- | --- |
| k8s-node-[]-ecshost 或 k8s-node-[,]-ecshost | k8s-node-000000-ecshost k8s-node-000001-ecshost k8s-node-000002-ecshost |
| k8s-node-[99]-ecshost 或 k8s-node-[99,]-ecshost | k8s-node-000099-ecshost k8s-node-000100-ecshost k8s-node-000101-ecshost |
| k8s-node-[99,1]-ecshost | k8s-node-000099-ecshost k8s-node-000100-ecshost k8s-node-000101-ecshost |
| k8s-node-[999998]-ecshost | k8s-node-999998-ecshost k8s-node-999999-ecshost k8s-node-999999-ecshost |
| k8s-node-[0,4] | k8s-node-0000 k8s-node-0001 k8s-node-0002 |
### 操作步骤
本文以创建3台实例名称和主机名称以k8s-node-开头，从0006开始排序，主机名以-ecshost结尾的ECS实例为例进行说明。
重要
您输入的ECS实例名称或主机名需要满足如下要求：
实例名称：长度为2～128个字符，以大小写字母或中文开头，可包含数字、点号（.）、下划线（_）、半角冒号（:）或连字符（-）。
主机名：
Windows系统：长度为2～15个字符，允许使用大小写字母、数字或连字符（-）。不能以连字符（-）开头或结尾，不能连续使用连字符（-），也不能仅使用数字。
其他操作系统（Linux等）：长度为2～64个字符，允许使用点号（.）分隔字符成多段，每段允许使用大小写字母、数字或连字符（-），但不能连续使用点号（.）或连字符（-）。不能以点号（.）或连字符（-）开头或结尾。
## 控制台
创建ECS实例的具体操作，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。在创建ECS实例时，您需要完成如下配置：
购买实例数量：在自定义购买页面右侧的购买实例数量调整框中，单击加号，将购买数量调整为3。
批量设置实例名称或主机名：指定排序的输入格式为name_prefix[begin_number,bits]name_suffix，具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
重要
本示例仅用于指定排序，此处不选中有序后缀。
实例名称：输入需要设置的实例名称。本文指定新创建的3台ECS实例名称以k8s-node-开头，从0006开始排序，因此，实例名称配置为k8s-node-[6,4]。
主机名：选中主机名下方的自定义有序主机名，然后再输入需要设置的主机名。本文指定新创建的3台ECS主机名称以k8s-node-开头，从0006开始排序，且以-ecshost结尾，因此，主机名配置为k8s-node-[6,4]-ecshost。
当您完成ECS实例配置，并确认下单后，可以单击管理控制台，然后查看实例信息：
您可以在实例列表中查看新增的实例。按照本文示例，生成的实例名分别为k8s-node-0006、k8s-node-0007、k8s-node-0008。
您可以在实例详情页面的其他信息区域，查看新增实例的主机名，按照本文实例，生成的主机名分别为k8s-node-0006-ecshost、k8s-node-0007-ecshost、k8s-node-0008-ecshost。
## API
您可以调用[RunInstances](../api-runinstances.md)来创建ECS实例，并指定实例名称和主机名称。以下内容主要描述指定排序名称的参数配置：
InstanceName（实例名称）和HostName（主机名）指定排序的配置格式为name_prefix[begin_number,bits]name_suffix。具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
本文以创建三台实例，实例名称和主机名称以k8s-node-开头，从0006开始排序，主机名以-ecshost结尾为例，具体参数配置如下：
Amount：3
InstanceName：k8s-node-[6,4]
HostName：k8s-node-[6,4]-ecshost
重要
本示例仅用于指定排序，此处UniqueSuffix保持默认不开启。
按照本文示例，生成的实例名分别为k8s-node-0006、k8s-node-0007、k8s-node-0008，生成的主机名分别为k8s-node-0006-ecshost、k8s-node-0007-ecshost、k8s-node-0008-ecshost。
## 自动排序ECS实例名称或主机名
当您批量创建ECS实例时，可以通过自动排序功能为您的ECS实例名称和主机名增加后缀。
### 自动排序
自动排序是一种自动为实例名称和主机名称添加3位有序后缀的方式。开启自动排序功能后，实例名称和主机名称后缀从001开始递增，最大不能超过999。因此，该有序后缀是多台ECS实例的实例名称或者主机名称的区别部分。
自动排序功能默认关闭。您只需要在创建ECS实例时，手动开启该功能，然后输入实例名称和主机名称，即可自动在实例名称和主机名称后添加有序的后缀，生成新的实例名称和主机名称。
当您开启自动排序时，支持输入实例名称与主机名称的命名格式如下。
重要
如果您需要搭配使用指定排序命名实例名称与主机名称，则您输入的指定排序命名格式必须指定name_suffix，否则将只生效自动排序。指定排序的具体规则，请参见[指定排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
自动排序命名格式
| 命名格式（实例名称或主机名称） | 输入参数示例 | 生成名称（以 3 台 ECS 实例为例） |
| --- | --- | --- |
| 普通名称（未使用指定排序） | ecs | ecs001 ecs002 ecs003 |
| 指定排序：name_prefix[begin_number,bits]name_suffix | k8s-node-[]-ecshost 或 k8s-node-[,]-ecshost | k8s-node-000000-ecshost001 k8s-node-000001-ecshost002 k8s-node-000002-ecshost003 说明 指定排序和自动排序同时生效。 |
| 指定排序：name_prefix[begin_number,bits] | k8s-node-[0,4] | k8s-node-0000 k8s-node-0001 k8s-node-0002 说明 指定排序格式未设置命名后缀 name_suffix ，自动排序不生效。 |
### 操作步骤
本文以创建3台实例名称为ecs，主机名为ecshost，自动在实例名和主机名后增加后缀为例进行说明。
重要
您输入的ECS实例名称或主机名需要满足如下要求：
实例名称：长度为2～128个字符，以大小写字母或中文开头，可包含数字、点号（.）、下划线（_）、半角冒号（:）或连字符（-）。
主机名：
Windows系统：长度为2～15个字符，允许使用大小写字母、数字或连字符（-）。不能以连字符（-）开头或结尾，不能连续使用连字符（-），也不能仅使用数字。
其他操作系统（Linux等）：长度为2～64个字符，允许使用点号（.）分隔字符成多段，每段允许使用大小写字母、数字或连字符（-），但不能连续使用点号（.）或连字符（-）。不能以点号（.）或连字符（-）开头或结尾。
## 控制台
创建ECS实例的具体操作，请参见[自定义购买实例](create-an-instance-by-using-the-wizard.md)。在创建ECS实例时，您需要完成如下配置：
购买实例数量：在自定义购买页面右侧的购买实例数量调整框中，单击加号，将购买数量调整为3。
批量设置实例名称或主机名：自动排序的具体规则，请参见[自动排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
实例名称：输入需要设置的实例名称。本文指定新创建的3台ECS实例名称以ecs开头，因此，实例名称配置为ecs。
主机名：输入需要设置的主机名。本文指定新创建的3台ECS主机名称以ecshost开头，因此，主机名配置为ecshost。
有序后缀：选中该参数后，ECS实例的实例名称和主机名会自动增加后缀，进行自动排序。
当您完成ECS实例配置，并确认下单后，可以单击管理控制台，然后查看实例信息：
您可以在实例列表中查看新增的实例。按照本文示例，生成的实例名分别为ecs001、ecs002、ecs003。
您可以在实例详情页面的其他信息区域，查看新增实例的主机名，按照本文示例，生成的主机名分别为ecshost001、ecshost002、ecshost003。
## API
您可以调用[RunInstances](../api-runinstances.md)来创建ECS实例，并指定实例名称和主机名称。以下内容主要描述自动排序名称的参数配置：
UniqueSuffix配置为true，系统会对InstanceName和HostName自动排序，增加的后缀从001开始，按实例数量依次递增。自动排序的具体规则，请参见[自动排序](batch-configure-sequential-names-or-hostnames-for-multiple-instances.md)。
本示例创建三台自动排序实例，具体参数配置如下：
Amount：3
InstanceName：ecs
HostName：ecshost
UniqueSuffix：true
按照本文示例，生成的实例名分别为ecs001、ecs002、ecs003，生成的主机名分别为ecshost001、ecshost002、ecshost003。
## 相关文档
如果您在使用ECS实例的过程中，需要修改ECS实例的属性（实例的名称、主机名、实例描述等信息）以符合实际管理需求，请参见[修改实例属性](modify-the-properties-of-an-instance.md)。
您可以根据实际需要管理和使用ECS实例，例如[管理与配置实例](manage-instance-status.md)或[管理实例配置](manage-instance-configurations.md)。
您可以使用阿里云云服务器ECS搭建自己的网站，具体操作，请参见[建站零基础入门](../use-cases/quick-start.md)或[自助建站方式汇总](../summary-of-website-building-methods.md)。
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
