# 什么是IPAM？-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/ip-address-management-ipam

# IP地址管理（IPAM）
有效的地址规划与管理是确保地址资源高效利用、避免地址冲突的基础，网络规划不当将会导致后期极高的重建成本。传统的 IP 地址管理依赖电子表格和自研工具，手动跟踪多账户、多 VPC 的地址分配。这种方式耗时、易出错，可能导致地址冲突。
VPC IP 地址管理 (IPAM) 作为 IP 地址管理工具，可以帮助自动化分配与管理 IP 地址，简化网络管理流程并避免地址冲突。IPAM 支持以下功能：
| 企业地址规划 地址规划不合理将造成网络冲突，带来极高的重建成本。 网络管理员使用 IPAM 整体规划业务域的可用地址段。 多账号企业中，网络管理员可以将规划后的地址池共享给各业务账号。 | 地址资源分配 手动管理和分配地址复杂度高且易出错。 使用 IPAM 地址池实现规划后，可根据分配规则为 VPC 自动分配地址段，提升地址管理的统一性与效率；也可以按需预留地址段，避免地址冲突。 |
| --- | --- |
| 全局地址资源管理 每个 VPC 有地域、账号归属，用户仅可在对应地域查看本账号下的 VPC 和交换机资源。 IPAM 关联资源发现后，可以统一查看并管理所有生效地域内的 VPC 和交换机。网络管理员将 IPAM 和各业务账号共享的资源发现关联，可以管理多账号下的资源，了解地址冲突情况。 | 地址冲突检测与利用率监控 通过地址 IP 地址利用率，资源团队可以根据监控配置自动化的容量管理，针对 IP 利用率高的资源及时完成扩容。 了解地址重叠情况，可以主动发现并解决网络连接中的地址冲突，避免网络互连时发生冲突。 |
## 工作原理
IPAM 作为单元化的功能，需要选择 1 个地域创建并托管 IPAM 实例，支持规划和管理多个地域内的全部地址资源。管理范围的某个地域出现故障时，不影响 IPAM 对其余地域资源的规划和管理。
创建 IPAM 时，选定的请求地域是 IPAM 实例的托管地域。在托管地域的基础上，可以增加其他地域，作为 IPAM 的生效地域。
创建 IPAM 后，系统默认创建两个作用范围，每个作用范围代表一个独立的 IP 地址空间。
公网作用范围：适用于所有公有空间，当前仅支持分配和使用阿里云提供的 IPv6 地址段。
私网作用范围：适用于所有私有空间，支持分配和使用 IPv4 地址段。支持自建私网作用范围来管理独立的地址空间。
在 IPAM 作用范围内可以创建IPAM地址池，结合业务需求，使用分层规划的方式划分地址池并预置 CIDR 。
通过创建子地址池，可以将较大的地址段（如按区域）逐级细分为更小的网段分配给不同部门或业务线。
逐层细化的方式能有效避免IP地址冲突。每个细分的地址池可以关联特定的安全规则，以满足不同业务场景的安全需求。
IPAM 地址池预置的 CIDR，可以为 VPC 分配网段或创建自定义分配来预留混合云/多云地址，从而避免地址冲突。
## 更多信息
### 计费说明
IP地址管理（IPAM）功能正在进行公测，公测期间免费使用。
### 支持的地域
| 区域 | IPAM 支持的地域 |
| --- | --- |
| 亚太-中国 | 华东 1（杭州） 、 华东 2（上海） 、 华东 5 （南京-本地地域-关停中） 、 华北 1（青岛） 、 华北 2（北京） 、 华北 3（张家口） 、 华北 5（呼和浩特） 、 华北 6（乌兰察布） 、 华南 1（深圳） 、 华南 2（河源） 、 华南 3（广州） 、 西南 1（成都） 、 西北 2（中卫） 、 中国香港 、 华中 1（武汉-本地地域） 、 华东 6（福州-本地地域-关停中） |
| 亚太-其他 | 日本（东京） 、 韩国（首尔） 、 新加坡 、 马来西亚（吉隆坡） 、 印度尼西亚（雅加达） 、 菲律宾（马尼拉） 、 泰国（曼谷） |
| 欧洲与美洲 | 德国（法兰克福） 、 英国（伦敦） 、 美国（硅谷） 、 美国（弗吉尼亚） |
| 中东 | 阿联酋（迪拜） 、 沙特（利雅得）- 合作伙伴运营 |
### 配额限制
| 配额名称 | 描述 | 默认限制 | 提升配额 |
| --- | --- | --- | --- |
| ipam_quota_per_region | 每个用户在每个地域支持创建的 IPAM 数量 | 1 个 | 无法提升 |
| ipam_scope_quota_per_ipam | 每个 IPAM 支持创建的 IPAM 作用范围数量 | 5 个 |  |
| ipam_pool_quota_depth | 每个地址池最大深度 | 10 |  |
| ipam_cidr_quota_per_ipam_pool | 每个地址池中允许预置的 CIDR 的数量 | 50 个 |  |
| ipam_sub_pool_quota_per_ipam_pool | 每个地址池允许创建的子地址池的数量 | 50 个 |  |
| ipam_pool_quota_per_scope | 每个 IPAM 私有范围支持创建的地址池的数量 | 500 个 |  |
| custom_ipam_resource_discovery_quota_per_region | 单地域单账号允许创建的自定义资源发现数量 | 1 个 |  |
| resource_share_quota_per_ipam_resource_discovery | 每个资源发现支持创建的共享资源数量 | 100 个 |  |
| shared_ipam_resource_discovery_quota_per_user | 每个用户允许拥有的共享资源发现的数量 | 100 个 |  |
| resource_share_quota_per_ipam_pool | 每个 IPAM 地址池允许创建的共享资源数量 | 100 个 |  |
| shared_ipam_pool_quota_per_user | 每个用户允许拥有的共享地址池的数量 | 100 个 |  |
| ipam_public_ipv6_top_pool_quota_per_region_isp | 每个用户在每个地域支持创建的每种 ISP 类型的公网 IPv6 IPAM 顶级地址池数量 | 1 个 |  |
| ipam_cidr_quota_per_public_ipv6_top_pool | 每个用户在每个地域支持为公网 IPv6 IPAM 顶级地址池预置的 CIDR 数量 | 1 个 |  |
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
