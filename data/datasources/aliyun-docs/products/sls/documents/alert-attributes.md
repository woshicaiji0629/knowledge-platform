# 告警属性的基本信息-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/alert-attributes

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 告警属性参考

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍告警属性的基本信息。

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

| 类别 | 属性名 | 子属性 | 标识性属性（指纹） | 描述 | 示例 |
| --- | --- | --- | --- | --- | --- |
| 监控规则 | 阿里云账号 ID | 不涉及 | 是 | 关联的阿里云账号 ID。 告警监控规则所在的阿里云账号 ID 或开放告警中设置的阿里云账号 ID。 | 12****90 |
| 告警类型 | 不涉及 | 否 | 告警类型。取值为： 告警监控规则：由告警监控规则触发的告警。 开放告警：来自于开放告警的告警。 | 开放告警 |  |
| 所属区域 | 不涉及 | 否 | 告警监控规则所属的地域。 | cn-hangzhou |  |
| 所属项目 | 不涉及 | 是 | 告警监控规则所属的项目。 | my-project |  |
| 规则 ID | 不涉及 | 是 | 告警监控规则 ID，项目内唯一。 | alert-12345 |  |
| 规则名 | 不涉及 | 否 | 告警监控规则名称。 | Nginx 告警 |  |
| 告警信息 | 状态 | 不涉及 | 否 | 告警状态。取值为： 触发告警。 恢复通知。 | 触发告警 |
| 严重度 | 不涉及 | 否 | 告警严重度。 严重 高 中 低 报告 | 严重 |  |
| 标题 | 不涉及 | 否 | 告警标注中的标题。 | 告警标题 |  |
| 描述 | 不涉及 | 否 | 告警标注中的描述。 | 告警描述 |  |
| 标签 | 自定义名称 | 是 | 告警的标签信息。 | 名称：env 值：prod |  |
| 标注 | 自定义名称 | 否 | 告警的标注信息。 | 名称：status 值：400 |  |
| 时间相关 | 触发时间。 | 否 | 触发时间。Unix 时间戳形式，单位：秒。 | 1616744734 |  |
| 首次触发时间 | 否 | 首次触发时间。Unix 时间戳形式，单位：秒。 | 1616059834 |  |  |
| 恢复时间 | 否 | 告警恢复时间。 如果告警状态是 firing，取值为 0。 如果告警状态是 resolved，取值为具体恢复时间。Unix 时间戳形式，单位：秒。 | 0 |  |  |
| 其他高级配置 | 策略配置 | 告警策略 ID | 否 | 告警策略 ID。 | sls.test-alert |
| 行动策略 ID | 否 | 行动策略 ID。 | sls.test-action |  |  |
| 开放告警 | 服务名 | 否 | 开放告警的服务名。 | test |  |
| 应用名 | 否 | 开放告警的应用名。 | test |  |  |
| 协议 | 否 | 开放告警的协议。 | zabbix |  |  |
| 接入区域 | 否 | 接入地域。 | cn-hangzhou |  |  |
| 查询统计 | 类型 | 否 | 查询统计类型： 对日志库进行查询统计时，取值为 日志库 。 对时序库进行查询统计时，取值为 时序库 。 对资源数据进行查询统计时，取值为 资源数据 。 | 日志库 |  |
| 区域 | 否 | 对日志库和时序库进行查询统计时，取值为目标 Project 所在地域。 说明 对资源数据进行查询统计时，无该参数。 | cn-hangzhou |  |  |
| 项目 | 否 | 对日志库和时序库进行查询统计时，取值为源数据所在 Project。 说明 对资源数据进行查询统计时，无该参数。 | my-project |  |  |
| 目标库 | 否 | 目标存储库名。 | my-LogStore |  |  |
| 查询关联的仪表盘 | 否 | 查询统计关联的仪表盘 ID。 | mydashboard |  |  |
| 使用服务角色 | 否 | RAM 角色标识。 | acs:ram::13****44:role/logrole |  |  |
| 查询语句 | 否 | 对日志库和时序库进行查询统计时，取值为查询和分析语句。 说明 对资源数据进行查询统计时，无该参数。 | * | select count(1) as cnt |  |  |
| 查询起始时间 | 否 | 对日志库和时序库进行查询统计时，取值为查询时间范围的开始时间。 说明 对资源数据进行查询统计时，无该参数。 | 1616744734 |  |  |
| 查询结束时间 | 否 | 对日志库和时序库进行查询统计时，取值为查询时间范围的结束时间。 说明 对资源数据进行查询统计时，无该参数。 | 1616744744 |  |  |


[上一篇：告警静默机制](products/sls/documents/silence-policies.md)[下一篇：行动策略](products/sls/documents/create-an-action-policy.md)

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
