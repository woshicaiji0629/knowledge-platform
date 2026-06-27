# 处理插件-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/processing-plug-ins

# 数据采集时处理（处理插件）
处理插件用于将原始日志进一步解析为结构化数据。
## 背景信息
处理插件可分为原生处理插件和扩展处理插件。
原生插件：性能较优，适用于大部分业务场景，推荐优先使用。
扩展插件：功能覆盖更广，当您的业务日志过于复杂，无法使用原生插件处理时，可以考虑使用扩展插件完成日志解析，但性能会受到一定影响。
## 使用限制
### 性能限制
使用扩展插件进行日志处理时，采集器会消耗更多的资源（以CPU为主），请根据实际情况调整采集器的参数配置，更多信息请参见[配置管理](loongcollector-management-linux.md)。
当原始数据量的生成速度超过5 MB/s时，不建议使用过于复杂的插件组合来处理日志，推荐使用扩展插件进行简单处理，再通过[数据加工](data-transformation-overview.md)完成进一步处理。
### 日志采集限制
扩展插件对文本日志的处理采用行模式，即文件级别的元数据（例如__tag__:__path__、__topic__等）会被存放到每一条日志中。
添加扩展插件后会影响和Tag相关的功能：
上下文查询和LiveTail功能不可用。如果您要使用这些功能，需要额外添加aggregators配置。
__topic__字段会被重命名为__log_topic__。如果您添加了aggregators配置，日志中将同时存在__topic__字段和__log_topic__字段。如果您不需要__log_topic__字段，可使用[processor_drop](drop-fields.md)插件删除该字段。
__tag__:__path__等字段不再具备原生字段索引，需要[创建字段索引](create-indexes.md)。
### 插件组合限制
Logtail 2.0以下版本（不包括2.0版本）：
不支持同时添加原生插件和扩展插件。
原生插件仅可用于采集文本日志。使用原生插件时，须符合如下要求：
第一个处理插件必须为正则解析插件、分隔符模式解析插件、JSON解析插件、Nginx模式解析插件、Apache模式解析插件或IIS模式解析插件。
第一个处理插件之后仅允许存在1个时间解析处理插件，1个过滤插件和多个脱敏插件。
Logtail 2.0版本：扩展处理插件只能出现在所有的原生处理插件之后，不能出现在任何原生处理插件之前。
### 原生插件解析参数组合限制
对于Logtail2.0以下版本的正则解析、JSON解析、分隔符解析、Nginx模式解析、Apache模式解析、IIS模式解析的原生插件，您可以根据不同场景选择不同的参数配置组合。其余的配置组合无效，日志服务不能保证配置效果。
只上传解析成功的日志：
不勾选解析失败时保留原始字段和解析成功时保留原始字段。
解析成功时上传解析后的日志，解析失败时上传原始日志：
勾选解析失败时保留原始字段，不勾选解析成功时保留原始字段，将重命名的原始字段设置为__raw__。
解析成功时不仅上传解析后的日志，且追加原始日志字段，解析失败时上传原始日志。
例如，原始日志"content": "{"request_method":"GET", "request_time":"200"}"解析成功，追加原始字段是在解析后日志的基础上再增加一个字段，字段名为重命名的原始字段（如果不填则默认为原始字段名），字段值为原始日志{"request_method":"GET", "request_time":"200"}。
勾选解析失败时保留原始字段和解析成功时保留原始字段，打开高级参数开关并填入{"CopingRawLog":true}。对于 Logtail 2.0 以下版本，仅部分参数组合有效。
## 处理插件列表
### 原生插件列表
| 插件名称 | 说明 |
| --- | --- |
| 正则解析 | [原生插件：正则解析](regular-parsing.md) |
| JSON 解析 | [原生插件：JSON](json-parsing.md) [解析](json-parsing.md) |
| 分隔符模式解析 | [原生插件：分隔符模式解析](separator-pattern-resolution.md) |
| Nginx 模式解析 | [原生插件：Nginx](nginx-schema-parsing.md) [模式解析](nginx-schema-parsing.md) |
| Apache 模式解析 | [原生插件：Apache](apache-pattern-parsing.md) [模式解析](apache-pattern-parsing.md) |
| IIS 模式解析 | [原生插件：IIS](iis-schema-parsing.md) [模式解析](iis-schema-parsing.md) |
| 时间解析 | [原生插件：时间解析](time-parsing.md) |
| 过滤处理 | [原生插件：过滤处理](filtration-treatment.md) |
| 脱敏处理 | [原生插件：脱敏处理插件](desensitization-treatment.md) |
### 扩展插件
| 功能 | 说明 |
| --- | --- |
| 提取字段 | [正则模式](extract-content-from-log-fields.md) |
| [标定模式](extract-content-from-log-fields.md) |  |
| [CSV](extract-content-from-log-fields.md) [模式](extract-content-from-log-fields.md) |  |
| [单字符分隔符模式](extract-content-from-log-fields.md) |  |
| [多字符分隔符模式](extract-content-from-log-fields.md) |  |
| [键值对模式](extract-content-from-log-fields.md) |  |
| [Grok](extract-content-from-log-fields.md) [模式](extract-content-from-log-fields.md) |  |
| 添加字段 | [扩展插件：添加字段](add-fields.md) |
| 丢弃字段 | [扩展插件：丢弃字段](drop-fields.md) |
| 重命名字段 | [扩展插件：重命名字段](rename-fields.md) |
| 打包字段 | 将一个或多个字段打包为一个 JSON Object 格式的字段。更多信息，请参见 [扩展插件：打包字段](encapsulate-fields.md) 。 |
| 展开 JSON 字段 | [扩展插件：展开](expand-json-fields.md) [JSON](expand-json-fields.md) [字段](expand-json-fields.md) |
| 过滤日志 | 通过正则表达式匹配日志字段的值，从而实现日志过滤。更多信息，请参见 [processor_filter_regex](filter-logs.md) 。 |
| 通过正则表达式匹配日志字段名称，从而实现日志过滤。更多信息，请参见 [processor_filter_key_regex](filter-logs.md) 。 |  |
| 提取日志时间 | 解析原始日志中的时间字段，并可将解析结果设置为日志时间。更多信息，请参见 [Go](extract-log-time.md) [语言时间格式](extract-log-time.md) 。 |
| 转换 IP 地址 | 将日志中的 IP 地址转换为地理位置（国家、省份、城市、经纬度）。更多信息，请参见 [扩展插件：转换](convert-ip-addresses.md) [IP](convert-ip-addresses.md) [地址](convert-ip-addresses.md) 。 |
| 数据脱敏 | 将日志中的敏感数据替换为指定字符串或 MD5 值。更多信息，请参见 [扩展插件：数据脱敏](desensitization-plug-in.md) 。 |
| 字段值映射 | [扩展插件：字段值映射处理](map-field-values.md) |
| 字段加密 | [扩展插件：字段加密](encrypt-fields.md) |
| 数据编码与解码 | [BASE64](encode-and-decode-data.md) [解码](encode-and-decode-data.md) |
| [BASE64](encode-and-decode-data.md) [编码](encode-and-decode-data.md) |  |
| [MD5](encode-and-decode-data.md) [编码](encode-and-decode-data.md) |  |
| Log 转为 Metric | 将采集到的日志转成 SLS Metric。更多信息，请参见 [扩展插件：Log](log-to-metric.md) [转为](log-to-metric.md) [Metric](log-to-metric.md) 。 |
| Log 转为 Trace | 将采集到的日志转成 SLS Trace。更多信息，请参见 [扩展插件：Log](log-to-trace.md) [转为](log-to-trace.md) [Trace](log-to-trace.md) 。 |
## 添加插件
### 在修改配置时添加插件
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储的日志库页签中，单击目标日志库前面的>，选择数据接入下的Logtail配置。
单击目标Logtail配置对应操作列的管理Logtail配置。
在Logtail配置列表中，单击目标Logtail配置后操作列的管理Logtail配置。
单击页面上方的编辑，在页面下方的处理配置区域，新增插件，然后单击保存。
### 在创建配置时添加插件
登录[日志服务控制台](https://sls.console.aliyun.com)。
单击控制台页面右侧的快速接入数据卡片。
在接入数据对话框中，单击任意卡片，按照配置向导进行操作，在Logtail配置步骤中添加插件。具体操作，请参见[采集主机文本日志](collect-host-logs.md)。
说明
该插件配置与在修改配置时的插件配置相同。
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
