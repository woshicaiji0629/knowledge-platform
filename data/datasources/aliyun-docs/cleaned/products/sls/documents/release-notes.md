# 日志服务的新功能发布记录-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/release-notes

# 新功能发布记录
本文介绍日志服务每次发布涉及的功能变更及对应的文档，帮助您了解日志服务的发布动态。
## 2026年03月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| OpenClaw 日志一键接入 | 通过日志服务接入中心，一键完成 OpenClaw AI Agent 的日志接入，配合内置审计大盘与观测大盘，实现开箱即用的安全审计与运维观测闭环。 | [全部地域](sls-supported-regions1.md) | [SLS](enable-managed-openclaw-with-sls.md) [一键接入实现](enable-managed-openclaw-with-sls.md) [OpenClaw](enable-managed-openclaw-with-sls.md) [受控运行](enable-managed-openclaw-with-sls.md) |
## 2026年02月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 智能问答助手 | 智能问答助手是基于数字员工构建的智能运维助手，它依托用户自定义的知识库进行问答。您可以为智能体配置特定权限、知识库、行为规则等，灵活定制符合特定业务场景的专属运维智能体。 | [全部地域](sls-supported-regions1.md) | [智能问答助手](question-and-answer-assistant.md) |
| 仪表盘查询加速 | 当 SQL 查询涉及超大规模数据或超长查询时间跨度时，仪表盘加速功能通过集成 [通过物化视图提升超大规模数据执行性能](improve-the-performance-of-hyperscale-data-execution-through-materialized-views.md) 能力，在后台自动进行预计算处理，将复杂的实时查询转化为高效的结果读取，实现仪表盘的高速渲染。 | 华北 6（乌兰察布） 华南 3（广州） | [仪表盘查询加速](dashboard-query-acceleration.md) |
## 2026年01月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 物化视图 | 对目标 SQL 自动提取出子视图（聚合、过滤、投影等）进行持久化，并在后续执行 SQL 分析时自动进行查询改写，从而显著加速超大规模数据的分析性能 | [全部地域](sls-supported-regions1.md) | [通过物化视图提升超大规模数据执行性能](improve-the-performance-of-hyperscale-data-execution-through-materialized-views.md) |
| 兼容 PostgreSQL 协议 | 支持使用 PG 协议读写 LogStore 数据 | 华东 1（杭州） | [使用](use-the-postgresql-protocol-to-access-sls.md) [PostgreSQL](use-the-postgresql-protocol-to-access-sls.md) [协议接入](use-the-postgresql-protocol-to-access-sls.md) [SLS](use-the-postgresql-protocol-to-access-sls.md) |
## 2025年08月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 软删除 | 阿里云日志服务新增软删除（Soft Deletion） 功能，允许用户在删除日志数据时，将数据标记为“已删除”状态而非立即物理清除。 | 新加坡和华北 6（乌兰察布） | [日志服务软删除](soft-delete.md) |
| 消费处理器 | 基于消费处理器消费是一种通过设置 SPL 实时处理日志服务数据的方式，适用于第三方软件、多语言应用、云产品、流式计算框架等多种应用场景。SPL 是 SLS 推出的一种高性能数据处理语言，专门用于处理日志的弱结构化特点。其原理是在服务端使用 SPL 对日志数据进行预处理和清洗，例如执行行过滤、列裁剪、正则提取等操作。经过处理后，客户端接收到的数据已是规整格式。 | [全部地域](sls-supported-regions1.md) | [消费处理器](data-consumption-processor.md) |
| 大语言模型（LLM）应用调用可观测 MCP 服务实现日志查询与分析 | 阿里云可观测的 MCP（Model Context Protocol）是一种统一的数据访问和分析协议，旨在通过自然语言交互和工具集成，帮助用户高效查询和分析阿里云可观测产品（如日志服务 SLS、ARMS 等）中的数据。 | 华北 1（青岛）、华北 2（北京）、华北 3（张家口）、华北 5（呼和浩特）、华北 6（乌兰察布）、华东 1（杭州）、华东 2（上海）、华南 1（深圳）、华南 2（河源）、华南 3（广州）、西南 1（成都） | [大语言模型（LLM）应用调用可观测](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md) [MCP](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md) [服务实现日志查询与分析](large-language-model-llm-application-calls-observable-mcp-service-to-implement-log-query-and-analysis.md) |
| 语义富化 | SLS 推出的语义富化能力，借助于 LLM 处理自然语言的能力，从非结构化日志中提取关键和有效的信息。 | 华北 1（青岛）、华北 2（北京）、华北 3（张家口）、华北 5（呼和浩特）、华北 6（乌兰察布）、华东 1（杭州）、华东 2（上海）、华南 1（深圳）、华南 2（河源）、华南 3（广州）、西南 1（成都） | [语义富化](semantic-enrichment.md) |
## 2025年06月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 扫描索引 | 扫描索引功能是在日志服务已支持的全文索引和字段索引基础上，提供的一种加速扫描计算性能的工具。通过为关键字段（如时间戳）构建轻量级索引，开启该功能后可提升数据扫描效率。 | [全部地域](sls-supported-regions1.md) | [基于扫描索引加速扫描（Scan）](accelerated-scan-based-on-scan-index.md) |
## 2025年05月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 机器学习语法 | 日志服务机器学习功能为您提供多种功能丰富的算法和便捷的调用方式，您可以在日志查询分析中通过分析语句和机器学习函数调用机器学习算法，分析某一字段或若干字段在一段时间内的特征。针对时序数据分析场景，日志服务提供了丰富的时序分析算法，可以帮助您快速解决时序预测、时序异常检测、序列分解、多时序聚类等场景问题，兼容 SQL 标准接口。大大降低了您使用算法的门槛，提高分析问题和解决问题的效率。 | [全部地域](sls-supported-regions1.md) | [机器学习语法](machine-learning-syntax.md) |
## 2025年03月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 高性能完全精确查询与分析（SQL 独享版） | SQL 独享版是 日志服务 提供的计费资源，用于 SQL 分析。当您对大规模（百亿到千亿级）数据有分析需求时，可使用 SQL 独享版。 | [开服地域](sls-supported-regions1.md) | [高性能完全精确查询与分析（SQL](dedicated-sql.md) [独享版）](dedicated-sql.md) |
| Project 回收站 | 日志服务支持 Project 回收站功能，开启回收站功能的 Project，在用户执行删除操作后，对应 Project 数据临时放入回收站空间，回收站里的 Project 不可读写，但可以重新恢复。恢复范围包括 Project 下的所有数据及相关配置（ LogStore 实例及对应的 LogStore 配置、仪表盘、数据加工作业、告警等），同时需要保持与应用之间的数据关联。 | [全部地域](sls-supported-regions1.md) | [管理](manage-project-recycle-bin.md) [Project](manage-project-recycle-bin.md) [回收站](manage-project-recycle-bin.md) |
| 采集配置生成器 | 若您计划通过 CRD-AliyunPipelineConfig 或 API 接口来配置 Logtail 采集任务，利用采集配置生成器来自动构建所需的 CRD 定义和 API 参数脚本。该工具可帮您快速完成配置，减少手动操作。 | [全部地域](sls-supported-regions1.md) | [采集配置生成器](collection-configuration-generator.md) |
## 2025年01月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| LoongCollector | LoongCollector 是一款集卓越性能、超强稳定性和灵活可编程性于一身的数据采集器，专为构建下一代可观测 Pipeline 设计。在继承了 Logtail 强大的日志采集与处理能力的基础上，进行了全面的功能升级与扩展。功能将从原来的单一日志场景，逐步扩展为可观测数据采集、本地计算、服务发现的统一体。 | 华南 2（河源）、华南 3（广州）、新加坡、韩国（首尔）、马来西亚（吉隆坡）、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷）、日本（东京）、德国（法兰克福）、英国（伦敦）、美国（硅谷）、美国（弗吉尼亚）、阿联酋（迪拜） | [LoongCollector](introduction-to-loongcollector.md) [简介](introduction-to-loongcollector.md) [LoongCollector](loongcollector-collects-host-text-logs.md) [采集主机文本日志（手动安装）](loongcollector-collects-host-text-logs.md) [LoongCollector](loongcollector-collects-host-text-logs-automatically-installed.md) [采集主机文本日志（自动安装）](loongcollector-collects-host-text-logs-automatically-installed.md) [采集自建](collect-text-logs-of-self-built-k8s-clusters-deploy-loongcollector-in-daemonset-mode.md) [K8s](collect-text-logs-of-self-built-k8s-clusters-deploy-loongcollector-in-daemonset-mode.md) [集群文本日志（DaemonSet](collect-text-logs-of-self-built-k8s-clusters-deploy-loongcollector-in-daemonset-mode.md) [方式部署](collect-text-logs-of-self-built-k8s-clusters-deploy-loongcollector-in-daemonset-mode.md) [LoongCollector）](collect-text-logs-of-self-built-k8s-clusters-deploy-loongcollector-in-daemonset-mode.md) [采集](collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md) [ACK](collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md) [集群文本日志（DaemonSet](collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md) [方式部署](collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md) [LoongCollector）](collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md) |
## 2024年11月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 日志服务支持使用 SPL 采集日志 | Logtail 支持三种处理模式：原生插件模式、扩展插件模式和 SPL 模式。通过编写 SPL 语句，您可以充分利用其计算能力来处理数据。 | [全部地域](sls-supported-regions1.md) | [使用](use-logtail-spl-to-parse-logs.md) [Logtail SPL](use-logtail-spl-to-parse-logs.md) [解析日志](use-logtail-spl-to-parse-logs.md) |
| 向量索引 | 日志服务 是一个一站式日志数据分析平台，解决日志数据的采集、处理、存储、检索分析的需求。大语言模型的兴起，对自然语言的搜索需求陡增。例如对用户问答数据，Agent 和 LLM 的交互日志，有审计、检索、分析的需求。 为了解决大语言模型领域的语义搜索需求，SLS 推出了向量索引功能。 | 华北 1（青岛）、华北 2（北京）、华北 3（张家口）、华北 5（呼和浩特）、华北 6（乌兰察布）、华东 1（杭州）、华东 2（上海）、华南 1（深圳）、华南 2（河源）、华南 3（广州）、西南 1（成都） | [向量索引](vector-index.md) |
## 2024年09月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 仪表盘免密分享至企业微信 | 被分享的企业微信账号可以在企业微信手机端或 PC 端免密查看日志服务的仪表盘。 | [全部地域](sls-supported-regions1.md) | [功能概览](secret-free-sharing-and-integrated-dashboard.md) |
| 网络质量分析器支持标签绑定 | 首先在控制台添加和选择标签，然后使用 [SDK](how-to-use-the-sdk-plug-in.md) [插件](how-to-use-the-sdk-plug-in.md) 为用户/设备添加相同的标签，只有当两个标签相同时，才会对用户/设备的数据进行探测和展示。 | [全部地域](sls-supported-regions1.md) | [使用网络质量分析器](use-network-quality-analyzer.md) |
| 通过 ECS 无需 AccessKey 访问日志服务 SDK | 当 ECS 实例或部署在 ECS 实例上的应用需要访问其他云资源时，必须配置访问凭证，阿里云服务会通过访问凭证验证您的身份信息和访问权限。实例 RAM 角色允许您将一个角色关联到 ECS 实例，实现在实例内部自动获取并刷新临时访问凭证，无需直接暴露 AccessKey，减少密钥泄露的风险。同时，也可借助 RAM 角色精细化控制资源访问权限，避免权限过度分配。 | [全部地域](sls-supported-regions1.md) | [通过](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) [ECS](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) [无需](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) [AccessKey](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) [使用日志服务](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) [SDK](developer-reference/use-log-service-sdk-by-using-ecs-without-using-accesskey.md) |
## 2024年08月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 写入处理器 | 如果您需要在日志数据写入 LogStore 前对数据进行处理，例如数据过滤、字段提取、字段扩展、数据脱敏，可以使用写入处理器（IngestProcessor）。 写入处理器的计费使用可观测资源额度 OCU。 | [全部地域](sls-supported-regions1.md) | [写入处理器概述](user-guide/overview-of-sls-data-processing.md) [按使用功能计费模式计费项](billable-items.md) [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) |
| 日志服务 Copilot | 使用日志服务 Copilot 生成、解释、优化 SQL 语句，提高查询效率。 | [全部地域](sls-supported-regions1.md) | [通过](copilot-automatic-generation-of-ai-assisted-sql-statements.md) [AI](copilot-automatic-generation-of-ai-assisted-sql-statements.md) [智能生成查询与分析语句（Copilot）](copilot-automatic-generation-of-ai-assisted-sql-statements.md) |
| 新版 资源包-预付计划 2.0（推荐） | CU（Cost Unit）支持抵扣数据加工（新版）、规则消费、传输加速的费用。 | [全部地域](sls-supported-regions1.md) | [按使用功能计费模式计费项](billable-items.md) [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) [资源包介绍](overview-11.md) |
## 2024年07月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 使用 CR 实例管理 Logtail 采集配置 | CRD（ [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) ）允许用户定义自定义资源类型，日志服务利用 CRD 定义了自己的资源类型，您可以通过创建 CR（CustomResource）实例来管理采集配置。 | [全部地域](sls-supported-regions1.md) | [【推荐】使用](recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md) [AliyunPipelineConfig](recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md) [管理采集配置](recommend-use-aliyunpipelineconfig-to-manage-collection-configurations.md) [使用](use-aliyunlogconfig-to-manage-collection-configurations.md) [AliyunLogConfig](use-aliyunlogconfig-to-manage-collection-configurations.md) [管理采集配置](use-aliyunlogconfig-to-manage-collection-configurations.md) [通过](collect-container-text-logs-through-the-daemonset-console.md) [DaemonSet](collect-container-text-logs-through-the-daemonset-console.md) [方式采集](collect-container-text-logs-through-the-daemonset-console.md) [Kubernetes](collect-container-text-logs-through-the-daemonset-console.md) [容器文本日志](collect-container-text-logs-through-the-daemonset-console.md) [通过](collect-container-text-logs-through-sidecar-console.md) [Sidecar](collect-container-text-logs-through-sidecar-console.md) [方式采集](collect-container-text-logs-through-sidecar-console.md) [Kubernetes](collect-container-text-logs-through-sidecar-console.md) [容器文本日志](collect-container-text-logs-through-sidecar-console.md) |
| 新版日志审计服务 | 与旧版日志服务审计相比，新版日志审计服务支持通过多日志项目中心管理日志数据，从而用户可以将云产品日志中心化汇总、查询、统计、分析，同时满足数据合规的相关地域限制要求，实现依法、有序的数据自由流动管理。 | [全部地域](sls-supported-regions1.md) | [新版日志审计服务概述](user-guide/overview-of-the-new-log-audit-service.md) |
| 传输加速 | 传输加速利用全球分布的云机房，将全球各地用户对日志服务的访问，经过智能路由解析至就近的接入点，使用优化后的网络及协议极大地提升访问速度。 传输加速功能正式开始商业化收费。 | [全部地域](sls-supported-regions1.md) | [管理传输加速](transmission-acceleration.md) [全球加速采集/规则消费/新版数据加工功能商业化通知](https://www.aliyun.com/noticelist/articleid/1073523191.html) |
| 仪表盘免密分享至钉钉 | 被分享的钉钉账号可以在钉钉手机端或 PC 端免密查看日志服务的仪表盘。 | [全部地域](sls-supported-regions1.md) | [将仪表盘免密分享给钉钉账号](share-dashboard-to-dingtalk-account-without-secret.md) |
| 可观测资源额度 OCU | 可观测资源额度 OCU（Observability Capacity Unit）是阿里云云原生可观测推出的新版计费单位，可根据每小时资源使用情况自动统计 OCU 用量。 可以抵扣传输加速/规则消费/数据加工（新版）功能的费用。 | [全部地域](sls-supported-regions1.md) | [按使用功能计费模式计费项](billable-items.md) [按写入数据量计费模式计费项](billing-items-in-the-pay-per-data-write-mode.md) [全球加速采集/规则消费/新版数据加工功能商业化通知](https://www.aliyun.com/noticelist/articleid/1073523191.html) |
| 跨 LogStore 查询日志（StoreView） | 在实际业务场景中，日志由不同的应用程序、服务、云产品生成，存储在不同地域的 Project 或同一地域的不同 LogStore 中。日志服务提供 StoreView 功能，支持跨地域、跨 Store 联合查询能力。 | [全部地域](sls-supported-regions1.md) | [数据视图（StoreView）概述](dataset-storeview-overview.md) |
## 2024年06月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 数据加工（新版） | 日志服务提供可托管、可扩展、高可用的数据加工（新版）服务。数据加工（新版）服务可应用于数据规整与信息提取、数据清洗与过滤、数据分发至多目标 LogStore 等数据处理场景。 | [全部地域](sls-supported-regions1.md) | [数据加工（新版）](data-processing-new-edition-overview.md) |
## 2024年03月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 字段分析 | SLS（Simple Log Service）具备字段分析功能，专注于对 text、long 和 double 类型字段的统计分析。此功能涵盖了字段的基本分布情况、各种统计指标以及 TOP5 的时间序列图，为用户提供了深入的数据洞察和可视化工具，便于理解和挖掘。 | [全部地域](sls-supported-regions1.md) | [字段分析](field-analysis.md) |
| 采集容器文本日志的控制台界面更新 | 如果需要只使用一个 Logtail 实例收集 Kubernetes 节点上所有容器的日志，可以使用 DaemonSet 方式在 Kubernetes 集群上部署 Logtail。 如果需要每个 Pod 使用单独的 Logtail 实例来收集 Pod 内所有容器的日志，可以使用 Sidecar 方式在 Kubernetes 集群上部署 Logtail。 | [全部地域](sls-supported-regions1.md) | [通过](collect-container-text-logs-through-the-daemonset-console.md) [DaemonSet](collect-container-text-logs-through-the-daemonset-console.md) [方式采集](collect-container-text-logs-through-the-daemonset-console.md) [Kubernetes](collect-container-text-logs-through-the-daemonset-console.md) [容器文本日志](collect-container-text-logs-through-the-daemonset-console.md) [通过](collect-container-text-logs-through-sidecar-console.md) [Sidecar](collect-container-text-logs-through-sidecar-console.md) [方式采集](collect-container-text-logs-through-sidecar-console.md) [Kubernetes](collect-container-text-logs-through-sidecar-console.md) [容器文本日志](collect-container-text-logs-through-sidecar-console.md) |
| 使用 Terraform 配置 Logtail 采集配置 | Terraform 是一种开源工具，用于安全高效地预览、配置和管理云基础架构和资源。用户可以使用 Terraform 调用接口创建 Logtail 采集配置。 | [全部地域](sls-supported-regions1.md) | [通过](developer-reference/configure-logtail-collection-through-terraform.md) [Terraform](developer-reference/configure-logtail-collection-through-terraform.md) [配置](developer-reference/configure-logtail-collection-through-terraform.md) [Logtail](developer-reference/configure-logtail-collection-through-terraform.md) [采集](developer-reference/configure-logtail-collection-through-terraform.md) |
## 2024年02月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 导入 Amazon S3 文件 | 阿里云日志服务 SLS 支持导入 Amazon S3 中的日志文件。您可以通过数据导入的方式将 Amazon S3 的日志文件导入到阿里云的日志服务，实现日志的查询和分析、加工等操作。 | [全部地域](sls-supported-regions1.md) | [导入](importing-amazon-s3-data.md) [Amazon S3](importing-amazon-s3-data.md) [文件](importing-amazon-s3-data.md) |
| 日志采集客户端 HarmonyOS SDK | 提供日志采集客户端 HarmonyOS SDK，支持采集各类 HarmonyOS 设备的日志。HarmonyOS SDK 通过 ArkTS 封装实现，使用 C 语言编写。 | [全部地域](sls-supported-regions1.md) | [HarmonyOS SDK](developer-reference/harmonyos-sdk-overview.md) [概述](developer-reference/harmonyos-sdk-overview.md) |
## 2024年01月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 控制台内嵌及分享（新版） | 使用 Ticket 方案将日志服务控制台免登分享给他人或免登嵌入到第三方系统。 | [全部地域](sls-supported-regions1.md) | [控制台内嵌及分享](developer-reference/console-embedding-and-sharing-new-version-2.md) |
| 通过消费组读取文本日志进行模板匹配 | 日志模板匹配通过在线匹配日志和模板，监控日志模板的统计信息，例如数量变化。本文介绍通过读取日志文本进行模板匹配的操作步骤。 | [全部地域](sls-supported-regions1.md) | [通过消费组读取文本日志进行模板匹配](read-text-logs-from-consumer-groups-for-template-matching.md) |
| CloudLens for SLS | CloudLens for SLS 控制台界面更新。 | [CloudLens for SLS](usage-notes-45.md) [支持的地域](usage-notes-45.md) | [使用前须知](usage-notes-45.md) [开启日志采集功能](enable-the-log-collection-feature-1.md) |
| 数据导入流程优化 | 日志文件导入流程优化，控制台界面更新。 | [全部地域](sls-supported-regions1.md) | [数据采集概述](data-collection-overview.md) |
## 2023年12月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 企业云监控日志 | 采集企业云监控的日志。 | [全部地域](sls-supported-regions1.md) | [采集企业云监控日志](enable-log-dump-function.md) |
| Alibaba CloudLens Copilot for OSS | 基于日志服务的 CloudLens for OSS 功能为您提供智能可观测数据分析服务，利用千问的大语言模型的能力，为您提供云产品可观测数据分析智能助手。 | [CloudLens for OSS](usage-notes-44.md) [的地域](usage-notes-44.md) | [Alibaba CloudLens Copilot for OSS](alibaba-cloudlens-copilot-for-oss.md) [使用指南](alibaba-cloudlens-copilot-for-oss.md) [使用前须知](usage-notes-44.md) |
## 2023年11月
| 功能名称 | 功能描述 | 支持地域 | 相关文档 |
| --- | --- | --- | --- |
| 仪表盘免密分享 | 日志服务 新增仪表盘免密分享功能，将日志服务仪表盘或统计图表免密分享给他人或嵌入到第三方系统进行查看。 | [全部地域](sls-supported-regions1.md) | [仪表盘免密分享](dashboard-secret-free-sharing.md) |
| Logtail 采集配置界面更新 | Logtail 采集配置的控制台界面已更新。 | 除了华北 2（北京）和华东 1（杭州）的 [全部地域](sls-supported-regions1.md) | [采集主机文本日志](collect-host-logs.md) [通过](collect-container-text-logs-through-the-daemonset-console.md) [DaemonSet](collect-container-text-logs-through-the-daemonset-console.md) [方式采集](collect-container-text-logs-through-the-daemonset-console.md) [Kubernetes](collect-container-text-logs-through-the-daemonset-console.md) [容器文本日志](collect-container-text-logs-through-the-daemonset-console.md) |
| 高精度时间戳（精确到纳秒）和全局排序 | 日志服务支持通过高精度时间戳（精确到纳秒）进行数据的全局排序，给您提供更加精准、可靠的时间顺序视图。 | [全部地域](sls-supported-regions1.md) | [高精度时间戳（精确到纳秒）和全局排序](high-precision-timestamp-and-global-sorting.md) |
## 2023年09月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 归档存储 | 日志服务 新增归档存储功能，在现有热存储、低频存储的基础上，为您提供更低成本且可查询、分析的长期数据存储方案。 | 2023-09-18 | [全部地域](sls-supported-regions1.md) | [智能存储分层](user-guide/intelligent-storage-tiering.md) |
| 按写入数据量计费模式节省计划 | 日志服务 按写入数据量计费模式支持节省计划，通过购买日志服务-按写入数据量计费模式节省计划可降低成本。 | 2023-09-11 | [全部地域](sls-supported-regions1.md) | [节省计划](savings-plan.md) |
## 2023年08月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 同城冗余存储 | 日志服务 支持同城冗余存储，保证数据的持久性和可用性。 | 2023-08-31 | 华东 1（杭州）、华东 2（上海）、华北 2（北京）、华北 3（张家口）、华北 6（乌兰察布）、华南 1（深圳）、中国香港、新加坡 | [存储冗余](storage-redundancy.md) |
| 低频存储 | 日志服务 冷存储更名为低频存储，智能冷热分层功能更名为智能存储分层。 | 2023-08-25 | [全部地域](sls-supported-regions1.md) | [开启智能存储分层](enable-hot-and-cold-tiered-storage-for-a-logstore.md) |
| 采集脚本执行日志 | 日志服务 支持通过 Logtail input_command 插件采集脚本执行日志。 | 2023-08-16 | [全部地域](sls-supported-regions1.md) | [采集脚本执行日志](collecting-script-execution-data.md) |
| Log 转为 Metric | 日志服务 支持通过 processor_log_to_sls_metric 插件将采集到的日志转成 SLS Metric。 | 2023-08-16 | [全部地域](sls-supported-regions1.md) | [扩展插件：Log](log-to-metric.md) [转为](log-to-metric.md) [Metric](log-to-metric.md) |
| 基于规则消费 | 日志服务 支持在实时消费场景下消费满足特定规则的日志。 | 2023-08-16 | [部分地域](rule-based-consumption.md) | [基于规则消费日志](rule-based-consumption.md) |
| SLS Playground | SLS Playground 提供了 日志服务 主要功能的演示环境，便于您快速了解及体验日志服务。 | 2023-08-11 | [全部地域](sls-supported-regions1.md) | [产品试用](product-trial.md) |
## 2023年05月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 事件库 | 日志服务 新增事件库。事件库是日志服务中事件数据的采集、存储和查询单元。 | 2023-05-26 | [全部地域](sls-supported-regions1.md) | [管理](manage-an-eventstore.md) [EventStore](manage-an-eventstore.md) |
| 设置资源配额 | 日志服务 提供默认的资源配额，当您的 日志服务 资源不足时，您可以根据实际需求调整资源的配额，以确保资源充足。 | 2023-05-23 | [全部地域](sls-supported-regions1.md) | [调整资源配额](adjust-resource-quotas.md) |
| Elasticsearch 兼容 | 日志服务 提供 Elasticsearch 兼容接口，最大程度保障 Elasticsearch 查询分析方案迁移的平滑度，降低将日志引擎从 Elasticsearch 切换为 日志服务 的使用难度。 | 2023-05-22 | [全部地域](sls-supported-regions1.md) | [日志服务与](compatibility-between-log-service-and-elasticsearch.md) [Elasticsearch](compatibility-between-log-service-and-elasticsearch.md) [的兼容性](compatibility-between-log-service-and-elasticsearch.md) |
| 查看及恢复仪表盘历史版本 | 如果您在编辑仪表盘过程中，误操作了仪表盘，则可以使用仪表盘历史版本功能，查看对应的历史版本并将其恢复到历史版本。 | 2023-05-08 | [全部地域](sls-supported-regions1.md) | [查看及恢复仪表盘历史版本](view-dashboard-versions-and-restore-a-previous-version.md) |
## 2023年04月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 下探分析 | 日志服务 提供下探分析功能，用于对多维时序进行自动化、智能化的根因定位。 | 2023-04-12 | [全部地域](sls-supported-regions1.md) | [下探分析](user-guide/how-it-works-46.md) |
| 全栈可观测 | 全栈可观测应用是 日志服务 提供的一站式 IT 系统可观测方案，包含 IT 系统监控、全链路 Trace、智能告警等功能。 | 2023-04-10 | [全部地域](sls-supported-regions1.md) | [全栈可观测](usage-notes-39.md) |
## 2023年03月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 轮播仪表盘 | 如果您要实现多个仪表盘轮播展示，可使用演示列表功能。 | 2023-03-21 | [全部地域](sls-supported-regions1.md) | [轮播仪表盘](user-guide/play-dashboards.md) |
| IPv6 函数 | 日志服务 新增 IPv6 函数，用于 SQL 分析。 | 2023-03-09 | [全部地域](sls-supported-regions1.md) | [IP](ip-functions.md) [函数](ip-functions.md) |
| 累积分布函数 | 日志服务 新增累积分布函数，用于 SQL 分析。 | 2023-03-09 | [全部地域](sls-supported-regions1.md) | [数学统计函数](mathematical-statistics-functions.md) |
## 2023年02月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| SREWorks | SREWorks 数智服务提供一站式的智能运维场景服务，包括机器画像、日志诊断和智能 QA 生成器，帮助企业将 日志服务 中的海量运维数据转化成有价值的数据资产。目前主要开放机器画像场景服务。 | 2023-02-13 | [全部地域](sls-supported-regions1.md) | [SREWorks](usage-notes-sreworks.md) |
| 字段值映射处理插件 | 日志服务 提供 processor_dict_map 插件，用于对字段值进行映射。 | 2023-02-07 | [全部地域](sls-supported-regions1.md) | [扩展插件：字段值映射处理](map-field-values.md) |
| 字段加密插件 | 日志服务 提供 processor_encrypt 插件，用于对指定字段进行加密。 | 2023-02-07 | [全部地域](sls-supported-regions1.md) | [扩展插件：字段加密](encrypt-fields.md) |
| 数据编码与解码插件 | 日志服务 提供 processor_base64_encoding、processor_base64_decoding 或 processor_md5 插件，用于对字段值进行编解码 | 2023-02-07 | [全部地域](sls-supported-regions1.md) | [扩展插件：数据编码与解码](encode-and-decode-data.md) |
## 2023年01月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 通过 Unity Plugin 接入数据 | 您可以通过 Unity Plugin 将 Unity 平台的移动终端（Android、iOS）游戏 App 的崩溃数据、应用数据接入到移动运维监控应用中。 | 2023-01-13 | [全部地域](sls-supported-regions1.md) | [通过](collect-metric-data-by-using-unity-plugin.md) [Unity Plugin](collect-metric-data-by-using-unity-plugin.md) [接入数据](collect-metric-data-by-using-unity-plugin.md) |
| 导入仪表盘 | 当您需要跨 Project 复制仪表盘时，可通过导入功能实现。 | 2023-01-10 | [全部地域](sls-supported-regions1.md) | [导入和导出日志服务仪表盘](import-and-export-sls-dashboards.md) |
| 导入 Grafana 仪表盘 | 您可以将 Grafana 仪表盘导入到 日志服务 中。 | 2023-01-10 | [全部地域](sls-supported-regions1.md) | [导入](user-guide/import-a-grafana-dashboard-to-log-service.md) [Grafana](user-guide/import-a-grafana-dashboard-to-log-service.md) [仪表盘到日志服务](user-guide/import-a-grafana-dashboard-to-log-service.md) |
| 导出 日志服务 仪表盘到 Grafana | 您可以将 日志服务 仪表盘导入到 Grafana 中。 | 2023-01-10 | [全部地域](sls-supported-regions1.md) | [导出日志服务仪表盘到](user-guide/export-a-log-service-dashboard-to-grafana.md) [Grafana](user-guide/export-a-log-service-dashboard-to-grafana.md) |
## 2022年12月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 脱敏插件 | 日志服务 新增 processor_desensitize 插件，支持将日志中的敏感数据替换为指定字符串或 MD5 值。 | 2022-12-30 | [全部地域](sls-supported-regions1.md) | [脱敏插件](desensitization-plug-in.md) |
| 新版成本管家 | 新版成本管家将数据存储在表格存储（OTS）中，能够更好地保证数据准确性和实时性，并且支持每日自动全量更新。 | 2022-12-30 | [全部地域](sls-supported-regions1.md) | [使用新版成本管家](use-the-new-version-of-cost-manager.md) |
| 扫描分析 | 日志服务 扫描分析功能支持免配置索引进行目标字段的扫描，用于分析相关日志。 | 2022-12-30 | [全部地域](sls-supported-regions1.md) | [扫描（Scan）分析语法](scan-based-analysis-syntax.md) |
## 2022年11月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 采集 IDaaS 日志 | 日志审计服务支持采集 IDaaS 管理操作日志、用户行为日志。 | 2022-11-29 | [全部地域](sls-supported-regions1.md) | [IDaaS](idaas.md) |
| e_redis_map 加工函数 | 日志服务 新增 e_redis_map 加工函数，实现以 云数据库 Tair（兼容 Redis） 作为维表数据对原始日志进行富化。 | 2022-11-22 | [全部地域](sls-supported-regions1.md) | [e_redis_map](mapping-and-enrichment-functions.md) |
| e_tablestore_map 加工函数 | 日志服务 新增 e_tablestore_map 加工函数，实现以阿里云表格存储（Tablestore）作为维表数据对原始日志进行富化。 | 2022-11-22 | [全部地域](sls-supported-regions1.md) | [e_tablestore_map](mapping-and-enrichment-functions.md) |
| url_parse_qs 加工函数 | 日志服务 新增 url_parse_qs 加工函数，用于解析 URL 中查询字符串包含的参数。 | 2022-11-22 | [全部地域](sls-supported-regions1.md) | [url_parse_qs](parsing-functions.md) |
| url_parse 加工函数 | 日志服务 新增 url_parse 加工函数，用于解析 URL 的组成部分。 | 2022-11-22 | [全部地域](sls-supported-regions1.md) | [url_parse](parsing-functions.md) |
| 接入 k8s JVM 监控数据 | Kubernetes JVM 监控基于灵活的 Logtail Kubernetes 能力，通过自动发现等手段，为 Kubernetes 中所有基于 JVM 运行的服务提供灵活且一站式的 JVM 指标采集方案。 | 2022-11-21 | [全部地域](sls-supported-regions1.md) | [接入](collect-monitoring-data-from-kubernetes-jvms.md) [Kubernetes JVM](collect-monitoring-data-from-kubernetes-jvms.md) [监控数据](collect-monitoring-data-from-kubernetes-jvms.md) |
| 接入 Kubernetes 数据面监控数据 | Kubernetes 数据面监控基于 日志服务 与龙蜥社区合作共建的无侵入监控能力，您可以直观地分析整个 Kubernetes 的数据流向与瓶颈问题，轻松应对复杂的云原生环境。 | 2022-11-16 | [全部地域](sls-supported-regions1.md) | [接入无侵入服务观测](collect-monitoring-data-about-kubernetes-data-planes.md) |
## 2022年10月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 采集 PostgreSQL 查询结果 | Linux Logtail 1.2.1 及以上版本支持采集 PostgreSQL 查询结果。 | 2022-10-25 | [全部地域](sls-supported-regions1.md) | [采集](collect-postgresql-query-results.md) [PostgreSQL](collect-postgresql-query-results.md) [查询结果](collect-postgresql-query-results.md) |
| 采集 SQL Server 查询结果 | Linux Logtail 1.2.1 及以上版本支持采集 SQL Server 查询结果。 | 2022-10-25 | [全部地域](sls-supported-regions1.md) | [采集](collect-sql-server-query-results.md) [SQL Server](collect-sql-server-query-results.md) [查询结果](collect-sql-server-query-results.md) |
| processor_grok 插件 | 日志服务 新增 processor_grok 插件，用于提取日志中的字段。 | 2022-10-24 | [全部地域](sls-supported-regions1.md) | [表单配置方式](extract-content-from-log-fields.md) |
| 扫描（Scan）日志 | 日志服务 扫描功能支持免配置索引进行目标字段的扫描，用于查询相关日志。 | 2022-10-14 | [全部地域](sls-supported-regions1.md) | [扫描（Scan）查询语法](scan-query-syntax.md) |
## 2022年09月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| CloudLens for OSS | 日志服务 联合阿里云 OSS 推出 CloudLens for OSS，支持 Bucket 粒度的统一管理视图，支持资源用量、访问分析、异常检测、安全分析等可视化分析能力，提供场景化运维管理，实现 Bucket 资产的可观测性。 | 2022-09-30 | [全部地域](sls-supported-regions1.md) | [CloudLens for OSS](usage-notes-44.md) |
| 网络质量分析器 | 网络质量分析器是一款针对真实终端用户网络质量性能进行分析的 SaaS 服务。您可以将网络质量分析器的 SDK 插件集成到 App 中，实时感知所有 App 真实用户在线情况、访问互联网的网络质量情况。 | 2022-09-27 | [全部地域](sls-supported-regions1.md) | [网络质量分析器](user-guide/usage-notes-19.md) |
| 直方图 | 日志服务 提供直方图，用于展示一组数据的频数分布。 | 2022-09-21 | [全部地域](sls-supported-regions1.md) | [直方图](histogram.md) |
| 散点图 | 日志服务 提供散点图，用于展示变量之间相互影响的程度。 | 2022-09-21 | [全部地域](sls-supported-regions1.md) | [散点图](scatter-chart.md) |
| 交叉表 | 日志服务 提供交叉表，用于对查询和分析结果进行分组。 | 2022-09-21 | [全部地域](sls-supported-regions1.md) | [交叉表](cross-table.md) |
| processor_filter_key_regex | 日志服务 新增 Logtail processor_filter_key_regex 插件，用于过滤日志。 | 2022-09-14 | [全部地域](sls-supported-regions1.md) | [扩展插件：过滤日志](filter-logs.md) |
## 2022年8月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 导入 MySQL Binlog | 您可以将自建 MySQL 数据库或 RDS MySQL 数据库中的 Binlog 导入到 日志服务 ，实现数据的查询分析、加工等操作。 | 2022-08-23 | [部分地域](import-mysql-binary-logs.md) | [导入](import-mysql-binary-logs.md) [MySQL Binlog](import-mysql-binary-logs.md) |
| 无侵入监控 | 日志服务 与阿里云龙蜥社区合作研发了无侵入监控功能，以开放、高性能、无侵入的内核观测技术为广大云上开发者提供更便捷的可观测方式。 | 2022-08-18 | [全部地域](sls-supported-regions1.md) | [无侵入观测概述](overview-of-data-plane-monitoring.md) |
| Logtail CSV 插件 | 支持通过 CSV 模式解析 CSV 格式的数据。 | 2022-08-16 | [全部地域](sls-supported-regions1.md) | [表单配置方式](extract-content-from-log-fields.md) |
| 拓扑图 | 日志服务 提供拓扑图，用于直观地描述模块或应用之间的依赖关系以及总体概况信息。 | 2022-08-01 | [全部地域](sls-supported-regions1.md) | [拓扑图](topology-chart.md) |
| 查询型 LogStore | 日志服务 新增查询型 LogStore。查询型 LogStore 支持高性能查询，索引流量费用约为标准型 LogStore 的一半，但不支持 SQL 分析。 | 2022-08-01 | [全部地域](sls-supported-regions1.md) | [管理](manage-a-logstore.md) [LogStore](manage-a-logstore.md) |
## 2022年7月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 雷达图 | 日志服务 提供雷达图，用于展示多维数据。 | 2022-07-22 | [全部地域](sls-supported-regions1.md) | [雷达图](radar-chart.md) |
| ARMS RUM | 日志服务 ARMS RUM 集成了阿里云应用实时监控服务 ARMS 的前端监控功能。ARMS 前端监控专注于对 Web 场景、Weex 场景和小程序场景的监控，从页面打开速度（测速）、页面稳定性（JS 诊断错误）和外部服务调用成功率（API）这三个方面监测页面的健康度。 | 2022-07-14 | [全部地域](sls-supported-regions1.md) | [ARMS RUM](user-guide/arms-rum-overview.md) [概述](user-guide/arms-rum-overview.md) |
| 导入 PostgreSQL 数据 | 您可以将自建 PostgreSQL 数据库或 RDS PostgreSQL 数据库中的数据导入到 日志服务 ，实现数据的查询分析、加工等操作。 | 2022-07-04 | [部分地域](import-postgresql-data.md) | [导入](import-postgresql-data.md) [PostgreSQL](import-postgresql-data.md) [数据](import-postgresql-data.md) |
## 2022年6月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 自定义告警监控规则模板 | 日志服务 支持您自定义告警监控规则模板，并支持跨地域引用。 | 2022-06-10 | [全部地域](sls-supported-regions1.md) | [自定义告警监控规则模板](create-custom-alert-monitoring-rule-templates.md) |
## 2022年5月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 饼图（Pro 版本） | 日志服务 新增饼图（Pro 版本），用于展示不同数据分类的占比情况。 | 2022-05-27 | [全部地域](sls-supported-regions1.md) | [饼图](pie-chart.md) |
| 计量图（Pro 版本） | 计量图（Pro 版本）包含一个或多个条形图，支持更强大的可视化功能，例如合并多个条形图在同一个计量图中展示、针对字段进行个性化设置等。 | 2022-05-24 | [全部地域](sls-supported-regions1.md) | [计量图](bar-gauge.md) |
| 导入 Elasticsearch 数据 | 日志服务 支持导入 Elasticsearch 数据，实现数据的查询分析、加工等操作。 | 2022-05-11 | [全部地域](sls-supported-regions1.md) | [导入](import-data-from-elasticsearch-to-log-service.md) [Elasticsearch/OpenSearch](import-data-from-elasticsearch-to-log-service.md) [数据](import-data-from-elasticsearch-to-log-service.md) |
| Logtail 支持解析高精度时间 | Logtail 支持通过扩展配置（"enable_precise_timestamp": true）或 processor_strptime 插件解析高精度时间（毫秒、微秒、纳秒）。 | 2022-05-06 | [全部地域](sls-supported-regions1.md) | [Logtail](developer-reference/logtail-configurations.md) [配置（旧版）](developer-reference/logtail-configurations.md) 、 [表单配置方式](extract-log-time.md) |
## 2022年4月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 采集 ping 和 tcping 数据 | 日志服务 支持通过 Logtail 采集 ping 和 tcping 数据到 Metricstore 中进行查询与分析。 | 2022-04-28 | [全部地域](sls-supported-regions1.md) | [采集](collect-ping-and-tcping-data.md) [ping](collect-ping-and-tcping-data.md) [和](collect-ping-and-tcping-data.md) [tcping](collect-ping-and-tcping-data.md) [数据](collect-ping-and-tcping-data.md) |
| CloudLens for SLS | 日志服务 推出 CloudLens for SLS 应用，帮助您监控和管理 Project、LogStore 等资产，以提升您对 日志服务 资产的管理效率、快速了解其消耗情况。 | 2022-04-27 | [部分地域](usage-notes-45.md) | [CloudLens for SLS](usage-notes-45.md) |
| 统计图 Pro 版本 | 统计图 Pro 版本包含一个或多个单值图，支持更强大的可视化功能，例如合并多个查询分析结果在同一个统计图中展示、针对字段进行个性化设置等。 | 2022-04-26 | [全部地域](sls-supported-regions1.md) | [统计图](single-value-chart.md) |
| 直接下载日志 | 直接下载日志功能升级，支持下载 100 万条日志，10 万行查询分析结果。 | 2022-04-14 | [全部地域](sls-supported-regions1.md) | [下载日志](download-logs.md) |
| 导入 Kafka 数据 | 日志服务 支持导入 Kafka 数据，实现数据的查询分析、加工等操作。 | 2022-04-14 | [全部地域](sls-supported-regions1.md) | [导入](import-data-from-kafka-to-log-service.md) [Kafka](import-data-from-kafka-to-log-service.md) [数据](import-data-from-kafka-to-log-service.md) |
| AWS CloudTrail 审计 | AWS CloudTrail 审计应用支持拉取 AWS CloudTrail 日志，为您提供存储、查询、分析以及可视化等一站式服务，帮助您完成对 AWS 账户的操作事件审计。 | 2022-04-07 | [全部地域](sls-supported-regions1.md) | [AWS CloudTrail](usage-notes-22.md) [审计](usage-notes-22.md) |
## 2022年3月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 导入 SQL Server 数据 | 您可以将自建 SQL Server 数据库或 RDS SQL Server 数据库中的数据导入到 日志服务 ，实现数据的查询分析、加工等操作。 | 2022-03-30 | [部分地域](import-sql-server-data.md) | [导入](import-sql-server-data.md) [SQL Server](import-sql-server-data.md) [数据](import-sql-server-data.md) |
| 时序预测 | 日志服务 提供时序预测功能，用于对时序数据进行自动化、智能化的预测。您可以根据预测结果判断时序数据未来的走势，提前感知系统或者业务关键指标的状态。 | 2022-03-28 | [全部地域](sls-supported-regions1.md) | [时序预测](user-guide/how-time-series-forecasting-works.md) |
| CloudLens for CLB | 日志服务 联合阿里云负载均衡推出 CloudLens for CLB，提供 CLB 访问日志分析、秒级监控指标分析、实时告警等功能，并提供基于 AIOps 的自动异常巡检功能。 | 2022-03-28 | [全部地域](sls-supported-regions1.md) | [CloudLens for CLB](cloudlens-for-clb-usage-notes.md) |
| SLS RUM | SLS RUM 应用提供一站式用户端监控解决方案，您只需通过一个轻量级的 SDK 即可实现 Web 页面的监控，包括网页指标监控、页面稳定性监控、性能监控、API 请求监控、会话回放和前后端链路追踪。 | 2022-03-18 | [全部地域](sls-supported-regions1.md) | [SLS RUM](user-guide/sls-rum-overview.md) |
| 短语查询 | 日志服务 查询采用的是分词法，例如查询语句为 abc def ，将匹配所有包含 abc 或 def 的日志，不区分先后顺序，无法精准匹配目标短语。现在 日志服务 推出短语查询，用于精准匹配一段短语。 | 2022-03-16 | [部分地域](phrase-search.md) | [短语查询](phrase-search.md) |
| Data Explorer | 辅助输入更名为 Data Explorer。 Data Explorer 功能帮助您简单、快速地构建查询和分析语句。 | 2022-03-01 | [全部地域](sls-supported-regions1.md) | [通过](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) [Data Explorer](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) [构建查询和分析语句](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) |
| MaxCompute 投递（新版） | 日志服务 推出 MaxCompute 投递（新版）功将支持投递历史数据投递新增数据到 MaxCompute 中。 | 2022-03-01 | [部分地域](create-a-maxcompute-logship-task-new-version.md) | [投递日志到](comparison-between-the-old-and-new-versions-of-the-data-shipping-feature-for-maxcompute.md) [MaxCompute（新版）](comparison-between-the-old-and-new-versions-of-the-data-shipping-feature-for-maxcompute.md) |
## 2022年2月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 接入 Grafana 告警（Grafana 8.0 及以上版本） | Grafana 提供丰富的可视化界面，同时具备告警功能。您可以在 Grafana 中，添加 Contact point 配置。添加完成后，Grafana 会将告警消息发送到 日志服务 告警系统中。由 日志服务 告警系统完成告警降噪、通知等处理。 | 2022-02-24 | [全部地域](sls-supported-regions1.md) | [接入](ingest-grafana-alerts-into-log-service-1.md) [Grafana](ingest-grafana-alerts-into-log-service-1.md) [告警（Grafana 8.0](ingest-grafana-alerts-into-log-service-1.md) [及以上版本）](ingest-grafana-alerts-into-log-service-1.md) |
| 通用数据库审计 | 日志服务 通用数据库审计应用支持通过抓包方式将数据库的操作记录和操作行为上传到 日志服务 。您可以基于 日志服务 的存储、查询分析、可视化和告警等一站式功能，完成对数据库的审计。 | 2022-02-24 | [全部地域](sls-supported-regions1.md) | [通用数据库审计](usage-notes-27.md) |
| ALB Lens | ALB 日志中心升级为 ALB Lens。ALB Lens 提供负载均衡七层日志分析、秒级监控指标分析、实时告警等功能，并提供基于 AIOps 的自动异常巡检功能。 | 2022-02-18 | [全部地域](sls-supported-regions1.md) | [ALB Lens](usage-notes-15.md) |
| 导入 MySQL 数据 | 您可以将自建 MySQL 数据库或 RDS MySQL 数据库中的数据导入到 日志服务 ，实现数据的查询分析、加工等操作。 | 2022-02-17 | [部分地域](import-data-from-a-mysql-database-to-log-service.md) | [导入](import-data-from-a-mysql-database-to-log-service.md) [MySQL](import-data-from-a-mysql-database-to-log-service.md) [数据](import-data-from-a-mysql-database-to-log-service.md) |
## 2022年1月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 告警管理中心 | 告警管理中心是以业务为中心的告警管理运维平台。您可以将已有监控平台（Zabbix、Prometheus 等）产生的告警和 日志服务 资源产生的告警添加到一个业务中进行统一管理和通知，有效提高运维效率。 | 2022-01-13 | [全部地域](sls-supported-regions1.md) | [告警管理中心](overview-of-alert-opscenter.md) |
| 柱状图（Pro 版本） | 柱状图（Pro 版本）包括柱状图和条形图，支持更强大的可视化功能，例如合并多个查询分析结果在同一个图中展示、针对字段进行个性化设置等。 | 2022-01-11 | [全部地域](sls-supported-regions1.md) | [柱状图](column-chart.md) |
| PolarDB Lens | 日志服务 联合云数据库 PolarDB 推出 PolarDB Lens，用于集中管理 PolarDB MySQL 集群以及采集 PolarDB MySQL 集群的慢查询日志、错误日志、审计日志和性能指标。 | 2022-01-06 | [部分地域](cloudlens-for-polardb-usage-notes.md) | [PolarDB Lens](cloudlens-for-polardb-usage-notes.md) |
| RDS Lens | RDS 审计中心更名为 RDS Lens | 2022-01-05 | [部分地域](cloudlens-for-rds-usage-notes.md) | [RDS Lens](cloudlens-for-rds-usage-notes.md) |
## 2021年12月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| OSS 投递（新版） | 日志服务 推出 OSS 投递（新版）功能，支持投递历史数据和新增数据到 OSS Bucket 中。 | 2021-12-24 | [部分地域](create-oss-shipping-tasks-new-version.md) | [创建](create-oss-shipping-tasks-new-version.md) [OSS](create-oss-shipping-tasks-new-version.md) [投递任务（新版）](create-oss-shipping-tasks-new-version.md) |
| Redis Lens | 日志服务 联合 云数据库 Tair（兼容 Redis） 推出 Redis Lens，用于集中管理 Redis 实例以及采集 Redis 运行日志、慢日志和审计日志。 | 2021-12-17 | [部分地域](cloudlens-for-redis-usage-notes.md) | [Redis Lens](cloudlens-for-redis-usage-notes.md) |
| 接入阿里云 Prometheus 监控的告警 | 阿里云 Prometheus 监控全面对接开源 Prometheus 生态，支持类型丰富的组件监控，提供多种开箱即用的预置监控大盘，且提供全面托管的 Prometheus 服务。您通过简单的配置，即可将阿里云 Prometheus 监控的告警消息发送到 日志服务 告警系统中，由 日志服务 告警系统完成告警降噪、通知等处理。 | 2021-12-15 | [全部地域](sls-supported-regions1.md) | [接入阿里云](ingest-managed-service-for-prometheus-alerts-into-log-service.md) [Prometheus](ingest-managed-service-for-prometheus-alerts-into-log-service.md) [监控的告警](ingest-managed-service-for-prometheus-alerts-into-log-service.md) |
| 全栈监控 | 全栈监控应用是 日志服务 提供的一站式 IT 系统监控方案，监控的目标包括主机监控、Kubernetes 监控、数据库监控、中间件监控等。 | 2021-12-08 | [全部地域](sls-supported-regions1.md) | [全栈监控概述](overview-of-full-stack-monitoring.md) |
| 智能异常分析 | 日志服务 提供智能异常分析应用，支持对日志、指标等数据进行自动化、智能化、自适应的异常巡检。 | 2021-12-08 | [全部地域](sls-supported-regions1.md) | [智能异常分析概述](overview-of-intelligent-anomaly-analysis.md) |
## 2021年11月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 代码诊断 | 日志服务 与云效代码管理 Codeup 联合推出代码诊断功能，帮助您一键定位并跳转到对应代码的位置，快速排查和修复代码问题。 | 2021-11-17 | [全部地域](sls-supported-regions1.md) | [代码诊断](code-diagnostics.md) |
| 免登录查看告警详情 | 日志服务 提供免登录功能，您收到告警通知后，无需登录控制台即可查看告警详情以及进行告警规则、告警事务的管理操作。 | 2021-11-17 | [全部地域](sls-supported-regions1.md) | [免登录查看告警详情](view-alert-details-in-logon-free-mode.md) |
| 统计图表（Pro 版本） | 日志服务 支持通过统计图表的方式对查询分析结果进行可视化展示。统计图表（Pro 版本）支持展示多个查询分析结果，并支持对不同查询分析的结果进行个性化的可视化设置。 | 2021-11-17 | [全部地域](sls-supported-regions1.md) | [统计图表概述](user-guide/overview-of-charts.md) |
| 新增事件总线和函数计算告警通知渠道 | 日志服务 支持将告警通知发送到事件总线、函数计算等阿里云服务中。 | 2021-11-16 | [全部地域](sls-supported-regions1.md) | [通知渠道说明](notification-methods.md) |
| 辅助输入 | 日志服务 提供辅助输入功能，帮助您简单、快速地构建查询语句。 | 2021-11-15 | [全部地域](sls-supported-regions1.md) | [通过](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) [Data Explorer](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) [构建查询和分析语句](user-guide/build-query-and-analysis-statements-by-using-data-explorer.md) |
| AliyunServiceRoleForSLSAlert 服务关联角色 | 您可以授予 SLS 告警服务使用 SLS 告警服务关联角色（AliyunServiceRoleForSLSAlert）来获取其他云产品中的资源。 | 2021-11-15 | [全部地域](sls-supported-regions1.md) | [管理服务关联角色](manage-the-aliyunserviceroleforslsalert-service-linked-role.md) [AliyunServiceRoleForSLSAlert](manage-the-aliyunserviceroleforslsalert-service-linked-role.md) |
| EBS Lens | 阿里云 EBS Lens，帮助您更方便的监控和管理块存储资源，包含云盘、快照和云盘异步复制等资源。 | 2021-11-08 | [全部地域](sls-supported-regions1.md) | [EBS Lens](user-guide/usage-notes-1.md) |
## 2021年10月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 窗口漏斗函数 | 窗口漏斗函数用于在滑动的时间窗口中搜索事件链并计算事件链中发生的最大连续的事件数。 | 2021-10-22 | [全部地域](sls-supported-regions1.md) | [窗口漏斗函数](window-funnel-function.md) |
| 单位换算函数 | 日志服务 提供单位换算函数，帮助您换算数据量的单位。 | 2021-10-20 | [全部地域](sls-supported-regions1.md) | [单位换算函数](unit-conversion-functions.md) |
## 2021年9月
| 功能名称 | 功能描述 | 发布时间 | 地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 新版内容模板语法 | 新版内容模板语法通过类似 Python 语法的方式，提供更加灵活且高级的自定义渲染逻辑，在定制通知内容（例如 Markdown 转义）、自定义内容样式等方面都做了优化，满足更多样化的定制内容需求。 | 2021-09-30 | [全部地域](sls-supported-regions1.md) | [内容模板语法（新版）](syntax-for-new-alert-templates.md) |
| 冷热分层存储 | 日志服务 提供冷存储功能，降低您长周期存储的成本，并同时保证日志的查询、分析、可视化、告警、投递和加工等能力不受影响。 | 2021-09-03 | [全部地域](sls-supported-regions1.md) | [开启智能存储分层](enable-hot-and-cold-tiered-storage-for-a-logstore.md) |
| 定时 SQL 告警 | 日志服务 定时 SQL 已内置监控规则模板，您只需添加对应的告警实例即可实时监控定时 SQL 任务，并可通过钉钉等渠道接收到告警通知。 | 2021-09-01 | [全部地域](sls-supported-regions1.md) | [为定时](configure-alerts-for-a-scheduled-sql-job.md) [SQL](configure-alerts-for-a-scheduled-sql-job.md) [任务设置告警](configure-alerts-for-a-scheduled-sql-job.md) |
## 2021年8月
| 功能名称 | 功能描述 | 发布时间 | 地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 半年期资源包 | 新版资源包新增半年期选项。 | 2021-08-16 | [全部地域](sls-supported-regions1.md) | [资源包介绍](overview-11.md) |
| DDoS 原生防护日志 | 日志审计服务支持接入 DDoS 原生访问日志。 | 2021-08-03 | 不涉及 | [日志审计服务](overview-of-log-audit-service.md) |
| DDoS 高防（非中国内地）访问日志 | 日志审计服务支持接入 DDoS 高防（非中国内地）访问日志。 | 2021-08-03 | 不涉及 | [日志审计服务](overview-of-log-audit-service.md) |
## 2021年7月
| 功能名称 | 功能描述 | 发布时间 | 地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 移动运维监控 | 日志服务 移动运维监控用于实时监控 App 崩溃、ANR 等问题，并且支持智能分析，帮助您低成本、高效率地发现 App 应用中的各类隐患。 | 2021-07-26 | [全部地域](sls-supported-regions1.md) | [移动运维监控](overview-of-mobile-o-and-m-monitoring.md) |
| Logtail 1.0.22 | 新增 Logtail 1.0.22 版本。 | 2021-07-17 | [全部地域](sls-supported-regions1.md) | [Logtail 1.0.22](sls-release-notes.md) |
| Logtail 0.16.68 | 新增 Logtail 0.16.68 版本。 | 2021-07-14 | [全部地域](sls-supported-regions1.md) | [Logtail 0.16.68](sls-release-notes.md) |
| VPC 边界云防火墙流量日志 | 日志审计服务支持接入云防火墙下的 VPC 边界防火墙流量日志。 | 2021-07-09 | [全部地域](sls-supported-regions1.md) | [日志审计服务](overview-of-log-audit-service.md) |
| Logtail 1.0.21 | 新增 Logtail 1.0.21 版本。 | 2021-07-06 | [全部地域](sls-supported-regions1.md) | [Logtail 1.0.21](sls-release-notes.md) |
## 2021年6月
| 功能名称 | 功能描述 | 发布时间 | 地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| Webhook 集成 | Webhook 集成用于管理 Webhook 通知渠道，您可以在行动策略中直接使用已创建的 Webhook。目前， 日志服务 支持钉钉、企业微信、飞书、Slack 以及自定义的通用 Webhook。 | 2021-06-30 | [全部地域](sls-supported-regions1.md) | [Webhook](create-a-webhook.md) [集成](create-a-webhook.md) |
| 接入 Zabbix 告警 | Zabbix 作为常用的开源监控系统，提供了丰富的告警规则用于系统监控，同时支持多种告警通知渠道。您可以将 日志服务 告警系统设为 Zabbix 的一个通知渠道，由 日志服务 告警系统完成告警降噪、通知等处理。 | 2021-06-29 | [全部地域](sls-supported-regions1.md) | [接入](ingest-zabbix-alerts-into-log-service.md) [Zabbix](ingest-zabbix-alerts-into-log-service.md) [告警（Zabbix 4.4](ingest-zabbix-alerts-into-log-service.md) [及以上版本）](ingest-zabbix-alerts-into-log-service.md) |
| RDS 审计中心 | 日志服务 与云数据库 RDS 联合推出 RDS 审计中心。您可以通过 RDS 审计中心实时查看 RDS SQL 审计日志的采集状态，集中管理采集配置，并可基于采集到的日志进行后续的审计、分析、告警等操作。 | 2021-06-28 | [部分地域](cloudlens-for-rds-usage-notes.md) | [RDS](cloudlens-for-rds-usage-notes.md) [审计中心](cloudlens-for-rds-usage-notes.md) |
| Flowlog 日志中心 | 日志服务 和专有网络联合推出 Flowlog 日志中心，用于 VPC 的策略统计、弹性网卡、流量统计以及网段间流量统计，帮助您快速、有效地分析 VPC 流日志。 | 2021-06-21 | [全部地域](sls-supported-regions1.md) | [Flowlog](usage-notes-6.md) [日志中心](usage-notes-6.md) |
| 接入负载均衡 4 层秒级监控指标 | 日志服务 与负载均衡联合推出负载均衡 4 层秒级监控功能。您可以通过秒级监控指标查看负载均衡相关的秒级流量、QPS、错误率等信息，进行更精细的服务监控和问题定位。 | 2021-06-04 | [全部地域](sls-supported-regions1.md) | [负载均衡](layer-4-monitoring-metrics-for-clb-usage-notes.md) [4](layer-4-monitoring-metrics-for-clb-usage-notes.md) [层秒级监控指标](layer-4-monitoring-metrics-for-clb-usage-notes.md) |
## 2021年5月
| 功能名称 | 功能描述 | 发布时间 | 支持地域 | 相关文档 |
| --- | --- | --- | --- | --- |
| 定时 SQL | 定时 SQL 功能用于定时分析数据、存储聚合数据、投影与过滤数据。 | 2021-05-13 | [全部地域](sls-supported-regions1.md) | [定时](how-scheduled-sql-works.md) [SQL](how-scheduled-sql-works.md) |
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
