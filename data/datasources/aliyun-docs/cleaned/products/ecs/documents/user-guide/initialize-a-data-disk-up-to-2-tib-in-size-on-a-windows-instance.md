# 初始化数据盘（Windows）-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance

# 初始化数据盘（Windows）
一块全新的Windows数据盘挂载到ECS实例后，不能直接存储数据，需要初始化后才能被操作系统识别并用于存储数据。
## 前提条件
已[创建空数据盘](create-a-disk.md)。
随实例创建的云盘，默认自动完成初始化操作，创建后即可使用，无需再次执行初始化操作。
数据盘状态为使用中。
## 操作步骤
登录ECS实例。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。选择连接方式为终端连接，输入账号和密码，登录图形化终端页面
联机。
在Windows Server桌面，右键单击图标，选择磁盘管理。
在磁盘管理页面中，找到脱机状态的目标数据盘。
若弹出初始化磁盘对话框，表示云盘已联机。可直接[初始化云盘](initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)。若数据盘已联机且分区状态良好，无需其余操作，可直接使用。
右键单击目标磁盘，选择联机。
若磁盘显示联机，目标分区显示状态良好，表示系统可正常使用该云盘。
若磁盘显示没有初始化，目标分区显示未分配，需要[初始化](initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)后才可存储数据。
初始化云盘。
初始化云盘会删除数据盘中数据，请确保云盘为空。
右键单击目标磁盘，选择初始化磁盘。
在初始化磁盘对话框，选择磁盘分区形式后，单击确定。
重要
MBR 分区最大支持 2 TiB 容量。如果云盘容量大于 2 TiB 或后续有扩容至 2 TiB 以上需求，分区时请采用 GPT 分区格式。
右键单击目标磁盘的未分配区域，选择新建简单卷。
在新建简单卷向导对话框中，单击下一步，根据向导完成初始化操作。
在指定卷大小对话框中，设置简单卷大小后，单击下一步。
如果只需要创建一个主区，保持默认即可。也可以根据需要设置简单卷大小，将目标磁盘分成多个分区来使用。
在分配驱动器号和路径对话框中，按需选择分配以下驱动器号，然后单击下一步。
在格式化分区对话框中，选择按下列设置格式化这个卷，设置格式化信息后，单击下一步。
重要
请谨慎选择分配单元大小，此设置一旦确定将无法修改。具体云盘容量限制，请参看[NTFS](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)[概述](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)。
后续有扩容至16TiB～32TiB（包括）需求，选8192。
后续有扩容至32TiB～64TiB（包括）需求，选16K。
其他情况请保持默认值。
查看新建的简单卷信息，单击完成，关闭新建简单卷向导。
判断是否操作成功。
若目标磁盘状态为联机，且分区状态良好，表示初始化并联机成功，可正常使用。
## 相关文档
当云盘使用空间不足时，可以[扩容云盘](resize-windows-cloud-disks.md)容量增加云盘存储空间。
若想为Linux实例初始化数据盘，请参考[初始化数据盘（Linux）](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
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
