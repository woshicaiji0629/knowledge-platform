# 日志服务主机文本日志采集-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/host-text-log-collection-auto-install

# 持续采集主机文本日志
分散在不同服务器上的业务日志或系统日志，难以统一检索、监控和分析。使用LoongCollector（Logtail）采集器，可将 ECS 实例、自建 IDC 或其他云厂商主机上的文本日志采集到日志服务，实现集中化管理与分析。支持持续采集（实时增量，适合生产环境持续监控）和一次性采集（批量导入静态文件，适合历史数据迁移）两种模式。
## 选择采集模式
| 场景 | 推荐模式 |
| --- | --- |
| 业务日志持续写入，需实时监控、告警 | 持续采集 |
| 历史归档文件一次性导入 | 一次性采集 |
| 系统迁移或数据迁移，补录历史数据 | 一次性采集 |
| 临时调查历史某段时间日志 | 一次性采集 |
说明
LoongCollector 默认只采集新增（增量）日志。如需采集已存在的历史静态文件，必须使用一次性采集模式。
## 适用范围
支持的操作系统与架构：
LoongCollector 当前仅支持 Linux 系统；Windows 主机请使用 Logtail。新接入场景建议优先选用 LoongCollector。
LoongCollector 是阿里云日志服务推出的新一代日志采集 Agent，是 Logtail 的升级版。用户在使用时，只需安装LoongCollector或Logtail其中之一，无需重复安装。
计算资源要求：
CPU：最少预留0.4 Core。
内存：最少需要 300 MB。
使用率建议：为保证稳定运行，建议LoongCollector（Logtail）的实际资源使用率低于限制值的80%。实际使用量与采集速率、监控目录和文件数量、发送阻塞程度等因素相关。
权限要求：
若使用 RAM 用户操作，需授予AliyunLogFullAccess和AliyunECSFullAccess权限。如需精细化授权，请参考[附录：自定义权限策略](host-text-log-collection-auto-install.md)。
## 采集配置创建流程
[准备工作](host-text-log-collection-auto-install.md)：创建Project和LogStore，Project是资源管理单元，用于隔离不同业务日志，而LogStore用于存储日志。
[配置机器组（安装](host-text-log-collection-auto-install.md)[LoongCollector）](host-text-log-collection-auto-install.md)：根据服务器类型，安装LoongCollector，并将其加入到机器组。使用机器组统一管理采集节点，对服务器进行配置分发与状态管理。
[创建并配置日志采集规则](host-text-log-collection-auto-install.md)：
[全局与输入配置](host-text-log-collection-auto-install.md)：定义采集配置的名称及日志采集的来源和范围。
[日志处理与结构化](host-text-log-collection-auto-install.md)：根据日志格式进行处理配置。
多行日志：适用于单条日志跨越多行（如 Java 异常堆栈、Python traceback），通过行首正则识别每条日志，并将同一日志的连续多行内容合并为一条完整日志。
结构化解析：通过配置解析插件（如正则、分隔符、NGINX 模式等）将原始字符串提取为结构化的键值对，每个字段都可以被独立查询与分析。
过滤处理：通过配置采集黑名单和内容过滤规则，筛选有效日志内容，减少冗余数据的传输与存储。
[日志分类](host-text-log-collection-auto-install.md)：通过配置日志主题（Topic）灵活区分不同业务、服务器、路径来源的日志。
查询分析配置：系统默认开启全文索引，支持关键词搜索。建议启用字段索引，以便对结构化字段进行精确查询和分析，提升检索效率。
[验证与故障排查](host-text-log-collection-auto-install.md)：完成配置后，验证日志是否成功采集，如遇采集无数据、心跳失败或解析错误等问题，参考[常见问题排查](host-text-log-collection-auto-install.md)。
## 准备工作
在采集日志前，需规划并创建用于管理与存储日志的Project和LogStore。若已有可用资源，可跳过此步骤，直接进入[配置机器组（安装](host-text-log-collection-auto-install.md)[LoongCollector）](host-text-log-collection-auto-install.md)。
创建Project
登录[日志服务控制台](https://sls.console.aliyun.com/)。
单击创建Project，并配置：
所属地域：根据日志来源选择，创建后不可修改。
Project名称：阿里云内全局唯一，创建后不可修改。
其他配置保持默认，单击创建。如需了解其他参数，请参见[创建](manage-a-project.md)[Project](manage-a-project.md)。
创建LogStore
单击Project名称，进入目标Project。
在左侧导航栏，选择日志库，单击+。
在创建LogStore页面，完成以下核心配置：
Logstore名称：设置一个在Project内唯一的名称，该名称创建后不可修改。
Logstore类型：根据规格对比选择标准型或查询型。
计费模式：
按使用功能计费（不支持更改）：按存储、索引、读写次数等各项资源独立计费。适合小规模或功能使用不确定的场景。
按写入数据量计费：仅按原始写入数据量计费，提供30天免费存储，以及免费的数据加工、投递等功能。适合存储周期接近30天或数据处理链路复杂的业务场景。
数据保存时间：设置日志的保留天数（1~3650天，3650为永久保存），默认为30天。
其他配置保持默认，单击确定。如需了解其他配置信息，请参考[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## 步骤一：配置机器组（安装LoongCollector）
在完成[准备工作](host-text-log-collection-auto-install.md)后，为不同类型的服务器安装LoongCollector并将其加入机器组。
说明
以下安装步骤仅适用于日志源为阿里云ECS实例，且该实例与日志服务Project属于同一阿里云账号和相同地域的场景。
如果您的ECS实例与Project不在同一账号或地域，或者日志源为自建服务器，请参考[LoongCollector 安装与配置](loongcollector-installation-linux.md)进行操作。
配置步骤：
在日志库页面，单击目标LogStore名称前的展开。
单击接入数据后的，在快速数据接入弹框中，选择文本日志接入模板（如单行-文本日志），单击立即接入。
所有文本日志接入模板仅在解析插件上有所差异，其余配置流程一致，后续均可修改。
在机器组配置页面，配置如下参数：
使用场景：主机场景
安装环境：ECS
配置机器组：根据目标服务器的LoongCollector安装情况与机器组配置状态，选择对应操作：
已安装LoongCollector且已加入某个机器组，直接在源机器组列表中勾选，将其添加至应用机器组列表，无需重复创建。
未安装LoongCollector，单击创建机器组：
以下步骤将引导您完成LoongCollector的一键自动安装并创建机器组。
系统会自动列出与 Project 同地域的 ECS 实例，勾选需要采集日志的一台或多台实例。
单击安装并创建为机器组，系统将自动在所选ECS实例上安装LoongCollector。
配置机器组名称并单击确定。
说明
如果安装失败或一直处于等待中，请检查ECS地域是否与Project相同。
如需将已安装LoongCollector的服务器加入已有机器组，请参考常见问题[如何将服务器加入到已有机器组？](host-text-log-collection-auto-install.md)
检查心跳状态：单击下一步，页面出现机器组心跳情况。查看心跳状态，若为OK表示机器组连接正常，单击下一步，进入Logtail配置页面。
若为FAIL，可能是初次建立心跳需要花费一些时间，请等待两分钟左右，再刷新心跳状态。若刷新后仍为FAIL，请参考[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进一步排查。
## 步骤二：创建并配置日志采集规则
完成[LoongCollector](host-text-log-collection-auto-install.md)[安装和机器组配置](host-text-log-collection-auto-install.md)后，进入Logtail配置页面，定义日志采集和处理规则。
### 1. 全局与输入配置
定义采集配置的名称及日志采集的来源和范围。
全局配置：
配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。命名规则：
仅支持小写字母、数字、连字符（-）和下划线（_）。
必须以小写字母或者数字作为开头和结尾。
输入配置：
类型：文本日志采集。
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.Log的文件。
Windows：以盘符开头，如C:\Program Files\Intel\**\*.Log。
最大目录监控深度：文件路径中通配符**匹配的最大目录深度。默认为0，表示只监控本层目录。
### 2. 日志处理与结构化
通过配置日志处理规则，将原始非结构化日志转换为结构化、可检索的数据，提升日志查询与分析效率。建议在配置前先添加日志样例：
在Logtail配置页面的处理配置区域，单击添加日志样例，输入待采集的日志内容。系统将基于样例识别日志格式，辅助生成正则表达式和解析规则，降低配置难度。
场景一：多行日志处理（如Java堆栈日志）
由于Java异常堆栈、JSON等日志通常跨越多行，在默认采集模式下会被拆分为多条不完整的记录，导致上下文信息丢失；为此，可启用多行模式，通过配置行首正则表达式，将同一日志的连续多行内容合并为一条完整日志。
效果示例：
| 未经任何处理的原始日志 | 默认采集模式下，每行作为独立日志，堆栈信息被拆散，丢失上下文 | 开启多行模式，通过行首正则表达式识别完整日志，保留完整语义结构。 |
| --- | --- | --- |
|  |  |  |
配置步骤：在Logtail配置页面的处理配置区域，开启多行模式：
类型：选择自定义或多行JSON。
自定义：原始日志的格式不固定，需配置行首正则表达式，来标识每条日志的起始行。
行首正则表达式：支持自动生成或手动输入，正则表达式需要能够匹配完整的一行数据，如上述示例中匹配的正则表达式为\[\d+-\d+-\w+:\d+:\d+,\d+]\s\[\w+]\s.*。
自动生成：单击自动生成正则表达式，然后在日志样例文本框中，选择需提取的日志内容，单击生成正则。
手动输入：单击手动输入正则表达式，输入完成后，单击验证。
多行JSON：当原始日志均为标准JSON格式时，日志服务会自动处理单条JSON日志内部的换行。
切分失败处理方式：
丢弃：如果一段文本无法匹配行首规则，则直接丢弃。
保留单行：将无法匹配的文本按原始的单行模式进行切分和保留。
场景二：结构化日志
当原始日志为非结构化或半结构化文本（如 Nginx 访问日志、应用输出日志）时，直接进行查询和分析往往效率低下。日志服务提供多种数据解析插件，能够自动将不同格式的原始日志转换为结构化数据，为后续的分析、监控和告警提供坚实的数据基础。
效果示例：
| 未经任何处理的原始日志 | 结构化解析后的日志 |
| --- | --- |
| 192.168.*.* - - [15/Apr/2025:16:40:00 +0800] "GET /nginx-logo.png HTTP/1.1" 0.000 514 200 368 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.*.* Safari/537.36" | body_bytes_sent: 368 http_referer: - http_user_agent : Mozi11a/5.0 (Nindows NT 10.0; Win64; x64) AppleMebKit/537.36 (KHTML, like Gecko) Chrome/131.0.x.x Safari/537.36 remote_addr:192.168.*.* remote_user: - request_length: 514 request_method: GET request_time: 0.000 request_uri: /nginx-logo.png status: 200 time_local: 15/Apr/2025:16:40:00 |
配置步骤：在Logtail配置页面的处理配置区域
添加解析插件：单击添加处理插件，根据实际格式配置[正则解析、分隔符解析、JSON 解析等插件](host-text-log-collection-auto-install.md)。此处以采集NGINX日志为例，选择原生处理插件>NGINX模式解析。
NGINX日志配置：将 Nginx 服务器配置文件（nginx.conf）中的log_format定义完整地复制并粘贴到此文本框中。
示例：
log_format main '$remote_addr - $remote_user [$time_local] "$request" ''$request_time $request_length ''$status $body_bytes_sent "$http_referer" ''"$http_user_agent"';
重要
此处的格式定义必须与服务器上生成日志的格式完全一致，否则将导致日志解析失败。
通用配置参数说明：以下参数在多种数据解析插件中都会出现，其功能和用法是统一的。
原始字段：指定要解析的源字段名。默认为content，即采集到的整条日志内容。
解析失败时保留原始字段：推荐开启。当日志无法被插件成功解析时（例如格式不匹配），此选项能确保原始日志内容不会丢失，而是被完整保留在指定的原始字段中。
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
字段名：过滤的日志字段。
字段值：用于过滤的正则表达式，仅支持全文匹配，不支持关键词部分匹配。
## 通过黑名单控制采集范围
通过黑名单机制排除指定目录或文件，避免无关或敏感日志被上传。
配置步骤：在Logtail配置页面的输入配置>其他输入配置区域，启用采集黑名单，并单击添加。
支持完整匹配和通配符匹配目录和文件名，通配符只支持星号（*）和半角问号（?）。
文件路径黑名单：需要忽略的文件路径，示例：
/home/admin/private*.log：在采集时忽略/home/admin/目录下所有以private开头，以.log结尾的文件。
/home/admin/private*/*_inner.log：在采集时忽略/home/admin/目录下以private开头的目录内，以_inner.log结尾的文件。
文件黑名单：配置采集时需要忽略的文件名，示例：
app_inner.log：在采集时忽略所有名为app_inner.log的文件。
目录黑名单：目录路径不能以正斜线（/）结尾，示例：
/home/admin/dir1/：目录黑名单不会生效。
/home/admin/dir*：在采集时忽略/home/admin/目录下所有以dir开头的子目录下的文件。
/home/admin/*/dir：在采集时忽略/home/admin/目录下二级目录名为dir的子目录下的所有文件。例如/home/admin/a/dir目录下的文件被忽略，/home/admin/a/b/dir目录下的文件被采集。
### 4. 日志分类
当多个应用或实例的日志格式相同但路径不同时（如/apps/app-A/run.log和/apps/app-B/run.log），采集日志难以区分来源。通过配置日志主题（Topic），对来自不同应用、服务或路径的日志进行逻辑区分，实现统一存储下的高效归类与精准查询。
配置步骤：全局配置>其他全局配置>日志主题类型：选择Topic生成方式，支持如下三种类型：
机器组Topic：采集配置应用于多个机器组时，LoongCollector 会自动使用服务器所属的机器组名称作为__topic__字段上传。适用于按主机划分日志场景。
自定义：格式为customized://<自定义主题名>，例如customized://app-login。适用于固定业务标识的静态主题场景。
文件路径提取：从日志文件的完整路径中提取关键信息，动态标记日志来源。适用于多用户/应用共用相同日志文件名但路径不同的情况。当多个用户或服务将日志写入不同顶级目录，但下级路径和文件名一致时，仅靠文件名无法区分来源，例如：
/data/logs ├── userA │ └── serviceA │ └── service.log ├── userB │ └── serviceA │ └── service.log └── userC └── serviceA └── service.log
此时您可以配置文件路径提取，并使用正则表达式从完整路径中提取关键信息，将匹配结果作为日志主题（Topic）上传至LogStore。
文件路径提取规则：基于正则表达式的捕获组
在配置正则表达式时，系统根据捕获组的数量和命名方式自动决定输出字段格式，规则如下：
文件路径的正则表达式中，需要对正斜线（/）进行转义。
| 捕获组类型 | 适用场景 | 生成字段 | 正则示例 | 匹配路径示例 | 生成字段示例 |
| --- | --- | --- | --- | --- | --- |
| 单捕获组（仅一个 (.*?) ） | 仅需一个维度区分来源（如用户名、环境） | 生成 __topic__ 字段 | \/logs\/(.*?)\/app\.log | /logs/userA/app.log | __topic__：userA |
| 多捕获组-非命名（多个 (.*?) ） | 需要多个维度区分来源但无需语义标签 | 生成 tag 字段 __tag__:__topic_{i}__ ，其中 {i} 为捕获组的序号 | \/logs\/(.*?)\/(.*?)\/app\.log | /logs/userA/svcA/app.log | __tag__:__topic_1__userA ； __tag__:__topic_2__svcA |
| 多捕获组-命名（使用 (?P<name>.*?) | 需要多个维度区分来源且希望字段含义清晰、便于查询与分析 | 生成 tag 字段 __tag__:{name} | \/logs\/(?P<user>.*?)\/(?P<service>.*?)\/app\.log | /logs/userA/svcA/app.log | __tag__:user:userA ； __tag__:service:svcA |
### 5. 输出配置
默认采集所有日志发送到当前日志库，压缩方式为lz4。如需将同一来源的日志分发到不同日志库，请参考如下步骤进行配置：
多目标动态分发
重要
多目标发送仅适用于LoongCollector 3.0.0及以上版本，Logtail不支持。
输出目标最多可配置5个。
配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考[如何管理多目标分发配置？](host-text-log-collection-auto-install.md)。
配置步骤：在Logtail配置页面的输出配置区域。
单击展开输出配置。
单击添加输出目标，完成如下配置：
日志库：选择目标日志库。
压缩方式：支持lz4和zstd。
路由配置：根据日志的Tag字段路由分发，满足路由配置的日志会被上传到目标日志库，路由配置为空时表示采集到的所有日志都会被上传到目标日志库。
Tag名称：用于路由的Tag字段名称，直接填写字段名（如__path__），无需__tag__:前缀。Tag字段分为如下两类：
关于Tag的详细信息请参考[管理](manage-loongcollector-to-collect-tags.md)[LoongCollector](manage-loongcollector-to-collect-tags.md)[采集](manage-loongcollector-to-collect-tags.md)[Tag](manage-loongcollector-to-collect-tags.md)。
Agent相关：与采集 Agent 本身相关，不依赖插件。 如__hostname__、__user_defined_id__等。
输入插件相关：依赖输入插件，由输入插件提供并富化相关信息到日志中。如文件采集的__path__；K8s采集的_pod_name_、_container_name_等。
Tag值：日志的Tag字段值与此匹配时，发送到该目标日志库。
是否丢弃该Tag字段：开启后上传的日志中不包含该Tag字段。
## 步骤三：查询与分析配置
在完成日志处理与插件配置后，单击下一步，进入查询分析配置页面：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[字段索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
## 步骤四：验证与故障排查
配置完成后，应用到机器组并保存。等待片刻后，按以下清单进行验证。
### 验证清单
确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。
检查LoongCollector状态：sudo /etc/init.d/loongcollectord status。
检查机器组心跳：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态。
如果心跳为OK，则表示机器组与日志服务 Project 连接正常。
如果心跳为FAIL：参考[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进行排查。
查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。
### 常见问题排查
机器组心跳连接为fail
检查用户标识：如果您的服务器类型不是ECS，或ECS和Project属于不同阿里云账号，请检查指定目录下是否存在正确的用户标识，如不存在请参考如下命令手动创建。
Linux：执行cd /etc/ilogtail/users/ && touch <uid>命令，创建用户标识文件。
Windows：进入C:\LogtailData\users\目录，创建一个名为<uid>的空文件。
检查机器组标识：如果您在创建机器组时使用了用户自定义标识，请检查指定目录下是否存在user_defined_id文件，如果存在请检查该文件中的内容是否与机器组配置的自定义标识一致。
Linux：
# 配置用户自定义标识,如目录不存在请手动创建 echo "user-defined-1" > /etc/ilogtail/user_defined_id
Windows：在C:\LogtailData目录下新建user_defined_id文件，并写入用户自定义标识。（如目录不存在，请手动创建）
如果用户标识和机器组标识均配置无误，请参考[LoongCollector（Logtail）机器组问题排查思路](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进一步排查。
日志采集无数据
检查是否有增量日志：配置LoongCollector（Logtail）采集后，如果待采集的日志文件没有新增日志，则LoongCollector（Logtail）不会采集该文件。
检查机器组心跳状态：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态。
如果心跳为OK，则表示机器组与日志服务 Project 连接正常。
如果心跳为FAIL：参考[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进行排查。
确认LoongCollector（Logtail）采集配置是否已应用到机器组：即使LoongCollector（Logtail）采集配置已创建，但如果未将其应用到机器组，日志仍无法被采集。
前往资源组>机器组页面，单击目标机器组名称，进入机器组配置页面。
在页面中查看管理配置，左侧展示全部Logtail配置，右侧展示已生效Logtail配置。如果目标LoongCollector（Logtail）采集配置已移动到右侧生效区域，则表示该配置已成功应用到目标机器组。
如果目标LoongCollector（Logtail）采集配置未移动到右侧生效区域，请单击修改，在左侧全部Logtail配置列表中勾选目标LoongCollector（Logtail）配置名称，单击移动到右侧生效区域，完成后单击确定。
采集日志报错或格式错误
排查思路：这种情况说明网络连接和基础配置正常，问题主要出在日志内容与解析规则不匹配。您需要查看具体的错误信息来定位问题：
在Logtail配置页面，单击采集异常的LoongCollector（Logtail）配置名称，在日志采集错误页签下，单击时间选择设置查询时间。
在区域，查看错误日志的告警类型，并根据[采集数据常见错误类型](log-collection-error-type.md)查询对应的解决办法。
## 配额与限制
| 限制项 | 限制说明 |
| --- | --- |
| 单条日志长度 | 默认限制为 512 KB。您可通过启动参数 max_read_buffer_size 进行调整，最大不能超过 8 MB。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 多行日志按行首正则表达式划分后，每条日志大小限制仍为 512 KB。如果日志超过 512 KB，会被强制拆分为多条进行采集。例如：单条日志大小为 1025 KB，则第一次处理 512 KB，第二次处理 512 KB，第三次处理 1 KB，最终采集结果为多条不完整的日志。 |
| 文件编码 | 支持 UTF-8 或 GBK 编码的日志文件，建议使用 UTF-8 编码获得更好的处理性能。 警告 如果日志文件为其它编码格式则会出现乱码、数据丢失等问题。 |
| 日志文件轮转 | 日志轮转队列大小默认为 20。您可通过启动参数 logreader_max_rotate_queue_size 进行调整。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 支持设置采集路径为 xxx.log 或 xxx.log* 形式。 重要 同一个 Logtail 实例中请勿混用两种形式，否则可能导致同一文件匹配多个 Logtail 采集配置，出现重复采集。 如果未处理完成的文件超过 20 个，将导致新生成的日志丢失。此类情况，请优先排查 LogStore Shard 写入 Quota 是否超限，并调整 Logtail 并发水平。具体操作，请 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 更多信息，请参见 [相关技术文章](https://yq.aliyun.com/articles/204554) 。 |
| 日志解析阻塞时采集行为 | 日志解析阻塞时，Logtail 会保持该日志文件描述符为打开状态，避免阻塞期间文件被删除，导致日志丢失。 如果解析阻塞期间出现多次日志文件轮转，Logtail 会将文件放入轮转队列。 |
| 正则表达式 | 支持 Perl 兼容正则表达式。 |
| JSON | 完全支持标准 JSON（ [RFC7159](https://tools.ietf.org/html/rfc7159) 、 [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/) ）。不支持非标准 JSON，例如 {"name": "\xE5\xAD\xA6"} 。 |
| 文件打开行为 | Logtail 会保持被采集的文件和轮转队列中待采集的文件处于打开状态，以保证采集数据完整性。出现以下情况，会关闭文件。 文件超过 5 分钟未被修改。 发生轮转且采集完毕。 Logtail 采集配置发生变更。 如果无论文件是否采集完成或仍有日志写入文件，您都希望文件在删除后的可控时间内释放文件句柄，则您可通过启动参数 force_release_deleted_file_fd_timeout 设置超时时间。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 |
| 首次日志采集行为 | Logtail 只采集增量的日志文件。首次发现文件被修改后，如果文件大小超过 1 MB（容器标准输出为 512 KB），则从最后 1 MB 处开始采集，否则从开始位置采集。 您可通过 Logtail 采集配置中的 tail_size_kb 参数调整新文件首次采集的大小。具体操作，请参见 [Logtail](developer-reference/logtail-configurations.md) [配置（旧版）](developer-reference/logtail-configurations.md) 。 如果下发 Logtail 采集配置后，日志文件一直无修改，则 Logtail 不会采集该文件。如果需要采集历史文件，请参见 [导入历史日志文件](import-historical-logs.md) 。 |
| 文件发生覆盖的行为 | Logtail 采用 inode+文件中前 1024 字节的 Hash 识别文件。文件被覆盖后，如果 inode 或文件前 1024 字节 Hash 发生变化，则文件会作为新文件从头开始采集，否则不会被采集。 |
| 文件发生移动的行为 | 文件发生移动后，如果匹配 Logtail 采集配置，且该 Logtail 采集配置之前从未匹配过该文件，则移动后的文档将被当成新文件从头开始采集，否则不会被采集。 |
| 文件采集历史 | Logtail 会在内存中保留文件采集历史进度，保证文件发生变化后仅采集增量部分，超过保留范围的日志如果发生写入，会导致重复采集。 默认最多保留 1 个月内的历史文件。 如果同一目录下历史文件超过 5,000 个时，仅保留最近 1 周的记录。 如果同一目录下历史文件超过 10,000 个时，仅保留 1 天内的记录。 |
| 非标准文本日志 | 对于日志中包含 \0 的行，版本>2.1.10 和>3.0.12 仅保留日志中间的 \0 ，前缀和后缀的 \0 部分丢弃。其他版本可能截断到第一个 \0 处或完全保留，建议升级。对于其他转义字符（如 ASCII 颜色）或不可见字符，Logtail 将按原样上报。 |
## 计费说明
安装 LoongCollector 或 Logtail本身不收费。
日志写入、存储、索引、查询、加工、投递等环节将根据 LogStore 计费模式产生费用。
如果在安装或配置中使用了全球加速功能，通过加速网络传输的数据会产生额外的流量费用。
## 常见问题（FAQ）
### 如何管理多目标分发配置？
由于多目标分发配置关联了多个日志库，这类配置需要通过 Project 级别的管理页面进行维护：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project名称。
在目标Project页面，单击左侧导航栏资源组>配置管理。
说明
此页面集中管理Project下的所有采集配置，包括那些因日志库被误删而残留的配置。
### 如何将ECS服务器的日志传输到另一个阿里云账号的Project？
如果您尚未安装LoongCollector，请参考[安装采集器](loongcollector-installation-linux.md)选择合适的跨账号场景进行安装；
如果您已安装了LoongCollector，请参考如下步骤配置用户标识，用于标识这台服务器有权限被日志服务Project所属账号访问、采集日志。
只有在采集非本账号ECS、自建IDC、其他云厂商服务器日志时需要配置用户标识。
复制日志服务所属的主账号ID：鼠标悬浮在右上角用户头像上，在弹出的标签页中查看并复制账号ID。
登录需要采集日志的服务器，创建阿里云账号ID文件配置用户标识：
touch /etc/ilogtail/users/{阿里云账号ID} # 如果/etc/ilogtail/users目录不存在，请手动创建目录。用户标识配置文件只需配置文件名，无需配置文件后缀。
### 如何将ECS服务器的日志传输到同账号不同地域的Project？
如果您尚未安装LoongCollector，请参考[安装采集器](loongcollector-installation-linux.md)选择合适的跨地域场景进行安装；
如果已安装LoongCollector，则需要修改LoongCollector配置。
执行sudo /etc/init.d/ilogtaild stop命令，停止LoongCollector。
修改LoongCollector启动配置文件ilogtail_config.json，根据您的网络需求从以下两种方式中选择一种进行修改：
配置文件路径：/usr/local/ilogtail/ilogtail_config.json
方式一：使用公网传输
参考[RegionID](loongcollector-installation-linux.md)，将配置文件中的地域替换为日志服务所在的地域，需要修改的字段包括：
primary_region
config_servers中的地域部分
data_servers中的region和endpoint_list地域部分
方式二：使用传输加速
将data_server_list参数中的endpoint一行替换为log-global.aliyuncs.com。文件路径，请参见[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
配置文件示例
$cat { "primary_region" : "cn-shanghai", "config_servers" : [ "http://logtail.cn-shanghai.log.aliyuncs.com" ], "data_servers" : [ { "region" : "cn-shanghai", "endpoint_list": [ "cn-shanghai.log.aliyuncs.com" ] } ], "cpu_usage_limit" : 0.4, "mem_usage_limit" : 384, "max_bytes_per_sec" : 20971520, "bytes_per_sec" : 1048576, "buffer_file_num" : 25, "buffer_file_size" : 20971520, "buffer_map_num" : 5 }
执行sudo /etc/init.d/ilogtaild start命令，启动LoongCollector。
### 如何将服务器加入到已有机器组？
当您已有配置好的机器组，希望将新的服务器（如新部署的 ECS 或自建服务器）加入其中并继承其采集配置时，可通过以下步骤完成绑定。
操作前提：
已存在一个配置完成的机器组。
新服务器已[安装 LoongCollector](host-text-log-collection-auto-install.md)。
操作步骤：
查看目标机器组标识：
在目标Project页面，单击左侧导航栏资源组>机器组。
进入机器组页面，单击目标机器组名称。
在机器组配置页面，查看机器组标识。
根据标识类型执行对应操作：
说明
同一机器组中不允许同时存在Linux服务器、Windows服务器，请勿在Linux和Windows服务器上配置相同的用户自定义标识。一个服务器可配置多个用户自定义标识，标识之间以换行符分隔。
类型一：机器组标识为IP地址
在服务器上，执行如下命令打开app_info.json文件，查看ip值。
cat /usr/local/ilogtail/app_info.json
在目标机器组配置页面，单击修改，填写服务器的IP地址，多个IP之间使用换行符分隔。
配置完成后，单击确定，并确认心跳状态。心跳为OK后，服务器将自动应用机器组的采集配置。
若心跳状态为FAIL，请参考常见问题[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进一步排查。
类型二：机器组标识为用户自定义标识
根据操作系统，向指定文件写入与目标机器组一致的用户自定义标识字符串：
若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。
Linux：向/etc/ilogtail/user_defined_id文件写入自定义字符串 。
Windows：向C:\LogtailData\user_defined_id写入自定义字符串。
### 如何导入其他Project的采集配置？
在完成[准备工作](host-text-log-collection-auto-install.md)、[机器组配置](host-text-log-collection-auto-install.md)的基础上，您可将已有 Project 中的采集配置快速导入到当前 LogStore，避免重复配置，提升效率。
操作步骤：
完成[机器组配置](host-text-log-collection-auto-install.md)后，单击下一步，进入Logtail配置页面。
单击页面右上角导入其他配置，
选择要导入的Project及该Project下的采集配置。
单击确定，系统将自动加载所选配置。
检查导入的配置信息无误后，即可单击下一步，进入[查询与分析配置](host-text-log-collection-auto-install.md)页面，完成后续配置。
### 如何获取服务器的IP地址，作为机器组标识？
在已安装LoongCollector（Logtail）的服务器上，打开/usr/local/ilogtail/app_info.json文件，查看ip值。
Logtail自动获取的服务器IP地址记录在app_info.json文件的ip字段中，如下所示。
重要
存在多台服务器时，请手动输入对应的IP地址，IP地址之间需使用换行符分隔。
同一机器组中不允许同时存在Linux和Windows服务器。请勿将Windows和Linux服务器IP添加到同一机器组中。
### 如何让同一个日志文件被多个采集配置同时采集？
默认情况下，日志服务为了避免数据重复，限制一个文本日志文件只能被一个Logtail配置采集。若需实现同一日志文件被多个采集配置同时采集，需要手动开启允许文件多次采集功能。
操作步骤：
重要
采集多份时，文件读取的IO、计算资源和网络IO都会线性增加。
登录[日志服务控制台](https://sls.console.aliyun.com/)，进入目标Project。
在左侧导航栏选择日志库，找到目标LogStore。
单击其名称前的展开LogStore。
单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。
在Logtail配置页面，单击编辑：
输入配置>其他输入配置，开启允许文件多次采集。
配置完成后，单击确定。
### 为什么最后一段日志延迟很久才上报？有时还会被截断？
原因分析：日志被截断通常发生在日志文件末尾缺少换行符，或多行日志（如异常堆栈）尚未完整写入时。由于采集器无法判断日志是否已结束，可能导致最后一段内容被提前切分或延迟上报。不同版本的LoongCollector（Logtail）处理机制有差异：
1.8 之前版本：
如果最后一行日志没有换行符（回车），或者一个多行日志段落未结束，采集器会一直等待下一次写入触发输出。这可能导致最后一条日志长时间滞留不发送，直到新日志写入。
1.8 及之后版本：
引入超时刷新机制，避免日志卡住。当检测到未完成的日志行时，系统启动计时器，超时后自动提交当前内容，确保日志最终能被采集。
默认超时时间：60 秒（保证大多数场景下的完整性）
您可根据实际需求调整该值，但不建议设为 0，否则可能导致日志截断或丢失部分内容。
解决方案：
您可以适当延长等待时间，确保完整日志写入后再被采集：
登录[日志服务控制台](https://sls.console.aliyun.com/)，进入目标Project。
在左侧导航栏选择日志库，找到目标LogStore。
单击其名称前的展开LogStore。
单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。
在Logtail配置页面，单击编辑：
输入配置>其他输入配置>高级参数：添加以下JSON配置自定义超时时间
{ "FlushTimeoutSecs": 1 }
默认值：由启动参数default_reader_flush_timeout决定（通常为几秒）。
单位：秒。
建议值：≥1 秒，不建议设为 0，否则可能导致日志截断或丢失部分内容。
配置完成后，单击确定。
### 为什么LoongCollector（Logtail）在运行过程中会从内网域名切换到公网？能否自动切回？
LoongCollector（Logtail）运行过程中，若检测到内网域名通信异常（如网络不通、连接超时等），为保障日志采集的连续性和可靠性，系统会自动切换至公网域名进行数据发送，避免日志堆积或丢失。
LoongCollector：内网恢复后，自动切回内网。
Logtail：不会自动切回，需手动重启才能恢复内网通信。
## 附录：原生解析插件详解
在Logtail配置页面的处理配置区域，可以通过添加处理插件，对原始日志进行结构化处理。如需为已有采集配置添加处理插件，可以参考如下步骤：
在左侧导航栏选择日志库，找到目标LogStore。
单击其名称前的展开LogStore。
单击Logtail配置，在配置列表中，找到目标Logtail配置，单击操作列的管理Logtail配置。
在Logtail配置页面，单击编辑。
此处仅介绍常用处理插件，覆盖常见日志处理场景，如需更多功能，请参考[拓展处理插件](developer-reference/api-sls-2020-12-30-createlogtailpipelineconfig.md)。
重要
插件组合使用规则（适用于 LoongCollector / Logtail 2.0 及以上版本）:
原生处理插件与拓展处理插件均可独立使用，也支持按需组合使用。
推荐优先选用原生处理插件，因其具备更优的性能和更高的稳定性。
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
正则表达式：用于匹配日志，支持自动生成或手动输入：
自动生成：
单击自动生成正则表达式。
在日志样例中划选需要提取的日志内容。
单击生成正则。
手动输入：根据日志格式手动输入正则表达式。
配置完成后，单击验证，测试正则表达式是否能够正确解析日志内容。
日志提取字段：为提取的日志内容（Value），设置对应的字段名（Key）。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### 分隔符解析
通过分隔符将日志内容结构化，解析为多个键值对形式，支持单字符分隔符和多字符分隔符。
效果示例：
| 未经任何处理的原始日志 | 按指定字符 , 切割字段 |
| --- | --- |
| 05/May/2025:13:30:28,10.10.*.*,"POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1",200,18204,aliyun-sdk-java | ip:10.10.*.* request:POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1 size:18204 status:200 time:05/May/2025:13:30:28 user_agent:aliyun-sdk-java |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>分隔符解析：
分隔符：指定用于切分日志内容的字符。
示例：对于CSV格式文件，选择自定义，输入半角逗号（,）。
引用符：当某个字段值中包含分隔符时，需要指定引用符包裹该字段，避免错误切割。
日志提取字段：按分隔顺序依次为每一列设置对应的字段名称（Key）。规则要求如下：
字段名只能包含：字母、数字、下划线（_）。
必须以字母或下划线（_）开头。
最大长度：128字节。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### 标准JSON解析
将Object类型的JSON日志结构化，解析为键值对形式。
效果示例：
| 未经任何处理的原始日志 | 标准 JSON 键值自动提取 |
| --- | --- |
| {"url": "POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10.200.98.220", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "18204"}, "time": "05/Jan/2025:13:30:28"} | ip: 10.200.98.220 request: {"status": "200", "latency" : "18204" } time: 05/Jan/2025:13:30:28 url: POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek******&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1 user-agent:aliyun-sdk-java |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>JSON解析：
原始字段：默认值为content（此字段用于存放待解析的原始日志内容）。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### 嵌套JSON解析
通过指定展开深度，将嵌套的JSON日志解析为键值对形式。
效果示例：
| 未经任何处理的原始日志 | 展开深度：0， 并使用展开深度作为前缀 | 展开深度：1， 并使用展开深度作为前缀 |
| --- | --- | --- |
| {"s_key":{"k1":{"k2":{"k3":{"k4":{"k51":"51","k52":"52"},"k41":"41"}}}}} | 0_s_key_k1_k2_k3_k41:41 0_s_key_k1_k2_k3_k4_k51:51 0_s_key_k1_k2_k3_k4_k52:52 | 1_s_key:{"k1":{"k2":{"k3":{"k4":{"k51":"51","k52":"52"},"k41":"41"}}}} |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择拓展处理插件>展开JSON字段：
原始字段：需要展开的原始字段名，例如content。
JSON展开深度：JSON对象的展开层级。0表示完全展开（默认值），1表示当前层级，以此类推。
JSON展开连接符：JSON展开时字段名的连接符，默认为下划线 _。
JSON展开字段前缀：指定JSON展开后字段名的前缀。
展开数组：开启此项可将数组展开为带索引的键值对。
示例：{"k":["a","b"]}展开为{"k[0]":"a","k[1]":"b"}。
如果需要对展开后的字段进行重命名（例如，将 prefix_s_key_k1 改为 new_field_name），可以后续再添加一个重命名字段插件来完成映射。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### JSON数组解析
使用json_extract[函数](json-functions.md)，从JSON数组中提取JSON对象。
效果示例：
| 未经任何处理的原始日志 | 提取 JSON 数组结构 |
| --- | --- |
| [{"key1":"value1"},{"key2":"value2"}] | json1:{"key1":"value1"} json2:{"key2":"value2"} |
配置步骤：在Logtail配置页面的处理配置区域，将处理模式切换为SPL，配置SPL语句，使用[json_extract](json-functions.md)函数从JSON数组中提取JSON对象。
示例：从日志字段content中提取 JSON 数组中的元素，并将结果分别存储在新字段json1和json2中。
* | extend json1 = json_extract(content, '$[0]'), json2 = json_extract(content, '$[1]')
### Apache日志解析
根据Apache日志配置文件中的定义将日志内容结构化，解析为多个键值对形式。
效果示例：
| 未经任何处理的原始日志 | Apache 通用日志格式 combined 解析 |
| --- | --- |
| 1 192.168.1.10 - - [08/May/2024:15:30:28 +0800] "GET /index.html HTTP/1.1" 200 1234 "https://www.example.com/referrer" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36" | http_referer:https://www.example.com/referrer http_user_agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.X.X Safari/537.36 remote_addr:192.168.1.10 remote_ident:- remote_user:- request_method:GET request_protocol:HTTP/1.1 request_uri:/index.html response_size_bytes:1234 status:200 time_local:[08/May/2024:15:30:28 +0800] |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>APACHE模式解析：
日志格式：combined。
APACHE配置字段：系统会根据日志格式自动填充配置。
重要
请务必核对自动填充的内容，确保与服务器上 Apache 配置文件（通常位于/etc/apache2/apache2.conf）中定义的 LogFormat 完全一致。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### IIS日志解析
根据IIS日志格式定义将日志内容结构化，解析为多个键值对形式。
对比示例：
| 原始日志 | 微软 IIS 服务器专用格式适配 |
| --- | --- |
| #Fields: date time s-sitename s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) sc-status sc-substatus sc-win32-status sc-bytes cs-bytes time-taken | c-ip: cs-username cs-bytes: sc-substatus cs-method: cs-method cs-uri-query: cs-uri-query cs-uri-stem: cs-uri-stem cs-username: s-port date: #Fields: s-computername: s-sitename s-ip: s-ip s-sitename: time sc-bytes: sc-status sc-status: c-ip sc-win32-status: cs (User-Agent) time: date time-taken: sc-win32-status |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>IIS模式解析：
日志格式：选择您的IIS服务器日志采用的日志格式。
IIS：Microsoft IIS日志文件格式。
NCSA：NCSA公用日志文件格式。
W3C：W3C扩展日志文件格式。
IIS配置字段：选择IIS或NCSA时，日志服务已默认设置了IIS配置字段，选择W3C时，设置为您的IIS配置文件中logExtFileFlags参数中的内容。例如：
logExtFileFlags="Date, Time, ClientIP, UserName, SiteName, ComputerName, ServerIP, Method, UriStem, UriQuery, HttpStatus, Win32Status, BytesSent, BytesRecv, TimeTaken, ServerPort, UserAgent, Cookie, Referer, ProtocolVersion, Host, HttpSubStatus"
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
### 数据脱敏
对日志中的敏感数据进行脱敏处理。
效果示例：
| 未经任何处理的原始日志 | 脱敏结果 |
| --- | --- |
| [{'account':'1812213231432969','password':'04a23f38'}, {'account':'1812213685634','password':'123a'}] | [{'account':'1812213231432969','password':'********'}, {'account':'1812213685634','password':'********'}] |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>脱敏处理：
原始字段：解析日志前，用于存放日志内容的原始字段。
脱敏方式：
const：将敏感内容替换成所修改的字符串。
md5：将敏感内容替换为其对应的MD5值。
替换字符串：选择脱敏方式为const时，需要输入字符串，用于替换敏感内容。
被替换内容前的内容表达式：用于查找敏感内容，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。
被替换的内容表达式：敏感内容的表达式，使用[RE2](https://github.com/google/re2/blob/master/doc/syntax.txt)[语法](https://github.com/google/re2/blob/master/doc/syntax.txt)配置。
### 时间解析
对日志中的时间字段进行解析，并将解析结果设置为日志的__time__字段。
效果示例：
| 未经任何处理的原始日志 | 时间解析 |
| --- | --- |
| {"level":"INFO","timestamp":"2025-09-23T19:11:47+0800","cluster":"yilu-cluster-0728","message":"User logged in successfully","userId":"user-123"} |  |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>时间解析：
原始字段：解析日志前，用于存放日志内容的原始字段。
时间格式：根据日志中的时间内容设置对应的[时间格式](time-parsing.md)。
时区：选择日志时间字段所在的时区。默认使用机器时区，即LoongCollector（Logtail）进程所在环境的时区。
## 附录：权限策略参考
阿里云主账号登录：默认拥有全部权限，可直接操作。
RAM账号登录：需要主账号[授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md)相应权限策略。
## 自定义权限策略（精细化控制）
当系统策略无法满足最小权限原则时，可通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化授权。以下为权限策略示例，包含的权限有：
查看Project：查看Project列表，查看指定Project详情。
管理日志库 (LogStore)：在Project下创建新的日志库，或修改、删除已有的日志库。
管理采集配置：创建、删除和修改采集配置。
查看日志：查询和分析指定Project下指定日志库中的数据。
替换${regionName}${uid}、${projectName}、${logstoreName}为实际的地域名称，主账号id，目标Project和LogStore。
示例策略
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:ListProject", "log:GetAcceleration", "log:ListDomains", "log:GetLogging", "log:ListTagResources" ], "Resource": "acs:log:${regionName}:${uid}:project/*" }, { "Effect": "Allow", "Action": "log:GetProject", "Resource": "acs:log:${regionName}:${uid}:project/${projectName}" }, { "Effect": "Allow", "Action": [ "log:ListLogStores", "log:*LogStore", "log:*Index", "log:ListShards", "log:GetCursorOrData", "log:GetLogStoreHistogram", "log:GetLogStoreContextLogs", "log:PostLogStoreLogs" ], "Resource": "acs:log:${regionName}:${uid}:project/${projectName}/*" }, { "Effect": "Allow", "Action": "log:*", "Resource": [ "acs:log:${regionName}:${uid}:project/${projectName}/logtailconfig/*", "acs:log:${regionName}:${uid}:project/${projectName}/machinegroup/*" ] }, { "Effect": "Allow", "Action": "log:ListSavedSearch", "Resource": "acs:log:${regionName}:${uid}:project/${projectName}/savedsearch/*" }, { "Effect": "Allow", "Action": "log:ListDashboard", "Resource": "acs:log:${regionName}:${uid}:project/${projectName}/dashboard/*" }, { "Effect": "Allow", "Action": "log:GetLogStoreLogs", "Resource": "acs:log:${regionName}:${uid}:project/${projectName}/logstore/${logstoreName}" }, { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations", "ecs:InvokeCommand" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" } ] }
| 权限 | 对应操作 | 资源 |
| --- | --- | --- |
| 只读 Project | GetAcceleration GetLogging ListProject ListDomains ListTagResources | acs:log:${regionName}:${uid}:project/* |
| 获取指定 Project | GetProject | acs:log:${regionName}:${uid}:project/${projectName} |
| 管理 LogStore | ListLogStores *LogStore *Index ListShards GetCursorOrData GetLogStoreHistogram GetLogStoreContextLogs PostLogStoreLogs | acs:log:${regionName}:${uid}:project/${projectName}/* |
| 管理 LoongCollector（Logtail）数据接入 | * | acs:log:${regionName}:${uid}:project/${projectName}/logtailconfig/* acs:log:${regionName}:${uid}:project/${projectName}/machinegroup/* |
| 查询快速查询 | ListSavedSearch | acs:log:${regionName}:${uid}:project/${projectName}/savedsearch/* |
| 查询仪表盘 | ListDashboard | acs:log:${regionName}:${uid}:project/${projectName}/dashboard/* |
| 查询指定日志库日志 | GetLogStoreLogs | acs:log:${regionName}:${uid}:project/${projectName}/logstore/${logstoreName} |
| 操作 ECS 的权限 | DescribeTagKeys DescribeTags DescribeInstances DescribeInvocationResults RunCommand DescribeInvocations InvokeCommand | * |
| 操作 OOS 的权限（ 可选） 仅在日志服务与 ECS 实例同账号同地域通过 OOS 自动化安装 LoongCollector(Logtail)时需要。 | ListTemplates StartExecution ListExecutions GetExecutionTemplate ListExecutionLogs ListTaskExecutions | * |
## 系统权限策略
若使用系统预定义策略，建议添加以下权限：
AliyunLogFullAccess：管理日志服务的权限。
AliyunECSFullAccess：管理ECS的权限。
（可选）AliyunOOSFullAccess：当通过 OOS 一键安装LoongCollector（Logtail）时需要。
## 更多信息
### 全局配置参数介绍
| 配置项 | 说明 |
| --- | --- |
| 配置名称 | LoongCollector（Logtail）配置名称，在其所属 Project 内必须唯一。创建成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。包含机器组 Topic，文件路径提取，自定义三种方式。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [LoongCollector（Logtail）流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
### 输入配置参数介绍
##
##
##
| 配置项 | 说明 |
| --- | --- |
| 文件路径 | 根据日志在主机（例如 ECS）上的位置，设置日志目录和文件名称： 目录名和文件名均支持完整模式和通配符模式，文件名规则请参见 [Wildcard matching](https://man7.org/linux/man-pages/man7/glob.7.html) 。其中，日志路径通配符只支持星号（*）和半角问号（?）。 日志文件查找模式为多层目录匹配，即符合条件的指定目录（包含所有层级的目录）下所有符合条件的文件都会被查找到。例如： /apsara/nuwa/**/*.log 表示 /apsara/nuwa 目录（包含该目录的递归子目录）中后缀名为.log 的文件。 /var/logs/app_*/**/*.log 表示 /var/logs 目录下所有符合 app_* 格式的目录（包含该目录的递归子目录）中后缀名为 .log 的文件。 /var/log/nginx/**/access* 表示 /var/log/nginx 目录（包含该目录的递归子目录）中以 access 开头的文件。 |
| 最大目录监控深度 | 设置日志目录被监控的最大深度，即 文件路径 中通配符 ** 匹配的最大目录深度。0 代表只监控本层目录。 |
| 文件编码 | 选择日志文件的编码格式。 |
| 首次采集大小 | 配置首次生效时，匹配文件的起始采集位置距离文件结尾的大小。首次采集大小设定值为 1024 KB。 首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。 首次采集时，如果文件大于 1024 KB，则从距离文件末尾 1024 KB 的位置开始采集。 您可以通过此处修改 首次采集大小 ，取值范围为 0~10485760KB。 |
| 采集黑名单 | 打开 采集黑名单 开关后，可进行黑名单配置，即可在采集时忽略指定的目录或文件。支持完整匹配和通配符匹配目录和文件名。其中，通配符只支持星号（*）和半角问号（?）。 重要 如果您在配置 文件路径 时使用了通配符，但又需要过滤掉其中部分路径，则需在 采集黑名单 中填写对应的完整路径来保证黑名单配置生效。 例如您配置 文件路径 为 /home/admin/app*/log/*.log ，但要过滤 /home/admin/app1* 目录下的所有子目录，则需选择 目录黑名单 ，配置目录为 /home/admin/app1*/** 。如果配置为 /home/admin/app1* ，黑名单不会生效。 匹配黑名单过程存在计算开销，建议黑名单条目数控制在 10 条内。 目录路径不能以正斜线（/）结尾，例如将设置路径为 /home/admin/dir1/ ，目录黑名单不会生效。 支持按照文件路径黑名单、文件黑名单、目录黑名单设置，详细说明如下： 文件路径黑名单 选择 文件路径黑名单 ，配置路径为 /home/admin/private*.log ，则表示在采集时忽略 /home/admin/ 目录下所有以 private 开头，以.log 结尾的文件。 选择 文件路径黑名单 ，配置路径为 /home/admin/private*/*_inner.log ，则表示在采集时忽略 /home/admin/ 目录下以 private 开头的目录内，以_inner.log 结尾的文件。例如 /home/admin/private/app_inner.log 文件被忽略， /home/admin/private/app.log 文件被采集。 文件黑名单 选择 文件黑名单 ，配置文件名为 app_inner.log ，则表示采集时忽略所有名为 app_inner.log 的文件。 目录黑名单 选择 目录黑名单 ，配置目录为 /home/admin/dir1 ，则表示在采集时忽略 /home/admin/dir1 目录下的所有文件。 选择 目录黑名单 ，配置目录为 /home/admin/dir* ，则表示在采集时忽略 /home/admin/ 目录下所有以 dir 开头的子目录下的文件。 选择 目录黑名单 ，配置目录为 /home/admin/*/dir ，则表示在采集时忽略 /home/admin/ 目录下二级目录名为 dir 的子目录下的所有文件。例如 /home/admin/a/dir 目录下的文件被忽略， /home/admin/a/b/dir 目录下的文件被采集。 |
| 允许文件多次采集 | 默认情况下，一个日志文件只能匹配一个 LoongCollector（Logtail）配置。如果文件中的日志需要被采集多份，需要打开 允许文件多次采集 开关。 |
| 高级参数 | 其它可选的与文件输入插件相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [LoongCollector（Logtail）流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |
### 处理配置参数介绍
| 配置项 | 说明 |
| --- | --- |
| 日志样例 | 待采集日志的样例，请务必使用实际场景的日志。日志样例可协助您配置日志处理相关参数，降低配置难度。支持添加多条样例，总长度不超过 1500 个字符。 [2023-10-01T10:30:01,000] [INFO] java.lang.Exception: exception happened at TestPrintStackTrace.f(TestPrintStackTrace.java:3) at TestPrintStackTrace.g(TestPrintStackTrace.java:7) at TestPrintStackTrace.main(TestPrintStackTrace.java:16) |
| 多行模式 | 多行日志的类型：多行日志是指每条日志分布在连续的多行中，需要从日志内容中区分出每一条日志。 自定义 ：通过 行首正则表达式 区分每一条日志。 多行 JSON ：每个 JSON 对象被展开为多行，例如： { "name": "John Doe", "age": 30, "address": { "city": "New York", "country": "USA" } } 切分失败处理方式： Exception in thread "main" java.lang.NullPointerException at com.example.MyClass.methodA(MyClass.java:12) at com.example.MyClass.methodB(MyClass.java:34) at com.example.MyClass.main(MyClass.java:½0) 对于以上日志内容，如果日志服务切分失败： 丢弃 ：直接丢弃这段日志。 保留单行 ：将每行日志文本单独保留为一条日志，共保留为四条日志。 |
| 处理模式 | 处理插件组合 ，包括 原生处理插件 和 拓展处理插件 。有关处理插件的更多信息，请参见 [处理插件概述](overview-22.md) 。 重要 处理插件的使用限制，请以控制台页面的提示为准。 2.0 版本的 Logtail： 原生处理插件可任意组合。 原生处理插件和拓展处理插件可同时使用，但拓展处理插件只能出现在所有的原生处理插件之后。 低于 2.0 版本的 Logtail： 不支持同时添加原生处理插件和拓展处理插件。 原生插件仅可用于采集文本日志。使用原生处理插件时，须符合如下要求： 第一个处理插件必须为正则解析插件、分隔符模式解析插件、JSON 解析插件、Nginx 模式解析插件、Apache 模式解析插件或 IIS 模式解析插件。 从第二个处理插件到最后一个处理插件，最多包括 1 个时间解析处理插件，1 个过滤处理插件和多个脱敏处理插件。 对于 解析失败时保留原始字段 和 解析成功时保留原始字段 参数，只有以下组合有效，其余组合无效。 只上传解析成功的日志： 解析成功时上传解析后的日志，解析失败时上传原始日志： 解析成功时不仅上传解析后的日志，并且追加原始日志字段，解析失败时上传原始日志。 例如，原始日志 "content": "{"request_method":"GET", "request_time":"200"}" 解析成功，追加原始字段是在解析后日志的基础上再增加一个字段，字段名为 重命名的原始字段 （如果不填则默认为原始字段名），字段值为原始日志 {"request_method":"GET", "request_time":"200"} 。 |
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
