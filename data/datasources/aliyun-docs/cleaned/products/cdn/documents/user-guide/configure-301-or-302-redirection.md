# 配置回源302跟随的前提条件和具体操作-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-301-or-302-redirection

# 配置回源301/302跟随
回源301/302跟随功能同时支持源站的301和302响应状态码，301和302状态码均支持相同功能。配置该功能后，CDN节点会直接处理源站的301/302响应，减少数据交互流程，加快用户获取资源的速度。
## 前提条件
用户源站使用了301/302重定向方式去实现业务逻辑。
## 背景信息
301/302是HTTP协议中的状态码，表示已存在的资源被临时改变了位置，导致用户无法访问到对应的资源。基于此情况，服务器通常会在响应头中加入Location参数，当客户端接收到带有Location头的301/302响应时，会跳转到Location对应的地址请求资源。
## 工作原理
回源301/302跟随功能指CDN节点在回源请求资源时，若收到源站返回的301/302状态码，CDN节点会直接跳转到Location地址获取资源，而不会将301/302状态码返回给用户。
用户请求访问http://example.com/examplefile.txt文件。
CDN节点上未缓存该文件，回源请求。
源站返回301/302状态码，Location地址为http://www.example.org/examplefile.txt。
CDN节点收到源站的响应后，向Location地址http://www.example.org/examplefile.txt发起请求获取资源。
CDN节点获取到所需资源后，缓存到CDN节点上。
CDN节点将获取到的资源返回给用户。
此时，如果其他用户再请求访问http://example.com/examplefile.txt文件，会直接在CDN节点命中缓存并返回给用户。
## 注意事项
配置回源301/302跟随之前，请先确认CDN是否配置了[默认回源](configure-the-default-origin-host.md)[HOST](configure-the-default-origin-host.md)或者[指定源站回源](specify-an-origin-host-for-each-origin.md)[HOST](specify-an-origin-host-for-each-origin.md)：
未配置默认回源HOST或指定源站回源HOST：当源站响应“301/302状态码+Location URL”给CDN节点时，回源请求的HOST头将使用Location域名。
配置了默认回源HOST：当源站响应“301/302状态码+Location URL”给CDN节点时，回源请求的HOST头将使用CDN配置的HOST头。如果源站要求使用Location域名作为回源HOST，请使用[指定源站回源](specify-an-origin-host-for-each-origin.md)[HOST](specify-an-origin-host-for-each-origin.md)功能。
源站响应给CDN节点的Location头部的格式支持以下3种：
Location: http://www.example.net/index.html：CDN节点将使用Location中的完整URL。
Location: //www.example.net/index.htmL：CDN节点将使用302前的回源协议加上Location中的信息拼接成一个URL。
Location: /index.html：CDN节点将使用302前的回源协议和域名加上Location中的信息拼接成一个URL。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名列表中选择目标域名，单击操作列的管理。
单击回源配置，在配置页签的回源301/302跟随区域打开开关。
在弹出的对话框中配置相关参数，然后单击确定。
| 参数 | 描述 |
| --- | --- |
| 301/302 跟随次数上限 | 指在一次用户请求过程中， CDN 节点可以跟随 Location 地址跳转访问的最大次数，超出限制将直接返回 301/302 状态码给用户。默认值为 2，取值范围为 1~5。 说明 配置 301/302 跟随次数上限，会影响回源次数上限。回源次数上限指在一次用户请求过程中， CDN 节点可以回源访问源站的最大次数。 回源次数上限=301/302 跟随次数上限+1，即默认的回源次数上限为 3，取值范围为 2~6。 |
| 301/302 跟随保留参数 | 保留：301/302 跟随时保留原请求参数回目标源站。如果您选择保留，那么请求参数将会传递给 Location 地址对应的服务器。 不保留：301/302 跟随时不保留原请求参数回目标源站。 |
| 301/302 跟随保留请求头 | 保留：301/302 跟随时保留原请求头回目标源站。如果您选择保留，那么请求头参数将会传递给 Location 地址对应的服务器。 不保留：301/302 跟随时不保留原请求头回目标源站。 |
## 配置示例
配置场景：您源站的资源挪至其他地址，但您并不希望您的用户感知该变动，希望使用原有域名正常访问资源。
配置方式：域名example.com开启回源301/302跟随，配置如下：在回源301/302跟随配置弹窗中，将301/302跟随次数上限设置为2（可配置范围1~5，回源次数=跟随次数+1，范围2~6），301/302跟随保留参数选择不保留，301/302跟随保留请求头选择不保留，单击确定。
结果说明：用户请求http://example.com/examplefile.txt文件，CDN节点未缓存时，向源站请求资源。源站返回301/302状态码和重定向地址http://www.example.org/examplefile.txt。
CDN节点收到301/302状态码后，向重定向地址发起请求（最多请求两次，失败后返回301/302状态码给用户）。
CDN节点获取资源，返回给用户，并缓存至CDN节点。
其他用户再请求该文件时，CDN直接返回已缓存资源。
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
