# 快速配置加速域名，方便接入CDN加速服务-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/add-a-domain-name

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 添加加速域名

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

如果您想通过CDN加速指定网站的业务，需要将目标网站配置为源站，并为其设置一个加速域名。CDN会通过该加速域名将源站内容缓存至全球分布的边缘节点，从而显著降低内容传输延迟，提升用户的访问速度。

## 准备工作

- 

您已经拥有稳定运行的源站（即业务服务器或OSS）。如果没有源站，请参见[通过控制台使用](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[ECS](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)[实例](products/ecs/documents/getting-started/create-and-manage-an-ecs-instance-by-using-the-ecs-console.md)或[创建存储空间](products/oss/documents/user-guide/create-a-bucket-4.md)创建。

- 

您已经拥有用于加速的域名。

说明

当目标加速区域为仅中国内地或全球时，域名需要完成备案。如果域名未备案，您可以登录[阿里云](https://beian.aliyun.com/pcContainer/myorder)[ICP](https://beian.aliyun.com/pcContainer/myorder)[代备案管理系统](https://beian.aliyun.com/pcContainer/myorder)完成备案。

- 

您已经开通了CDN服务。如果未开通，请参见[开通](products/cdn/documents/activate-alibaba-cloud-cdn.md)[CDN](products/cdn/documents/activate-alibaba-cloud-cdn.md)[服务](products/cdn/documents/activate-alibaba-cloud-cdn.md)进行开通。

## 步骤一：配置域名信息

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

单击添加域名，在域名信息页面，配置加速区域、加速域名和业务类型，其他参数均保持默认。

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

| 参数 | 说明 |
| --- | --- |
| 加速区域 | 仅中国内地 ：所有用户访问均会调度至中国内地就近节点提供加速服务（ 海外地区和中国香港、中国澳门、中国台湾地区的访问流量将会被调度至华东电信的 CDN 节点 ）。 全球 ：所有用户访问将会择优调度至全球就近节点提供服务。 全球（不包含中国内地） ：非中国内地用户访问会被调度至就近节点服务；中国内地用户访问会被调度至日本、新加坡和中国香港的 CDN 加速节点服务。 重要 加速区域为 仅中国内地 或 全球 时，加速域名要求 必须备案 ，您可以登录 [阿里云](https://beian.aliyun.com/pcContainer/myorder) [ICP](https://beian.aliyun.com/pcContainer/myorder) [代备案管理系统](https://beian.aliyun.com/pcContainer/myorder) 完成备案。由于工信部备案系统存在数据延迟，刚完成备案的域名请在 8 小时后再配置。 加速区域为 全球（不包含中国内地） 时，对加速域名 备案不作要求 。 不同的加速区域价格不一样，请根据您的实际需求选择。计费详情，请参见 [CDN](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail) [定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.10.1b444ee22Dxy8y#/cdn/detail) 。 |
| 加速域名 | 填写 [加速域名](products/cdn/documents/product-overview/terms.md) 名称，填写要求请参见 [使用限制](products/cdn/documents/product-overview/limits.md) 。 说明 首次在 CDN 控制台添加一个新域名时，需要完成域名归属权验证。具体操作，请参见 [验证域名归属权](products/cdn/documents/verify-domain-name-ownership.md) 。如果之前已经验证通过根域名的归属权，请忽略。 |
| 业务类型 | [图片小文件](products/cdn/documents/product-overview/scenarios.md) ：适用于电商类、网站类、游戏图片类等小型的静态资源加速场景。 [大文件下载](products/cdn/documents/product-overview/scenarios.md) ：适用于大于 20 MB 的静态文件加速场景。 [视音频点播](products/cdn/documents/product-overview/scenarios.md) ：适用于音频或视频文件加速场景。 [全站加速](https://help.aliyun.com/zh/edge-security-acceleration/dcdn/product-overview/what-is-dcdn#concept-hdt-3t2-xdb) ：适用于含有大量动态和静态内容混合，且多为动态资源请求的加速场景。 当业务类型选择 ESA 边缘安全加速 时，您需根据界面提示，前往全站加速控制台添加域名并进行相关配置。具体操作，请参见 [添加服务域名](https://help.aliyun.com/zh/edge-security-acceleration/dcdn/getting-started/add-a-domain-name#task-alv-1fk-xdb) 。 说明 配置后业务类型不可修改。 |


## 步骤二：配置源站

- 

完成域名业务信息配置后，在源站信息区域单击新增源站信息。

- 

在新增源站信息对话框中，选择源站的类型，并填写源站地址，其他参数均保持默认。

- 

- 

- 

- 

- 

- 

- 

| 参数 | 说明 |
| --- | --- |
| 源站信息 | 选择 [源站](products/cdn/documents/product-overview/terms.md) 的类型，并填写源站地址。源站类型支持 OSS 域名 、 IP 、 源站域名 和 函数计算域名 。此处以 OSS 域名 举例说明，其他类型的源站配置，详情请参见 [配置源站](products/cdn/documents/user-guide/configure-an-origin-server.md) 。 源站信息 选择 OSS 域名 ，并在下方的 域名 列表中选择同账号下的 OSS Bucket，或选择输入阿里云 OSS Bucket 的外网域名作为源站（不支持 OSS 内网域名作为源站），示例值为 ***.oss-cn-hangzhou.aliyuncs.com 。 |
| 优先级 | 源站优先级支持设置主备，主优先级大于备优先级。用户请求通过阿里云 CDN 回源时，会优先回源到优先级为主的源站地址。主源站出现故障的情况下，将会回源到备源站。源站优先级的取值范围为 0~127，数值越小，优先级越高。主源站的优先级默认值为 20，备源站的优先级默认值为 30。如需配置其他值，请 [填写信息](https://page.aliyun.com/form/act2017566026/index.htm) 申请。 例如，有 A、B 两个源站，A 源站的优先级为主，B 源站的优先级为备，则用户请求通过阿里云 CDN 回源时会优先回源到 A 源站，如果 A 源站出现故障，将会回源到 B 源站，当 A 源站恢复正常后会从 B 源站切换回 A 源站。 |
| 权重 | 当多个源站的优先级相同时，阿里云 CDN 会按照源站的权重分配用户请求回源到不同源站的比例，实现按权重的负载均衡。您可以根据业务需求，自行设置权重值。 取值范围：1~100，数值越大，源站分配到的用户请求比例越高。 默认值：10。 例如：有 A、B 两个源站，两个源站的优先级都是主，A 源站的权重为 80，B 源站的权重为 20，则用户请求将会按照 8:2 的比例在 A、B 两个源站之间分配。 |
| 端口 | 表示 CDN 节点回到源站哪个端口请求资源。默认为 80，根据您源站的支持情况，可自定义设置回源端口，允许设置的端口范围为 1~65535。 默认值：80。 端口值为 443 时，以 HTTPS 协议回源；80 或其他自定义端口，以 HTTP 协议回源。 说明 如果需要以 HTTPS 协议回源到其他自定义端口，请参见 [配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md) 。 如果配置了 回源协议 功能（默认为关闭状态），这里配置的端口会失效。关闭回源协议的方法，请参见 [配置回源协议](products/cdn/documents/user-guide/configure-the-origin-protocol-policy.md) 。 当源站选择 OSS 域名时，回源端口是否支持自定义端口，取决于 OSS 产品。 |


- 

配置完成后，单击确定。

## 步骤三：完成域名审核

- 

完成源站配置后，阅读并勾选合规承诺，单击下一步。

- 

页面跳转至推荐配置页面，请根据实际需要配置缓存过期时间、忽略参数、页面优化、Range回源、Gzip压缩等基础配置，有效提升CDN的缓存命中率和访问性能，请参见[推荐配置（可选）](products/cdn/documents/configure-system-recommended-features.md)。

您可以单击页面下方的一键配置按钮，CDN会快速帮您完成相关配置；您也可以单击返回域名管理在域名列表页的操作栏单击推荐配置再次进入。

- 

等待人工审核。

审核通过后，域名状态显示为正常运行，表示添加成功。

说明

- 

如果您的加速域名无需人工审核，将直接进入下一个配置环节，您可根据实际业务需求，完成推荐配置。

- 

新增域名的生效时长通常在10分钟以内，偶尔会因为系统波动延长到30分钟，如果超过30分钟仍未完成域名新增，那么将会有阿里云的工程师介入处理。

## 后续步骤

[配置](products/cdn/documents/add-a-cname-record-for-a-domain-name.md)[CNAME](products/cdn/documents/add-a-cname-record-for-a-domain-name.md)：添加域名后，阿里云CDN会为您分配对应的CNAME域名，您需要完成CNAME配置，CDN服务才能生效。

说明

同时，建议您在[配置](products/cdn/documents/add-a-cname-record-for-a-domain-name.md)[CNAME](products/cdn/documents/add-a-cname-record-for-a-domain-name.md)前，完成以下操作：

- 

[推荐配置（可选）](products/cdn/documents/configure-system-recommended-features.md)：为域名配置缓存过期时间、带宽封顶等功能，提升CDN的缓存命中率、安全性和访问性能。

- 

[模拟访问测试（可选）](products/cdn/documents/test-whether-a-domain-name-is-accessible.md)：保证DNS解析顺利切换而不影响现有业务。

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
