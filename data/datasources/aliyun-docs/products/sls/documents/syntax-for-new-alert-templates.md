# 使用内容模板语法自定义告警通知-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/syntax-for-new-alert-templates

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

# 内容模板语法（新版）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

新版告警支持两个版本的内容模板语法。本文介绍新版内容模板语法。

## 概述

相对于旧版的内容模板语法，新版通过类似Python语法的方式，提供更加灵活且高级的自定义渲染逻辑，在定制通知内容（例如Markdown转义）、自定义内容样式等方面都做了优化，满足更多样化的定制内容需求。例如：

- 

根据告警的严重度进行动态的内容渲染，不同严重度使用不同颜色的文字进行区分。

- 

对告警的查询结果进行迭代渲染，在邮件中渲染为列表或者表格。

- 

通过函数对某个字段进行BASE64编码和解码、对数值进行数学运算等。

新版的内容模板语法完全兼容旧版，并支持新旧版混合使用。但在不同版本的内容模板语法中使用告警属性时，其类型、取值和展示形式等存在差异，因此建议您不要混合使用新旧版本的内容模板语法。推荐您使用新版本的内容模板语法。

## 快速开始

通过新版内容模板定义通知内容的示例如下：

- 

告警内容

{ "alert_id": "test-alert", "alert_name": "PV/UV Alert", "project": "project-1", "status": "firing", "severity": 6, "labels": { "app": "nginx", "host": "host-1" }, "results": [ { "project": "project-1", "logstore": "logstore-1", "query": "* | select count(*) as pv" }, { "project": "project-2", "logstore": "logstore-2", "query": "* | select count(distinct user_id) as uv" } ] }

- 

内容模板配置

- Alert ID: {{ alert.alert_id }} - Alert Name: {{ alert.alert_name }} - Project: {{ alert.project }} - Status: {% if alert.status == "firing" %}FIRING{% else %}RESOLVED{% endif %} - Labels: {%- for key, val in alert.labels.items() %} - {{ key }}: {{ val }} {%- endfor %} - Query: {{ alert.results[0].query }}

- 

输出结果

- Alert ID: test-alert - Alert Name: PV/UV Alert - Project: project-1 - Status: FIRING - Labels: - app: nginx - host: host-1 - Query: * | select count(*) as pv

## 基本语法

### 数据类型

内容模板语法类似于Python语法，支持如下数据类型。

| 数据类型 | 说明 |
| --- | --- |
| 数字 | 包含整数和浮点数。例如 3、-1。 |
| 字符串 | 需要使用单引号（''）或者双引号（""）包裹。例如"foo"、'bar'。 当字符串中存在特殊字符时，需使用反斜线（\）进行转义。例如 \foo 需写为 "\\foo" 。 |
| 布尔值 | True、False。 |
| 空值 | None。 |
| 列表 | 不同编程语言中的叫法不同，可以为列表、数组、Slice 等。例如['foo', 'bar']。 |
| 字典 | 不同编程语言中的叫法不同，可以为字典、对象等。例如{'foo': 'bar'}。 |


### 分隔符

- 

- 

- 

- 

| 分隔符 | 使用场景 | 示例 |
| --- | --- | --- |
| {{ }} | 在变量或表达式中使用。 | 数字： {{ 123 }} 字符串： {{ "abc" }}或{{ 'xyz' }} 需要使用双引号（""）或单引号（''）。 变量： {{ alert.alert_name }} 表达式： {{ alert.project + '/' + alert.alert_id }} |
| {% %} | 用于控制语句。 | {% if alert.status == 'firing' %}FIRING{% else %}RESOLVED{% endif % } |
| {# #} | 用于注释，不会出现在通知内容中。 | {# this is a comment #} |


### 清除空字符

默认情况下，在分隔符内部，分隔符与表达式之间的空格会被忽略。例如{{ 23 }} < {{ 45 }}等同于{{23}} < {{45}}，渲染结果都为23 < 45。但是分隔符外部的空字符（空格、Tab、换行等）会被保留，例如{{ 23 }} < {{ 45 }}的渲染结果为23 < 45，而不是23<45。

当您需要删除多余的空字符时，可以使用清除空字符操作。在分隔符开始或结束的地方添加一个短划线（-），用于清除该分隔符前面和后面所有紧连着的空字符。例如{{ 23 -}} < {{- 45 }}的渲染结果为23<45。

- 

{{-、{{%-、{#-用于删除分隔符左侧紧连着的所有空字符。

- 

-}}、-%}、-%}用于删除分隔符右侧紧连着的所有空字符。

重要

- 

短划线（-）和分隔符之间不能有空格。例如{{- 3 }}是有效的，渲染结果为3；{{ - 3 }}是无效的，渲染结果为-3。

- 

清除空字符操作只对分隔符外部的空格有效，不影响分隔符内部的空格。例如{{ "hello " }} {{- "world"}}渲染结果为hello world。

### 条件语句

条件判断支持对参数或者逻辑比较表达式进行判断。通过条件判断，可以进行动态渲染。

- 

如果if后面传入的是常量或者普通变量，则对该值进行真值判断。其中布尔值false、数字0、空字符串""、空值null、空数组[]、空对象{}都会被判定为假，其它值被判定为真。

- 

如果if后面传入的是逻辑比较表达式，则按照比较结果进行判断。例如{{ if alert.severity >= 8 }}用于判断告警严重度是否大于等于8。

条件判断支持如下几种形式：

| 使用方式 | 示例 |
| --- | --- |
| if | {% if alert.severity >= 8 %} 严重告警 {% endif %} |
| if-else | {% if alert.severity >= 8 %} 严重告警 {% else %} 普通告警 {% endif %} |
| if-elif | {% if alert.severity >= 8 %} 严重告警 {% elif alert.severity >= 4 %} 普通告警 {% endif %} |
| if-elif-else | {% if alert.severity >= 8 %} 严重告警 {% elif alert.severity >= 4 %} 普通告警 {% else %} 通知 {% endif %} |
| 嵌套使用 | {% if alert.severity >= 8 %} 严重告警 {% else %} {% if alert.severity >= 4 %} 普通告警 {% else %} 通知 {% endif %} {% endif %} |


### 迭代

循环语句用于对数组和对象进行迭代操作。支持如下几种使用方式：

| 使用方式 | 示例 |
| --- | --- |
| 数组迭代 | {% for result in alert.results %} {{ result }} {% endfor %} |
| 数组迭代，包含下标 | 使用 enumerate 函数对数组进行下标迭代。关于 enumerate 函数的更多信息，请参见 [enumerate](products/sls/documents/built-in-functions-in-alert-templates.md) [函数](products/sls/documents/built-in-functions-in-alert-templates.md) 。 {% for index, result in enumerate(alert.results) %} {{ index }}: {{ result }} {% endfor %} 下标默认从 0 开始。您也可以通过 enumerate 函数中的 start 参数自定义起始下标。例如： {% for index, result in enumerate(alert.results, start=1) %} {{ index }}: {{ result }} {% endfor %} |
| 对象迭代 | 通过 items()方法将对象转为 Key:Value 形式的数组进行迭代。 {% for key, val in alert.labels.items() %} {{ key }}: {{ val }} {% endfor %} |
| 嵌套使用 | {% for result in alert.fire_results %} {% for key, val in result.items() %} {{ key }}: {{ val }} {% endfor %} {% endfor %} |


### 转义

如果您希望特殊字符串（例如{{）不被内容模板解析和渲染，可对特殊字符串进行转义。例如：根据如下配置表示保留{% raw %}和{% endraw %}之间所有的内容。

- 

内容模板配置

{% raw %} {% for result in alert.results %} {{ result }} {% endfor %} {% endraw %}

- 

结果

{% for result in alert.results %} {{ result }} {% endfor %}

### 函数

内置模板函数便于您对数据进行各种操作，丰富了通知内容的格式和展示样式。更多信息，请参见[内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md)。

例如您要通过Webhook方式发送JSON格式的内容，相关信息如下：

- 

告警的查询语句（包含一个换行）

* | select count(*) as cnt

- 

不同使用方式的对比说明

| 对比项 | 内容模板 | 结果 | 说明 |
| --- | --- | --- | --- |
| 不使用函数 | { "query": "{{ alert.results[0].query }}" } | { "query": "* | select count(*) as pv" } | JSON 格式不合法 |
| 使用 quote 函数 | { "query": {{ quote(alert.results[0].query) }} } | { "query": "* | \nselect count(*) as pv" } | JSON 格式合法 |


### 过滤器

在函数嵌套使用场景中，通知内容的编辑麻烦且不够直观，例如{{ block(to_list(alert.labels)) }}，此时您可以使用过滤器功能。过滤器使用竖线（|） 操作符，并支持链式调用，一般格式为{{ xxx | filiter1 | filter2 | ... }}。例如{{ blockquote(to_list(alert.labels)) }}等同于{{ alert.labels | to_list | blockquote }}。

使用过滤器方式时，请先确认目标内置函数是否支持过滤器方式。大部分内置函数都支持过滤器方式的调用。更多信息，请参见[内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md)。

重要

- 

如果函数中没有参数，则只能使用函数方式，不支持过滤器方式。

- 

当函数中只有一个参数时，推荐使用过滤器方式，即使用{{ arg | fn }}。例如{{ abs(-1) }}等同于{{ -1 | abs }}。

- 

如果函数中有多个参数，且从第二个参数开始有默认值，也可以使用过滤器。如果有多个参数值需要传递，通过过滤器方式并不直观。不建议对多参数的函数使用过滤器方式。

### 操作符

内容模板表达式中支持如下操作符。操作符的优先级说明请参见[Operator precedence](https://docs.python.org/zh-cn/3/reference/expressions.html#operator-precedence)。

- 

- 

- 

| 类别 | 操作符 | 说明 |
| --- | --- | --- |
| 算数 | + | 加法 |
| - | 减法 |  |
| * | 乘法 |  |
| / | 除法，返回值是一个浮点数。 |  |
| // | 除法，返回整数。 |  |
| % | 取模 |  |
| 比较 | == | 等于 |
| != | 不等于 |  |
| > | 大于 |  |
| >= | 大于等于 |  |
| < | 小于 |  |
| <= | 小于等于 |  |
| 逻辑 | and | 且操作 |
| or | 或操作 |  |
| not | 取反 |  |
| 其它 | in | 判断是否包含，返回布尔类型的结果。 数组： {{ 1 in [1, 2, 3] }} 。 对象： {{ "foo" in {"foo": "bar" } }} 。 字符串： {{ "ll" in "hello" }} 。 |
| () | 操作组合，例如：{{ a > b and (a > c or b > c) }} |  |


## 使用告警变量

在新版内容模板中，告警变量的使用形式为alert.xxx，例如alert.project。更多信息，请参见[内容模板变量说明（新版）](products/sls/documents/variables-in-new-alert-templates.md)。

## 配置示例

- 

示例1：根据告警状态展示不同内容

触发告警后，展示告警状态、告警严重度和触发结果等信息；告警恢复时，只展示告警状态。

- 

不使用函数

{% if alert.status == "firing" %} - 状态: <font color="#E03C39">触发</font> - 严重度：{{ alert.severity | format_severity }} - Results: {{ alert.results | to_json }} {% else %} - 状态: <font color="#72C140">恢复</font> {% endif %}

- 

使用函数

使用format_status函数和format_severity函数简化配置。

- 状态: {{ alert.status | format_status }} {% if alert.status == "firing" %} - 严重度：{{ alert.severity | format_severity }} - Results: {{ alert.results | to_json }} {% endif %}

- 

结构化数据展示

将告警标签的内容转换为列表形式，内容为Markdown格式。

- 

不使用函数

- 项目: {{ alert.project }} - 告警名称: {{ alert.alert_name }} - 告警标签: {%- for key, val in alert.labels.items() %} > - {{ key }}: {{ val }} {%- endfor %}

- 

使用函数

使用to_list函数和blockquote函数简化配置。

- 项目: {{ alert.project }} - 告警名称: {{ alert.alert_name }} - 告警标签: {{ alert.labels | to_list | blockquote }}

[上一篇：通知内容定制](products/sls/documents/custom-notification-content.md)[下一篇：内置模板函数](products/sls/documents/built-in-functions-in-alert-templates.md)

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
