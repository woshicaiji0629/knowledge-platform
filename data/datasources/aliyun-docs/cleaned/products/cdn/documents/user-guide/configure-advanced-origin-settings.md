# 根据不同的参数回源到不同的源站-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-advanced-origin-settings

# 高级回源
高级回源可以根据客户端请求的Request Header、Query String Parameter、Path、Request Cookie不同参数回到不同的源站。本文为您介绍配置高级回源功能的操作步骤。
## 注意事项
配置数量：最多可以设置120条规则。
功能冲突：[条件源站](configure-a-conditional-origin.md)功能与高级回源功能存在功能冲突，只能二选一配置。
配置生效：按功能的配置顺序匹配，命中某一条后不再继续匹配。
端口号：高级回源功能目前仅支持通过域名配置源站，不支持配置端口号。若您需要为域名源站指定端口号，或者需要配置IP源站、OSS源站、函数计算源站，请改用条件源站。
Path 匹配：高级回源中的 Path 匹配仅支持精确值匹配，不支持通配符或正则表达式。如需按路径通配符回源（如/api/*），请改用条件源站功能，配合规则引擎实现。
## 条件源站与基础源站、高级回源的区别
条件源站和高级回源均可引用规则引擎中配置的规则条件，从而实现更灵活的回源策略。CDN 根据请求是否命中规则条件，自动选择对应的源站：
| 源站类型 | 触发条件 |
| --- | --- |
| 条件源站 | 请求命中条件源站引用的规则条件 |
| 高级回源 | 请求命中高级回源引用的规则条件 |
| 基础源站 | 请求 未命中 任何条件源站 / 高级回源规则（默认兜底） |
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
在高级回源区域，单击添加。
在高级回源对话框中，选择使用条件并填写源站域名。
说明
任意选择Request Header、Query String Parameter、Path、Request Cookie配置不同源站。CDN节点在接收到客户端请求后将读取请求中对应的字段进行判断并回源到不同源站。
使用条件需配置字段名、匹配方式（如等于）及对应值。源站域名格式示例：img.yourdomain.com，源站域名不能与加速域名相同。
单击确定。
## 示例
CDN节点行为：接收到的请求中含参数 test=1 时，该请求回源至img.yourdomain1.com源站。在高级回源对话框中，将使用条件设置为Query String Parameter，参数名为test，条件为等于，值为1。将源站域名设置为img.yourdomain1.com，然后单击确定。
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
