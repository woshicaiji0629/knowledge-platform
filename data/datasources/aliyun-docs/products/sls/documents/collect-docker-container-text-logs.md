# 采集Docker容器日志（标准输出/文件）-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-docker-container-text-logs

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

# 采集Docker容器日志（标准输出/文件）

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在容器化环境中，业务日志通常分散于各个Docker 容器的标准输出或日志文件中，难以集中管理和快速检索。通过日志服务的 LoongCollector 采集器，可将多节点容器日志汇聚至统一日志库，实现日志的集中存储、结构化解析、脱敏过滤和高效查询分析。

## 适用范围

- 

权限要求：部署使用的阿里云主账号或子账号需具备AliyunLogFullAccess权限。

- 

Docker 版本与 LoongCollector 要求：

- 

如果您的Docker Engine版本大于等于v29.0，或支持的最低Docker API版本大于等于1.42，请使用LoongCollector 3.2.4及以上版本，否则将无法采集容器标准输出或文件日志。

- 

LoongCollector3.2.4及以上版本支持的Docker API版本范围为1.24 ~ 1.48。

- 

LoongCollector3.2.3及以下版本支持的Docker API版本范围为1.18 ~ 1.41。

- 

采集标准输出限制：

- 

必须在Docker的配置文件daemon.json中添加"log-driver": "json-file"。

- 

如果是CentOS 7.4及以上版本（除CentOS 8.0以外），需设置fs.may_detach_mounts=1。

- 

采集文本日志限制：仅支持overlay、overlay2两种存储驱动（其他类型需手动挂载日志目录）。

## 采集配置创建流程

- 

[准备工作](products/sls/documents/collect-docker-container-text-logs.md)：创建Project和LogStore，Project是资源管理单元，用于隔离不同业务日志，LogStore用于存储日志。

- 

[配置机器组（安装](products/sls/documents/collect-docker-container-text-logs.md)[LoongCollector）](products/sls/documents/collect-docker-container-text-logs.md)：在需要采集日志的服务器上安装LoongCollector，并将其加入到机器组中。使用机器组统一管理采集节点，对服务器进行配置分发与状态管理。

- 

[创建并配置日志采集规则](products/sls/documents/collect-docker-container-text-logs.md)

- 

[全局与输入配置](products/sls/documents/collect-docker-container-text-logs.md)：定义采集配置的名称及日志采集的来源和范围。

- 

[日志处理与结构化](products/sls/documents/collect-docker-container-text-logs.md)：根据日志格式进行处理配置。

- 

多行日志：适用于单条日志跨越多行（如 Java 异常堆栈、Python traceback），需通过行首正则识别每条日志的起始行。

- 

结构化解析：通过配置解析插件（如正则、分隔符、NGINX 模式等）将原始字符串提取为结构化的键值对，便于后续查询与分析。

- 

过滤处理：通过配置采集黑名单和内容过滤规则，筛选有效日志内容，减少冗余数据的传输与存储。

- 

[日志分类](products/sls/documents/collect-docker-container-text-logs.md)：通过配置日志主题（Topic）和日志打标灵活区分不同业务、容器或路径来源的日志。

- 

查询分析配置：系统默认开启全文索引，支持关键词搜索。建议启用字段索引，以便对结构化字段进行精确查询和分析，提升检索效率。

- 

[验证与故障排查](products/sls/documents/collect-docker-container-text-logs.md)：配置完成后，验证日志是否成功采集，如遇采集无数据、心跳失败或解析错误等问题，请参考[常见问题排查](products/sls/documents/collect-docker-container-text-logs.md)。

## 准备工作

在采集日志前，需规划并创建用于管理与存储日志的Project和LogStore。若已有可用资源，可跳过此步骤，直接进行[步骤一：配置机器组（安装](products/sls/documents/collect-docker-container-text-logs.md)[LoongCollector）](products/sls/documents/collect-docker-container-text-logs.md)。

创建Project

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。

- 

单击创建Project，并配置：

- 

所属地域：根据日志来源选择，创建后不可修改。

- 

Project名称：阿里云内全局唯一，创建后不可修改。

- 

其他配置保持默认，单击创建。如需了解其他参数，请参见[创建](products/sls/documents/manage-a-project.md)[Project](products/sls/documents/manage-a-project.md)。

创建LogStore

- 

单击Project名称，进入目标Project。

- 

在左侧导航栏，选择日志库，单击+。

- 

在创建LogStore页面，完成以下核心配置：

- 

Logstore名称：设置一个在Project内唯一的名称。该名称创建后不可修改。

- 

Logstore类型：根据规格对比选择标准型或查询型。

- 

计费模式：

- 

按使用功能计费（不支持更改）：按存储、索引、读写次数等各项资源独立计费。适合小规模或功能使用不确定的场景。

- 

按写入数据量计费：仅按原始写入数据量计费，提供30天免费存储，以及免费的数据加工、投递等功能。适合存储周期接近30天或数据处理链路复杂的业务场景。

- 

数据保存时间：设置日志的保留天数（1~3650天，3650为永久保存），默认为30天。

- 

其他配置保持默认，单击确定。如需了解其他配置信息，请参考[管理](products/sls/documents/manage-a-logstore.md)[LogStore](products/sls/documents/manage-a-logstore.md)。

## 步骤一：配置机器组（安装LoongCollector）

在Docker宿主机上以容器方式部署LoongCollector，并将其加入到机器组中。通过机器组实现对多个采集节点的统一管理、配置分发与状态监控。

- 

拉取镜像

在已安装Docker的宿主机上执行如下命令，拉取 LoongCollector 镜像。请将${region_id}替换为宿主机所在地域或就近[地域](products/sls/documents/collect-docker-container-text-logs.md)[ID](products/sls/documents/collect-docker-container-text-logs.md)（如cn-hangzhou），以提升下载速度和稳定性。

# LoongCollector镜像地址 docker pull aliyun-observability-release-registry.${region_id}.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun # Logtail镜像地址 docker pull registry.${region_id}.aliyuncs.com/log-service/logtail:v2.1.11.0-aliyun

- 

启动LoongCollector容器

运行以下命令启动容器，确保正确挂载目录并设置必要环境变量：

docker run -d \ -v /:/logtail_host:ro \ -v /var/run/docker.sock:/var/run/docker.sock \ --env ALIYUN_LOGTAIL_CONFIG=/etc/ilogtail/conf/${sls_upload_channel}/ilogtail_config.json \ --env ALIYUN_LOGTAIL_USER_ID=${aliyun_account_id} \ --env ALIYUN_LOGTAIL_USER_DEFINED_ID=${user_defined_id} \ aliyun-observability-release-registry.${region_id}.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun

参数说明：

- 

${sls_upload_channel}：日志上传通道，由Project所在[地域](products/sls/documents/collect-docker-container-text-logs.md)-网络传输类型构成。示例：

- 

- 

| 传输类型 | 配置值格式 | 示例 | 适用场景 |
| --- | --- | --- | --- |
| 内网传输 | regionId | cn-hangzhou | ECS 与 Project 同地域 |
| 公网传输 | regionId-internet | cn-hangzhou-internet | ECS 和 Project 属于不同地域 服务器为其他云厂商服务器或自建 IDC |
| 传输加速 | regionId-acceleration | cn-hangzhou-acceleration | 国内外跨区域通信 |


- 

${aliyun_account_id}：阿里云主账号ID。

- 

${user_defined_id}：机器组的用户自定义标识，用于绑定机器组（如user-defined-docker-1），需在地域内唯一。

重要

必须满足的启动条件：

- 

正确配置三个关键环境变量：

ALIYUN_LOGTAIL_CONFIG、ALIYUN_LOGTAIL_USER_ID、ALIYUN_LOGTAIL_USER_DEFINED_ID。

- 

挂载/var/run/docker.sock：用于监听容器生命周期事件。

- 

挂载/→/logtail_host：用于访问宿主机文件系统。

- 

验证容器运行状态

docker ps | grep loongcollector

预期输出示例：

6ad510001753 aliyun-observability-release-registry.cn-beijing.cr.aliyuncs.com/loongcollector/loongcollector:v3.0.12.0-25723a1-aliyun "/usr/local/ilogtail…" About a minute ago Up About a minute recursing_shirley

- 

配置机器组

在左侧导航栏资源组>机器组，单击创建机器组，配置如下参数并单击确定：

- 

名称：自定义机器组名称（如docker-host-group）。

- 

机器组标识：：选择用户自定义标识。

- 

用户自定义标识：输入启动容器时设置的${user_defined_id}。必须完全一致，否则无法关联成功。

- 

验证机器组心跳状态

单击新建机器组名称，进入机器组详情页，查看机器组状态：

- 

OK：表示LoongCollector 已成功连接到日志服务。

- 

FAIL：请参考[心跳异常问题汇总](products/sls/documents/troubleshooting-of-abnormal-heartbeat-problems.md)排查。

## 步骤二：创建并配置日志采集规则

定义 LoongCollector 采集哪些日志、如何解析日志结构、如何过滤内容，并将配置绑定到已注册的机器组。

- 

在日志库页面，单击目标LogStore名称前的展开。

- 

单击接入数据后的，在快速数据接入弹框中，根据日志源选择接入模板，并单击立即接入：

- 

Docker 标准输出：选择Docker标准输出-新版

容器标准输出采集支持新版与旧版两种模板，推荐使用新版。如需了解新、旧版本差异，请参考[附录：容器标准输出新旧版本对比](products/sls/documents/collect-docker-container-text-logs.md)。使用旧版采集参考[采集](products/sls/documents/collect-docker-container-standard-output.md)[Docker](products/sls/documents/collect-docker-container-standard-output.md)[容器的标准输出（旧版）](products/sls/documents/collect-docker-container-standard-output.md)。

- 

Docker 文件日志：选择Docker文件-容器

- 

机器组配置，完成后单击下一步：

- 

使用场景：选择Docker场景。

- 

将[步骤一](products/sls/documents/collect-docker-container-text-logs.md)中创建好的机器组从源机器组列表添加至右侧应用机器组。

- 

在Logtail配置页面，完成如下配置，并单击下一步。

### 1. 全局与输入配置

配置前，请确保已完成数据接入模板选择和机器组绑定。本步骤用于定义采集配置的名称、日志来源及采集范围。

## 采集Docker标准输出

全局配置

- 

配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。命名规则：

- 

仅支持小写字母、数字、连字符（-）和下划线（_）。

- 

必须以小写字母或者数字作为开头和结尾。

输入配置

- 

选择开启标准输出或标准错误开关（默认全部开启）。

重要

建议不要同时开启标准输出和标准错误，可能会导致采集日志出现混乱。

## 采集Docker容器文本日志

全局配置：

- 

配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。命名规则：

- 

仅支持小写字母、数字、连字符（-）和下划线（_）。

- 

必须以小写字母或者数字作为开头和结尾。

输入配置：

- 

文件路径类型：

- 

容器内路径：采集容器内的日志文件。

- 

宿主机路径：采集宿主机本地服务日志。

- 

文件路径：日志采集的绝对路径。

- 

Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。

- 

Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。

- 

最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0（仅本层），取值范围是0~1000。

建议设置为0，配置路径到文件所在的目录。

### 2. 日志处理与结构化

配置日志处理规则可将原始非结构化日志转换为结构化的数据，提升日志查询与分析效率。建议在配置前先添加日志样例：

在Logtail配置页面的处理配置区域，单击添加日志样例，输入待采集的日志内容。系统将基于样例识别日志格式，辅助生成正则表达式和解析规则，降低配置难度。

场景一：多行日志处理（如Java堆栈日志）

由于Java异常堆栈、JSON等日志通常跨越多行，在默认采集模式下会被拆分为多条不完整的记录，导致上下文信息丢失；为此，可启用多行采集模式，通过配置行首正则表达式，将同一日志的连续多行内容合并为一条完整日志。

效果示例：

| 未经任何处理的原始日志 | 默认采集模式下，每行作为独立日志，堆栈信息被拆散，丢失上下文 | 开启多行模式，通过行首正则表达式识别完整日志，保留完整语义结构。 |
| --- | --- | --- |
| [2025-11-13T10:52:20,557] [ERROR] java.sql.SQLException: No suitable driver found for jdbc:mysql://db.host:3306/prod_db at com.datastore.util.DataProcessor.save(DataProcessor.java:434) at io.awesomeapp.util.PaymentGateway.fetchData(PaymentGateway.java:463) at org.awesomeapp.util.UserService.processRequest(UserService.java:252) at io.datastore.service.DatabaseConnector.fetchData(DatabaseConnector.java:172) at org.datastore.service.UserService.fetchData(UserService.java:517) |  |  |


配置步骤：在Logtail配置页面的处理配置区域，开启多行模式：

- 

类型：选择自定义或多行JSON。

- 

自定义：原始日志的格式不固定，需配置行首正则表达式，来标识每条日志的起始行。

- 

行首正则表达式：支持自动生成或手动输入，正则表达式需要能够匹配完整的一行数据，如上述示例中匹配的正则表达式为\[\d+-\d+-\w+:\d+:\d+,\d+]\s\[\w+]\s.*。

- 

自动生成：单击自动生成正则表达式，然后在日志样例文本框中，选择需提取的日志内容，单击生成正则。

- 

手动输入：单击手动输入正则表达式，输入完成后，单击验证。

- 

多行JSON：当原始日志均为标准JSON格式时，日志服务会自动处理单条JSON日志内部的换行。

- 

切分失败处理方式：

- 

丢弃：如果一段文本无法匹配行首规则，则直接丢弃。

- 

保留单行：将无法匹配的文本按原始的单行模式进行切分和保留。

场景二：结构化日志

当原始日志为非结构化或半结构化文本（如 Nginx 访问日志、应用输出日志）时，直接进行查询和分析往往效率低下。日志服务提供多种数据解析插件，能够自动将不同格式的原始日志转换为结构化数据，为后续的分析、监控和告警提供坚实的数据基础。

效果示例：

| 未经任何处理的原始日志 | 结构化解析后的日志 |
| --- | --- |
| 192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36" | body_bytes_sent: 368 http_referer: - http_user_agent : Mozi11a/5.0 (Nindows NT 10.0; Win64; x64) AppleMebKit/537.36 (KHTML, like Gecko) Chrome/131.0.x.x Safari/537.36 remote_addr:192.168.*.* remote_user: - request_length: 514 request_method: GET request_time: 0.000 request_uri: /nginx-logo.png status: 200 time_local: 15/Apr/2025:16:40:00 |


配置步骤：在Logtail配置页面的处理配置区域

- 

添加解析插件：单击添加处理插件，根据实际格式配置[正则解析、分隔符解析、JSON 解析等插件](products/sls/documents/collect-docker-container-text-logs.md)。此处以采集NGINX日志为例，选择原生处理插件>NGINX模式解析。

- 

NGINX日志配置：将 Nginx 服务器配置文件（nginx.conf）中的log_format定义完整地复制并粘贴到此文本框中。

示例：

log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"';

重要

此处的格式定义必须与服务器上生成日志的格式完全一致，否则将导致日志解析失败。

- 

通用配置参数说明：以下参数在多种数据解析插件中都会出现，其功能和用法是统一的。

- 

原始字段：指定要解析的源字段名。默认为content，即采集到的整条日志内容。

- 

解析失败时保留原始字段：推荐开启。当日志无法被插件成功解析时（例如格式不匹配），此选项能确保原始日志内容不会丢失，而是被完整保留在指定的原始字段中。

- 

解析成功时保留原始字段：选中后，即使日志解析成功，原始日志内容也会被保留。

### 3. 日志过滤

在日志采集过程中，大量低价值或无关日志（如 DEBUG/INFO 级别日志）的无差别收集，不仅造成存储资源浪费、增加成本，还影响查询效率并带来数据泄露风险。为此，可通过精细化过滤策略实现高效、安全的日志采集。

## 通过内容过滤降低成本

基于日志内容的字段过滤（如仅采集 level 为 WARNING 或 ERROR 的日志）。

效果示例：

| 未经任何处理的原始日志 | 只采集 WARNING 或 ERROR 日志 |
| --- | --- |
| {"level":"WARNING","timestamp":"2025-09-23T19:11:40+0800","cluster":"yilu-cluster-0728","message":"Disk space is running low","freeSpace":"15%"} {"level":"ERROR","timestamp":"2025-09-23T19:11:42+0800","cluster":"yilu-cluster-0728","message":"Failed to connect to database","errorCode":5003} {"level":"INFO","timestamp":"2025-09-23T19:11:47+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} | {"level":"WARNING","timestamp":"2025-09-23T19:11:40+0800","cluster":"yilu-cluster-0728","message":"Disk space is running low","freeSpace":"15%"} {"level":"ERROR","timestamp":"2025-09-23T19:11:42+0800","cluster":"yilu-cluster-0728","message":"Failed to connect to database","errorCode":5003} |


配置步骤：在Logtail配置页面的处理配置区域

单击添加处理插件，选择原生处理插件>过滤处理：

- 

字段名：过滤的日志字段。

- 

字段值：用于过滤的正则表达式，仅支持全文匹配，不支持关键词部分匹配。

## 通过黑名单控制采集范围

通过黑名单机制排除指定目录或文件，避免无关或敏感日志被上传。

配置步骤：在Logtail配置页面的输入配置>其他输入配置区域，启用采集黑名单，并单击添加。

支持完整匹配和通配符匹配目录和文件名，通配符只支持星号（*）和半角问号（?）。

- 

文件路径黑名单：需要忽略的文件路径，示例：

- 

/home/admin/private*.log：在采集时忽略/home/admin/目录下所有以private开头，以.log结尾的文件。

- 

/home/admin/private*/*_inner.log：在采集时忽略/home/admin/目录下以private开头的目录内，以_inner.log结尾的文件。

- 

文件黑名单：配置采集时需要忽略的文件名，示例：

- 

app_inner.log：在采集时忽略所有名为app_inner.log的文件。

- 

目录黑名单：目录路径不能以正斜线（/）结尾，示例：

- 

/home/admin/dir1/：目录黑名单不会生效。

- 

/home/admin/dir*：在采集时忽略/home/admin/目录下所有以dir开头的子目录下的文件。

- 

/home/admin/*/dir：在采集时忽略/home/admin/目录下二级目录名为dir的子目录下的所有文件。例如/home/admin/a/dir目录下的文件被忽略，/home/admin/a/b/dir目录下的文件被采集。

## 容器过滤

基于容器元信息（如环境变量、Pod 标签、命名空间、容器名称等）设置采集条件，精准控制采集哪些容器的日志。

配置步骤：在Logtail配置页面的输入配置区域，启用容器过滤，并单击添加

多个条件之间为“且”的关系，所有正则匹配均基于 Go 语言的 RE2 正则引擎，功能较 PCRE 等引擎有所限制，请遵循[附录：正则表达式使用限制（容器过滤）](products/sls/documents/collect-docker-container-text-logs.md)编写正则表达式。

- 

环境变量黑/白名单：指定待采集容器的环境变量条件。

- 

K8s Pod标签黑/白名单：指定待采集容器所在Pod 的标签条件。

- 

K8s Pod 名称正则匹配：通过Pod名称指定待采集的容器

- 

K8s Namespace 正则匹配：通过Namespace名称指定待采集的容器。

- 

K8s 容器名称正则匹配：通过容器名称指定待采集的容器。

- 

容器label黑/白名单：采集容器标签符合条件的容器，Docker场景使用，K8s场景不推荐使用。

### 4. 日志分类

在多应用、多实例共用相同日志格式的场景下，日志来源难以区分，导致查询时上下文缺失、分析效率低下。为此，可通过配置日志主题（Topic）和日志打标实现自动化的上下文关联与逻辑分类。

## 配置日志主题（Topic）

当多个应用或实例的日志格式相同但路径不同时（如/apps/app-A/run.log和/apps/app-B/run.log），采集日志难以区分来源。此时可基于机器组、自定义名称或文件路径提取方式生成 Topic，灵活区分不同业务或路径来源的日志。

配置步骤：全局配置>其他全局配置>日志主题类型：选择Topic生成方式，支持如下三种类型：

- 

机器组Topic：将采集配置应用于多个机器组时，LoongCollector 会自动使用服务器所属的机器组名称作为__topic__字段上传。适用于按主机集群划分日志场景。

- 

自定义：格式为customized://<自定义主题名>，例如customized://app-login。适用于固定业务标识的静态主题场景。

- 

文件路径提取：从日志文件的完整路径中提取关键信息，动态标记日志来源。适用于多用户/应用共用相同日志文件名但路径不同的情况。

当多个用户或服务将日志写入不同顶级目录，但下级路径和文件名一致时，仅靠文件名无法区分来源，例如：

/data/logs ├── userA │ └── serviceA │ └── service.log ├── userB │ └── serviceA │ └── service.log └── userC └── serviceA └── service.log

此时您可以配置文件路径提取，并使用正则表达式从完整路径中提取关键信息，并将匹配结果作为日志主题（Topic）上传至LogStore。

提取规则：基于正则表达式的捕获组

在配置正则表达式时，系统根据捕获组的数量和命名方式自动决定输出字段格式，规则如下：

文件路径的正则表达式中，需要对正斜线（/）进行转义。

| 捕获组类型 | 适用场景 | 生成字段 | 正则示例 | 匹配路径示例 | 生成字段 |
| --- | --- | --- | --- | --- | --- |
| 单捕获组（仅一个 (.*?) ） | 仅需一个维度区分来源（如用户名、环境） | 生成 __topic__ 字段 | \/logs\/(.*?)\/app\.log | /logs/userA/app.log | __topic__：userA |
| 多捕获组-非命名（多个 (.*?) ） | 需要多个维度但无需语义标签 | 生成 tag 字段 __tag__:__topic_{i}__ ，其中 {i} 为捕获组的序号 | \/logs\/(.*?)\/(.*?)\/app\.log | /logs/userA/svcA/app.log | __tag__:__topic_1__userA ； __tag__:__topic_2__svcA |
| 多捕获组-命名（使用 (?P<name>.*？) | 需多维且希望字段含义清晰、便于查询与分析 | 生成 tag 字段 __tag__:{name} | \/logs\/(?P<user>.*?)\/(?P<service>.*?)\/app\.log | /logs/userA/svcA/app.log | __tag__:user:userA ； __tag__:service:svcA |


## 日志打标

启用日志标签富化功能，从容器环境变量或 Kubernetes Pod 标签中提取关键信息并附加为 tag，实现日志的精细化分组。

配置步骤：在Logtail配置页面的输入配置区域，启用日志标签富化，并单击添加。

- 

环境变量相关：配置环境变量名和tag名，环境变量值将存放在tag名中。

- 

环境变量名：指定需要提取的环境变量名称。

- 

tag名：环境变量标签名称。

- 

Pod标签相关：配置Pod标签名和tag名，Pod标签值将存放在tag名中。

- 

Pod标签名：需要提取的 Kubernetes Pod 标签名称。

- 

tag名：标签名称。

### 5. 输出配置

默认采集所有日志发送到当前日志库，压缩方式为lz4。如需将同一来源的日志分发到不同日志库，请参考如下步骤进行配置：

多目标动态分发

重要

- 

多目标发送仅适用于LoongCollector 3.0.0及以上版本，Logtail不支持。

- 

输出目标最多可配置5个。

- 

配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考[如何管理多目标分发配置？](products/sls/documents/collect-docker-container-text-logs.md)。

配置步骤：在Logtail配置页面的输出配置区域。

- 

单击展开输出配置。

- 

单击添加输出目标，完成如下配置：

- 

日志库：选择目标日志库。

- 

压缩方式：支持lz4和zstd。

- 

路由配置：根据日志的Tag字段路由分发，满足路由配置的日志会被上传到目标日志库，路由配置为空时表示采集到的所有日志都会被上传到目标日志库。

- 

Tag名称：用于路由的Tag字段名称，直接填写字段名（如__path__），无需__tag__:前缀。Tag字段分为如下两类：

关于Tag的详细信息请参考[管理](products/sls/documents/manage-loongcollector-to-collect-tags.md)[LoongCollector](products/sls/documents/manage-loongcollector-to-collect-tags.md)[采集](products/sls/documents/manage-loongcollector-to-collect-tags.md)[Tag](products/sls/documents/manage-loongcollector-to-collect-tags.md)。

- 

Agent相关：与采集 Agent 本身相关，不依赖插件。 如__hostname__、__user_defined_id__等。

- 

输入插件相关：依赖输入插件，由输入插件提供并富化相关信息到日志中。如文件采集的__path__；K8s采集的_pod_name_、_container_name_等。

- 

Tag值：日志的Tag字段值与此匹配时，发送到该目标日志库。

- 

是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。

## 步骤三：查询与分析配置

在完成日志处理与插件配置后，单击下一步，进入查询分析配置页面：

- 

系统默认开启[全文索引](products/sls/documents/create-indexes.md)，支持对日志原始内容进行关键词搜索。

- 

如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[字段索引](products/sls/documents/create-indexes.md)。

配置完成后，单击下一步，完成整个采集流程的设置。

## 步骤四：验证与故障排查

完成采集配置并应用到机器组后，系统将自动下发配置并开始采集增量日志。

### 查看上报日志

- 

确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。

- 

查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。采集的每条Docker容器文本日志中默认包含以下字段信息：

| 字段名 | 说明 |
| --- | --- |
| __source__ | LoongCollector（Logtail）容器的 IP 地址。 |
| _container_ip_ | 业务容器的 IP 地址。 |
| __tag__:__hostname__ | LoongCollector（Logtail）所在 Docker 主机的名称。 |
| __tag__:__path__ | 日志采集路径。 |
| __tag__:__receive_time__ | 日志到达服务端的时间。 |
| __tag__:__user_defined_id__ | 机器组的自定义标识。 |


### 常见问题排查

机器组心跳连接为fail

- 

检查用户标识：如果您的服务器类型不是ECS，或使用的ECS和Project属于不同阿里云账号，请根据如下表格检查指定目录下是否存在正确的用户标识。

- 

Linux：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。

- 

Windows：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。

如果指定路径下存在以当前Project所属的阿里云账号ID命名的文件，则说明用户标识配置正确。

- 

检查机器组标识：如果您使用了用户自定义标识机器组，请检查指定目录下是否存在user_defined_id文件，如果存在请检查该文件中的内容是否与机器组配置的自定义标识一致。

| 系统 | 指定目录 | 解决方法 |
| --- | --- | --- |
| Linux | /etc/ilogtail/user_defined_id | # 配置用户自定义标识,如目录不存在请手动创建 echo "user-defined-1" > /etc/ilogtail/user_defined_id |
| Windows | C:\LogtailData\user_defined_id | 在 C:\LogtailData 目录下新建 user_defined_id 文件，并写入用户自定义标识。（如目录不存在，请手动创建） |


- 

如果用户标识和机器组标识均配置无误，请参考[LoongCollector（Logtail）机器组问题排查思路](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进一步排查。

日志采集无数据

- 

检查是否有增量日志：配置LoongCollector（Logtail）采集后，如果待采集的日志文件没有新增日志，则LoongCollector（Logtail）不会采集该文件。

- 

检查机器组心跳状态：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态。

- 

如果心跳为OK，则表示机器组与日志服务 Project 连接正常。

- 

如果心跳为FAIL：参考[机器组心跳连接为](products/sls/documents/host-text-log-collection-auto-install.md)[fail](products/sls/documents/host-text-log-collection-auto-install.md)进行排查。

- 

确认LoongCollector（Logtail）采集配置是否已应用到机器组：即使LoongCollector（Logtail）采集配置已创建，但如果未将其应用到机器组，日志仍无法被采集。

- 

前往资源组>机器组页面，单击目标机器组名称，进入机器组配置页面。

- 

在页面中查看管理配置，左侧展示全部Logtail配置，右侧展示已生效Logtail配置。如果目标LoongCollector（Logtail）采集配置已移动到右侧生效区域，则表示该配置已成功应用到目标机器组。

- 

如果目标LoongCollector（Logtail）采集配置未移动到右侧生效区域，请单击修改，在左侧全部Logtail配置列表中勾选目标LoongCollector（Logtail）配置名称，单击移动到右侧生效区域，完成后单击确定。

采集日志报错或格式错误

排查思路：这种情况说明网络连接和基础配置正常，问题主要出在日志内容与解析规则不匹配。您需要查看具体的错误信息来定位问题：

- 

在Logtail配置页面，单击采集异常的LoongCollector（Logtail）配置名称，在日志采集错误页签下，单击时间选择设置查询时间。

- 

在区域，查看错误日志的告警类型，并根据[采集数据常见错误类型](products/sls/documents/log-collection-error-type.md)查询对应的解决办法。

## 后续步骤

- 

[日志查询与分析](products/sls/documents/quick-guide-to-query-and-analysis.md)：可以使用内置的[通过](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[AI](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)[智能生成查询与分析语句（Copilot）](products/sls/documents/copilot-automatic-generation-of-ai-assisted-sql-statements.md)，自动生成查询分析语句。

- 

[数据可视化](products/sls/documents/dashboard-overview.md)：借助可视化仪表盘监控关键指标趋势。

- 

[数据异常自动预警](products/sls/documents/alarm-settings-quick-start.md)：设置告警策略，实时感知系统的异常情况。

## 常用命令

### 查看LoongCollector（Logtail）运行状态

docker exec ${logtail_container_id} /etc/init.d/ilogtaild status

### 查看LoongCollector（Logtail）的版本号、IP地址和启动时间等信息

docker exec ${logtail_container_id} cat /usr/local/ilogtail/app_info.json

### 查看LoongCollector（Logtail）的运行日志

LoongCollector（Logtail）运行日志保存在容器内的/usr/local/ilogtail/目录下，文件名为ilogtail.LOG，轮转文件会压缩存储为ilogtail.LOG.x.gz。示例如下：

# 查看LoongCollector运行日志 docker exec a287de895e40 tail -n 5 /usr/local/ilogtail/loongcollector.LOG # 查看Logtail运行日志 docker exec a287de895e40 tail -n 5 /usr/local/ilogtail/ilogtail.LOG

输出结果示例如下：

[2025-08-25 09:17:44.610496] [info] [22] /build/loongcollector/file_server/polling/PollingModify.cpp:75 polling modify resume:succeeded [2025-08-25 09:17:44.610497] [info] [22] /build/loongcollector/file_server/polling/PollingDirFile.cpp:100 polling discovery resume:starts [2025-08-25 09:17:44.610498] [info] [22] /build/loongcollector/file_server/polling/PollingDirFile.cpp:103 polling discovery resume:succeeded [2025-08-25 09:17:44.610499] [info] [22] /build/loongcollector/file_server/FileServer.cpp:117 file server resume:succeeded [2025-08-25 09:17:44.610500] [info] [22] /build/loongcollector/file_server/EventDispatcher.cpp:1019 checkpoint dump:succeeded

### 重启LoongCollector（Logtail）

# 停止loongcollector docker exec a287de895e40 /etc/init.d/ilogtaild stop # 启动loongcollector docker exec a287de895e40 /etc/init.d/ilogtaild start

## 常见问题

### 常见错误信息

| 错误现象 | 原因 | 解决方案 |
| --- | --- | --- |
| Failed to connect to Logtail | Project 地域与 LoongCollector（Logtail）容器不一致 | 检查 ALIYUN_LOGTAIL_CONFIG 中的地域配置 |
| No logs in LogStore | 文件路径配置错误 | 确认业务容器内日志路径与采集配置匹配 |


### 错误日志：The parameter is invalid : uuid=none

问题描述：如果LoongCollector（Logtail）日志（/usr/local/ilogtail/ilogtail.LOG）中出现The parameter is invalid : uuid=none的错误日志。

解决方案：请在宿主机上创建一个product_uuid文件，在其中输入任意合法UUID（例如169E98C9-ABC0-4A92-B1D2-AA6239C0D261），并把该文件挂载到LoongCollector（Logtail）容器的/sys/class/dmi/id/product_uuid目录。

### 如何让同一个日志文件或容器标准输出被多个采集配置同时采集？

默认情况下，日志服务为了防止数据重复，限制了每个日志源只能被一个采集配置采集：

- 

文本日志文件只能匹配一个 Logtail 采集配置；

- 

容器的标准输出（stdout） ：

- 

如果使用的是标准输出-新版模板， 默认只能被一个标准输出采集配置采集。

- 

如果使用的是标准输出-旧版模板，无需额外配置，默认支持采集多份。

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，进入目标Project。

- 

在左侧导航选择日志库，找到目标LogStore。

- 

单击其名称前的展开LogStore。

- 

单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。

- 

在Logtail配置页面，单击编辑，下滑至输入配置区域：

- 

采集文本文件日志：开启允许文件多次采集。

- 

采集容器标准输出：开启允许标准输出多次采集。

### 如何管理多目标分发配置？

由于多目标分发配置关联了多个日志库，这类配置需要通过 Project 级别的管理页面进行维护：

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project名称。

- 

在目标Project页面，单击左侧导航栏资源组>配置管理。

说明

此页面集中管理Project下的所有采集配置，包括那些因日志库被误删而残留的配置。

## 附录：原生解析插件详解

在Logtail配置页面的处理配置区域，可以通过添加处理插件，对原始日志进行结构化配置。如需为已有采集配置添加处理插件，可以参考如下步骤：

- 

在左侧导航栏选择日志库，找到目标LogStore。

- 

单击其名称前的展开LogStore。

- 

单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。

- 

在Logtail配置页面，单击编辑。

此处仅介绍常用处理插件，覆盖常见日志处理场景，如需更多功能，请参考[拓展处理插件](products/sls/documents/developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)。

重要

插件组合使用规则（适用于 LoongCollector / Logtail 2.0 及以上版本）:

- 

原生处理插件与拓展处理插件均可独立使用，也支持按需组合使用。

- 

推荐优先选用原生处理插件，因其具备更优的性能和更高的稳定性。

- 

当原生功能无法满足业务需求时，可在已配置的原生处理插件之后，追加配置拓展处理插件以实现补充处理。

顺序约束：

所有插件按照配置顺序组成处理链，依次执行。需要注意：所有原生处理插件必须先于任何拓展处理插件，添加任意拓展处理插件后，将无法继续添加原生处理插件。

### 正则解析

通过正则表达式提取日志字段，并将日志解析为键值对形式，每个字段都可以被独立查询和分析。

效果示例：

| 未经任何处理的原始日志 | 使用正则解析插件 |
| --- | --- |
| 127.0.0.1 - - [16/Aug/2024:14:37:52 +0800] "GET /wp-admin/admin-ajax.php?action=rest-nonce HTTP/1.1" 200 41 "http://www.example.com/wp-admin/post-new.php?post_type=page" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0" | body_bytes_sent: 41 http_referer: http://www.example.com/wp-admin/post-new.php?post_type=page http_user_agent: Mozilla/5.0 (Windows NT 10.0; Win64; ×64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0 remote_addr: 127.0.0.1 remote_user: - request_method: GET request_protocol: HTTP/1.1 request_uri: /wp-admin/admin-ajax.php?action=rest-nonce status: 200 time_local: 16/Aug/2024:14:37:52 +0800 |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>正则解析：

- 

正则表达式：用于匹配日志，支持自动生成或手动输入：

- 

自动生成：

- 

单击自动生成正则表达式。

- 

在日志样例中划选需要提取的日志内容。

- 

单击生成正则。

确认日志样例区域中已粘贴正确格式的日志内容（例如 Apache Combined 格式的访问日志），再单击该区域中的生成正则按钮以自动生成解析正则表达式。

- 

手动输入：根据日志格式手动输入正则表达式。

配置完成后，单击验证，测试正则表达式是否能够正确解析日志内容。

- 

日志提取字段：为提取的日志内容（Value），设置对应的字段名（Key）。

- 

其他参数请参考[场景二：结构化日志](products/sls/documents/collect-docker-container-text-logs.md)中的通用配置参数说明。

### 分隔符解析

通过分隔符将日志内容结构化，解析为多个键值对形式，支持单字符分隔符和多字符分隔符。

效果示例：

| 未经任何处理的原始日志 | 按指定字符 , 切割字段 |
| --- | --- |
| 05/May/2025:13:30:28,10.10.*.*,"POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1",200,18204,aliyun-sdk-java | ip:10.10.*.* request:POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1 size:18204 status:200 time:05/May/2025:13:30:28 user_agent:aliyun-sdk-java |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>分隔符解析：

- 

分隔符：指定用于切分日志内容的字符。

示例：对于CSV格式文件，选择自定义，输入半角逗号（,）。

- 

引用符：当某个字段值中包含分隔符时，需要指定引用符包裹该字段，避免错误切割。

- 

日志提取字段：按分隔顺序依次为每一列设置对应的字段名称（Key）。规则要求如下：

- 

字段名只能包含：字母、数字、下划线（_）。

- 

必须以字母或下划线（_）开头。

- 

最大长度：128字节。

- 

其他参数请参考[场景二：结构化日志](products/sls/documents/collect-docker-container-text-logs.md)中的通用配置参数说明。

### 标准JSON解析

将Object类型的JSON日志结构化，解析为键值对形式。

效果示例：

| 未经任何处理的原始日志 | 标准 JSON 键值自动提取 |
| --- | --- |
| {"url": "POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10.200.98.220", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "18204"}, "time": "05/Jan/2025:13:30:28"} | ip: 10.200.98.220 request: {"status": "200", "latency" : "18204" } time: 05/Jan/2025:13:30:28 url: POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek******&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1 user-agent:aliyun-sdk-java |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>JSON解析：

- 

原始字段：默认值为content（此字段用于存放待解析的原始日志内容）。

- 

其他参数请参考[场景二：结构化日志](products/sls/documents/collect-docker-container-text-logs.md)中的通用配置参数说明。

### 嵌套JSON解析

通过指定展开深度，将嵌套的JSON日志解析为键值对形式。

效果示例：

| 未经任何处理的原始日志 | 展开深度：0， 并使用展开深度作为前缀 | 展开深度：1， 并使用展开深度作为前缀 |
| --- | --- | --- |
| {"s_key":{"k1":{"k2":{"k3":{"k4":{"k51":"51","k52":"52"},"k41":"41"}}}}} | 0_s_key_k1_k2_k3_k41:41 0_s_key_k1_k2_k3_k4_k51:51 0_s_key_k1_k2_k3_k4_k52:52 | 1_s_key:{"k1":{"k2":{"k3":{"k4":{"k51":"51","k52":"52"},"k41":"41"}}}} |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择拓展处理插件>展开JSON字段：

- 

原始字段：需要展开的原始字段名，例如content。

- 

JSON展开深度：JSON对象的展开层级。0表示完全展开（默认值），1表示当前层级，以此类推。

- 

JSON展开连接符：JSON展开时字段名的连接符，默认为下划线 _。

- 

JSON展开字段前缀：指定JSON展开后字段名的前缀。

- 

展开数组：开启此项可将数组展开为带索引的键值对。

示例：{"k":["a","b"]}展开为{"k[0]":"a","k[1]":"b"}。

如果需要对展开后的字段进行重命名（例如，将 prefix_s_key_k1 改为 new_field_name），可以后续再添加一个重命名字段插件来完成映射。

- 

其他参数请参考[场景二：结构化日志](products/sls/documents/collect-docker-container-text-logs.md)中的通用配置参数说明。

### JSON数组解析

使用json_extract[函数](products/sls/documents/json-functions.md)，从JSON数组中提取JSON对象。

效果示例：

| 未经任何处理的原始日志 | 提取 JSON 数组结构 |
| --- | --- |
| [{"key1":"value1"},{"key2":"value2"}] | json1:{"key1":"value1"} json2:{"key2":"value2"} |


配置步骤：在Logtail配置页面的处理配置区域，将处理模式切换为SPL，配置SPL语句，使用[json_extract](products/sls/documents/json-functions.md)函数从JSON数组中提取JSON对象。

示例：从日志字段content中提取 JSON 数组中的元素，并将结果分别存储在新字段json1和json2中。

* | extend json1 = json_extract(content, '$[0]'), json2 = json_extract(content, '$[1]')

### Apache日志解析

根据Apache日志配置文件中的定义将日志内容结构化，解析为多个键值对形式。

效果示例：

| 未经任何处理的原始日志 | Apache 通用日志格式 combined 解析 |
| --- | --- |
| 1 192.168.1.10 - - [08/May/2024:15:30:28 +0800] "GET /index.html HTTP/1.1" 200 1234 "https://www.example.com/referrer" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36" | http_referer:https://www.example.com/referrer http_user_agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36 remote_addr:192.168.1.10 remote_ident:- remote_user:- request_method:GET request_protocol:HTTP/1.1 request_uri:/index.html response_size_bytes:1234 status:200 time_local:[08/May/2024:15:30:28 +0800] |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>APACHE模式解析：

- 

日志格式：combined

- 

APACHE配置字段：系统会根据日志格式自动填充配置。

重要

请务必核对自动填充的内容，确保与服务器上 Apache 配置文件（通常位于/etc/apache2/apache2.conf）中定义的 LogFormat 完全一致。

- 

其他参数请参考[场景二：结构化日志](products/sls/documents/collect-docker-container-text-logs.md)中的通用配置参数说明。

### 数据脱敏

对日志中的敏感数据进行脱敏处理。

效果示例：

| 未经任何处理的原始日志 | 脱敏结果 |
| --- | --- |
| [{'account':'1812213231432969','password':'04a23f38'}, {'account':'1812213685634','password':'123a'}] | [{'account':'1812213231432969','password':'********'}, {'account':'1812213685634','password':'********'}] |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>脱敏处理：

- 

原始字段：解析日志前，用于存放日志内容的原始字段。

- 

脱敏方式：

- 

const：将敏感内容替换成所修改的字符串。

- 

md5：将敏感内容替换为其对应的MD5值。

- 

替换字符串：选择脱敏方式为const时，需要输入字符串，用于替换敏感内容。

- 

被替换内容前的内容表达式：用于查找敏感内容，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。

- 

被替换的内容表达式：敏感内容的表达式，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。

### 时间解析

对日志中的时间字段进行解析，并将解析结果设置为日志的__time__字段。

效果示例：

| 未经任何处理的原始日志 | 时间解析 |
| --- | --- |
| {"level":"INFO","timestamp":"2025-09-23T19:11:47+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} | 解析 timestamp 字段的时间值，将日志的 __time__ 字段设置为对应的 Unix 时间戳 1758625907 （对应 2025-09-23T19:11:47+0800 ）。 |


配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>时间解析：

- 

原始字段：解析日志前，用于存放日志内容的原始字段。

- 

时间格式：根据日志中的时间内容设置对应的[时间格式](products/sls/documents/time-parsing.md)。

- 

时区：选择日志时间字段所在的时区。默认使用机器时区，即LoongCollector（Logtail）进程所在环境的时区。

## 附录：正则表达式使用限制（容器过滤）

容器过滤时所使用的正则表达式基于Go语言的RE2引擎，与PCRE等其他引擎相比存在部分语法限制。请在编写正则表达式时注意以下事项：

1. 命名分组语法差异

Go语言使用(?P<name>...)语法定义命名分组，不支持 PCRE中的(?<name>...)语法。

- 

正确示例：(?P<year>\d{4})

- 

错误写法：(?<year>\d{4})

2. 不支持的正则特性

以下常见但复杂的正则功能在RE2中不可用，请避免使用：

- 

断言：(?=...)、(?!...)、(?<=...)、（?<!...)

- 

条件表达式：(?(condition)true|false)

- 

递归匹配：(?R)、(?0)

- 

子程序引用：(?&name)、(?P>name)

- 

原子组：(?>...)

3. 使用建议

推荐使用[Regex101](https://regex101.com/)等工具调试正则表达式时，选择 Golang (RE2) 模式进行验证，以确保兼容性。若使用了上述不支持的语法，插件将无法正确解析或匹配。

## 附录：容器标准输出新旧版本对比

为提升日志存储效率与采集一致性，容器标准输出的日志元信息格式已完成升级。新版格式将元信息统一归类至__tag__字段中，实现存储优化和格式标准化。

- 

新版标准输出核心优势

- 

性能大幅提升

- 

采用C++重构，相较旧版Go实现，性能提升180%-300%。

- 

支持原生插件处理数据，支持多线程并行处理，充分利用系统资源。

- 

支持原生插件与Go插件灵活组合使用，满足复杂场景需求。

- 

更强的可靠性

- 

支持标准输出日志轮转队列，日志采集机制和文件采集机制统一，在标准输出日志快速轮转时的场景可靠性高。

- 

更低的资源消耗

- 

CPU使用率降低20%-25%。

- 

内存占用减少20%-25%。

- 

运维一致性增强

- 

参数配置统一：新版标准输出采集插件的配置参数和文件采集插件保持一致。

- 

元信息统一管理：容器元信息字段命名和Tag日志存储位置，与文件采集场景进行了统一，消费端只需维护同套处理逻辑。

- 

新旧版本特性对比

| 特性维度 | 旧版特点 | 新版特点 |
| --- | --- | --- |
| 存储方式 | 元信息作为普通字段直接嵌入日志内容中 | 元信息集中存放于 __tag__ 标签中 |
| 存储效率 | 每条日志重复携带完整元信息，占用较多存储空间 | 相同上下文下的多条日志可复用元信息，节省存储成本 |
| 格式一致性 | 与容器文件采集格式不一致 | 字段命名及存储结构与容器文件采集完全对齐，实现统一体验 |
| 查询访问方式 | 可通过字段名直接查询（如 _container_name_ ） | 需通过 __tag__ 访问对应键值（如 __tag__: _container_name_ ） |


- 

容器元信息字段映射表

| 旧版字段名称 | 新版字段名称 |
| --- | --- |
| _container_ip_ | __tag__:_container_ip_ |
| _container_name_ | __tag__:_container_name_ |
| _image_name_ | __tag__:_image_name_ |
| _namespace_ | __tag__:_namespace_ |
| _pod_name_ | __tag__:_pod_name_ |
| _pod_uid_ | __tag__:_pod_uid_ |


所有元信息字段在新版中均以__tag__:<key>形式存储于日志的标签（Tag）区域，而非嵌入日志内容中。

- 

新版变更对用户影响

- 

消费端适配：由于存储位置从“内容”变为“Tag”，用户的日志消费逻辑需做相应调整（例如查询时需通过 __tag__ 访问字段）。

- 

SQL兼容性：查询SQL已经自动兼容适配，因此用户无需修改查询语句即可同时处理新旧版本日志。

## 更多信息

### 全局配置参数介绍

| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。包含机器组 Topic，文件路径提取，自定义三种方式。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |


### 输入配置参数介绍

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

- 

| 配置项 | 说明 |
| --- | --- |
| Logtail 部署模式 | DaemonSet ：在集群的每个 Node 节点上部署一个 LoongCollector，负责采集该节点上所有容器的日志。 Sidecar ：每个容器组（Pod）运行一个 LoongCollector 容器，用于采集当前容器组（Pod）所有容器（Containers）的日志。不同 Pod 的日志采集相互隔离。 |
| 文件路径类型 | 支持配置 容器内路径 和 宿主机路径 。 容器内路径 ：采集容器内文本日志文件时，请选择容器内路径。 宿主机路径 ：采集集群节点上的服务日志时，请选择宿主机路径。 |
| 文件路径 | 根据日志在主机（例如 ECS）上的位置，设置日志目录和文件名称。 如果目标主机是 Linux 系统，则日志路径必须以正斜线（/）开头，例如 /apsara/nuwa/**/app.Log 。 如果目标主机是 Windows 系统，则日志路径必须以盘符开头，例如 C:\Program Files\Intel\**\*.Log 。 目录名和文件名均支持完整模式和通配符模式，文件名规则请参见 [Wildcard matching](https://man7.org/linux/man-pages/man7/glob.7.html) 。其中，日志路径通配符只支持星号（*）和半角问号（?）。 日志文件查找模式为多层目录匹配，即符合条件的指定目录（包含所有层级的目录）下所有符合条件的文件都会被查找到。例如： /apsara/nuwa/**/*.log 表示 /apsara/nuwa 目录（包含该目录的递归子目录）中后缀名为.log 的文件。 /var/logs/app_*/**/*.log 表示 /var/logs 目录下所有符合 app_* 格式的目录（包含该目录的递归子目录）中后缀名为 .log 的文件。 /var/log/nginx/**/access* 表示 /var/log/nginx 目录（包含该目录的递归子目录）中以 access 开头的文件。 |
| 最大目录监控深度 | 设置日志目录被监控的最大深度，即 文件路径 中通配符 ** 匹配的最大目录深度。0 代表只监控本层目录。 |
| 标准输出 | 打开 标准输出 后，Logtail 将采集容器标准输出。 |
| 标准错误 | 打开 标准错误 后，Logtail 将采集容器标准错误。 |
| 允许标准输出多次采集 | 默认情况下，一个容器的标准输出日志只能匹配一个 Logtail 新版标准输出采集配置。如果标准输出需要被多个新版标准输出采集配置采集，需打开 允许文件多次采集 开关。 |
| 启用容器元信息预览 | 打开 启用容器元信息预览 后，可在创建 Logtail 配置后，查看容器元信息，包括匹配容器信息和全量容器信息。 |
| 容器过滤 | 过滤条件说明 重要 容器 Label 为 Docker inspect 中的 Label，不是 Kubernetes 中的 Label。如何获取，请参见 [获取容器](products/sls/documents/how-do-i-obtain-the-labels-and-environment-variables-of-a-container.md) [Label](products/sls/documents/how-do-i-obtain-the-labels-and-environment-variables-of-a-container.md) 。 环境变量为容器启动中配置的环境变量信息。如何获取，请参见 [获取容器环境变量](products/sls/documents/how-do-i-obtain-the-labels-and-environment-variables-of-a-container.md) 。 Kubernetes 场景下，推荐使用 Kubernetes 层级的信息（ K8s Pod 名称正则匹配 、 K8s Namespace 正则匹配 、 K8s 容器名称正则匹配 、 K8s Pod 标签白名单 等）进行容器过滤。 Kubernetes 中的 Namespace 和容器名称会映射到容器 Label 中，分别为 io.kubernetes.pod.namespace 和 io.kubernetes.container.name ，推荐使用这两个容器 Label 进行容器过滤。例如，某 Pod 所属的命名空间为 backend-prod ，容器名为 worker-server ，如要采集包含该容器的日志，可以设置容器 Label 白名单为 io.kubernetes.pod.namespace : backend-prod 或 io.kubernetes.container.name : worker-server 。 如果以上两个容器 Label 不满足过滤需求，请使用环境变量的黑白名单进行容器过滤。 K8s Pod 名称正则匹配 通过 Pod 名称指定待采集的容器，支持正则匹配。例如设置为 ^(nginx-log-demo.*)$ ，表示匹配以 nginx-log-demo 开头的 Pod 下的所有容器。 K8s Namespace 正则匹配 通过 Namespace 名称指定采集的容器，支持正则匹配。例如设置为 ^(default|nginx)$ ，表示匹配 nginx 命名空间、default 命名空间下的所有容器。 K8s 容器名称正则匹配 通过容器名称指定待采集的容器（Kubernetes 容器名称是定义在 spec.containers 中），支持正则匹配。例如设置为 ^(container-test)$ ，表示匹配所有名为 container-test 的容器。 容器 label 白名单(docker 场景使用，k8s 场景不推荐使用) 容器 Label 白名单，用于指定待采集的容器。默认为空，表示采集所有容器的标准输出。如要设置容器 Label 白名单，那么 LabelKey 必填，LabelValue 可选填。 如果 LabelValue 为空，则容器 Label 中包含 LabelKey 的容器都匹配。 如果 LabelValue 不为空，则容器 Label 中包含 LabelKey=LabelValue 的容器才匹配。 LabelValue 默认为字符串匹配，即只有 LabelValue 和容器 Label 的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配。例如：配置 LabelKey 为 io.kubernetes.container.name ，配置 LabelValue 为 ^(nginx|cube)$ ，表示可匹配名为 nginx、cube 的容器。 多个白名单之间为或关系，即只要容器 Label 满足任一白名单即可被匹配。 容器 label 黑名单(docker 场景使用，k8s 场景不推荐使用) 容器 Label 黑名单，用于排除不采集的容器。默认为空，表示不排除任何容器。如要设置容器 Label 黑名单，那么 LabelKey 必填，LabelValue 可选填。 如果 LabelValue 为空，则容器 Label 中包含 LabelKey 的容器都将被排除。 如果 LabelValue 不为空，则容器 Label 中包含 LabelKey=LabelValue 的容器才会被排除。 LabelValue 默认为字符串匹配，即只有 LabelValue 和容器 Label 的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配。例如：设置 LabelKey 为 io.kubernetes.container.name ，设置 LabelValue 为 ^(nginx|cube)$ ，表示可匹配名为 nginx、cube 的容器。 多个黑名单之间为或关系，即只要容器 Label 满足任一黑名单对即可被排除。 环境变量白名单 环境变量白名单，用于指定待采集的容器。默认为空，表示采集所有容器的标准输出。如要设置环境变量白名单，那么 EnvKey 必填，EnvValue 可选填。 如果 EnvValue 为空，则容器环境变量中包含 EnvKey 的容器都匹配。 如果 EnvValue 不为空，则容器环境变量中包含 EnvKey=EnvValue 的容器才匹配。 EnvValue 默认为字符串匹配，即只有 EnvValue 和环境变量的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配，例如：设置 EnvKey 为 NGINX_SERVICE_PORT ，设置 EnvValue 为 ^(80|6379)$ ，表示可匹配服务端口为 80、6379 的容器。 多个白名单之间为或关系，即只要容器的环境变量满足任一键值对即可被匹配。 环境变量黑名单 环境变量黑名单，用于排除不采集的容器。默认为空，表示不排除任何容器。如要设置环境变量黑名单，那么 EnvKey 必填，EnvValue 可选填。 如果 EnvValue 为空，则容器环境变量中包含 EnvKey 的容器的日志都将被排除。 如果 EnvValue 不为空，则容器环境变量中包含 EnvKey=EnvValue 的容器才会被排除。 EnvValue 默认为字符串匹配，即只有 EnvValue 和环境变量的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配，例如：设置 EnvKey 为 NGINX_SERVICE_PORT ，设置 EnvValue 为 ^(80|6379)$ ，表示可匹配服务端口为 80、6379 的容器。 多个黑名单之间为或关系，即只要容器的环境变量满足任一键值对即可被排除。 K8s Pod 标签白名单 通过 Kubernetes Label 白名单指定待采集的容器。如要设置 Kubernetes Label 白名单，那么 LabelKey 必填，LabelValue 可选填。 如果 LabelValue 为空，则 Kubernetes Label 中包含 LabelKey 的容器都匹配。 如果 LabelValue 不为空，则 Kubernetes Label 中包含 LabelKey=LabelValue 的容器才匹配。 LabelValue 默认为字符串匹配，即只有 LabelValue 和 Kubernetes Label 的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配。例如设置 LabelKey 为 app ，设置 LabelValue 为 ^(test1|test2)$ ，表示匹配 Kubernetes Label 中包含 app:test1、app:test2 的容器。 多个白名单之间为或关系，即只要 Kubernetes Label 满足任一白名单即可被匹配。 说明 由于在 Kubernetes 管控类资源（例如 Deployment）运行时更改 Label，不会重启具体的工作资源 Pod，因此 Pod 无法感知此变更，可能导致匹配规则失效。设置 K8s Label 黑白名单时，请以 Pod 中的 Kubernetes Label 为准。关于 Kubernetes Label 的更多信息，请参见 [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) 。 K8s Pod 标签黑名单 通过 Kubernetes Label 黑名单排除不采集的容器。如要设置 Kubernetes Label 黑名单，那么 LabelKey 必填，LabelValue 可选填。 如果 LabelValue 为空，则 Kubernetes Label 中包含 LabelKey 的容器都被排除。 如果 LabelValue 不为空，则 Kubernetes Label 中包含 LabelKey=LabelValue 的容器才会被排除。 LabelValue 默认为字符串匹配，即只有 LabelValue 和 Kubernetes Label 的值完全相同才会匹配。如果该值以 ^ 开头并且以 $ 结尾，则为正则匹配。例如设置 LabelKey 为 app ，设置 LabelValue 为 ^(test1|test2)$ ，表示匹配 Kubernetes Label 中包含 app:test1、app:test2 的容器。 多个黑名单之间为或关系，即只要 Kubernetes Label 满足任一黑名单对即可被排除。 说明 由于在 Kubernetes 管控类资源（例如 Deployment）运行时更改 Label，不会重启具体的工作资源 Pod，因此 Pod 无法感知此变更，可能导致匹配规则失效。设置 K8s Label 黑白名单时，请以 Pod 中的 Kubernetes Label 为准。关于 Kubernetes Label 的更多信息，请参见 [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) 。 |
| 日志标签富化 | 可将环境变量和 Kubernetes Label 添加到日志，作为日志标签。 环境变量相关 设置环境变量扩展字段后，日志服务将在日志中新增环境变量相关字段。例如设置 环境变量名 为 VERSION ，设置 tag 名 为 env_version ，当容器中包含环境变量 VERSION=v1.0.0 时，会将该信息添加到日志中，即添加字段 __tag__:__env_version__: v1.0.0 。 Pod 标签相关 设置 Kubernetes Pod 扩展字段后，日志服务将在日志中新增 Kubernetes Pod 相关字段。例如设置 Pod 标签名 为 app ，设置 tag 名 为 k8s_pod_app ，当 Kubernetes 中包含 Label app=serviceA 时，会将该信息添加到日志中，即添加字段 __tag__:__k8s_pod_app__: serviceA 。 |
| 文件编码 | 选择日志文件的编码格式。 |
| 首次采集大小 | 配置首次生效时，匹配文件的起始采集位置距离文件结尾的大小。首次采集大小设定值为 1024 KB。 首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。 首次采集时，如果文件大于 1024 KB，则从距离文件末尾 1024 KB 的位置开始采集。 可通过此处修改 首次采集大小 ，取值范围为 0~10485760，单位为 KB。 |
| 采集黑名单 | 打开 采集黑名单 开关后，可进行黑名单配置，即可在采集时忽略指定的目录或文件。支持完整匹配和通配符匹配目录和文件名。其中，通配符只支持星号（*）和半角问号（?）。 重要 如在配置 文件路径 时使用了通配符，但又需要过滤掉其中部分路径，则需在 采集黑名单 中填写对应的完整路径来保证黑名单配置生效。 例如配置 文件路径 为 /home/admin/app*/log/*.log ，但要过滤 /home/admin/app1* 目录下的所有子目录，则需选择 目录黑名单 ，配置目录为 /home/admin/app1*/** 。如果配置为 /home/admin/app1* ，黑名单不会生效。 匹配黑名单过程存在计算开销，建议黑名单条目数控制在 10 条内。 目录路径不能以正斜线（/）结尾，例如将设置路径为 /home/admin/dir1/ ，目录黑名单不会生效。 支持按照文件路径黑名单、文件黑名单、目录黑名单设置，详细说明如下： 文件路径黑名单 选择 文件路径黑名单 ，配置路径为 /home/admin/private*.log ，则表示在采集时忽略 /home/admin/ 目录下所有以 private 开头，以.log 结尾的文件。 选择 文件路径黑名单 ，配置路径为 /home/admin/private*/*_inner.log ，则表示在采集时忽略 /home/admin/ 目录下以 private 开头的目录内，以_inner.log 结尾的文件。例如 /home/admin/private/app_inner.log 文件被忽略， /home/admin/private/app.log 文件被采集。 文件黑名单 选择 文件黑名单 ，配置文件名为 app_inner.log ，则表示采集时忽略所有名为 app_inner.log 的文件。 目录黑名单 选择 目录黑名单 ，配置目录为 /home/admin/dir1 ，则表示在采集时忽略 /home/admin/dir1 目录下的所有文件。 选择 目录黑名单 ，配置目录为 /home/admin/dir* ，则表示在采集时忽略 /home/admin/ 目录下所有以 dir 开头的子目录下的文件。 选择 目录黑名单 ，配置目录为 /home/admin/*/dir ，则表示在采集时忽略 /home/admin/ 目录下二级目录名为 dir 的子目录下的所有文件。例如 /home/admin/a/dir 目录下的文件被忽略， /home/admin/a/b/dir 目录下的文件被采集。 |
| 允许文件多次采集 | 默认情况下，一个日志文件只能匹配一个 Logtail 配置。如果文件中的日志需要被采集多份，需要打开 允许文件多次采集 开关。 |
| 高级参数 | 其它可选的与文件输入插件相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |


### 处理配置参数介绍

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

| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:½0) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，保留为一共四条日志。 |
| 处理模式 | 处理插件组合 ，包括 原生处理插件 和 拓展处理插件 。有关处理插件的更多信息，请参见 [处理插件概述](products/sls/documents/overview-22.md) 。 重要 处理插件的使用限制，请以控制台页面的提示为准。 2.0 版本的 Logtail： 原生处理插件可任意组合。 原生处理插件和扩展处理插件可同时使用，但扩展处理插件只能出现在所有的原生处理插件之后。 低于 2.0 版本的 Logtail： 不支持同时添加原生插件和扩展插件。 原生插件仅可用于采集文本日志。使用原生插件时，须符合如下要求： 第一个处理插件必须为正则解析插件、分隔符模式解析插件、JSON 解析插件、Nginx 模式解析插件、Apache 模式解析插件或 IIS 模式解析插件。 从第二个处理插件到最后一个处理插件，最多包括 1 个时间解析处理插件，1 个过滤处理插件和多个脱敏处理插件。 对于 解析失败时保留原始字段 和 解析成功时保留原始字段 参数，只有以下组合有效，其余组合无效。 只上传解析成功的日志： 解析成功时上传解析后的日志，解析失败时上传原始日志： 解析成功时不仅上传解析后的日志，并且追加原始日志字段，解析失败时上传原始日志。 例如，原始日志 "content": "{"request_method":"GET", "request_time":"200"}" 解析成功，追加原始字段是在解析后日志的基础上再增加一个字段，字段名为 重命名的原始字段 （如果不填则默认为原始字段名），字段值为原始日志 {"request_method":"GET", "request_time":"200"} 。 |


### 地域

- 

登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.70905a3dccueNa)，在Project列表中，单击目标Project。

- 

单击Project名称右侧的进入项目概览页面。

- 

在基础信息中可查看当前Project的地域名称，地域名称对应RegionID请参考下表。

地域代表云服务资源的物理数据中心所在的地理位置，RegionID 是云服务地域的唯一标识符。

| 地域名称 | RegionID |
| --- | --- |
| 华北 1（青岛） | cn-qingdao |
| 华北 2（北京） | cn-beijing |
| 华北 3（张家口） | cn-zhangjiakou |
| 华北 5（呼和浩特） | cn-huhehaote |
| 华北 6（乌兰察布） | cn-wulanchabu |
| 华东 1（杭州） | cn-hangzhou |
| 华东 2（上海） | cn-shanghai |
| 华东 5（南京-本地地域-关停中） | cn-nanjing |
| 华东 6（福州-本地地域-关停中） | cn-fuzhou |
| 华南 1（深圳） | cn-shenzhen |
| 华南 2（河源） | cn-heyuan |
| 华南 3（广州） | cn-guangzhou |
| 菲律宾（马尼拉） | ap-southeast-6 |
| 韩国（首尔） | ap-northeast-2 |
| 马来西亚（吉隆坡） | ap-southeast-3 |
| 日本（东京） | ap-northeast-1 |
| 泰国（曼谷） | ap-southeast-7 |
| 西南 1（成都） | cn-chengdu |
| 新加坡 | ap-southeast-1 |
| 印度尼西亚（雅加达） | ap-southeast-5 |
| 中国香港 | cn-hongkong |
| 德国（法兰克福） | eu-central-1 |
| 美国（弗吉尼亚） | us-east-1 |
| 美国（硅谷） | us-west-1 |
| 英国（伦敦） | eu-west-1 |
| 阿联酋（迪拜） | me-east-1 |
| 沙特（利雅得） | me-central-1 |


### 网络传输类型

- 

- 

| 网络类型 | 对应域名类型 | 描述 | 适用场景 |
| --- | --- | --- | --- |
| 阿里云内网 | 私网域名 | 阿里云内网为千兆共享网络，日志数据通过阿里云内网传输比公网传输更快速、稳定，内网包括 VPC 和经典网络。 | ECS 实例和日志服务 Project 属于同一地域或 [服务器通过高速通道连接专有网络（VPC）](products/ecs/documents/user-guide/manage-servers-that-are-not-provided-by-alibaba-cloud.md) 的情况。 说明 推荐在 ECS 所在地域创建日志服务 Project，通过阿里云内网采集 ECS 中日志，不消耗公网带宽。 |
| 公网 | 公网域名 | 使用公网传输日志数据，不仅会受到网络带宽的限制，还可能会因网络抖动、延迟、丢包等影响数据采集的速度和稳定性。 | 以下两种情况，可以选择公网传输数据。 ECS 实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 |
| 传输加速 | 传输加速域名 | 利用阿里云 CDN 边缘节点进行日志采集加速，相对公网采集在网络延迟、稳定性上具有很大优势，但流量需额外计费。 | 如果业务服务器、日志服务 Project 分别属于国内地域和国外地域，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，您可以选择传输加速传输数据。更多信息，请参见 [传输加速](products/sls/documents/select-a-network-type.md) 。 |


[上一篇：采集Kubernetes Pod文本日志（Sidecar模式）](products/sls/documents/collect-k8s-cluster-logs-through-sidecar.md)[下一篇：采集SQL查询结果](products/sls/documents/retrieving-sql-query-results.md)

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
