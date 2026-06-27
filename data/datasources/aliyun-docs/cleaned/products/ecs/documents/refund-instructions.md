# 退订退款规则影响与操作指南-云服务器ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/refund-instructions

# 退订说明
退订退款仅针对预付费（包年包月、资源包等）商品，当您想终止服务时，阿里云将基于退订规则回收资源并退还相应的款项。对于后付费（按量付费）商品，不涉及退款，您可以参照对应计费项的停止计费指引，直接在阿里云控制台通过释放、删除资源来停止计费。
## 退订流程
## 一、退订前须知
### 确认是否支持退订
ECS包年包月实例支持退订。若购买了ECS服务下的其他预付费商品，可以访问对应文档进行查询，了解是否支持退订。
不支持退订场景
后付费（即按量付费）商品不需要退订，若不需要继续使用，可备份数据后，将按量付费云产品停止并释放即可立即停止计费。
活动限制：实例资源“命中的活动不允许退订”导致不能退订。例如，尝试退订的某个实例资源正处于一个特定的促销活动或优惠计划中，而根据该活动的规定，参与该活动的资源不允许被中途退订。
资源过户：资源发生过户后无法进行退订。
关联云市场收费镜像：云产品关联云市场的收费镜像，无法进行退订。
存在未支付订单：实例下存在未支付订单无法进行退订。
如果您经过检查发现上述场景均不符合您的具体情况，或者按照相关产品的服务条款确认当前订购的商品支持退订，但不支持自助退订服务，可[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex?spm=5176.12818093.top-nav.ditem-sub.699816d04WNWdc)申请人工审核退订。
### 退订影响
费用结算：如果您选择中途退订某项服务，在满足退款条件的情况下，未使用的部分费用会按照阿里云的[退订规则说明](https://help.aliyun.com/zh/user-center/cancel-subscription/)进行退还。
数据处理：对于一些存储类的服务，退订后您的数据会被删除。因此，在正式退订之前，请确保已将所有重要信息备份。
服务停止：完成退订流程后，您所选择取消订阅的服务及其直接依赖的相关服务将立即停止运行。这意味着您将无法继续使用该服务提供的功能，直到重新订购为止。例如，以ACK容器服务和ECS云服务器为例，如果您退订了ECS，那么ACK将无法再使用ECS提供的计算资源和服务功能。
### 退订规则
在执行退订操作前，请务必先了解退订策略和退订金额计算方式。当您申请退订包年包月ECS实例时，退订资源为ECS实例及挂载并设置随实例释放的ECS资源，具体包括：包年包月ECS实例、包年包月系统盘、包年包月数据盘、固定公网带宽和云市场镜像。部分资源如云市场镜像、带宽等资源支持单独退订，退订条件或场景请参见下表，退款金额的计算方式请参见[退订规则说明](https://help.aliyun.com/zh/user-center/cancel-subscription/)。
| 资源 | 退订规则 |
| --- | --- |
| 包年包月 ECS 实例 | 五天无理由全额退订： ECS 支持五天无理由全额退订，在包年包月新购五天内，可申请无理由全额退款。 每个用户每个产品在一个自然年内（1 月 1 日-12 月 31 日），可五天无理由全额退订一台实例，若账户持有人有相关的安全风险或违规行为，阿里云有权否决退订申请。不支持退款的特殊情况，请参见 [五天无理由全额退订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#p-22w-fce-nu4) 。 说明 五天无理由全额退订场景中，包年包月 ECS 实例和资源包、预留实例券等共享一年一台的额度。 |
| （实例到期前）非全额退订： 不满足五天无理由和五天未使用全额退订规则的预付费云产品退货退款，可以自助申请非全额退订。 不支持退款的特殊情况，请参见 [非全额退订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#p-1qo-3ce-m7z) 。 |  |
| （未生效）退订续费周期 ：退订续费周期又称退订未生效续费或退订未生效续订。资源创建成功后，若资源已进行续费操作，可选择单独退订未生效的续费订单。更多信息，请参见 [退订未生效续订规则](https://help.aliyun.com/zh/user-center/cancel-subscription/#8303bfedb3dfz) 。 |  |
| 云盘 | 退订实例时，实例所绑定的系统盘或数据盘会随实例按规则退订。 包年包月的系统盘 不支持单独退订，实例释放或退订后，系统盘上的数据会被全部释放，无法找回。 包年包月的数据盘 不支持单独退订，若您想保留实例的同时不再使用该数据盘，您可以将数据盘的计费方式转换后，再将该云盘从 ECS 实例上卸载，并手动释放该云盘，操作方式请参见 [转换云盘计费方式](switch-the-billing-method-of-a-disk.md) 。 重要 针对按量付费的数据盘，您可以直接将云盘从 ECS 实例上卸载，然后手动释放云盘。释放后，存储在云盘上的数据会被全部释放且无法找回，云盘会停止计费。如果只卸载但未释放云盘，云盘仍将继续扣费。 云盘释放后，云盘中的数据无法找回。建议您在释放云盘之前，为云盘 [手动创建单个快照](user-guide/create-a-snapshot.md) 进行数据备份。 |
| 镜像 | 退订实例时镜像商品会随实例按规则退订，单独退订镜像商品的规则如下： 阿里云公共镜像： Red Hat Enterprise Linux 和 SUSE Linux Enterprise Server 来自云市场镜像，不支持退款。当您在退订选用该类镜像的包年包月 ECS 实例时，镜像费用不支持退款。 云市场镜像： 支付完成后 5 天（担保期）内，镜像订单可单独申请无理由全额退款。不支持 5 天（担保期）内退款的特殊情况，请参见 [云市场商品退款说明](https://help.aliyun.com/zh/marketplace/user-guide/refund-rules) 。 支付完成后超出 5 天（担保期）则不支持无理由全额退款。 支持 5 天无理由退款的镜像商品，如果镜像和 ECS 一起购买的续费订单暂未生效，在退 ECS 续费订单的同时可同步退订镜像订单，无需进行更换系统盘的操作。 |
| 带宽 | 内网带宽退订： 内网带宽是指同一地域同一专有网络内的云服务器 ECS 实例之间传输的内网带宽流量，其大小跟实例规格有关，用户无法直接修改实例的内网带宽。 同地域内网带宽 ：免费，无需退订。 跨地域内网带宽 ：遵循对应云产品退订说明。您通过云企业网、VPC 对等连接等方式实现的跨地域的 ECS 实例内网互通，请遵循对应云产品的退订说明。 公网带宽退订 ：公网带宽是指 ECS 实例到公网之间的网络带宽流量。ECS 可以通过固定公网 IP、弹性公网 IP（EIP）、公网 NAT 网关这三种方式访问公网。不同的公网带宽方式支持的计费方式不同，退订方式也不相同。 |
| 节省计划 | 默认不支持退订，如有特殊情况不再使用已购买的节省计划， 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 协商退款。 |
| 预留实例券 | 支持五天无理由退订，若不满足五天无理由退订条件，请 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请退订。 |
| 弹性保障 | 普通弹性保障支持五天无理由退订，若不满足五天无理由退订条件，可以自助申请非全额退订。非全额退订支持按照生效时间/总保障周期的比例退订，无惩罚系数。 分时弹性保障（带有间歇性重复规则的弹性保障）不支持退订。 |
| 存储容量单位包 SCU | 支持五天无理由退订，若不满足五天无理由退订条件，请 请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 |
## 二、发起退订
针对已生效订单，可以参照以下流程发起自助退订。
针对未生效订单及旧版（橙色版）费用与成本中心，请参见[发起退订](https://help.aliyun.com/zh/user-center/initiate-unsubscribe#2f836ff974t0n)进行退订。
### 退订包年包月ECS实例
退订操作
准备工作。
在退订资源前，请务必确认即将退订的ECS实例内没有您所需的数据，或需要的数据已完成备份或迁移。
您可以[使用实例创建自定义镜像](user-guide/create-a-custom-image-from-an-instance.md)备份数据。
您可以把ECS实例内的数据迁移至另一台新购的ECS实例，操作参见[跨账号和同账号](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)[ECS](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)[实例间迁移](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)。
申请自助退订。
在[资源退订](https://billing-cost.console.aliyun.com/refund/)页面的退订资源页签下，单击选择普通云资源页签。
根据商品名称、实例ID及订单时间筛选，找到并勾选需退订的资源后，单击退订资源或批量退订资源发起退订。
仅非全额退订类型的资源支持批量退订，单次最多可操作50个实例。退订后资源保留说明
为避免误操作导致数据丢失，包年包月实例退款后进入退款后过期状态，相关资源会保留一定时间。若误操作退订，可在实例资源释放前，尽快前往访问[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)，手动续费已退订实例。
重要
以下期限是最长保留时间，实际释放时间可能提前，建议您退订前做好数据备份或迁移。已操作退订的ECS实例续费恢复后，实例仍可能会产生数据丢失、固定公网IP变动等影响。
vCPU、内存、固定公网IP在退款后24小时内释放。
云盘在退款后15天内释放。
### 退订公网带宽
固定公网带宽退订
可以通过更改带宽，将带宽的固定带宽值调整为0 Mbit/s，实现固定公网IP的释放，进而实现包年包月实例带宽的退订。
说明
关于固定公网带宽计费说明，请参见[公网带宽计费](public-bandwidth.md)。
如果当前固定公网带宽的计费方式不满足您的需求，可以[转换固定公网](user-guide/change-the-billing-method-for-network-usage-1.md)[IP](user-guide/change-the-billing-method-for-network-usage-1.md)[的带宽计费方式](user-guide/change-the-billing-method-for-network-usage-1.md)。
弹性公网带宽退订
说明
如果当前EIP的计费方式不满足您的需求，可以[转换](https://help.aliyun.com/zh/eip/switch-billing-methods)[EIP](https://help.aliyun.com/zh/eip/switch-billing-methods)[计费方式](https://help.aliyun.com/zh/eip/switch-billing-methods)。
关于弹性公网IP计费的更多问题，请参见[计费](https://help.aliyun.com/zh/eip/support/billing-faq)[FAQ](https://help.aliyun.com/zh/eip/support/billing-faq)。
查询EIP账单详情，请参见[账单查询](https://help.aliyun.com/zh/eip/product-overview/view-your-bills)。
在[资源退订](https://billing-cost.console.aliyun.com/refund/)页面的退订资源页签下，单击选择普通云资源页签。
您可根据商品名称、实例ID及订单时间筛选，找到并勾选需退订的资源后，单击退订资源或批量退订资源发起退订。
公网NAT网关带宽退订
公网NAT网关通过EIP来提供公网访问的能力，如果不再使用公网NAT网关，您需要分别删除公网NAT网关实例以及退订EIP。
删除公网NAT网关实例：实例删除后停止计费。具体操作，请参见[管理公网](https://help.aliyun.com/zh/nat-gateway/user-guide/use-internet-nat-gateway-for-public-network-access#26f6e36dafgev)[NAT](https://help.aliyun.com/zh/nat-gateway/user-guide/use-internet-nat-gateway-for-public-network-access#26f6e36dafgev)[网关实例](https://help.aliyun.com/zh/nat-gateway/user-guide/use-internet-nat-gateway-for-public-network-access#26f6e36dafgev)中的删除公网NAT网关。
说明
公网NAT网关计费，请参见[NAT 网关计费](https://help.aliyun.com/zh/nat-gateway/nat-gateway-billing)。
查询NAT网关账单和用量明细，请参见[查询](https://help.aliyun.com/zh/nat-gateway/product-overview/view-bills-and-usage-details)[NAT](https://help.aliyun.com/zh/nat-gateway/product-overview/view-bills-and-usage-details)[网关账单和用量明细](https://help.aliyun.com/zh/nat-gateway/product-overview/view-bills-and-usage-details)。
退订EIP：请参见[弹性公网带宽退订](refund-instructions.md)。
## 三、查看退订明细
### 查看退款到账日期
如果产品退订成功，款项一般在2-3个工作日内到账。
### 查看退订资金流向
可参见[查看退还资金去向](https://help.aliyun.com/zh/user-center/initiate-unsubscribe#e9d04e8fa0uxp)进行查询，退款后的资金流向、到账时间等说明，请参见[退订资金流向](https://help.aliyun.com/zh/user-center/refund-flow#topic-2059665)。
重要
退款仅指用户以现金或储值卡方式支付的订单款项，用户通过代金券、优惠券抵扣的部分不支持退回。
## 退订常见问题
[为什么我不能申请退订？](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#60a265a585law)
[能否使用](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#c54e9de1c0iso)[API](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#c54e9de1c0iso)[退订包年包月资源？](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#c54e9de1c0iso)
[为什么我申请退订时显示的退款金额为](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#a6e3dfc292vvw)[0？](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription#a6e3dfc292vvw)
[阿里云账号注销了还能恢复](billing-and-subscription-management-faqs.md)[ECS](billing-and-subscription-management-faqs.md)[的数据么？](billing-and-subscription-management-faqs.md)
其他[退订常见问题](https://help.aliyun.com/zh/user-center/support/faq-about-unsubscription)。
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
