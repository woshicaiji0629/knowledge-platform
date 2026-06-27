# 内容模板内置函数参考手册-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/built-in-functions-in-alert-templates

# 内置模板函数
新版内容模板的内置函数便于您对数据进行各种操作，丰富了通知内容的格式和展示样式。本文介绍内置模板函数的语法及示例。
## 通用函数
### 数学函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| float(value, default=0.0) | 将整数或字符串转换成浮点数。 如果转换失败，默认返回 0.0。通过 default 参数，可指定转换失败的返回值。 | 支持 | {{ float("123") }} 的结果为 123.0。 {{ float("foo") }} 的结果为 0.0。 {{ float("foo", default=1.23) }} 的结果为 1.23。 |
| int(value, default=0) | 将一个字符串或数字转换为整数。 如果转换失败，默认返回 0。通过 default 参数，可指定转换失败的返回值。 | 支持 | {{ int(1.23) }} 的结果为 1。 {{ int("1.23") }} 的结果为 1。 {{ int("foo") }} 的结果为 0。 {{ int("foo", default=5) }} 的结果为 5。 |
| length(value) | 返回对象（字符串、列表、元组等）的长度或个数。 | 支持 | {{ length("foo") }} 的结果为 3。 {{ length([1, 2]) }} 的结果为 2。 {{ length({"foo": "bar"}) }} 的结果为 1。 |
| abs(value) | 返回数字的绝对值。 | 支持 | {{ abs(-1) }} 的结果为 1。 |
| min(value) | 返回最小值。 | 支持 | {{ min([1, 3, 2]) }} 的结果为 1。 |
| max(value) | 返回最大值。 | 支持 | {{ max([1, 3, 2]) }} 的结果为 3。 |
| ceil(value) | 向上取整数。 | 支持 | {{ ceil(1.23) }} 的结果为 2。 |
| floor(value) | 向下取整数。 | 支持 | {{ floor(1.23) }} 的结果为 1。 |
| round(value, 1) | 四舍五入取整数。 其中， 1 表示保留 1 位小数。 | 支持 | {{ round(1.23) }} 的结果为 1。 {{ round(1.56) }} 的结果为 2。 {{ round(1.56, 1) }} 的结果为 1.6。 |
| sum(value) | 求和计算。 | 支持 | {{ sum([1, 2, 3]) }} 的结果为 6。 |
### 字符串函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| string(value) | 将对象转为字符串类型。 | 支持 | {{ string(1.23) }} 的结果为 1.23。 此处的 1.23 为字符串类型。 |
| capitalize(value) | 将字符串的首字母转换为大写形式，其它字符转换为小写形式。 | 支持 | {{ capitalize("heLLO World") }} 的结果为 Hello world。 |
| lower(value) | 将字符串转换为小写形式。 | 支持 | {{ lower("FOO") }} 的结果为 foo。 |
| upper(value) | 将字符串转换为大写形式。 | 支持 | {{ upper("foo") }} 的结果为 FOO。 |
| title(value) | 返回标题化的字符串，即每个单词的首字母为大写形式，其余字母为小写形式。 | 支持 | {{ title("hello world") }} 的结果为 Hello World。 |
| trim(value) | 删除字符串头尾的空字符。 | 支持 | {{ trim(" foo\n") }} 的结果为 foo。 |
| replace(value, old, new) | 替换目标字符串。 | 不支持 | {{ replace("foo", "oo", "ly") }} 的结果为 fly。 |
| wordcount(value) | 统计单词个数。 | 支持 | {{ wordcount("hello world") }} 的结果为 2。 |
| truncate(value, n, end='') | 截断字符串。 通过 truncate(value, n)，指定截断的字符数。 通过 truncate(value, n, end='...')，指定要添加的后缀。 | 不支持 | {{ truncate("foo bar", 5) }} 的结果为 foo b。 {{ truncate("foo bar", 5, end="...") }} 的结果为 foo b...。 |
| quote(value) | 使用半角双引号（""）包裹字符串。 | 支持 | {{ quote(123) }} 的结果为"123" {{ quote("foo") }} 的结果为 "foo"。 |
| indent(value, n=4) | 对每一行字符串进行缩进，默认缩进 4 个空格。 通过 n 参数，可指定缩进的空格数。 | 支持 | {{ "foobar\n" }}{{ indent("foo\nbar") }} 的结果如下： foobar foo bar {{ "foobar\n" }}{{ indent("foo\nbar", 2) }} 的结果如下： foobar foo bar |
| startswith(value, prefix) | 判断字符串是否以特定子串开始。 | 支持 | {{ startswith("football", "foo") }} 的结果为 true。 |
| endswith(value, suffix) | 判断字符串是否以特定子串结束。 | 支持 | {{ endswith("football", "all") }} 的结果为 true。 |
| removeprefix(value, prefix) | 移除字符串的前缀。 | 支持 | {{ removeprefix("football", "foot") }} 的结果为 ball。 |
| removesuffix(value, suffix) | 移除字符串的后缀。 | 支持 | {{ removesuffix("football", "ball") }} 的结果为 foot。 |
| split(value, sep=None, maxsplit=-1) | 切割字符串。 通过 sep 参数指定分隔符。 通过 maxsplit 参数限制切割次数。 如果未指定 maxsplit 或设置为-1，表示对切割数量没有限制。 | 支持 | {{ split('a b c ') }} 的结果为['a', 'b', 'c']。 {{ split('a-b-c', sep='-') }} 的结果为['a', 'b', 'c']。 {{ split('a-b-c', sep='-', maxsplit=1) }} 的结果为['a', 'b-c']。 {{ split('a<>b<>c', sep='<>') }} 的结果为['a', 'b', 'c']。 |
### 列表和对象函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| enumerate(value) | 将一个可迭代的对象组合为一个索引序列，并列出原始元素和元素的下标。 | 不支持 | {{ enumerate(["foo", "bar"]) }} 的结果为[(0, 'foo'), (1, 'bar')]。 |
| list(value) | 将一个可迭代的对象转换为列表类型。 | 支持 | {{ list(("foo", "bar")) }} 的结果为 ['foo', 'bar']。 {{ list("foo") }} 的结果为 ['f', 'o', 'o']。 |
| dict(value) | 创建一个字典，类似于直接使用 {} 创建字典。 | 不支持 | {{ dict(foo=1, bar="hello") }} 的结果为{'foo': 1, 'bar': 'hello'}。 |
| first(value) | 返回列表中的第一项。 | 支持 | {{ first([1, 2, 3]) }} 的结果为 1。 |
| last(value) | 返回列表中的最后一项。 | 支持 | {{ last([1, 2, 3]) }} 的结果为 3。 |
| sort(value, reverse=true) | 对列表中的元素进行排序。 通过 reverse=true ，可实现逆序排序。 | 支持 | {{ sort([3, 1, 2]) }} 的结果为[1, 2, 3]。 {{ sort([3, 1, 2], reverse=true) }} 的结果为[3, 2, 1]。 |
| dictsort(value) | 将对象中的键值对（Key:Value）按照 Key 进行排序，返回数组。 | 支持 | alert.labels 字段示例 { "host": "host-1", "app": "nginx" } 内容模板配置 {%- for key, val in dictsort(alert.labels) %} {{ key }}: {{ val }} {%- endfor %} 结果 app: nginx host: host-1 |
| join(value, d='') | 使用连接符连接列表中的元素。 通过 d 参数，可指定连接符。 | 支持 | {{ join([1, 2, 3]) }} 的结果为 123。 {{ join([1, 2, 3], ',') }} 的结果为 1,2,3。 |
### 格式化函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| escape_markdown(value) | 转义特殊的 Markdown 字符。 | 支持 | {{ escape_markdown("__a__ **b** #c") }} 的结果为 &#95;&#95;a&#95;&#95; &#42;&#42;b&#42;&#42; &#35;c 。 |
| escape_html(value) | 转义特殊的 HTML 字符。 | 支持 | {{ escape_html("<div>") }} 的结果为 &lt;div&gt; 。 |
| to_json(value) | 将对象转为 JSON 格式。 | 支持 | {{ to_json("foo") }} 的结果为"foo"。 {{ to_json(1.23) }} 的结果为 1.23。 {{ to_json(True) }} 的结果为 true。 {{ to_json(alert.labels) }} 的结果为{"host": "host-1", "app": "nginx"}。 |
| parse_json(value) | 将字符串解析为 JSON 数据结构。 | 支持 | {{ parse_json('{"foo": "bar"}').foo }} 的结果为 bar。 {{ parse_json('[1, 2, 3]')[1] }} 的结果为 2。 |
### 编码和解码函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| base64_encoding(value) | 对输入值进行 Base64 编码。 | 支持 | {{ base64_encoding("foo") }} 的结果为 Zm9v。 |
| base64_decoding(value) | 对输入值进行 Base64 解码。 | 支持 | {{ base64_decoding("Zm9v") }} 的结果为 foo。 |
| md5_encoding(value) | 对输入值进行 MD5 编码。 | 支持 | {{ md5_encoding("foo") }} 的结果为 acbd18db4cc2f85cedef654fccc4a4d8。 |
| url_encoding(value) | 对输入值进行 URL 编码。 | 支持 | {{ url_encoding("https://example.com?a=b&c=d") }} 的结果为 https%3A%2F%2Fexample.com%3Fa%3Db%26c%3Dd。 |
| url_decoding(value) | 对输入值进行 URL 解码。 | 支持 | {{ url_decoding("https%3A%2F%2Fexample.com%3Fa%3Db%26c%3Dd") }} 的结果为 https://example.com?a=b&c=d。 |
### 日期和时间函数
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| parse_date(value, fmt="%Y-%m-%d %H:%M:%S") | 将输入值转为 timestamp 类型的日期和时间表达式。 通过 fmt 参数，可指定日期和时间表达式的格式。 | 支持 | {{ parse_date(1629820800) }} 的结果为 2021-08-25 00:00:00。 {{ parse_date("2021|08|25|00|00|00", fmt="%Y|%m|%d|%H|%M|%S") }} 的结果为 2021-08-25 00:00:00。 |
| format_date(value, tz=None, fmt="%Y-%m-%d %H:%M:%S") | 将输入值进行格式化。 通过 fmt 参数，可指定日期和时间表达式的格式。 如果输入值不是日期对象，则函数会将其转换为日期对象，再进行格式化。关于日期时间格式化指令的更多信息，请参见 [日期时间格式化指令](date-and-time-formatting-directives.md) 。关于时区列表的更多信息，请参见 [时区列表](time-zones.md) 。 | 不支持 | {{ format_date(1629820800) }} 的结果为 2021-08-25 00:00:00。 {{ format_date(1629820800, fmt="%Y/%m/%d %H:%M:%S") }} 的结果为 2021/08/25 00:00:00。 {{ format_date(1629820800, tz="UTC", fmt="%Y/%m/%d %H:%M:%S") }} 的结果为 2021/08/24 16:00:00。 |
| timestamp(value) | 将时间和日期字符串转换为 Unix 时间戳。 如果输入值不是日期对象，则函数会将其转换为日期对象，再进行格式化。 | 支持 | {{ timestamp("2021-08-25 00:00:00") }} 的结果为 1629820800。 {{ timestamp(parse_date("2021-08-25 00:00:00")) }} 的结果为 1629820800。 |
| format_duration(value, locale='en-US', sep='') | 格式化时间间隔。其中 value 的单位为秒。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | {{ 10 | format_duration }} 的结果为 10s。 {{ 60 | format_duration }} 的结果为 1m。 {{ 3600 | format_duration }} 的结果为 1h。 {{ 86400 | format_duration }} 的结果为 1d。 {{ 100000 | format_duration }} 的结果为 1d3h46m40s。 {{ 100000 | format_duration(sep=",") }} 的结果为 1d,3h,46m,40s。 {{ 100000 | format_duration(locale="zh-CN") }} 的结果为 1 天 3 小时 46 分钟 40 秒。 |
## 告警业务函数
告警业务函数是和告警上下文以及内容模板配置相关，可自动感知如下信息：
说明
在不同的告警上下文中执行告警业务函数时，返回的结果有可能不同。
告警属性，例如当前告警的严重度、状态等。
内容模板语言配置，例如是中文、英文。
通知渠道，例如钉钉、邮件等。
| 函数 | 说明 | 过滤器 | 示例 |
| --- | --- | --- | --- |
| format_type(alert.type, locale=None) | 将告警类型转换为文字描述。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | 告警类型为 sls_pub 内容模板配置 {{ format_type(alert.type) }} 结果 内容模板中的语言配置为中文时，通知内容为 开放告警 。 内容模板中的语言配置为英文时，通知内容为 Pub Alert 。 |
| format_region(alert.region, locale=None) | 将告警所在地域转换为文字描述。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | 当前告警地域为 cn-hangzhou 内容模板配置 {{ format_region(alert.region) }} 结果 内容模板中的语言配置为中文时，通知内容为 华东 1（杭州） 。 内容模板中的语言配置为英文时，通知内容为 China (Hangzhou) 。 |
| format_severity(alert.severity, locale=None) | 将告警严重度转换为文字描述，且支持彩色字体。 说明 目前只有钉钉、企业微信、邮件和消息中心这四个渠道支持彩色文本。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | 告警严重度为 6 内容模板配置 {{ format_severity(alert.severity) }} 结果 内容模板中的语言配置为中文时，通知内容为 中级 ，黄色字体。 内容模板中的语言配置为英文时，通知内容为 Medium ，黄色字体。 |
| format_status(alert.status, locale=None) | 将告警状态转换为文字描述，且支持彩色字体。 说明 目前只有钉钉、企业微信、邮件和消息中心这四个渠道支持彩色文本。其他渠道时调用该函数会无改变。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | 当前告警为 触发状态 内容模板配置 {{ format_status(alert.status) }} 结果 内容模板中的语言配置为中文时，通知内容为 触发 ，红色字体。 内容模板中的语言配置为英文时，通知内容为 Firing ，红色字体。 |
| to_list(value) | 将数组或对象转换为列表。 | 支持 | 告警标签 { "app": "nginx", "host": "host-1" } 内容模板配置 {{ to_list(alert.labels) }} 结果 通知内容为 Markdown 格式时，返回结果如下： 支持根据渠道是否需要进行 Markdown 转义而自动转义。 - app: nginx - host: host&#45;1 通知内容为 HTML 格式时，返回结果如下： <ul> <li>app: nginx</li> <li>host: host-1</li> </ul> 通知内容为普通文本格式时，返回结果如下： [app: nginx][host: host-1] |
| annotations_to_list(alert.annotations, locale=None) | 将告警标注转换为列表形式。类似于 to_list(alert.annotations)，区别在于 annotations_to_list 函数支持自动将标准名称转换为文字描述，例如将 title 字段转换为 标题 或者 Title 。标准名称列表，请参见 [告警标注字段映射](built-in-functions-in-alert-templates.md) 。 通过 locale 参数，可指定文字的语言。 locale 参数的取值请参见 [告警业务函数](built-in-functions-in-alert-templates.md) [locale](built-in-functions-in-alert-templates.md) [取值](built-in-functions-in-alert-templates.md) 。 | 支持 | 告警标注 { "title": "Nginx 访问异常", "desc": "PV 同比下降 80%", "cnt": "120" } 内容模板配置 {{ annotations_to_list(alert.annotations) }} 结果 通知内容为 Markdown 格式时，返回结果如下： - 标题: Nginx 访问异常 - 描述: PV 同比下降 80% - cnt: 120 |
| blockquote(value) | 为通知内容添加引用样式。 通知内容为 Markdown 格式时，在每一行的开头添加 > 符号。 通知内容为 HTML 格式时，使用 <blockquote> 标签包裹通知内容。 | 支持 | 内容模板配置 {{ blockquote("foo\nbar") }} 结果 通知内容为 Markdown 格式时，返回结果如下： > foo > bar 通知内容为 HTML 格式时，返回结果如下： <blockquote> foo bar </blockquote> |
## 参考信息
告警业务函数中locale参数的取值
| locale 取值 | 说明 |
| --- | --- |
| None 或空字符串 | 使用内容模板中配置的语言。 |
| en-US | 英文。 |
| zh-CN | 中文。 |
告警标注字段映射
| 标注 | 映射值（中文） | 映射值（英文） |
| --- | --- | --- |
| title | 标题 | Title |
| desc | 描述 | Description |
| anomaly_score | 异常分数 | Anomaly Score |
| job_id | 任务 ID | Task ID |
| model_id | 模型 ID | Model ID |
| severity | 异常严重度 | Anomaly Severity |
| __pub_alert_app__ | 应用 | Application |
| __pub_alert_protocol__ | 协议 | Protocol |
| __pub_alert_region__ | 接入区域 | Region |
| __pub_alert_service__ | 服务 | Service |
| __ensure_url__ | 异常确认 | Anomaly Confirmation |
| __mismatch_url__ | 误报确认 | False Positive Confirmation |
| __plot_image__ | 时序图 | Time Series Chart |
| __host_ip__ | 机器地址 | Machine Address |
| __host_group_name__ | 机器组名称 | Machine Group Name |
| __cloud_monitor_type__ | 阿里云云监控 | CloudMonitor |
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
