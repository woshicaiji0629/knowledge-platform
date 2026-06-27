# 更换ECS实例的操作系统（更换系统盘）-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/replace-the-operating-system-of-an-instance

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

# 更换操作系统（更换系统盘）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当您需要全新的操作系统环境时，可通过更换系统盘实现，该方式支持更丰富的操作系统选项，但需要在新系统上完全重新部署业务环境。若希望在保留现有系统盘数据的基础上更换操作系统，可选择[操作系统迁移](products/ecs/documents/user-guide/migrate-the-operating-system-of-an-ecs-instance.md)。

重要

更换系统盘将导致原系统盘被释放产生业务中断，盘上所有数据将被永久删除且无法恢复。操作前，请务必[手动创建单个快照](products/ecs/documents/user-guide/create-a-snapshot.md)备份数据。

## 变更影响

更换操作系统是高风险操作，请务必了解以下事项：

- 

系统盘

- 

数据清除：原系统盘被释放，所有数据和分区信息将被永久清除。

- 

ID 变更：系统会分配一块新的系统盘，因此系统盘 ID 会发生变更。

- 

属性不变：云盘类型、实例 IP 地址和弹性网卡 MAC 地址保持不变。

- 

数据盘

- 

同类型系统更换：在 Windows 系统间或 Linux 系统间更换，数据盘不受影响，更换后重新挂载即可。

- 

跨类型系统更换：在 Windows 与 Linux 系统间更换，新系统无法直接识别原数据盘的文件系统。需要参见[后续任务](products/ecs/documents/user-guide/replace-the-operating-system-of-an-instance.md)，重新初始化数据盘或安装特定软件才能读取数据。

- 

快照

- 

原系统盘的快照无法用于回滚新系统盘。

- 

手动创建的快照会被保留。

- 

自动快照的保留策略取决于是否开启自动快照随云盘释放功能。

- 

开启：自动快照将被删除。

- 

未开启：自动快照将按其生命周期到期后释放。

- 

原系统盘的自动快照策略在新系统盘上会失效，需要重新设置。

- 

费用

更换操作系统功能本身免费，以下两种情况会产生新费用：

- 

付费镜像：如果选择的镜像是付费镜像，将按镜像价格收费。

- 

系统盘扩容：如果在更换时增加了系统盘的容量，将对新增容量收费。

## 限制说明

- 

地域支持说明：仅中国内地地域支持 Windows 和 Linux 系统间的互相更换，其他地域仅支持同类型系统间的更换（如Linux换Linux，Windows换Windows）。

- 

主机名：在跨类型系统更换前，需确保实例主机名（Hostname）符合目标操作系统的规范。例如，Windows 系统的主机名为2～15 个字符。

- 

非 I/O 优化实例：在实例详情页面下方其他信息区域可查看实例类型，若为非I/O优化，则该实例不支持在控制台更换为 Windows 系统，仅支持通过调用 API[ReplaceSystemDisk](products/ecs/documents/api-replacesystemdisk.md)更换为下列Windows Server公共镜像。

Windows Server公共镜像

- 

Windows Server 2012 R2数据中心版中文：win2012r2_64_dtc_17196_zh-cn_40G_alibase_20170915.vhd

- 

Windows Server 2012 R2数据中心版英文：win2012r2_64_dtc_17196_en-us_40G_alibase_20170915.vhd

- 

Windows Server 2008 R2企业版中文：win2008r2_64_ent_sp1_zh-cn_40G_alibase_20170915.vhd

- 

Windows Server 2008 R2企业版英文：win2008r2_64_ent_sp1_en-us_40G_alibase_20170915.vhd

- 

目标系统盘容量要求：当更换为Windows操作系统时，系统盘需预留至少1GiB空间，否则更换后实例将无法启动。

- 

镜像限制说明：Alibaba Cloud Linux 3 Pro实例，暂不支持更换为其他操作系统。

## 操作步骤

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面顶部选择目标资源所在资源组和地域。

- 

在实例列表页面，单击目标实例 ID 进入详情页。在页面右上角，选择全部操作>更换操作系统。

- 

设置操作系统更换方式。

- 

选择更换方式设置为更换系统盘，系统将自动执行前置检查，如果检查失败，请根据页面提示修复问题后重试。

- 

仔细阅读注意事项，选中我已知晓以上风险，并确认继续操作，之后单击继续更换操作系统。

- 

配置新操作系统及实例信息。

- 

选择镜像：选择当前实例规格支持的镜像类型（公共镜像、自定义镜像等）和具体的镜像版本。

- 

安全设置：

| 安全设置选项 | 说明 |
| --- | --- |
| 密钥对 | （仅限 Linux 实例） 选择一个已有密钥对。如果无可用密钥对，可单击 创建密钥对 新建一个。 |
| 使用镜像预设密码 | （仅限自定义/共享镜像） 使用镜像中已设置的密码作为登录凭证。请确保所选镜像已配置密码。 |
| 自定义密码 | 为新系统设置登录用户名和密码。Linux 系统用户名可选 root 或 ecs-user （推荐），Windows 系统默认为 administrator 。 |
| 更换后设置 | 跳过登录凭证设置，更换成功后，需 [绑定](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) [SSH](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) [密钥对](products/ecs/documents/user-guide/bind-an-ssh-key-pair-to-an-instance.md) 或者 [重置实例登录密码](products/ecs/documents/user-guide/reset-the-logon-password-of-an-instance.md) 后登录实例。 |


- 

系统盘（可选）：可根据需要扩容系统盘容量或启用[加密云盘](products/ecs/documents/user-guide/encryption-overview.md)功能。系统盘类型不可更改。

扩容系统盘的费用说明请参考[块存储计费](products/ecs/documents/block-storage-devices.md)。

- 

确认配置和费用后，更换操作系统。

- 

（条件必选）若实例为运行中，请停止实例。

- 

包年包月：若在更换操作系统时扩容了系统盘，需按照页面提示支付订单，支付后更换操作系统流程才会正常进行。

- 

按量付费：停止时建议选择普通停机模式。若使用节省停机模式，更换操作系统后实例可能因库存不足导致启动失败。

更换过程约需要10分钟，实例将会自动重启。完成后，实例状态将变为运行中，且操作系统会更新为新选择的系统。

## 后续任务

- 

（条件必选）处理数据盘

- 

同类型系统更换：如果更换前后的系统均为 Linux，且存在数据盘。更换后需登录实例，[挂载数据盘文件系统](products/ecs/documents/user-guide/initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。

- 

跨类型系统更换：

- 

Linux 更换为 Windows：Windows 默认无法识别 ext4、XFS 等文件系统格式。可使用Ext2Fsd等第三方工具读取数据盘，或在无重要数据的情况下[重新初始化数据盘](products/ecs/documents/user-guide/re-initialize-a-data-disk.md)。

- 

Windows 更换为 Linux：Linux 默认无法识别 NTFS 文件系统格式。可[安装 ntfs-3g 工具挂载文件系统](products/ecs/documents/user-guide/how-do-i-move-an-ntfs-disk-between-a-linux-instance-and-a-windows-instance.md)，或在无重要数据的情况下[重新初始化数据盘](products/ecs/documents/user-guide/re-initialize-a-data-disk.md)。

- 

（可选）恢复原系统盘数据如果需要恢复原系统盘的数据，可[通过原系统盘快照恢复系统盘中的数据](products/ecs/documents/user-guide/use-a-snapshot-of-the-original-system-disk-to-restore-data-after-the-operating-system-of-an-ecs-instance-is-replaced.md)，使用更换前创建的快照创建一个新的按量付费云盘，并将其挂载到实例上进行数据恢复。数据恢复完成后，请及时释放该云盘以避免产生不必要的费用。

- 

（可选）扩容系统盘分区与文件系统

通过更换操作系统（系统盘）对系统盘进行扩容时，可能会因为超时导致分区扩容不生效。针对未扩容成功的系统，需参考[扩容分区与文件系统（Linux）](products/ecs/documents/user-guide/resize-linux-cloud-disks.md)手动扩展分区。该方式只是扩展系统盘分区，不会影响系统的版本。

- 

重新部署业务环境在新的操作系统中重新安装业务所需的软件、配置环境变量并迁移业务代码。

## 相关操作

- 

[为云盘设置自动快照策略](products/ecs/documents/user-guide/enable-or-disable-an-automatic-snapshot-policy.md)，以实现数据的定期自动备份。

- 

确认原系统盘数据已无需使用后，[删除快照](products/ecs/documents/user-guide/delete-a-snapshot-1.md)以节约存储成本。

- 

可以通过模板共模板[ACS-ECS-BulkyReplaceSystemDisk](https://help.aliyun.com/zh/oos/user-guide/acs-ecs-bulkyreplacesystemdisk)批量更换ECS系统盘。

- 

通过API接口[ReplaceSystemDisk](products/ecs/documents/developer-reference/api-ecs-2014-05-26-replacesystemdisk.md)更换操作系统。

- 

[哪些操作系统支持可视化（图形化桌面）](products/ecs/documents/faq-about-images-during-instance-creation.md)。

- 

[更换操作系统相关问题](products/ecs/documents/faq-about-replacing-the-operating-system-of-an-instance.md)。

## 常见问题

为什么更换操作系统时看不到某些镜像（包括自定义镜像）？

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

[上一篇：操作系统更换与迁移](products/ecs/documents/user-guide/operating-system-replacement-and-migration.md)[下一篇：操作系统迁移](products/ecs/documents/user-guide/migrate-the-operating-system-of-an-ecs-instance.md)

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
