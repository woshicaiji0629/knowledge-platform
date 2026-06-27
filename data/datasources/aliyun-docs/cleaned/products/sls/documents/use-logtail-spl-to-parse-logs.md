# 使用Logtail SPL解析日志-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/use-logtail-spl-to-parse-logs

# 使用Logtail SPL解析日志
iLogtail 支持三种处理模式：原生插件模式（C++实现，性能最强）、拓展插件模式（Go实现，生态丰富且灵活）和SPL模式（在iLogtail 2.0中引入，结合了性能和灵活性）。通过编写SPL语句，您可以充分利用其计算能力来处理数据。本文将介绍如何使用SPL语句实现与其他两种处理模式相同的功能。
## 前提条件
已开通日志服务。具体操作，请参见[存储资源层级关系说明](resource-management-overview.md)。
## 使用限制
SPL采集日志仅支持Logtail 2.0及以上版本。
文本日志采集支持通过控制台配置，其他数据接入暂不支持控制台配置，请通过API或CRD配置。
## 使用示例
SPL 使用示例请参见[使用](use-spl-to-collect-text-logs.md)[SPL](use-spl-to-collect-text-logs.md)[采集文本日志](use-spl-to-collect-text-logs.md)。
SPL 使用场景请参见[数据处理最佳实践](spl-data-processing-best-practices.md)。
## 操作步骤
## 在修改Logtail配置时添加SPL
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标日志库前面的>，依次选择数据接入>Logtail配置。
在Logtail配置列表中，单击目标Logtail配置后操作列的管理Logtail配置。
单击页面上方的编辑，在页面下方的处理配置区域，处理配置中处理模式选择SPL，然后单击保存。
全局配置
| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。更多信息，请参见 [日志主题](log-topics.md) 。 机器组 Topic ：设置为机器组的 Topic 属性，用于明确区分不同机器组产生的日志。 文件路径提取 ：设置为文件路径正则，则需要设置 自定义正则 ，用正则表达式从路径里提取一部分内容作为 Topic。用于区分不同源产生的日志。 自定义： 自定义日志主题。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
输入配置
###
###
###
| 配置项 | 说明 |
| --- | --- |
| 文件路径 | 根据日志在主机（例如 ECS）上的位置，设置日志目录和文件名称。 如果目标主机是 Linux 系统，则日志路径必须以正斜线（/）开头，例如 /apsara/nuwa/**/app.Log 。 如果目标主机是 Windows 系统，则日志路径必须以盘符开头，例如 C:\Program Files\Intel\**\*.Log 。 目录名和文件名均支持完整模式和通配符模式，文件名规则请参见 [Wildcard matching](https://man7.org/linux/man-pages/man7/glob.7.html) 。其中，日志路径通配符只支持星号（*）和半角问号（?）。 日志文件查找模式为多层目录匹配，即符合条件的指定目录（包含所有层级的目录）下所有符合条件的文件都会被查找到。例如： /apsara/nuwa/**/*.log 表示 /apsara/nuwa 目录（包含该目录的递归子目录）中后缀名为.log 的文件。 /var/logs/app_*/**/*.log 表示 /var/logs 目录下所有符合 app_* 格式的目录（包含该目录的递归子目录）中后缀名为 .log 的文件。 /var/log/nginx/**/access* 表示 /var/log/nginx 目录（包含该目录的递归子目录）中以 access 开头的文件。 |
| 最大目录监控深度 | 设置日志目录被监控的最大深度，即 文件路径 中通配符 ** 匹配的最大目录深度。0 代表只监控本层目录。 |
| 文件编码 | 选择日志文件的编码格式。 |
| 首次采集大小 | 配置首次生效时，匹配文件的起始采集位置距离文件结尾的大小。首次采集大小设定值为 1024 KB。 首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。 首次采集时，如果文件大于 1024 KB，则从距离文件末尾 1024 KB 的位置开始采集。 您可以通过此处修改 首次采集大小 ，取值范围为 0~10485760，单位为 KB。 |
| 采集黑名单 | 打开 采集黑名单 开关后，可进行黑名单配置，即可在采集时忽略指定的目录或文件。支持完整匹配和通配符匹配目录和文件名。其中，通配符只支持星号（*）和半角问号（?）。 重要 如果您在配置 文件路径 时使用了通配符，但又需要过滤掉其中部分路径，则需在 采集黑名单 中填写对应的完整路径来保证黑名单配置生效。 例如您配置 文件路径 为 /home/admin/app*/log/*.log ，但要过滤 /home/admin/app1* 目录下的所有子目录，则需选择 目录黑名单 ，配置目录为 /home/admin/app1*/** 。如果配置为 /home/admin/app1* ，黑名单不会生效。 匹配黑名单过程存在计算开销，建议黑名单条目数控制在 10 条内。 目录路径不能以正斜线（/）结尾，例如将设置路径为 /home/admin/dir1/ ，目录黑名单不会生效。 支持按照文件路径黑名单、文件黑名单、目录黑名单设置，详细说明如下： 文件路径黑名单 选择 文件路径黑名单 ，配置路径为 /home/admin/private*.log ，则表示在采集时忽略 /home/admin/ 目录下所有以 private 开头，以.log 结尾的文件。 选择 文件路径黑名单 ，配置路径为 /home/admin/private*/*_inner.log ，则表示在采集时忽略 /home/admin/ 目录下以 private 开头的目录内，以_inner.log 结尾的文件。例如 /home/admin/private/app_inner.log 文件被忽略， /home/admin/private/app.log 文件被采集。 文件黑名单 选择 文件黑名单 ，配置文件名为 app_inner.log ，则表示采集时忽略所有名为 app_inner.log 的文件。 目录黑名单 选择 目录黑名单 ，配置目录为 /home/admin/dir1 ，则表示在采集时忽略 /home/admin/dir1 目录下的所有文件。 选择 目录黑名单 ，配置目录为 /home/admin/dir* ，则表示在采集时忽略 /home/admin/ 目录下所有以 dir 开头的子目录下的文件。 选择 目录黑名单 ，配置目录为 /home/admin/*/dir ，则表示在采集时忽略 /home/admin/ 目录下二级目录名为 dir 的子目录下的所有文件。例如 /home/admin/a/dir 目录下的文件被忽略， /home/admin/a/b/dir 目录下的文件被采集。 |
| 允许文件多次采集 | 默认情况下，一个日志文件只能匹配一个 Logtail 配置。如果文件中的日志需要被采集多份，需要打开 允许文件多次采集 开关。 |
| 高级参数 | 其它可选的与文件输入插件相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
处理配置
| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助您配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:½0) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，保留为一共四条日志。 |
| 处理模式 | 处理模式 选择 SPL 。 |
| SPL 语句 | SPL 语句具体请参考 [SPL](user-guide/spl-syntax.md) [语法](user-guide/spl-syntax.md) 。解析日志前，日志默认存在 content 字段中。 |
| 超时时间 | SPL 语句执行一次的最大时间。 |
## 在创建Logtail配置时添加SPL
登录[日志服务控制台](https://sls.console.aliyun.com)。
在快速数据接入对话框的自建开源/商业软件页签下，选择包含文本日志后缀的入口。
说明
目前SPL采集支持文本日志采集，其他数据接入（Kubernetes - 标准输出、Docker标准输出等）暂不支持控制台配置。
在快速接入数据区域，单击接入数据进入快速数据接入对话框。
在选择日志空间页面，按照选择目标Project和Logstore，单击下一步。
在机器组配置页面，配置机器组。
根据实际需求，选择使用场景和安装环境。
重要
无论是否已有机器组，都必须根据实际需求正确选择使用场景和安装环境，这将影响后续的页面配置。
确认目标机器组已在应用机器组区域，单击下一步。
### 已有机器组
从源机器组列表选择目标机器组。
### 没有可用机器组
单击创建机器组，在创建机器组面板设置相关参数。机器组标识分为IP地址和用户自定义标识，更多信息请参见[创建用户自定义标识机器组（推荐）](create-a-user-defined-identity-machine-group.md)或[创建](create-an-ip-address-based-machine-group.md)[IP](create-an-ip-address-based-machine-group.md)[地址机器组](create-an-ip-address-based-machine-group.md)。
重要
创建机器组后立刻应用，可能因为连接未生效，导致心跳为FAIL，您可单击自动重试。如果还未解决，请参见[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
创建Logtail配置，单击下一步，创建Logtail配置。全局配置、输入配置和处理插件相同，处理配置中处理模式选择SPL。
全局配置
| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。更多信息，请参见 [日志主题](log-topics.md) 。 机器组 Topic ：设置为机器组的 Topic 属性，用于明确区分不同机器组产生的日志。 文件路径提取 ：设置为文件路径正则，则需要设置 自定义正则 ，用正则表达式从路径里提取一部分内容作为 Topic。用于区分不同源产生的日志。 自定义： 自定义日志主题。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
输入配置
###
###
###
| 配置项 | 说明 |
| --- | --- |
| 文件路径 | 根据日志在主机（例如 ECS）上的位置，设置日志目录和文件名称。 如果目标主机是 Linux 系统，则日志路径必须以正斜线（/）开头，例如 /apsara/nuwa/**/app.Log 。 如果目标主机是 Windows 系统，则日志路径必须以盘符开头，例如 C:\Program Files\Intel\**\*.Log 。 目录名和文件名均支持完整模式和通配符模式，文件名规则请参见 [Wildcard matching](https://man7.org/linux/man-pages/man7/glob.7.html) 。其中，日志路径通配符只支持星号（*）和半角问号（?）。 日志文件查找模式为多层目录匹配，即符合条件的指定目录（包含所有层级的目录）下所有符合条件的文件都会被查找到。例如： /apsara/nuwa/**/*.log 表示 /apsara/nuwa 目录（包含该目录的递归子目录）中后缀名为.log 的文件。 /var/logs/app_*/**/*.log 表示 /var/logs 目录下所有符合 app_* 格式的目录（包含该目录的递归子目录）中后缀名为 .log 的文件。 /var/log/nginx/**/access* 表示 /var/log/nginx 目录（包含该目录的递归子目录）中以 access 开头的文件。 |
| 最大目录监控深度 | 设置日志目录被监控的最大深度，即 文件路径 中通配符 ** 匹配的最大目录深度。0 代表只监控本层目录。 |
| 文件编码 | 选择日志文件的编码格式。 |
| 首次采集大小 | 配置首次生效时，匹配文件的起始采集位置距离文件结尾的大小。首次采集大小设定值为 1024 KB。 首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。 首次采集时，如果文件大于 1024 KB，则从距离文件末尾 1024 KB 的位置开始采集。 您可以通过此处修改 首次采集大小 ，取值范围为 0~10485760，单位为 KB。 |
| 采集黑名单 | 打开 采集黑名单 开关后，可进行黑名单配置，即可在采集时忽略指定的目录或文件。支持完整匹配和通配符匹配目录和文件名。其中，通配符只支持星号（*）和半角问号（?）。 重要 如果您在配置 文件路径 时使用了通配符，但又需要过滤掉其中部分路径，则需在 采集黑名单 中填写对应的完整路径来保证黑名单配置生效。 例如您配置 文件路径 为 /home/admin/app*/log/*.log ，但要过滤 /home/admin/app1* 目录下的所有子目录，则需选择 目录黑名单 ，配置目录为 /home/admin/app1*/** 。如果配置为 /home/admin/app1* ，黑名单不会生效。 匹配黑名单过程存在计算开销，建议黑名单条目数控制在 10 条内。 目录路径不能以正斜线（/）结尾，例如将设置路径为 /home/admin/dir1/ ，目录黑名单不会生效。 支持按照文件路径黑名单、文件黑名单、目录黑名单设置，详细说明如下： 文件路径黑名单 选择 文件路径黑名单 ，配置路径为 /home/admin/private*.log ，则表示在采集时忽略 /home/admin/ 目录下所有以 private 开头，以.log 结尾的文件。 选择 文件路径黑名单 ，配置路径为 /home/admin/private*/*_inner.log ，则表示在采集时忽略 /home/admin/ 目录下以 private 开头的目录内，以_inner.log 结尾的文件。例如 /home/admin/private/app_inner.log 文件被忽略， /home/admin/private/app.log 文件被采集。 文件黑名单 选择 文件黑名单 ，配置文件名为 app_inner.log ，则表示采集时忽略所有名为 app_inner.log 的文件。 目录黑名单 选择 目录黑名单 ，配置目录为 /home/admin/dir1 ，则表示在采集时忽略 /home/admin/dir1 目录下的所有文件。 选择 目录黑名单 ，配置目录为 /home/admin/dir* ，则表示在采集时忽略 /home/admin/ 目录下所有以 dir 开头的子目录下的文件。 选择 目录黑名单 ，配置目录为 /home/admin/*/dir ，则表示在采集时忽略 /home/admin/ 目录下二级目录名为 dir 的子目录下的所有文件。例如 /home/admin/a/dir 目录下的文件被忽略， /home/admin/a/b/dir 目录下的文件被采集。 |
| 允许文件多次采集 | 默认情况下，一个日志文件只能匹配一个 Logtail 配置。如果文件中的日志需要被采集多份，需要打开 允许文件多次采集 开关。 |
| 高级参数 | 其它可选的与文件输入插件相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
处理配置
| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助您配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:½0) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，保留为一共四条日志。 |
| 处理模式 | 处理模式 选择 SPL 。 |
| SPL 语句 | SPL 语句具体请参考 [SPL](user-guide/spl-syntax.md) [语法](user-guide/spl-syntax.md) 。解析日志前，日志默认存在 content 字段中。 |
| 超时时间 | SPL 语句执行一次的最大时间。 |
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
