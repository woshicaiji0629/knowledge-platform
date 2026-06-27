# 告警条件表达式语法-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/syntax-of-trigger-conditions-in-alert-rules

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

# 告警条件表达式语法

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务根据告警条件表达式的执行结果来判断是否产生告警。

在判断告警条件表达式的执行结果时，您查询语句的执行结果将作为输入，日志字段作为变量，一旦条件为真则触发告警。

## 限制说明

告警条件表达式相关限制说明如下所示：

- 

负数需要使用括号，如 x+(-100)<100。

- 

数值类型都被当成64位浮点数，如果使用比较操作（例如等于）可能存在误差。

- 

变量只能包含字母和数字，且首字母必须是字母。

- 

表达式长度为1~128个字符。

- 

组合求值时最多计算1000种组合，如果没有找到结果为真的组合，则视为false。

- 

最多只支持三个查询。

- 

当且仅当表达式的值为true时，才会触发告警。例如100+100，计算结果为200，不会触发告警。

- 

true、false、美元符号（$）和英文句点（.）是保留词，不能作为变量使用。

## 基础语法

告警条件表达式支持如下语法类型。

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

| 语法类型 | 说明 | 示例 |
| --- | --- | --- |
| 基础运算符 | 支持加减乘除、取模运算符，如下所示： +-*/% | x * 100 + y > 200 x % 10 > 5 |
| 比较运算符 | 支持大于（>）、大于等于（>=）、小于（<）、小于等于（<=）、等于（==）、不等于（!=）、正则匹配 （=~）、 正则不匹配（!~）8 种比较运算符。 说明 反斜线（\）需要转义。 目前正则表达式支持符合 [RE2](https://github.com/google/re2/wiki/Syntax) [规范](https://github.com/google/re2/wiki/Syntax) 的语法。 | x >= 0 x < 100 x <= 100 x == 100 x == "foo" 正则匹配：x =~ "\\w+" |
| 逻辑操作符 | 支持与（&&）、或（||）。 | x >= 0 && y <= 100 x > 0 || y >0 |
| 取反前缀操作 | 支持取反前缀操作（!）。 | !(a < 1 && a > 100) |
| 数值常量 | 支持数值常量，作为 64 位浮点数处理。 | x > 100 |
| 字符串常量 | 支持字符串常量，格式为 '字符串' ，例如'string'。 | foo == 'string' |
| 布尔常量 | 支持布尔常量，true、false。 | (x > 100) == true |
| 括号 | 支持使用括号改变计算的优先级。 | x * (y + 100) > 100 |
| contains 函数 | 支持使用 contains 函数判断是否包含子串，例如 contains(foo, 'hello')返回 true 则表示 foo 中包含 hello 子串。 | contains(foo, 'hello') |


## 多个结果组合求值

- 

语法

支持关联多个查询，在使用多个查询结果进行计算时，变量需要加上特定前缀以区分从哪个结果中获取对应的变量值，格式为$N.fieldname，其中N为查询编号，详情请参见[如何查看查询编号](products/sls/documents/configure-an-alert-rule.md)。目前最多配置三个查询，则N的取值范围为0~2。如$0.foo表示第1个查询的foo字段。当仅有一个查询时，前缀可以省略。

- 

表达式求值

在多个查询结果返回时，根据表达式的变量来判断需要使用哪些结果求值。例如您配置了三个查询，分别返回了x、y、z条结果，告警条件表达式为$0.foo > 100 && $1.bar < 100，则说明判断表达式的值只需要使用前两个结果，进行x*y次求值直到某次求值返回true，或者达到计算次数上限后直接返回false，目前计算次数上限为1000次。

## 运算方式

说明

- 

number为64位浮点数类型。

- 

string常量需要使用单引号或英文双引号进行包裹，例如'string'、"string"。

- 

布尔值包括true和false。

- 

- 

| 运算符 | 运算方式 |  |  |
| --- | --- | --- | --- |
| 变量与变量运算 | 非 string 常量与变量运算 | string 常量与变量运算 |  |
| 四则运算（+-*/%） | 左右值转 number 后运算。 | 不支持。 |  |
| 比较运算： 大于（>）、大于等于（>=）、小于（<）、小于等于（<=）、等于（==）、不等于（!=） | 按照以下优先级决定运算顺序： 左右值转 number 后按照数值序运算，例如转换失败则执行下一优先级的运算。 左右值按 string 类型字典序运算。 | 左右值转 number 后运算（数值序）。 | 左右值按 string 类型运算（字典序）。 |
| 正则是否匹配： 正则匹配 （=~）、 正则不匹配（!~） | 左右值按 string 类型运算。 | 不支持。 | 左右值按 string 类型运算。 |
| 逻辑运算： 与（&&）、或（||） | 不支持对查询结果字段直接应用该运算符，左右值必须分别为子运算式，且运算结果为布尔值。 |  |  |
| 取反前缀（!） | 不支持对查询结果字段直接应用该运算符，被取反的值必须为子运算式，且运算结果为布尔值。 |  |  |
| 字符串查找（contains） | 左右值转 string 类型运算。 | 不支持。 | 左右值按 string 类型运算。 |
| 括号（） | 决定运算结合顺序与优先级。 |  |  |


## 示例

- 

示例1：如果1天（相对）内任务成功率低于90%且延时超过60秒则产生告警。告警名称设置为任务延时告警，关联两个图表：图表0名称为任务成功率，查询语句为* | select round(sum(case when code = 200 then 1 else 0 end) * 100.0 / count(*), 2) as success，查询区间为1天（相对）；图表1名称为延时情况，查询语句为delay > 0 | select time_series(__time__, '10m', '%m-%d %H:%i', '0') as time, round(avg(delay)/100, 3) as delay group by time order by time limit 14400，查询区间为1天（相对）。检查频率为固定间隔15分钟，触发条件为$0.success < 90 && $1.delay > 60。

- 

示例2：如果15分钟内状态码500出现10次则产生告警。告警名称设置为500 状态码报警，关联图表0名称为响应状态分布，查询语句为* | SELECT status, COUNT(*) as total GROUP BY status，查询区间为15分钟（相对）。检查频率为固定间隔15分钟，触发条件为$0.status == 500 && $0.total > 10。

- 

示例3：如果1小时内加工速率低于1000条则产生告警。告警名称设置为数据加工速率过低告警，关联图表0名称为加工速率 (lines/s)，查询语句为__topic__: __etl-log-status__ AND __tag__: __schedule_type__: Resident and event_id: "shard_worker:metrics:checkpoint" | select time_series(__time__, '1m', '%y/%m/%d %H:%i', '0') as dt, round(sum("progress.accept") / 60.0, 3) as "accept", round(sum("progress.dropped") / 60.0, 3) as "dropped", round(sum("progress.delivered") / 60.0, 3) as "delivered", round(sum("progress.failed") / 60.0, 3) as "failed" group by dt order by dt asc limit 10000，查询区间为1小时（相对）。检查频率为固定间隔1小时，触发条件为$0.accept < 1000。

[上一篇：旧版告警的模板变量](products/sls/documents/template-variables.md)[下一篇：告警日志字段](products/sls/documents/fields-in-alert-rule-evaluation-logs.md)

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
