# ECS快照计费规则、计费示例及欠费影响-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/snapshots-1

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

# 快照计费

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云根据使用的快照类型以及对应的快照容量，按每个地域单独结算快照费用。本文介绍ECS快照的计费规则、计费周期以及如何停止快照计费等。

## 计费规则

### 计费项说明

- 

在初次使用快照前，需要先开通快照服务，[开通快照](products/ecs/documents/user-guide/activate-ecs-snapshot.md)不收费，创建快照后才开始计费。创建的[手动快照](products/ecs/documents/user-guide/create-a-snapshot.md)和[自动快照策略](products/ecs/documents/user-guide/automatically-create-snapshots.md)默认是标准快照，阿里云在各地域会根据标准快照容量和使用时长收取标准快照存储费。

- 

在使用标准快照过程中如果需要将标准快照归档以降低快照存储成本，标准快照会转换为[归档快照](products/ecs/documents/user-guide/archive-snapshots.md)，阿里云在各地域会根据归档快照容量和使用时长收取归档快照存储费。

重要

归档快照的最短保留时间为60天（1,440小时），如果在60天内提前删除归档快照，除了需要支付归档快照存储费，还需支付归档快照不足规定时长费。

- 

使用[复制快照](products/ecs/documents/user-guide/copy-a-snapshot.md)功能将标准快照复制到目标地域实现跨地域数据备份，在目标地域会产生复制快照流量费和标准快照存储费。归档快照不支持复制。

- 

使用[（公测）快照预热](products/ecs/documents/user-guide/public-preview-snapshot-prefetch.md)功能将数据先从对象存储OSS中加载，以消除首次数据访问时的延迟，需要收取快照预热费。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 计费项 | 计费公式 | 计费方式 |
| --- | --- | --- |
| 标准快照存储费 | 标准快照单价 ：访问 [ECS](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) [定价详情页](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) ，在 快照 页签下查看各地域的标准快照单价。 标准快照容量 ：单位为 GB。查看快照容量的方法，请参见 [查看快照容量](products/ecs/documents/user-guide/view-the-snapshot-size.md) 。 计费时长 ：快照创建完成后开始计费，直至删除标准快照后停止计费。 | 仅支持 [按量付费](products/ecs/documents/pay-as-you-go-1.md) 。按小时计费。不足 1 小时，按 1 小时计算。 支持购买预付费的资源包抵扣标准快照的存储费用账单，节约快照使用成本。 可以购买 [OSS](products/ecs/documents/oss-storage-bag.md) [资源包（标准-本地冗余存储包）](products/ecs/documents/oss-storage-bag.md) 或 [存储容量单位包](products/ecs/documents/storage-capacity-units-1.md) [SCU](products/ecs/documents/storage-capacity-units-1.md) 抵扣标准快照的存储费用。 抵扣规则：购买后，在资源包有效期内每小时优先自动使用资源包抵扣同地域内标准快照存储费用，超出部分自动采用按量付费。 抵扣顺序： 标准-本地冗余存储包 >存储容量单位包 SCU>按量付费。 抵扣示例： [OSS](products/ecs/documents/oss-storage-bag.md) [资源包抵扣示例](products/ecs/documents/oss-storage-bag.md) 、 [存储容量单位包抵扣示例](products/ecs/documents/storage-capacity-units-1.md) 。 |
| 归档快照存储费 | 归档快照单价 ：访问 [ECS](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) [定价详情页](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) ，在 快照 页签下查看各地域的归档快照单价。 归档快照容量 ：单位为 GB。查看快照容量的方法，请参见 [查看快照容量](products/ecs/documents/user-guide/view-the-snapshot-size.md) 。 计费时长 ：快照归档后开始计费，直至删除归档快照后停止计费。 | 仅支持 [按量付费](products/ecs/documents/pay-as-you-go-1.md) ，不支持购买资源包抵扣。按小时计费。不足 1 小时，按 1 小时计算。 |
| 归档快照不足规定时长费 | 归档快照单价 ：访问 [ECS](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) [定价详情页](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) ，在 快照 页签下查看各地域的归档快照单价。 被删除归档快照容量 ：单位为 GB。查看快照容量的方法，请参见 [查看快照容量](products/ecs/documents/user-guide/view-the-snapshot-size.md) 。 剩余时长 ：1,440（60 天）-已存储时长，单位为小时。 | 仅支持 [按量付费](products/ecs/documents/pay-as-you-go-1.md) ，不支持购买资源包抵扣。按小时计费。不足 1 小时，按 1 小时计算。 删除归档快照后，当前小时仍会产生计费，并在下一个小时产生一条消费明细。 |
| 复制快照流量费 | 快照复制单价 ：访问 [ECS](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) [定价详情页](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs) ，在 快照 页签下查看各地域的快照单价。 快照容量 ：与复制类型相关，更多信息，可查看 [费用说明](products/ecs/documents/user-guide/copy-a-snapshot.md) 。 重要 如果复制快照选择加密复制，在使用默认密钥过程中不会产生密钥费用，其余情况可查看 [KMS](products/kms/documents/key-management-service/product-overview/kms-billing.md) [产品计费](products/kms/documents/key-management-service/product-overview/kms-billing.md) ，了解详细费用说明。 | 仅支持 [按量付费](products/ecs/documents/pay-as-you-go-1.md) ，不支持购买资源包抵扣。按小时计费，不足 1 小时，按 1 小时计算。 |
| 快照预热费 | 单个地域的快照预热总费用是该地域下所有开启预热功能的快照在各个可用区产生的费用总和。单个可用区内的费用计算公式如下： 快照容量 ：全量快照容量，单位为 GB。 访问 [ECS](https://ecs.console.aliyun.com/snapshot) [控制台-快照](https://ecs.console.aliyun.com/snapshot) ，通过目标快照中的 全量快照大小 列获取。 时长 ：开启预热功能的保留时间，单位为小时。 并发创盘个数 ：预热配置的并发创盘个数。 快照预热单价 ：访问 [价格计算器](https://www.aliyun.com/price/product#/disk/detail/disk) ，在 快照服务价格 页签下查看各地域的快照预热单价。 | 仅支持 [按量付费](products/ecs/documents/pay-as-you-go-1.md) ，不支持购买资源包抵扣。按秒计费，最低收费 1 小时。 |


### 计费示例

本示例价格仅为示例，具体价格以[ECS](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs)[定价详情页](https://www.aliyun.com/price/detail?spm=5176.29987058.nav-v2-dropdown-menu-dropdown.nav-v2-dropdown-menu-4.d_main_0&scm=20140722.M_10944837._.V_1&saleProductCode=ecs)为准。

示例1：创建标准快照计费示例

在某地域创建了标准快照，则该地域会产生标准快照存储费。

假设在杭州地域有100 GB的标准快照，杭州地域的标准快照单价为0.12元/GB/月。标准快照存储费=标准快照单价*标准快照容量*计费时长。则杭州地域产生的标准快照费用为：

- 

1小时费用：0.016元，计算方式为（0.12 元/GB/月）/30天/24小时*100 GB*1小时

- 

1天费用：0.4元，计算方式为（0.016元*24小时）

- 

1个月费用：12元，计算方式为（0.12元/GB/月*100 GB*1月）

示例2：归档快照计费示例

在某地域将标准快照进行归档，则该地域会产生归档快照存储费。

假设在杭州地域将标准快照B（容量100 GB）进行归档，杭州地域的归档快照单价为0.06元/GB/月。归档快照存储费=归档快照单价*归档快照容量*计费时长。则杭州地域产生的归档快照费用为：

- 

1小时费用：0.0083元，计算方式为（0.06 元/GB/月）/30天/24小时*100 GB*1小时

- 

1天费用：0.1992‬元，计算方式为（0.0083元*24小时）

- 

1个月费用：6元，计算方式为（0.06元/GB/月*100 GB*1月）

示例3：归档快照不足规定时长计费示例

假设在杭州地域将快照B（容量100 GB）进行归档，使用了30天后删除了该归档快照，则还需要支付剩余30天的存储费用。归档快照不足规定时长费用=归档快照单价*归档快照容量*剩余时长，杭州地域的归档快照单价为0.06元/GB/月，剩余时长为30天（60天-30天）。

则杭州地域产生的归档快照不足规定时长费用为：（ 0.06 元/GB/月）/30天/24小时*100 GB*（30*24）小时=6元

示例4：复制快照计费示例

在某地域创建了标准快照，且将该快照复制到其他地域，则在当前地域会产生标准快照存储费，在目标地域会产生快照复制流量费和标准快照存储费。

假设在杭州地域有100 GB的标准快照，将该快照复制到青岛地域。复制完成后青岛地域会生成一份100 GB的标准快照。杭州地域向青岛地域的快照复制服务单价为0.5元/GB，青岛地域的标准快照单价为0.12元/GB/月，计费时长1个月。

则青岛地域产生的费用为：

- 

复制快照流量费：50元（快照复制单价 * 快照容量=0.5元/GB*100 GB）。

- 

标准快照存储费：12元（标准快照单价 * 快照容量 * 计费时长=0.12元/GB/月*100 GB*1月）。

- 

总费用：62元（复制快照流量费+标准快照存储费）。

杭州地域的标准快照存储费为：12元（标准快照单价 * 快照容量 * 计费时长=0.12元/GB/月*100 GB*1月）。

示例5：快照预热计费示例

快照预热按照快照的全量大小计费，假设呼和浩特地域存在标准快照A（全量快照大小 100GB）和标准快照B（全量快照大小120 GB）， 对两个标准快照在单可用区A预热，设置的预热保留时间均为2小时，并发创盘个数为100个。呼和浩特地域的快照预热单价为0.0000138889元/（GB*个*小时）。单可用区下预热费用 = 快照容量* 预热保留时长* 并发创盘个数 * 快照预热单价。则：

标准快照A的预热费用为：100 GB*2小时*100个*0.0000138889元/（GB*个*小时）= 0.277778元

标准快照B的预热费用为：120 GB*2小时*100个*0.0000138889元/（GB*个*小时）= 0.3333336元

## 计费周期

快照计费周期从快照创建时间点的所在整点开始计费，直至删除快照时间点的所在整点停止计费。创建快照操作请参见[手动创建单个快照](products/ecs/documents/user-guide/create-a-snapshot.md)，删除快照操作请参见[删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md)。

例如在2024年12月20日11:02:06创建快照，在2024年12月20日15:20:20删除快照，则该快照的计费周期为2024年12月20日11:00:00~2024年12月20日16:00:00，计费时长5小时。

说明

释放云盘不会影响快照的计费周期。如果自动快照关联的云盘开启了自动快照随云盘释放属性，释放云盘（手动释放云盘、云盘随实例释放或更换系统盘）时，会同步删除该云盘的自动快照并停止快照计费。更多信息，请参见[设置自动快照随云盘释放](products/ecs/documents/user-guide/enable-or-disable-an-automatic-snapshot-policy.md)。

## 欠费影响

如果阿里云账号发生欠费，对正在使用的快照会产生影响。具体说明，请参见[欠费说明](products/ecs/documents/overdue-payments.md)。

## 查看快照明细账单

重要

查看快照容量的方法，请参见[查看快照容量](products/ecs/documents/user-guide/view-the-snapshot-size.md)。

- 

登录[费用与成本](https://usercenter2.aliyun.com/home)控制台，在左侧导航栏，选择账单>账单详情，单击明细。

- 

商品名称选择云服务器ECS-快照，单击搜索。

## 节约快照使用成本

- 

建议购买[OSS](products/ecs/documents/oss-storage-bag.md)[资源包（标准-本地冗余存储包）](products/ecs/documents/oss-storage-bag.md)或[存储容量单位包](products/ecs/documents/storage-capacity-units-1.md)[SCU](products/ecs/documents/storage-capacity-units-1.md)抵扣标准快照的存储费用，资源包相比按量付费更划算，以便抵扣快照的按量付费账单。

- 

也可以通过删除不再使用的快照、取消不必要的自动快照策略、归档快照等方式[优化快照使用成本](products/ecs/documents/user-guide/reduce-snapshot-fees.md)。

## 停止快照计费

### 停止快照全部计费

开通快照服务后，无法关闭快照服务，可以按照以下场景停止快照计费。

重要

若在归档层保留时间内删除归档快照，除需支付归档快照存储费，还需支付归档快照不足规定时长费。

- 

手动删除目标快照。

- 

停止单个实例的快照计费：在当前地域下查看单个实例中所有云盘已创建的快照，包括手动快照和自动快照，然后手动[删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md)。

- 

停止当前阿里云账号的快照计费：快照按地域收费，只有删除全部地域下的快照，当前账号下才不会再产生快照费用，因此需切换地域查看并[删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md)。

- 

确保后续不再新增快照计费。

手动删除所有快照后，检查并[删除还在应用的自动快照策略](products/ecs/documents/user-guide/delete-an-automatic-snapshot-policy.md)，确保后续不再自动新增快照。

### 停止快照预热费

关闭快照预热功能、预热保留时长到期或账号欠费，预热功能都将关闭并停止计费。以关闭快照预热功能为例：

- 

访问[ECS](https://ecs.console.aliyun.com/snapshot)[控制台-快照](https://ecs.console.aliyun.com/snapshot)，在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在云盘快照页签中找到目标快照，在操作列中选择>管理快照预热。

- 

在快照预热页面，找到目标预热可用区，单击操作列中的关闭。预热状态会变为已关闭并停止计费。

## 常见问题

使用快照过程中其他常见问题，请参见[数据保护与恢复](products/ecs/documents/data-protection-and-recovery-faqs.md)。

[上一篇：公网带宽计费](products/ecs/documents/public-bandwidth.md)[下一篇：计费方式](products/ecs/documents/billing-methods.md)

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
