# 使用图形化工具ossbrowser 2.0快速入门文件管理-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/ossbrowser?spm=a2c4g.11186623.help-menu-31815.d_1_3.7afa6bd2pjIrgs

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# ossbrowser 2.0快速入门

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ossbrowser 2.0是一款用于管理OSS的免费图形化桌面客户端。该客户端支持Windows、macOS和Linux操作系统，提供直观的图形用户界面，使您能够高效地执行各种操作，包括文件的上传、下载和删除。由于其本地部署特性，ossbrowser 2.0可在您的设备上直接运行，确保操作的流畅性。

## 操作视频

请观看以下视频快速了解如何使用ossbrowser 2.0。

## 前提条件

- 

已[开通](https://oss.console.aliyun.com/overview)[OSS](https://oss.console.aliyun.com/overview)[服务](https://oss.console.aliyun.com/overview)。

- 

已[安装](products/oss/documents/developer-reference/installing-the-ossbrowser-2-0.md)[ossbrowser 2.0](products/oss/documents/developer-reference/installing-the-ossbrowser-2-0.md)。

- 

已[登录](products/oss/documents/developer-reference/login-to-ossbrowser-2-0.md)[ossbrowser 2.0](products/oss/documents/developer-reference/login-to-ossbrowser-2-0.md)。

## 管理Object

ossbrowser 2.0支持的Object级别的操作与控制台支持的操作类似，请按照ossbrowser 2.0界面指引完成Object相关操作。管理Object前，您需要先单击Bucket名称，进入文件列表页面。

说明

进行object操作时，请参考以下说明。

- 

- 

| 操作 | 说明 |
| --- | --- |
| 上传文件 | ossbrowser 2.0 默认使用分片上传和断点续传上传文件，上传文件最大不能超过 48.8 TB。若您因意外中断了文件上传的过程，且未继续完成该文件的上传，则已上传的部分会以碎片（Part）的形式存储在 OSS 的 Bucket 中。若您不再需要这些 Part，建议您通过以下方式删除，以免产生额外的存储费用。 手动删除 Part 的具体操作，请参见 [删除碎片](products/oss/documents/user-guide/delete-parts.md) 。 通过生命周期规则自动删除 Part 的具体操作，请参见 [基于最后一次修改时间的生命周期规则](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-modified-time.md) 。 重要 如果上传的文件与 Bucket 中已有的文件重名，则覆盖已有文件。 |
| 上传文件夹 | 单击页面上方 上传 按钮，在下拉列表框中选择上传文件夹。 |
| 下载文件 | 选中文件，然后单击页面上方的 下载 按钮进行下载。 说明 您也可以选中多个文件，然后单击页面上方的 下载 进行批量下载。 |
| 下载文件夹 | 选中文件夹，然后单击页面上方的 下载 按钮进行下载。 |
| 列举文件 | 单击 Bucket 名称后，直接列举 Object 信息。 |
| 预览文件 | 直接单击文件名称进行预览。文本预览大小限制为 100 MB，支持直接编辑。 |
| 拷贝文件 | 选中文件单击页面上方 更多 > 复制到 ，然后选择目标路径，单击 复制 > 确认复制 。 |
| 移动文件 | 选中文件单击页面上方 更多 > 移动到 ，然后选择目标路径，单击 移动 > 确认移动 。 说明 移动或复制文件最大不能超过 5 GB，5 GB 以上文件的移动或复制操作建议使用 [ossutil](products/oss/documents/developer-reference/overview-59.md) 。 |
| 重命名文件 | 选中目标文件，单击右侧 图标，选择 重命名 ， 修改完点击 确认修改 。 |
| 搜索文件 | 在页面上方搜索框中输入指定的文件名前缀，您可以查看 Bucket 根目录下与指定前缀匹配的文件和文件夹。 |
| 解冻文件 | 选中目标文件，单击 更多 > 解冻 进行操作。 |
| 删除文件 | 选择目标文件，单击 更多 > 删除 删除文件。 |
| 设置软链接 | 选中目标文件，单击右侧 图标，选择 设置软链接 ， 在 设置软链接 面板，设置 软链接文件目录 ，然后单击确定。 |
| 设置文件元数据 | 选中目标文件，单击右侧 图标，选择 设置文件元数据 ， 在 设置元数据 面板，设置文件元数据，然后单击确定。 |
| 分享文件 | 文件上传至 Bucket 后，您可以将文件 URL 分享给第三方，供其下载或预览。 选中目标文件，单击右侧 图标，选择 获取地址 ， 输入链接有效期单击 生成 ，获取分享地址。 |
| 设置读写权限 | 选中目标文件，单击右侧 图标，选择 设置读写权限 ，在读写权限弹出框选择权限单击 确认授权 。 |


[上一篇：控制台快速入门](products/oss/documents/user-guide/console-quick-start.md)[下一篇：ossfs快速入门](products/oss/documents/user-guide/ossfs-quick-start.md)

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
