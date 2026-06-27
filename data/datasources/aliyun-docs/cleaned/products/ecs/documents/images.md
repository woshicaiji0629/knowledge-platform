# 镜像计费-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/images

# 镜像计费
使用付费镜像创建ECS实例可能会产生镜像软件许可证费用。本文详细介绍了镜像费用的计费规则、费用示例以及费用明细查询方法。
## 费用组成
使用付费商业镜像，或基于付费商业镜像制作的镜像创建ECS实例时会产生操作系统许可证费用。
说明
使用自定义镜像的相关操作可能产生快照等其他产品的费用，详情请参见[镜像功能关联操作计费](images.md)。
若释放实例后仍存在镜像相关计费，请检查是否存在未清理的相关付费资源，详情请参见[停止计费](images.md)。
产生操作系统许可证的费用具体情况如下：
| 镜像类型 | 产生镜像软件许可证的使用场景 |
| --- | --- |
| 公共镜像 | 使用阿里云公共镜像创建实例时，选择 Red Hat、SUSE 、 [Alibaba Cloud Linux Pro](https://help.aliyun.com/zh/alinux/product-overview/what-is-alibaba-cloud-linux-pro) 、Windows（在中国香港及海外地域创建）操作系统时，需支付操作系统许可证费用。 |
| 自定义镜像 | 使用最终来源为阿里云公共镜像付费操作系统制作的自定义镜像。 在中国香港及海外地域使用导入的 Windows 系统自定义镜像创建实例，镜像软件的许可证费用将根据许可证类型计算。 当许可证类型为阿里云（Aliyun）时，将收取费用。 当许可证类型为自带许可（BYOL）时，则不收取费用。 使用最终来源为云市场镜像制作的自定义镜像创建实例时，需支付云市场镜像的软件许可证费用。 |
| 共享镜像 | 使用最终来源为付费操作系统的镜像创建 ECS 实例时，会产生操作系统许可证费用。 |
| 社区镜像 |  |
| 云市场镜像 | 云市场镜像中的镜像由镜像服务商 ISV 提供，如果您使用云市场镜像的付费镜像创建实例时，除操作系统许可证的费用外，会额外收取软件应用许可证费用。详细费用以云市场镜像购买页面为准。 |
## 计费方式
ECS镜像的软件许可证费用的计费时长与实例规格的计费时长保持一致。根据实例的不同计费方式，镜像软件许可证费用在ECS实例上的计费方式如下表所示。
| 计费规则 | 包年包月 | 按量付费 |
| --- | --- | --- |
| 实例计费方式 | 包年包月 | 按量付费、抢占式实例 |
| 计费时长 | 计费时长默认为购买时长，若中途退订则计费时长为从使用付费镜像的包年包月实例创建完成开始计费，到实例释放时结束计费。 | 按秒计量计费时长，从使用付费镜像的实例创建完成开始计费，到实例释放或者更换为其他操作系统时结束计费。 |
## 操作系统许可证价格
### Windows
在中国香港及海外地域使用Windows Server操作系统，需支付操作系统许可证费用，具体费用以创建实例时显示的信息为准。
### Red Hat
Red Hat镜像按照使用镜像的实例的vCPU核数，阶梯区分每vCPU的费用单价，并按区间单核单价、具体vCPU核数及使用时长计算价格。计费公式如下：
不同计费方式下按vCPU核数的区间单核单价如下所示：
| 镜像种类 | vCPU 核数 | 按量付费单价 （元/vCPU/小时） | 包年包月按月单价 （元/vCPU/月） | 包年包月按年单价 （元/vCPU/年） |
| --- | --- | --- | --- | --- |
| Red Hat Enterprise Linux（RHEL） | 1 vCPU~8 vCPU | 0.1041 | 70.43 | 732.48 |
| 9 vCPU~127 vCPU | 0.0781 | 52.82 | 549.36 |  |
| 128 vCPU 及以上 | 0.0694 | 45.78 | 476.11 |  |
| Red Hat Enterprise Linux for SAP with HA and US（RHEL for SAP） | 1 vCPU~8 vCPU | 0.1619 | 105.61 | 1098.38 |
| 9 vCPU~127 vCPU | 0.1169 | 79.21 | 823.78 |  |
| 128 vCPU 及以上 | 0.1080 | 68.65 | 713.94 |  |
说明
阿里云上Red Hat相关订阅价格已于2024年07月31日随红帽价格模型调整而更新，包括RHEL和RHEL for SAP。操作系统订阅价格变更之后，您拥有的基于RHEL或者RHEL for SAP的ECS实例的费用将发生变化。请参见[阿里云上](https://help.aliyun.com/noticelist/articleid/1073610503.html)[Red Hat](https://help.aliyun.com/noticelist/articleid/1073610503.html)[产品订阅价格变更公告](https://help.aliyun.com/noticelist/articleid/1073610503.html)。
2024年06月30日后，RHEL7将进入到延长生命（Extended Life）阶段，建议您将RHEL 7升级到RHEL 8，如果您当前必须保留在RHEL 7版本，您可以购买RHEL 7 ELS Add-on订阅以持续获得安全更新和错误修复，请您[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)咨询购买。更多信息及RHEL 7 ELS Add-on订阅价格，请参见[Red Hat Enterprise Linux](user-guide/actions-to-take-when-red-hat-7-enters-the-extended-life-phase.md)[操作系统](user-guide/actions-to-take-when-red-hat-7-enters-the-extended-life-phase.md)。
### SUSE
SUSE镜像按照使用镜像的实例的vCPU核数，阶梯区分费用单价，与Red Hat操作系统不同，SUSE仅按vCPU核数区分时长单价，具体计费公式如下：
不同计费方式下按vCPU核数的区间单价如下所示：
| 镜像种类 | vCPU 核数 | 按量付费单价 （元/小时） | 包年包月按月单价 （元/月） | 包年包月按年单价 （元/年） |
| --- | --- | --- | --- | --- |
| SUSE Linux Enterprise Server | 1 vCPU~2 vCPU | 0.41 | 159.00 | 1529.00 |
| 3 vCPU~4 vCPU | 0.82 | 326.00 | 3,065.00 |  |
| 5 vCPU 及以上 | 0.99 | 381.00 | 3,670.00 |  |
| SUSE Linux Enterprise Server for SAP | 1 vCPU~4 vCPU | 2.54 | 1,221.00 | 12,459.00 |
| 5 vCPU 及以上 | 3.06 | 1,471.00 | 15,000.00 |  |
### Alibaba Cloud Linux Pro
[Alibaba Cloud Linux Pro](https://help.aliyun.com/zh/alinux/product-overview/what-is-alibaba-cloud-linux-pro)是Alibaba Cloud Linux 的商业版付费镜像，当您创建ECS实例选用该镜像时，计价公式如下：
不同计费方式下单价如下所示：
| 镜像种类 | 按量付费单价 （元/小时） | 包年包月按月单价 （元/月） |
| --- | --- | --- |
| Alibaba Cloud Linux Pro | 0.5 | 240.00 |
## 计费示例
假设您使用Red Hat Enterprise Linux（RHEL）公共镜像创建了一台32vCPU的ECS实例，则在采用包年包月购买和按量付费方式使用24小时、3个月及1年情况下，镜像软件许可证的费用计算如下：
说明
价格仅为示例，具体价格请以页面显示的价格为准。
首先根据[操作系统许可证价格](images.md)表格查询镜像单价，一台32vCPU的ECS实例的该镜像的计费价格为：
| vCPU 核数 | 按量付费单价 （元/vCPU/小时） | 包年包月按月单价 （元/vCPU/月） | 包年包月按年单价 （元/vCPU/年） |
| --- | --- | --- | --- |
| 9 vCPU~127 vCPU | 0.0781 | 52.82 | 549.36 |
根据计费公示，计算价格如下表所示：
| 使用/购买时长 | 包年包月 | 按量付费 |
| --- | --- | --- |
| 24 小时 | 包年包月条件下实例和镜像费用均为预付费。由于包年包月实例最短购买时长为 一周 ，因此不存在该场景的收费。 | 使用 24 小时的费用= 0.0781 元/vCPU/时*32 vCPU*24 小时 =59.9808‬元 |
| 3 个月（91 天） | 购买 3 个月的费用为 52.82 元/vCPU/月*32 vCPU *3 个月= 5070.72 元 | 使用 91 天的费用= 0.0781 元/vCPU/小时*32 vCPU*2184 小时= 5,446.7328 元 |
| 1 年（365 天） | 购买 1 年的费用为 549.36 元/vCPU/年*32 vCPU*1 年= 17579.52 元 | 使用 365 天的费用= 0.0781 元/vCPU/时*32 vCPU*24 小时*365 天= 21,892.992 元 |
## 镜像功能关联操作计费
除镜像本身的软件许可证费用外，使用自定义镜像的功能可能会产生额外快照存储费用，OSS存储、流量及请求费用。快照默认采用按量付费，更多信息，请参见[快照计费](snapshots-1.md)。OSS的计费详情，请参见[计费概述](../../oss/documents/billing-overview.md)。
使用实例创建自定义镜像时，系统默认会创建一份快照，保留自定义镜像会产生快照存储费用。
复制自定义镜像时，复制生成的自定义镜像会产生快照存储费用。
将本地镜像导入阿里云生成自定义镜像时，系统会默认创建一份快照，产生快照存储费用。同时也会产生OSS存储费用、流量费用和访问OSS API的请求费用。
导出镜像文件会存储到OSS Bucket中，会产生OSS存储费用、流量费用和访问OSS API的请求费用。
## 成本优化方案
如果您想针对镜像的操作系统许可证费用进行成本优化，您可以选择开启节省停机模式，或者购买阿里云权益折扣类商品进行抵扣。
### 节省停机模式
适用于按量付费实例或抢占式实例，通过节省停机模式停止实例，可以在保留服务器的数据和配置信息的同时，节省部分资源使用成本。开启节省停机模式停止实例后，不再收取镜像软件许可证费用，云盘（系统盘和数据盘）、弹性公网IP、快照等资源继续收费。开启节省停机模式的详细计费规则，请参见[节省停机模式](user-guide/economical-mode.md)。
### 使用折扣权益
若您在中国香港及海外地域创建实例时使用了阿里云公共镜像中Windows Server操作系统，可以通过以下折扣权益抵扣按量付费计费方式创建的实例产生的操作系统许可证费用：
开通节省计划：通过承诺一定周期内的每小时消费金额，换取更低折扣购买使用资源。节省计划的详细介绍与购买方式，请参见[什么是节省计划](savings-plans.md)。
预留实例券：您可以在对应地域购买Windows类型的预留实例券，抵扣公共镜像中镜像软件许可证费用产生的账单。
## 到期影响及欠费说明
包年包月与按量付费方式使用的镜像在到期和欠费时的处理方式不同。具体如下：
包年包月：若未启用实例的自动续费，到期后镜像将不可用，详细说明请参见[包年包月](subscription.md)。
按量付费：账户欠费时，可能影响镜像的可用状态，详细说明请参见[欠费说明](overdue-payments.md)。
## 账单查询
查询计费项的明细操作请参见[账单查询](view-billing-details.md)。
## 退订说明
退订仅针对预付费（包年包月、资源包等）商品。当您想终止服务时，阿里云将基于退订规则退还资源并退还相应的款项。
退订包年包月实例及实例关联资源并了解退款相关事项，请参见[退订说明](refund-instructions.md)。
云市场镜像的退订规则及退款金额说明，请参见[云市场镜像退款说明](https://help.aliyun.com/zh/marketplace/user-guide/refund-rules)。
## 停止计费
场景1：您已经通过自定义镜像创建实例，并且不再需要使用该自定义镜像，则可以删除该自定义镜像及其关联快照，以节约费用。
场景2：若您使用付费镜像创建了ECS实例，期望节约镜像成本，则可以考虑通过更换操作系统将付费镜像更换为免费镜像。镜像的许可证费用与ECS实例生命周期一致，当您释放ECS后，镜像也停止计费。
## 相关文档
关于镜像使用过程计费的常见问题及解答，请参见[镜像费用问题](faq-about-image-fees.md)。
关于镜像类型及使用的更多介绍，请参见[镜像概述](user-guide/image-overview.md)。
使用云服务器ECS时，您需要关注镜像运行的操作系统在官方平台公布的生命周期计划，这有助于您及时更新至稳定的软件版本，详细说明请参见[操作系统生命周期概述](user-guide/eol-overview.md)。
当操作系统因生命周期、第三方支持、开源计划演进等原因停止技术支持后，如果您的操作系统后续想得到维护和技术支持且同时需要保留ECS实例系统盘数据时，可以将操作系统迁移或升级至稳定的软件版本。详细操作请参见[操作系统迁移](user-guide/migrate-the-operating-system-of-an-ecs-instance.md)。
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
