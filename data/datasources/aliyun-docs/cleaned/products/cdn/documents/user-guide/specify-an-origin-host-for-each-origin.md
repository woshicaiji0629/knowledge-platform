# 指定源站回源HOST的背景信息以及操作步骤-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/specify-an-origin-host-for-each-origin

# 指定源站回源HOST
当您的同一个加速域名配置了多个回源站点并且需要结合HOST头请求不同虚拟站点的资源时，可以使用指定源站回源HOST功能，为不同的源站配置不同的回源HOST。
## 功能说明
当您的加速域名绑定了多个源站时，默认回源HOST会将相同的域名发送给所有源站，这要求每个源站都必须配置对应的虚拟站点。而使用指定回源HOST功能，您可以为每个源站单独设置不同的回源HOST，灵活适配复杂的业务需求，避免不必要的配置麻烦。回源HOST的相关技术原理，请参见[配置默认回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)。
条件回源与指定回源HOST是两个不同维度的回源配置功能，两者的区别如下：
条件回源：决定回源到哪个源站。根据请求URL路径、参数等条件，将不同的请求分流到不同的源站地址。
指定回源HOST：决定回源时携带的域名（即HTTP请求中的Host头）。为每个源站单独配置回源HOST，不影响请求被路由到哪个源站。
在多源站场景下，条件回源和指定回源HOST需配合使用：先通过条件回源将请求分流到对应的源站，再通过指定回源HOST为每个源站设置正确的Host头，确保源站能正确响应请求。
说明
在同时配置了默认回源HOST和指定源站回源HOST的情况下，CDN节点访问指定源站时，将会携带指定源站配置的回源HOST。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
在指定源站回源HOST区域，单击添加。
在弹出的指定源站HOST对话框中，配置相关参数。
| 参数 | 说明 |
| --- | --- |
| 源站类型 | 在下拉列表中选择当前要配置的源站类型： 基础源站地址 ：在 [配置源站](configure-an-origin-server.md) 时添加的源站地址。 所有源站 ： CDN 回源到的任意一个源站地址。 自定义源站 ：需要配置的源站地址不在源站信息列表中时，可以通过 自定义源站 来设置。 |
| 源站地址 | 与 源站类型 的对应关系如下： 如果 源站类型 选择 基础源站地址 ，可在下拉列表中选择源站地址。 如果 源站类型 选择 所有源站 ，无需配置源站地址。 如果 源站类型 选择 自定义源站 ，您可以输入自定义源站地址。 |
| 回源 HOST 类型 | 在下拉列表中选择当前要配置的回源 HOST 类型： 基础源站域名 ：在 [配置源站](configure-an-origin-server.md) 时添加的源站地址（IP 类型的源站除外）。 加速域名 ：当前在配置的 CDN 加速域名。 自定义回源 HOST ：需要配置的回源 HOST 不在源站信息列表中，同时也不是加速域名时，可以通过自定义回源 HOST 来设置。 |
| 回源 HOST | 与 回源 HOST 类型 的对应关系如下： 如果 回源 HOST 类型 选择 基础源站域名 ，可在下拉列表中选择回源 HOST。 如果 回源 HOST 类型 选择 加速域名 ，为当前在配置的 CDN 加速域名，无需配置。 如果 回源 HOST 类型 选择 自定义回源 HOST ，您可以输入自定义回源 HOST。 |
| 规则条件 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 重要 引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](rules-engine.md) 中进行管理。 |
单击确定。
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
