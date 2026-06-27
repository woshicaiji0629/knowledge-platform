# 管理日志项目Project-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/manage-a-project/

# 管理Project
项目（Project）是日志服务中的资源管理单元，是进行资源隔离与访问控制的主要边界。同时它也是您访问日志服务资源的入口。
## 什么是Project
项目（Project）是日志服务的资源管理单元，用于资源隔离和控制。
Project中可包含LogStore、MetricStore和机器组等资源，同时它也是您访问日志服务资源的入口。建议使用不同的Project管理不同的应用、产品或项目中的数据。具体说明如下：
组织、管理不同的LogStore或MetricStore：在实际使用中，您可能需要使用日志服务采集及存储不同项目、产品或者环境的日志。您可以把不同项目、产品或者环境中的日志分类管理在不同Project中，便于后续的日志消费、导出或者分析。
用于访问控制隔离：您可以为RAM用户授予指定Project的操作权限。
提供日志服务资源的访问入口：日志服务为每个Project配置一个独立的访问入口。该访问入口支持通过网络写入、读取及管理日志。关于访问入口的更多信息，请参见[服务接入点](developer-reference/api-sls-2020-12-30-endpoint.md)。
权限须知（可展开）
若您使用阿里云主账号登录，默认拥有所有操作权限，可直接对Project进行相关操作。
若您使用RAM用户登录，请根据需要向主账号使用者申请如下两种日志服务的系统策略。
AliyunLogFullAccess：管理日志服务的权限。
AliyunLogReadOnlyAccess：只读访问日志服务的权限。
当系统策略无法满足您的需求，您可以参考下表通过[创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)实现精细化权限管理。
| 操作 | 所需权限 |
| --- | --- |
| 创建 Project | log:ListProject log:CreateProject |
| 删除 Project | log:ListProject log:GetProject log:DeleteProject |
| 回收站 Project 操作 | log:ListProjectsInRecycleBin log:CreateProject log:DeleteProject log:UpdateProject |
| 查看指定 Project | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources |
| 管理资源配额 | 同查看指定 Project。 |
| 设置传输加速 | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources log:PutProjectTransferAcceleration |
| 设置资源组 | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources log:ChangeResourceGroup |
| 设置标签 | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources log:TagResources log:UntagResources |
| 设置自定义域名 | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources log:CreateDomain |
| Project 资源监控 | log:ListProject log:GetProject log:ListLogStores log:ListSavedSearch log:ListDashboard log:ListDomains log:GetSqlInstance log:ListTagResources log:GetLogging log:CreateLogStore log:CreateIndex log:UpdateIndex log:CreateDashboard log:UpdateDashboard log:GetLogStore log:UpdateLogStore log:UpdateLogging log:GetLogStoreLogs |
Project全量参数列表（可展开）
| 参数 | 描述 |
| --- | --- |
| 所属地域 | 请根据日志来源等信息选择合适的阿里云地域。创建 Project 后，您无法修改其所属地域，且日志服务不支持跨地域迁移 Project。如果您要采集 ECS 日志，建议选择与 ECS 相同的地域，实现通过阿里云内网采集日志，加快日志采集速度。 |
| Project 名称 | Project 名称在阿里云地域内全局唯一，创建后不可修改。 |
| Project 回收站 | 重要数据对应的 Project 建议开启回收站功能，避免误删。开启后 Project 被删除将进入回收站，回收站中的 Project 进入静默状态，不支持读写，如静默后发现存在业务关联可快速恢复。回收站仅收取数据存储费用。 |
| Project 注释 | Project 注释，不支持尖括号（<>）、撇号（'）、反斜线（\）、双引号（"）和两个反斜线（\\），最多包含 64 个字符。 |
| 资源组 | 资源组是在单个云账号下将一组相关资源进行统一管理的容器 一个资源只能归属于一个资源组 根据不同的业务场景，可将资源组映射为项目、应用或组织等概念 |
| 开通日志 | 开通服务日志会在您选择的存储位置创建对应的 LogStore 和仪表盘，存放操作日志的 LogStore 按照正常 LogStore 计费，存放其他日志的 LogStore 不产生费用。 详细日志：完整操作日志，按量收费。 重要日志：计量、消费组延迟和 Logtail 心跳日志等，免费。 任务运行日志：数据导入、定时 SQL、投递任务的运行日志，免费。 |
| 日志存储位置 | 自动创建名称为 log-service-{用户 ID}-{region}的 Project，建议将同一 Region 的日志都保存到该 Project 中。 |
## 创建Project
您可以通过创建项目来管理某一个应用的所有日志及相关的日志源。
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击创建Project。
配置Project：
所属地域：请根据日志来源等信息选择合适的阿里云地域。创建Project后，您无法修改其所属地域，且日志服务不支持跨地域迁移Project。如果您要采集ECS日志，建议选择与ECS相同的地域，实现通过阿里云内网采集日志，加快日志采集速度。
Project名称：Project名称在阿里云内全局唯一，创建后不可修改。
其余配置无需修改，使用默认值即可。
## API
[创建](developer-reference/api-sls-2020-12-30-createproject.md)[Project](developer-reference/api-sls-2020-12-30-createproject.md)。
创建 Project 时提示ProjectAlreadyExist，但控制台列表不可见
原因：Project 名称在阿里云地域内全局唯一。若当前账号下看不到该 Project，极可能是被其他阿里云账号占用。
处理建议：由于阿里云资源隔离机制，无法查看或删除其他账号名下的 Project。建议更换一个未被占用的 Project 名称，重新尝试创建。
## 定位Project来源
日志服务与其他云产品关联时，可能会自动创建Project。当Project数量较多时，您可能会希望进行Project溯源，了解各个Project来源，保存的数据内容，费用等信息。
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域查看目标Project。
可通过云产品标记或注释列查看Project创建来源说明：
若Project名称前有图标，可将鼠标移至图标处，会显示该Project关联的云产品名称。
若注释列中包含内容，描述了Project的来源。
若不符合上述两种情况，说明该Project是由用户自行手动创建。
系统自动创建的默认 Project 类型
部分 Project 是由系统或其他云产品自动创建的，用于支撑特定云服务功能。此类 Project 通常有固定的命名规则和用途，常见类型包括：
云监控元数据 Project：名称格式为aliyun-metadata-{用户ID}-{地域ID}，由云监控（Cloud Monitor Service，CMS）2.0 自动创建，用于存储云监控元数据等信息。此类 Project 免费且不产生费用。如需删除，目前仅支持通过云命令行（CloudShell）执行删除命令，控制台操作可能受限。
其他云产品自动创建的 Project：
应用实时监控服务（ARMS）：自动创建 Project 用于存储链路追踪数据。
操作审计（ActionTrail）：自动创建 Project 用于存储操作日志。
日志审计服务（Log Audit Service）：自动创建区域级或中心化的 Project 用于集中管理日志。
当明确Project关联的云产品后，若想了解更多信息，如存储的数据内容等，请参考[云产品日志采集](collection-of-alibaba-cloud-service-logs.md)。
判断 Project 是否正在使用：建议检查关联云产品（如云防火墙、WAF 等）是否仍在运行。若 Project 基础信息中无数据，且 Logtail 配置中无数据，可能暂无业务关联。但删除前务必确认对应云产品不再需要日志服务。若云产品仍在使用中，关联云产品从而自动创建的Project不建议删除。
若希望分析Project的资源用量与计费，可以参考[使用](use-cloudlens-for-sls-to-analyze-resource-usage.md)[CloudLens for SLS](use-cloudlens-for-sls-to-analyze-resource-usage.md)[分析资源用量](use-cloudlens-for-sls-to-analyze-resource-usage.md)进行查看与预估。
## 开启Project删除防护
重要数据对应的Project建议开启回收站功能，避免误删。开启后Project被删除将进入回收站，回收站中的Project进入静默状态，不支持读写，如静默后发现存在业务关联可快速恢复。回收站仅收取数据存储费用。
说明
Project进入回收站后，默认保存7天，到期后自动执行删除操作。
## 控制台
开启回收站功能
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的项目概览-基础信息-Project回收站中查看状态，若为未开启，单击开启。
## API
修改[更新](developer-reference/api-sls-2020-12-30-updateproject.md)[Project](developer-reference/api-sls-2020-12-30-updateproject.md)接口中的recycleBinEnabled。
## Project资源删除与恢复
删除Project可能导致日志库的数据丢失，请确认LogStore，MetricStore、EventStore等数据无用或已做好数据备份。
说明
删除Project的当天仍会产生存储等费用，次日[停止计费](stop-billing.md)。即您在删除Project的第三天不会再收到日志服务的账单。
## 控制台
删除前清理
无关联资源：
在弹性计算、存储服务、安全、数据库等多种阿里云云产品开通日志分析服务，会在日志服务控制台自动创建对应的Project和LogStore。如果不需要云产品日志，需要在对应云产品控制台关闭日志分析服务。确保Project与其他阿里云服务无关联。
无计费依赖：Project若为付费类型（如存储包、预留实例），需先退订或释放资源。
删除步骤
备份重要数据（可选）
LogStore数据备份：若Project中包含需保留的日志数据，需通过SLS的[下载日志](download-logs.md)功能提前导出。
配置信息备份：记录Project名称、存储容量、访问控制等关键配置，避免删除后信息丢失。
执行Project删除
在Project列表中，单击目标Project对应的删除。
出现ProjectDeletionNotAllowe的处理方法
故障现象：删除 Project 时，系统提示ProjectDeletionNotAllowed错误。
原因：Project 已开启删除保护功能。删除保护是防止 Project 被意外删除的安全机制，开启后无法通过控制台或 API 直接删除 Project。
解决方法：需先关闭删除保护，然后再执行删除操作。
登录[日志服务控制台](https://sls.console.aliyun.com)，在 Project 列表区域单击目标 Project。在 Project 页面的项目概览-基础信息中，找到删除保护开关，将其关闭。
在删除Project面板中，输入Project名称并选择删除原因，然后单击确定。
警告
删除Project后，其管理的所有日志数据及配置信息都会被释放，不可恢复。在删除Project前请慎重确认，避免数据丢失。
确认操作：阅读提示后，输入Project名称进行二次确认。
若目标Project已开启Project回收站功能，您可在Project列表的回收站Project中查看，Project进入回收站后，默认保存7天，在此期间您可以选择恢复或者彻底删除。
删除后状态确认
删除操作是异步执行的，提交删除请求后，Project 会在后台逐步清理。若删除后再次尝试删除同一 Project 时提示"Project 不存在"，通常表示该 Project 已成功删除。
建议访问[日志服务控制台](https://sls.console.aliyun.com/lognext/profile)，在 Project 列表中查看目标 Project 是否已消失。若列表为空，则代表该地域的 Project 资源已全部清理。
若已开启回收站功能，还需在回收站Project列表中确认目标 Project 是否已被彻底删除或恢复。
## API
[删除指定](developer-reference/api-sls-2020-12-30-deleteproject.md)[Project](developer-reference/api-sls-2020-12-30-deleteproject.md)。
## 管理资源配额
当您的资源配额不足时，您可以根据实际需求调整Project的多个指标，包括LogStore上限，shard上限，logtail采集配置上限，机器组上限等。
一个阿里云账号下最多可创建150个Project。如您有更大的使用需求，请[提工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)申请。
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的项目概览-基础信息-资源配额中单击管理，即可在资源配额面板中，调整目标资源的配额，然后单击保存提交申请。修改申请需要等待1小时左右完成。
支持的配置项
| Quota 指标 | 指标说明 | 默认值 | 可调整上限 |
| --- | --- | --- | --- |
| LogStore 上限 | 一个 Project 中最多可创建的 LogStore 数量。 | 200 | 400 |
| shard 上限 | 一个 Project 中最多可创建 Shard 数量。 | 400 | 800 |
| logtail 采集配置上限 | 一个 Project 中最多可创建 Logtail 配置数量。 | 200 | 400 |
| 机器组上限 | 一个 Project 中最多可创建机器组数量。 | 200 | 400 |
| 仪表盘上限 | 一个 Project 中最多可创建仪表盘数量。 | 100 | 400 |
| 仪表盘中图表上限 | 一个仪表盘最多可包含统计图表数量。 | 200 | 400 |
| 快速查询上限 | 一个 Project 中最多可创建快速查询数量。 | 100 | 400 |
| 导出任务上限 | 一个 Project 中最多可创建导出任务数量。 | 100 | 400 |
| 导入任务上限 | 一个 Project 中最多可创建导入任务数量。 | 100 | 400 |
| 定时 SQL 上限 | 一个 Project 中最多可创建定时 SQL 数量。 | 100 | 400 |
| 加工任务上限 | 一个 Project 中最多可创建加工任务数量。 | 100 | 400 |
| 告警上限 | 一个 Project 中最多可创建告警数量。 | 100 | 400 |
| 订阅任务上限 | 一个 Project 中最多可创建订阅任务数量。 | 100 | 400 |
| project 写入流量上限（GB/min） | 一个 Project 在 1 分钟内所有 LogStore 写入流量的总和。 | 100 | 200 |
| project 写入次数上限（万次/min） | 一个 Project 在 1 分钟内所有 LogStore 写入次数的总和。 | 60 | 200 |
| project 读取次数上限（万次/min） | 一个 Project 在 1 分钟内所有 LogStore 读取次数的总和。 | 60 | 200 |
## 日志跨域传输加速
如果需要远距离日志传输，例如从海外向中国内地的地域写入日志，可以开启传输加速功能。传输加速利用全球分布的云机房，将全球各地用户对日志服务的访问，经过智能路由解析至就近的接入点，使用优化后的网络及协议极大地提升访问速度，传输加速按照实际传输的数据量进行计费。
## 控制台
开启传输加速
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的项目概览-访问域名-传输加速域名中单击开启，阅读对话框的提示，然后单击确认修改。
开启传输加速后在后续使用Logtail进行日志采集，以及执行数据加工任务时能够提高传输速度。
## API
首先使用[配置传输加速](developer-reference/api-sls-2020-12-30-putprojecttransferacceleration.md)。
在后续使用时将endpoint配置为传输加速域名才能获得加速效果。传输加速域名仅支持HTTP/HTTPS协议的API接入，暂不支持Kafka、GRPC等协议接入。在不需要传输加速的场景中，建议使用[服务接入点](developer-reference/api-sls-2020-12-30-endpoint.md)以减少传输费用。
/** * 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 */String accessId = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_ID"); String accessKey = System.getenv("ALIBABA_CLOUD_ACCESS_KEY_SECRET"); /** * 日志服务的服务接入点，使用传输加速域名。 */String endpoint = "log-global.aliyuncs.com"; /** * 创建日志服务Client。 */static Client client = new Client(host, accessId, accessKey);
## 资源分组管理
当您需要对Project进行分组管理时，可以使用标签或资源组来区分Project，标签与资源组的不同之处在于分组层级。其中标签是Project层级下分组管理的方式，资源组则是在阿里云账号下进行资源分组管理的一种机制。
### 设置资源组
一个Project只能归属于一个资源组。
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
鼠标悬浮在Project页面的项目概览-资源组信息-资源组ID上，单击修改，选择资源组。
## API
[修改资源组](developer-reference/api-sls-2020-12-30-changeresourcegroup.md)。
### 设置标签
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的项目概览-标签-中单击编辑，在编辑标签面板中设置标签。
## API
[绑定标签](developer-reference/api-sls-2020-12-30-tagresources.md)。
## 查看域名与设置自定义域名
当您需要查看域名信息或将公网域名换为自定义域名时，可以按如下方式操作。完成后即可在接口调用中使用相应域名作为endpoint。
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的项目概览-访问域名中可查看当前Project的域名信息。
鼠标悬浮在项目概览-基础信息-自定义域名上，单击设置，在设置自定义域名面板，配置[域名注册快速入门](https://help.aliyun.com/zh/dws/getting-started/quickly-register-a-new-domain-name)，然后单击绑定。
在[云解析](https://dns.console.aliyun.com/)[DNS](https://dns.console.aliyun.com/)[产品控制台](https://dns.console.aliyun.com/)，做CNAME解析，域名绑定才能生效。记录值填写Project页面的项目概览-基础信息-访问域名中的公网域名，详细操作，请参见[CNAME 记录](https://help.aliyun.com/zh/dns/add-a-dns-record#a11de0e439vrv)。
## API
[创建自定义域名](developer-reference/api-sls-2020-12-30-createdomain.md)。
自定义域名绑定 SSL 证书
现状说明：日志服务控制台目前不支持直接上传或绑定 SSL 证书到自定义域名。
解决方案：
方案一（推荐方案）：通过 CDN/SLB 间接实现。使用阿里云 CDN 加速 SLS 域名，在 CDN 控制台绑定 SSL 证书，通过 CDN 访问；或使用 SLB 负载均衡配置 HTTPS 监听并绑定证书，后端指向 SLS 公网地址。
方案二（默认方案）：使用 SLS 默认域名。SLS 内置的默认域名已默认支持 HTTPS 及内置 SSL 证书，无需额外配置。如无特殊需求，可直接使用默认域名。
## Project资源监控与运维
如果您需要获取Project内的资源操作日志（创建、修改、更新、删除）和任务执行日志（定时SQL、数据导入、数据投递），LogStore内消费组消费延时日志以及Logtail的错误、心跳和统计日志，可以使用服务日志功能。
## 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表区域，单击目标Project。
在Project页面的服务日志页面，单击开通详细日志，在修改服务日志配置面板，选择需要开通的服务日志与服务日志存储的Project。
详细日志：完整操作日志，按量收费。
重要日志：计量、消费组延迟和Logtail心跳日志等，免费。
任务运行日志：数据导入、定时SQL、投递任务的运行日志，免费。
日志存储位置：选择已存在的Project或者自动创建Project进行存储。
## 操作限制与兼容性说明
批量删除限制：日志服务目前不支持批量删除 Project 或 LogStore 的工具，需要手动逐个删除。
移动端操作：可以通过手机端浏览器访问[日志服务控制台](https://sls.console.aliyun.com/lognext/profile)进行登录和管理 Project（包括创建、修改、删除等操作）。
创建 Project 后列表不显示：若创建 Project 后在列表中看不到新创建的 Project，请检查地域选择是否正确，并尝试刷新页面。
## 更多信息
Project中存储不同类型的数据需要创建不同的Store，具体请参考[管理](manage-sls-store.md)[Store](manage-sls-store.md)。
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
