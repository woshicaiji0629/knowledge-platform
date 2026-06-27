# 使用内容模板定制告警通知内容-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/custom-notification-content

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

# 通知内容定制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务支持您在配置内容模板时，定制通知内容。

## 使用模板变量丰富通知内容

您在配置内容模板时，可在标题或消息内容中添加模板变量。日志服务发送告警通知时，会将消息内容和标题中的模板变量替换为真实值。例如{{ alert.project }}替换为实际的Project名称。

每次产生告警时，系统自动生成告警上下文信息，存储于Results字段中。Results字段中的子字段都可作为模板变量。更多信息，请参见[内容模板语法（新版）](products/sls/documents/syntax-for-new-alert-templates.md)和[内容模板变量说明（新版）](products/sls/documents/variables-in-new-alert-templates.md)。

## 新旧版内容模板对比

新版告警支持两个版本的内容模板语法。相对于旧版的内容模板语法，新版提供更加灵活且高级的自定义渲染逻辑。

- 

- 

- 

- 

- 

- 

- 

- 

| 功能 | 新版 | 旧版 |
| --- | --- | --- |
| 引用方式 | 普通字段： {{ alert.project }} 嵌套字段： {{ alert.policy.alert_policy_id }} 数组元素： {{ alert.results[0] }} 数组元素字段： {{ alert.results[0].query }} | 普通字段： ${project} 嵌套字段： ${policy.alert_policy_id} 数组元素： ${results[0]} 数组元素字段： ${results[0].query} |
| 模板变量 | 内容和样式分离。由告警变量提供内容，通过控制流和函数实现多样化的样式。更多信息，请参见 [内容模板变量说明（新版）](products/sls/documents/variables-in-new-alert-templates.md) ）。 | 内容和样式不分离，都由告警变量提供。更多信息，请参见 [内容模板变量说明（旧版）](products/sls/documents/variables-in-original-alert-templates.md) 。 |
| 控制流（条件判断、迭代等） | 支持。更多信息，请参见 [内容模板语法（新版）](products/sls/documents/syntax-for-new-alert-templates.md) 。 | 不支持。 |
| 过滤器处理 | 支持。更多信息，请参见 [内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md) 。 | 不支持。 |


## 内容格式

- 

钉钉

钉钉渠道的内容支持Markdown语法，具体支持的元素如下。更多信息，请参见[钉钉开放平台-自定义机器人接入](https://developers.dingtalk.com/document/app/custom-robot-access/title-72m-8ag-pqw)。

- 

标题

# 一级标题 ## 二级标题 ### 三级标题 #### 四级标题 ##### 五级标题 ###### 六级标题

- 

引用

> A man who stands for nothing will fall for anything.

- 

文字加粗、斜体

**bold** *italic*

- 

链接

[this is a link](http://example.com)

- 

图片

![](http://example.com/pic.jpg)

- 

无序列表

- item1 - item2

- 

有序列表

1. item1 2. item2

- 

企业微信

企业微信渠道的内容支持Markdown语法，具体支持的元素如下。更多信息，请参见[群机器人配置](https://work.weixin.qq.com/api/doc/90000/90136/91770#markdown%E7%B1%BB%E5%9E%8B)。

重要

\n\n在企业微信的消息内容中会被渲染为\n，因此如果您需要空行效果，请使用\n\n\n。

- 

标题

# 标题一 ## 标题二 ### 标题三 #### 标题四 ##### 标题五 ###### 标题六

- 

加粗

**bold**

- 

链接

[这是一个链接](http://work.weixin.qq.com/api/doc)

- 

行内代码段

`code`

- 

引用

> 引用文字

- 

字体颜色

只支持3种内置颜色。

<font color="info">绿色</font> <font color="comment">灰色</font> <font color="warning">橙红色</font>

- 

飞书

飞书渠道的内容支持Markdown语法，具体支持的元素如下。更多信息，请参见[使用](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)[markdown](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)[标签](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)。

- 

加粗

**粗体**

- 

斜体

*斜体*

- 

删除线

～～删除线～～

- 

超链接

<a>https://open.feishu.cn</a>

- 

文字链接

[开发文档](https://open.feishu.cn)

- 

图片

![hover_text](image_key)

- 

分割线

---

- 

Slack

Slack应用中的Incoming Webhook支持Markdown类型的消息，但只支持部分Markdown语法。更多信息，请参见[Slack Markdown Reference](https://www.markdownguide.org/tools/slack/#messages)。

- 

Webhook

Webhook渠道支持逐条发送和合并发送。

- 

内容模板：

{ "项目": "${project}", "告警名称": "${alert_name}" }

- 

合并发送的通知内容：

[ { "项目": "project-name1", "告警名称": "alert-name1" }, { "项目": "project-name2", "告警名称": "alert-name2" } ]

- 

邮件

邮件渠道的内容支持HTML标签。更多信息，请参见[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)。例如：

- 

使用<br>换行。

- 

使用<a href="${query_url}">查看详情</a>添加链接。您可以单击该链接查看触发告警的详细信息。

- 

使用<strong>${severity}</strong>加粗显示告警严重度。

[上一篇：默认内容模板](products/sls/documents/default-alert-templates.md)[下一篇：内容模板语法（新版）](products/sls/documents/syntax-for-new-alert-templates.md)

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
