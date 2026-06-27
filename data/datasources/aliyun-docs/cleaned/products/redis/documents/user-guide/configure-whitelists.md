# 不同场景IP白名单配置方法-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/configure-whitelists

# 设置IP白名单
为保障云数据库 Tair（兼容 Redis）实例的安全稳定，系统默认禁止所有IP地址访问Tair（以及Redis开源版）实例。在开始使用Tair（以及Redis开源版）实例前，您需要将客户端的IP地址或IP地址段添加到实例的白名单中。正确使用白名单可以让实例得到高级别的访问安全保护，建议您定期维护白名单。
## 白名单设置方法介绍
| 设置方法 | 说明 | 适用场景 |
| --- | --- | --- |
| 添加白名单 | 手动添加客户端所属的 IP 地址到实例的白名单，以允许该客户端访问实例。 | [相同](configure-whitelists.md) [VPC](configure-whitelists.md) [的](configure-whitelists.md) [ECS](configure-whitelists.md) [实例访问](configure-whitelists.md) [Redis](configure-whitelists.md) [不同](configure-whitelists.md) [VPC](configure-whitelists.md) [的](configure-whitelists.md) [ECS](configure-whitelists.md) [实例访问](configure-whitelists.md) [Redis](configure-whitelists.md) [本地设备访问](configure-whitelists.md) [Redis](configure-whitelists.md) |
| 添加安全组 | [安全组](../../../ecs/documents/user-guide/overview-44.md) 是一种虚拟防火墙，用于控制安全组中的 ECS 的出入流量。 如果需要授权多个 ECS 访问实例，您可以为实例绑定 ECS 所属安全组的方式，绑定后安全组内所有 ECS 都可以访问该实例（无需手动填写 ECS 的 IP 地址）。 | [通过安全组批量添加](configure-whitelists.md) [ECS](configure-whitelists.md) [私网和公网](configure-whitelists.md) [IP](configure-whitelists.md) |
| [通过阿里云](configure-whitelists.md) [App](configure-whitelists.md) [设置白名单](configure-whitelists.md) （手机端） | [阿里云](https://help.aliyun.com/zh/document_detail/52854.html) [App](https://help.aliyun.com/zh/document_detail/52854.html) 是阿里云官方出品的移动应用，为您提供随时随地触达阿里云的能力。通过阿里云 App，您可以在手机端快速完成 IP 白名单的设置，同时还支持云资源监控、了解产品动态、购买云产品等功能。 | 通过手机 App 添加专有网络 IP 或公网 IP 到白名单 |
说明
您也可以同时设置白名单分组和ECS安全组，白名单分组中的IP地址和安全组中的ECS都可以访问该实例。
## 添加ECS私网IP到白名单
如果您的ECS与实例位于同一专有网络（VPC），推荐您通过专有网络访问。
说明
如果您的ECS与实例不属于同一专有网络，您可以更换ECS所属的专有网络。具体操作，请参见[更换](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[ECS](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[的](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)[VPC](../../../ecs/documents/user-guide/change-the-vpc-of-an-ecs-instance.md)。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
在default默认安全组，单击修改。
说明
您也可以单击添加白名单分组创建一个新的分组。分组名称长度为2~32个字符，由小写字母、数字或下划线（_）组成，需以小写字母开头，以小写字母或数字结尾。
添加方式选择加载ECS私网IP，页面将展示该实例同一地域的ECS私网IP。
鼠标指针悬浮在IP地址上，可查看该IP地址所属ECS的ID和名称
选中需要的IP地址，将其移至右侧。
单击确定。
可选：若某个白名单分组中的所有IP地址均需要移除，您可以在目标白名单分组的右侧单击删除来完成该操作。
系统默认生成的白名单分组无法删除，例如default、hdm_security_ips等。
## 添加公网IP到白名单
当您需要从本地设备远程访问实例或您的ECS与实例不在同一专有网络（VPC）时，请参考以下步骤添加白名单。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
在default默认安全组，单击修改。
说明
您也可以单击添加白名单分组创建一个新的分组。分组名称长度为2~32个字符，由小写字母、数字或下划线（_）组成，需以小写字母开头，以小写字母或数字结尾。
添加方式选择手动添加。
在组内白名单文本框中，输入IP地址或IP地址段。
查询本地设备公网IP和ECS公网IP的方法
| 类别 | 查询公网 IP 地址的方法 |
| --- | --- |
| [ECS](../../../ecs/documents/user-guide/what-is-ecs.md) [实例](../../../ecs/documents/user-guide/what-is-ecs.md) | [查询](../../../ecs/documents/user-guide/network-faq.md) [ECS](../../../ecs/documents/user-guide/network-faq.md) [的](../../../ecs/documents/user-guide/network-faq.md) [IP](../../../ecs/documents/user-guide/network-faq.md) [地址？](../../../ecs/documents/user-guide/network-faq.md) |
| 本地 | 查询本地设备公网 IP 地址的方式可能因您所处的网络环境或操作不同而不同。以下是不同系统通过命令方式获取本地设备公网 IP 地址的参考方法： Linux 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 Windows 操作系统：打开命令提示符，输入 curl ip.me 命令后回车。 macOS 操作系统：打开终端，输入 curl ifconfig.me 命令后回车。 |
IP地址以英文逗号（,）分隔，不可重复，最多1000个。支持格式为：
具体IP地址，例如10.23.12.24。
[CIDR](../../../vpc/documents/faq-about-cidr-blocks.md)[模式](../../../vpc/documents/faq-about-cidr-blocks.md)，即无类域间路由，/24表示地址中前缀的长度，范围为1~32，例如10.23.12.0/24表示的IP段范围为10.23.12.0 ~ 10.23.12.255。
警告
在白名单中添加0.0.0.0/0表示允许所有IP地址访问该实例。该操作存在高安全风险，请谨慎设置。
单击确定。
可选：若某个白名单分组中的所有IP地址均需要移除，您可以在目标白名单分组的右侧单击删除来完成该操作。
系统默认生成的白名单分组无法删除，例如default、hdm_security_ips等。
## 通过安全组批量添加ECS私网和公网IP
多个ECS实例需要访问Tair实例时，您可以在Tair白名单中添加安全组。添加后，Tair实例将允许该安全组中所有关联的实例（如ECS、弹性容器实例等）通过私网IP与公网IP进行访问。
说明
此处IP访问控制仅对安全组中关联的实例（ECS实例等）生效，与安全组中自定义网段、IP地址无关。
Tair实例版本需兼容Redis 4.0（最新小版本）及以上的大版本，升级方法请参见[升级大版本](upgrade-the-major-version-1.md)。
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击白名单设置。
单击安全组。
在安全组页签，单击添加安全组。
在弹出的对话框中，选择需要添加的安全组。
支持通过安全组名称、安全组ID进行模糊搜索。
图 3.添加安全组
说明
每个实例最多可设置10个安全组。
单击确定。
可选：当您需要移除所有安全组时，您可以单击清除安全组来实现。
## 通过阿里云App设置白名单
选择下述方式，下载并安装阿里云App：
访问[阿里云](https://promotion.aliyun.com/ntms/mobile.html)[App](https://promotion.aliyun.com/ntms/mobile.html)[介绍页面](https://promotion.aliyun.com/ntms/mobile.html)，扫描右上角的二维码。
在应用市场中搜索阿里云。
[登录阿里云](https://help.aliyun.com/zh/document_detail/185103.html)[App](https://help.aliyun.com/zh/document_detail/185103.html)。
打开阿里云App，在运维页面我的资源中，找到云数据库 Tair（兼容 Redis），单击实例列表。
单击目标实例。在页面顶部单击账号&白名单。
根据业务需求，选择执行下述操作：
手动修改白名单：单击目标白名单分组右侧的图标，然后单击修改并输入IP白名单。
新增白名单分组：在页面下方单击添加白名单分组，输入分组名称和IP白名单。
删除白名单分组：单击目标白名单分组右侧的图标，然后选择删除。
## 相关API
| API | 说明 |
| --- | --- |
| [DescribeSecurityIps](../developer-reference/api-r-kvstore-2015-01-01-describesecurityips-redis.md) | 查询实例的 IP 白名单。 |
| [ModifySecurityIps](../developer-reference/api-r-kvstore-2015-01-01-modifysecurityips-redis.md) | 设置实例的 IP 白名单。 |
| [DescribeSecurityGroupConfiguration](../developer-reference/api-r-kvstore-2015-01-01-describesecuritygroupconfiguration-redis.md) | 查询实例白名单中已配置的安全组。 |
| [ModifySecurityGroupConfiguration](../developer-reference/api-r-kvstore-2015-01-01-modifysecuritygroupconfiguration-redis.md) | 重新设置实例白名单中的安全组。 |
## 常见问题
### 为什么通过redis-cli连上后提示(error) ERR illegal address？
您的redis-cli所属设备的IP地址未添加至白名单中，请确认白名单配置。
### 我的实例为什么没有安全组设置？
以下实例暂不支持通过安全组的方式添加白名单。
实例的大版本需为Redis 4.0（最新小版本）及以上的大版本，升级方法请参见[升级大版本](upgrade-the-major-version-1.md)。
暂不支持设置ECS安全组的实例架构：云原生版集群架构、云原生版读写分离架构。
### 安全组设置了访问规则，为什么对实例不生效?
现象：安全组设置了访问规则，例如允许118.31.XX.XX这个IP的访问，但其他IP依然可以访问。
原因：您为安全组设置的出入流量规则不适用于Tair（以及Redis开源版）实例。Tair（以及Redis开源版）实例添加安全组，表示安全组内的ECS可以通过专有网络或公网访问实例。
### 通过telnet测试端口报错Connection closed by foreign host，怎么解决？
报错如下。
Escape character is '^]'. Connection closed by foreign host.
表示当前设备的IP地址未添加到目标实例的白名单中，请参考上文方法将IP地址添加至白名单中，并重试。
### 实例里自动生成的白名单分组，它们的来源是什么？可以删除吗？
初始情况下，实例的白名单分组仅包含default，随着对实例执行某些操作，白名单分组会逐渐增多，详情请参见下表。
| 白名单分组名称 | 来源说明 |
| --- | --- |
| default | 系统默认的白名单分组，不可删除。 |
| ali_dms_group | 通过 DMS 登录实例时，DMS 自动创建的白名单分组。具体操作，请参见 [通过](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) [DMS](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) [连接实例](log-on-to-an-apsaradb-for-redis-instance-by-using-dms.md) 。请勿删除或修改该白名单分组，否则可能导致无法通过 DMS 登录实例。 |
| hdm_security_ips | 使用 CloudDBA 相关功能时（例如 [离线全量](offline-key-analysis.md) [Key](offline-key-analysis.md) [分析](offline-key-analysis.md) ），DAS 自动创建的白名单分组。请勿删除或修改该白名单分组，否则可能导致 CloudDBA 功能使用异常。 |
### 白名单分组中包含了127.0.0.1，此时白名单中其他IP地址的客户端能否连接实例？
可以的。当白名单中增加了任意客户端IP地址或增加安全组时，127.0.0.1均会自动失效，客户端可以正常连接。如果所有白名单分组中仅剩下127.0.0.1，则禁止所有IP地址连接实例。
### 本地设备的公网IP地址每次都会变化，每次都需要重新添加IP地址，有什么解决方案？
若本地设备的公网为动态IP，会时常发生变化，您可以在实例的IP白名单中加入相关IP网段。例如IP地址总是在10.10.10.*网段（10.10.10.15或10.10.10.155等），您可以在白名单中添加10.10.10.0/24，表示将10.10.10.0 ~ 10.10.10.255范围的IP都添加至白名单中。
警告
该方案会导致实例的安全性有所降低，请谨慎使用。
### 开通公网访问后，为什么不在白名单中的设备可通过ping或者telnet命令连通公网连接地址？
云数据库 Tair（兼容 Redis）是基于访问鉴权的白名单模式，根据登录请求进行验证。而通过ping和telnet命令联通实例仅代表网络是连通的，并不能连接到实例。
### 删除某个IP白名单后，为什么此IP的客户端仍可连接实例？
连接保持机制：白名单策略仅作用于新建立的连接。已建立的长连接（例如连接池、持久会话）在未主动断开前仍可继续通信。如果您想禁止某客户端访问实例，可在删除IP白名单后，重启客户端服务。
专有网络免密访问：若实例启用了专有网络（VPC）免密访问功能，同一VPC内的客户端可能无需白名单即可访问。可通过[设置参数](modify-the-values-of-parameters-for-an-instance.md)#no_loose_check-whitelist-always为yes启用白名单检查。
安全组策略冲突：若配置了安全组规则，需检查安全组是否仍允许该IP访问实例。
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
