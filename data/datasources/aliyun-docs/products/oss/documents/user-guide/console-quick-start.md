# 通过控制台快速使用OSS-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/console-quick-start

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

# 控制台快速入门

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

OSS管理控制台是阿里云提供的一款简单且易于上手的OSS网页管理工具。通过本教程，您可以在10分钟内完成创建存储空间、上传文件、分享文件等基础操作，预计费用不超过0.01元。

## 前提条件

- 

已[注册阿里云账号](https://account.aliyun.com/register/qr_register.htm?oauth_callback=https%3A%2F%2Fbailian.console.aliyun.com%2F%3FapiKey%3D1)。

- 

已[个人实名认证](https://help.aliyun.com/zh/document_detail/324614.html#task-2020003)或[企业实名认证](https://help.aliyun.com/zh/account/overview)。

- 

已[开通](https://oss.console.aliyun.com/overview)[OSS](https://oss.console.aliyun.com/overview)[服务](https://oss.console.aliyun.com/overview)。

购买OSS资源包并不等于自动开通OSS，您仍需手动开通OSS服务，并且开通OSS服务是免费的。

## 步骤一：创建存储空间

存储空间（Bucket）是存放文件的容器，开始使用OSS前，需要先创建一个Bucket。

- 

在左侧导航栏进入Bucket 列表页面，单击创建 Bucket。

- 

配置以下关键参数，其余保留默认值：

- 

Bucket名称：输入一个全局唯一的名称，为确保唯一，建议使用项目名-地域-随机字符串的组合，例如my-project-hangzhou-a1b2c3d4。

- 

地域：选择距离您较近的地域，例如华东1（杭州），以降低访问延迟。

- 

单击完成创建。

## 步骤二：上传文件

创建Bucket后，可将图片、视频、文档等各种类型的文件（Object）上传至其中。

通过控制台单次可上传不超过5GB的文件。对于更大的文件，推荐使用[命令行工具](products/oss/documents/command-line-tools-ossutil-quickstart.md)[ossutil](products/oss/documents/command-line-tools-ossutil-quickstart.md)。

- 

如果本地没有合适的测试文件，可先下载此示例文件[exampleobject.jpg](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20240926/tajhik/exampleobject.jpg)到本地。

- 

在Bucket 列表页面，单击刚刚创建的Bucket名称。

- 

在左侧导航栏进入文件管理>文件列表，然后单击上传文件。

- 

将本地的exampleobject.jpg文件拖拽到待上传文件区域，或通过扫描文件选择该文件。

- 

保持其他参数默认，单击上传文件。

此时，您可以在上传列表页签查看各个文件的上传进度。上传完成后，您可以在目标路径下查看上传文件的文件名、文件大小以及存储类型等信息。

## 步骤三：下载文件

Bucket中的文件可下载至本地。

- 

在文件列表页面，找到刚才上传的exampleobject.jpg文件。

- 

勾选该文件，然后单击列表下方的下载按钮。

## 步骤四：分享文件

私有Bucket中的文件，可生成带有时效性的安全链接（URL）进行分享。

- 

在文件列表页面，单击exampleobject.jpg的文件名。

- 

在右侧弹出的详情面板中，可以按需设置链接的过期时间（秒）（默认为600），然后单击复制文件 URL。

- 费用：此URL使用外网Endpoint，任何通过此URL的下载都会产生外网流出流量费。

- 安全：分享前，请务必确认文件中不包含任何敏感数据。

- 时效：URL在设定的有效期后会自动失效，如需再次访问，需要重新生成。

- 

将复制的URL粘贴到浏览器地址栏访问。默认行为是直接下载该图片文件，如需在浏览器中预览图片，则需要[绑定自定义域名](products/oss/documents/user-guide/access-buckets-via-custom-domain-names.md)，使用自定义域名生成URL。

## 步骤五：清理

为防止文件持续产生费用，需先清空存储空间内的所有文件，然后删除存储空间本身。删除操作不可逆。

### 删除文件

- 

在左侧导航栏，选择文件管理>文件列表。

- 

勾选已上传的示例文件exampleobject.jpg，

- 

单击列表下方的彻底删除，并在弹窗中单击确定。

### 删除存储空间

删除Bucket后，需要等待数小时（通常为4到8个小时）才能再次创建同名的Bucket。

- 

在Bucket 列表页面，单击您要删除的存储空间的名称。

- 

在左侧导航栏，单击删除 Bucket。

- 

单击立即删除，并按控制台提示完成后续操作。

## 费用说明

本教程涉及的OSS计费项主要包括：

- 

存储费用：文件存放期间，会持续产生标准存储费用。

- 

外网下行流量费用：他人使用分享链接（URL）下载文件，会产生外网流出流量费。

- 

请求费用：上传、下载操作会产生API请求次数费用。

完成本教程（上传一个小于1MB的文件并下载一次）的总费用预计低于0.01元。定价详情参见[OSS](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.0.0.628c4d22ZdP2B0#/oss/detail/oss)。

## 下一步

- 

深入成本管理：通过[计费概述](products/oss/documents/billing-overview.md)了解费用详情，并通过[资源包](products/oss/documents/resource-plan.md)节省成本。

- 

实现自动化：学习[SDK](products/oss/documents/user-guide/oss-sdk-quick-start.md)[快速入门](products/oss/documents/user-guide/oss-sdk-quick-start.md)，在应用中通过代码管理OSS。

- 

更多文件操作：查看[功能指引](products/oss/documents/user-guide/object-overview.md)，获取更多管理文件的方法。

- 

加固数据安全：通过配置[权限与访问控制概述](products/oss/documents/user-guide/permissions-and-access-control-overview.md)，精细化管理数据访问权限。

说明

通过OSS控制台创建Bucket时默认开启[阻止公共访问](products/oss/documents/user-guide/block-public-access.md)。开启后，不允许创建公共访问权限，包括公共读或者公共读写ACL、以及公共访问语义的Bucket Policy。如果您的业务有公共访问需求，可在Bucket创建后关闭阻止公共访问。

## 常见问题

- 

[用量查询](products/oss/documents/usage-query.md)

- 

[对象/文件（Object）](products/oss/documents/data-upload-and-download.md)

- 

[资源包](products/oss/documents/package-faq.md)

[上一篇：快速入门](products/oss/documents/user-guide/get-started-with-oss.md)[下一篇：图形化管理工具ossbrowser 2.0快速入门](products/oss/documents/user-guide/ossbrowser.md)

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
