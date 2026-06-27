# kube-apiserver组件监控指标及大盘使用说明-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/monitor-kube-apiserver

# kube-apiserver组件监控指标及大盘使用说明
kube-apiserver组件提供了Kubernetes的RESTful API接口，使得外部客户端、集群内的其他组件可以与ACK集群交互。本文介绍kube-apiserver组件的监控指标清单、大盘使用指导以及常见指标异常解析。
## 使用前须知
### 操作入口
请参见[查看集群控制面组件监控大盘](view-control-plane-component-dashboards-in-ack-pro-clusters.md)。
### 指标清单
指标是组件对外透出状态和参数的方式之一。kube-apiserver组件使用的指标清单如下。
| 指标清单 | 类型 | 解释 |
| --- | --- | --- |
| apiserver_request_duration_seconds_bucket | Histogram | 该指标用于统计 API Server 客户端对 API Server 不同请求的访问时延分布。 请求的维度包括： Verb：请求的类型，例如 GET、POST、PUT、DELETE 等。 Group：API 组，即相关 API 接口的集合，用于扩展 Kubernetes API。 Version：API 版本，例如 v1、v1beta1 等。 Resource：请求针对的资源类型，例如 Pod、Service、Lease 等。 Subresource：资源的子资源，例如 Pod 详细信息、Pod 日志等。 Scope：请求的范围，例如命名空间维度的资源（Namespace-scoped）或集群维度的资源（Cluster-scoped）。 Component：发起请求的组件的名称，例如 kube-controller-manager 、 kube-scheduler 、 cloud-controller-manager 等。 Client：发起请求的客户端，可能是内部组件或外部服务。 API Server Histogram 的 Bucket 阈值为 {0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 40, 50, 60} 。单位：秒。 |
| apiserver_request_total | Counter | 对 API Server 不同请求的计数。请求的维度包括 Verb、Group、Version、Resource、Scope、Component、HTTP contentType、HTTP code（响应的 HTTP 状态码）和 Client。 |
| apiserver_request_no_resourceversion_list_total | Counter | 对 API Server 的请求中参数未配置 resourceVersion 的 LIST 请求的计数。评估 Quorum Read 类型的 LIST 请求可以定位是否存在过多的此类请求以及发起相应请求的客户端，以便优化客户端的请求行为，提高集群性能。请求的维度包括 Group、Version、Resource、Scope 和 Client。 |
| apiserver_current_inflight_requests | Gauge | API Server 当前处理的请求数量。请求包括两种： ReadOnly：这类请求不会改变集群的状态，通常为读取资源的操作，例如获取 Pods 列表、查询节点状态等。 Mutating：这类请求会改变集群的状态，通常为创建、更新或删除资源的操作，例如新建 Pod、更新 Service 配置等。 |
| apiserver_dropped_requests_total | Counter | API Server 执行限流策略过程中，主动丢弃掉的请求数。HTTP 返回值为 429 'Try again later' 。 |
| etcd_request_duration_seconds_bucket | Histogram | 该指标用于统计 API Server 对 etcd 请求的访问时延分布。 请求的维度包括操作（Operation）和操作对象的类型（Type）。 Bucket 阈值为 {0.005, 0.025, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.25, 1.5, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 45, 60} 。单位：秒。 |
| apiserver_flowcontrol_request_concurrency_limit | Gauge | APF 请求并发限制。表示某个优先级队列的最大并发限制，即该队列理论上允许同时处理的最大请求数，供您了解 API Server 如何通过流量控制策略将资源分配给不同优先级的队列，从而确保高优先级请求可以及时处理。 该指标在 Kubernetes 1.30 版本变为 Deprecated，自 1.31 版本起移除，1.31 及以上版本的集群中建议使用 apiserver_flowcontrol_nominal_limit_seats 指标代替。 |
| apiserver_flowcontrol_current_executing_requests | Gauge | 某个优先级队列中当前正在执行的请求数量，即该队列的实际并发负载，供您了解 API Server 的实际负载情况，判断是否接近系统最大并发限制，防止过载。 |
| apiserver_flowcontrol_current_inqueue_requests | Gauge | 某个优先级队列中当前在队列中等待处理的请求数量，即该队列的请求积压情况，以了解 API Server 的流量压力以及队列是否过载。 |
| apiserver_flowcontrol_nominal_limit_seats | Gauge | APF 名义并发限制席位数量，即 API Server 理论上（nominal）的最大并发处理能力，以 Seat 为单位。供您了解 API Server 如何通过流量控制策略将资源分配给不同优先级的队列。 |
| apiserver_flowcontrol_current_limit_seats | Gauge | APF 当前并发限制席位数量。表示某个优先级队列的当前并发限制（Current Concurrency Limit），即在动态调整后实际允许的最大并发席位数量，反映当前队列的实际并发能力（可能因系统负载或其他因素而动态变化）。 与 nominal_limit_seats 不同，此值可能会受全局流量控制策略影响。 |
| apiserver_flowcontrol_current_executing_seats | Gauge | APF 当前在执行的席位数量，表示某个优先级队列中当前正在执行的请求数对应的席位数量，反映了当前队列中正在消耗的并发资源。供您了解队列的实际负载情况。 如果 current_executing_seats 接近 current_limit_seats，表明该队列的并发资源可能即将耗尽。 您可以提升 API Server 的 maxMutatingRequestsInflight 和 maxRequestsInflight 的参数取值以优化配置。操作入口及参数取值，请参见 [自定义](customize-ack-pro-control-plane-component-parameters-1693464061811.md) [Pro](customize-ack-pro-control-plane-component-parameters-1693464061811.md) [版集群的控制面组件参数](customize-ack-pro-control-plane-component-parameters-1693464061811.md) 。 |
| apiserver_flowcontrol_current_inqueue_seats | Gauge | APF 当前队列中席位数量，表示某个优先级队列中当前等待处理的请求数对应的席位数量，反映了当前队列中等待处理的请求所占用的资源，以供您了解队列的积压情况。 |
| apiserver_flowcontrol_request_execution_seconds_bucket | Histogram | 请求的实际执行时间，记录了请求从开始执行到最终完成所花费的时间。 时间区间分布为{0, 0.005, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 30}。单位：秒。 |
| apiserver_flowcontrol_request_wait_duration_seconds_bucket | Histogram | 请求在队列中等待的时间分布，记录了请求从进入队列到开始执行之间的等待时间 时间区间分布为{0, 0.005, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 15, 30}。单位：秒。 |
| apiserver_flowcontrol_dispatched_requests_total | Counter | 成功调度并处理的请求数量，反映了 API Server 成功处理的请求总数。 |
| apiserver_flowcontrol_rejected_requests_total | Counter | 因超出并发限制或队列容量而被拒绝的请求数量。 |
| apiserver_admission_controller_admission_duration_seconds_bucket | Histogram | 准入控制器（Admission Controller）的处理延时。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate 或 admit）和请求是否被拒绝（true 或 false）。 Bucket 阈值为 {0.005, 0.025, 0.1, 0.5, 2.5} 。单位：秒。 |
| apiserver_admission_webhook_admission_duration_seconds_bucket | Histogram | 准入 Webhook（Admission Webhook）的处理延时。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate，校验请求的合法性，或 admit，在请求合法的情况下，决定是否允许该请求）和请求是否被拒绝（true 或 false）。 Bucket 的阈值为 {0.005, 0.025, 0.1, 0.5, 2.5} 。单位：秒。 |
| apiserver_admission_webhook_admission_duration_seconds_count | Counter | 准入 Webhook（Admission Webhook）的处理请求统计。标签包括 Admission Controller 名称、操作（CREATE、UPDATE、CONNECT 等）、API 资源、操作类型（validate 或 admit）和请求是否被拒绝（true 或 false）。 |
| cpu_utilization_core | Gauge | CPU 使用量。单位：核（Core）。 |
| memory_utilization_byte | Gauge | 内存使用量。单位：字节（Byte）。 |
| resource_utilization_level | Gauge | 资源使用水位。 resource：资源类型，包括 cpu 和 memory。 utilization_level：水位等级，high（使用率 ≥80%）或 normal（使用率 <80%）。 container：目标容器。包括 kube-apiserver、kube-scheduler、kube-controller-manager、cloud-controller-manager 和 etcd。 |
| up | Gauge | 服务可用性。 1：表示服务可用。 0：表示服务不可用。 |
说明
如下资源使用率指标已废弃，请及时去除依赖该指标的告警和监控。
cpu_utilization_ratio：CPU使用率。
memory_utilization_ratio：内存使用率。
请使用resource_utilization_level指标做资源使用水位相关的告警和监控，该指标在灰度开放中。如果内存和CPU资源水位相关看板不可见，请先[升级监控组件](../../../../arms/documents/prometheus-monitoring/update-monitoring-components.md)再[升级托管探针](../../../../arms/documents/prometheus-monitoring/update-monitoring-components.md)。
### 大盘使用指导
大盘基于组件指标和相关PromQL绘制，包括关键指标、概览、资源分析、QPS和时延、准入控制器和Webhook、客户端分析部分。
大盘构成模块如下，常见的使用顺序为：
[关键指标](monitor-kube-apiserver.md)：快速查看集群关键指标。
[概览](monitor-kube-apiserver.md)：分析API Server的响应时延、当前处理请求数和是否有限流发生。
[资源分析](monitor-kube-apiserver.md)：查看托管侧组件的资源水位。
[QPS](monitor-kube-apiserver.md)[和时延](monitor-kube-apiserver.md)：通过多维度深入分析QPS、RT。
[APF](monitor-kube-apiserver.md)[限流](monitor-kube-apiserver.md)：根据[APF](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/)指标确认API Server的请求流量分布、限流状态以及系统性能瓶颈。
[注入控制器和](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)：分析准入控制器和Webhook的QPS、RT。
[客户端分析](monitor-kube-apiserver.md)：通过客户端多维度分析QPS。
## 筛选框
在大盘上方，您可以根据筛选框配置观测API Server请求的Verb、资源（Resource）、分位数（Quantile）和面板使用的PromQL的采样时长（Interval）。
说明
调整分位数（Quantile）时，以0.9为例，表示大盘上Histogram类型指标的采样值的数量占该类型指标总体采样值的90%。分位数为0.9（简称为P90）的指标可以去除采样值占比小的长尾样本的影响，分位数为0.99（简称为P99）的指标会包含长尾样本的影响。
以下筛选框可以选择观测的时间段和页面刷新周期。
## 关键指标
可观测性展示功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| API QPS | sum(irate(apiserver_request_total[$interval])) | API Server 的总 QPS。 |
| 读请求成功率 | sum(irate(apiserver_request_total{code=~"20.*",verb=~"GET|LIST"}[$interval]))/sum(irate(apiserver_request_total{verb=~"GET|LIST"}[$interval])) | API Server 处理读请求的成功率。 |
| 写请求成功率 | sum(irate(apiserver_request_total{code=~"20.*",verb!~"GET|LIST|WATCH|CONNECT"}[$interval]))/sum(irate(apiserver_request_total{verb!~"GET|LIST|WATCH|CONNECT"}[$interval])) | API Server 处理写请求的成功率。 |
| 在处理读请求数量 | sum(apiserver_current_inflight_requests{requestKind="readOnly"}) | API Server 当前在处理的读请求数量。 |
| 在处理写请求数量 | sum(apiserver_current_inflight_requests{requestKind="mutating"}) | API Server 当前在处理的写请求数量。 |
| 请求限流速率 | sum(irate(apiserver_dropped_requests_total[$interval])) | Dropped Request Rate。 API Server 限流策略过程中，主动丢弃掉的请求数所占总请求数的比例。 |
## 概览
可观测性展示功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| GET 读请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb="GET",resource!="",subresource!~"log|proxy"}[$interval])) by (pod, verb, resource, subresource, scope, le)) | 展示 GET 请求的响应时间，维度包括 API Server Pod、Verb（GET）、Resources、Scope。 |
| LIST 读请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb="LIST"}[$interval])) by (pod_name, verb, resource, scope, le)) | 展示 LIST 请求的响应时间，维度包括 API Server Pod、Verb（LIST）、Resources、Scope。 |
| 写请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb!~"GET|WATCH|LIST|CONNECT"}[$interval])) by (cluster, pod_name, verb, resource, scope, le)) | 展示 Mutating 请求的响应时间，维度包括 API Server Pod、Verb（GET、WATCH、LIST、CONNECT）、Resources、Scope。 |
| 在处理读请求数量 | apiserver_current_inflight_requests{request_kind="readOnly"} | API Server 正在处理的读请求数量。 |
| 在处理写请求数量 | apiserver_current_inflight_requests{request_kind="mutating"} | API Server 正在处理的写请求数量。 |
| 请求限流速率 | sum(irate(apiserver_dropped_requests_total{request_kind="readOnly"}[$interval])) by (name) sum(irate(apiserver_dropped_requests_total{request_kind="mutating"}[$interval])) by (name) | API Server 的限流速率 ， No data 或者 0 表示没有限流。 |
## 资源分析
可观测性展示
功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 内存使用量 | memory_utilization_byte{container="kube-apiserver"} | API Server 的内存使用量。单位：字节。 |
| CPU 使用量 | cpu_utilization_core{container="kube-apiserver"}*1000 | API Server 的 CPU 使用量。单位：毫核。 |
| 资源对象数量 | max by(resource)(apiserver_storage_objects) max by(resource)(etcd_object_counts) | 当 ACK 为 1.22 及以上版本时， 指标名字为 apiserver_storage_objects 当 ACK 为 1.22 及以下版本时，指标名字为 etcd_object_counts。 说明 由于兼容性问题，1.22 版本中 apiserver_storage_objects 名称和 etcd_object_counts 名称均存在。 |
| 内存资源水位 | resource_utilization_level{resource="memory",container="kube-apiserver",utilization_level="high"} resource_utilization_level{resource="memory",container="kube-apiserver",utilization_level="normal"} | 当 resource_utilization_level{utilization_level="high",...} == 1，表明容器资源利用率（水位）>= 80%。 当 resource_utilization_level{utilization_level="normal",...} == 1，表明容器资源利用率（水位）< 80%。 |
| CPU 资源水位 | resource_utilization_level{resource="cpu",container="kube-apiserver",utilization_level="high"} resource_utilization_level{resource="cpu",container="kube-apiserver",utilization_level="normal"} |  |
## QPS和时延
可观测性展示功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 按 Verb 维度分析 QPS | sum(irate(apiserver_request_total{verb=~"$verb"}[$interval]))by(verb) | 按 Verb 维度，统计单位时间（1s）内的请求 QPS。 |
| 按 Verb+Resource 维度分析 QPS | sum(irate(apiserver_request_total{verb=~"$verb",resource=~"$resource"}[$interval]))by(verb,resource) | 按 Verb+Resource 维度，统计单位时间（1s）内的请求 QPS。 |
| 按 Verb 维度分析请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb=~"$verb", verb!~"WATCH|CONNECT",resource!=""}[$interval])) by (le,verb)) | 按 Verb 维度，分析请求时延。 |
| 按 Verb+Resource 维度分析请求时延 | histogram_quantile($quantile, sum(irate(apiserver_request_duration_seconds_bucket{verb=~"$verb", verb!~"WATCH|CONNECT", resource=~"$resource",resource!=""}[$interval])) by (le,verb,resource)) | 按 Verb+Resource 维度，分析请求时延。 |
| 非 2xx 返回值的读请求 QPS | sum(irate(apiserver_request_total{verb=~"GET|LIST",resource=~"$resource",code!~"2.*"}[$interval])) by (verb,resource,code) | 统计非 2xx 返回值（除成功以外的所有情况，例如 4xx、5xx 等）的读请求 QPS。 |
| 非 2xx 返回值的写请求 QPS | sum(irate(apiserver_request_total{verb!~"GET|LIST|WATCH",verb=~"$verb",resource=~"$resource",code!~"2.*"}[$interval])) by (verb,resource,code) | 统计非 2xx 返回值（除成功以外的所有情况，例如 4xx、5xx 等）的写请求 QPS。 |
| Apiserver 对 etcd 请求时延 | histogram_quantile($quantile, sum(irate(etcd_request_duration_seconds_bucket[$interval])) by (le,operation,type,instance)) | 统计 API Server 对 etcd 的请求时延。 |
## APF限流
说明
APF限流相关指标监控处于灰度发布中。
APF相关指标仅支持1.20及以上版本集群。如需升级，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)。
APF相关指标大盘还依赖如下组件的升级，请参见[组件监控升级说明](https://help.aliyun.com/zh/prometheus/user-guide/update-monitoring-components)完成升级：
容器集群监控组件：0.06及以上版本。
[ack-arms-prometheus](../../../../arms/documents/prometheus-monitoring/prometheus-monitoring-change-records-2.md)组件：v1.1.31及以上版本。
托管探针：v1.1.31及以上版本。
可观测性展示
功能解析
下表中部分指标按PL、Instance、FS维度进行统计。
PL：Priority Level维度，即根据不同优先级进行统计。
Instance：根据API Server实例维度进行统计。
FS：Flow Schema维度，即根据请求分类进行统计。
关于APF及上述维度的详细信息，请参见[APF](https://kubernetes.io/docs/concepts/cluster-administration/flow-control/)。
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| APF 请求并发限制（维度：PL） | sum by(priority_level) (apiserver_flowcontrol_request_concurrency_limit) | 按 PL 或 Instance + PL 维度统计 APF 请求并发限制，即某个优先级队列理论上允许同时处理的最大请求数。 apiserver_flowcontrol_request_concurrency_limit 在 Kubernetes 1.30 版本变为 Deprecated，自 1.31 版本起移除 ， 1.31 及以上版本的集群中建议使用 apiserver_flowcontrol_nominal_limit_seats 指标代替。 |
| APF 请求并发限制（维度：Instance + PL） | sum by(instance,priority_level) (apiserver_flowcontrol_request_concurrency_limit) |  |
| APF 当前执行请求数量（维度：FS + PL） | sum by(flow_schema,priority_level) (apiserver_flowcontrol_current_executing_requests) | 按 FS + PL 或 Instance + FS + PL 维度统计 APF 当前正在执行的请求数量。 |
| APF 当前执行请求数量（维度：Instance + FS + PL） | sum by(instance,flow_schema,priority_level)(apiserver_flowcontrol_current_executing_requests) |  |
| APF 当前在队列中待处理请求数量（维度：FS + PL） | sum by(flow_schema,priority_level) (apiserver_flowcontrol_current_inqueue_requests) | 按 FS + PL 或 Instance + FS + PL 维度统计当前队列中待处理的请求数量。 |
| APF 当前队列中待处理请求数量（维度：Instance + FS + PL） | sum by(instance,flow_schema,priority_level) (apiserver_flowcontrol_current_inqueue_requests) |  |
| APF 名义并发限制席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_nominal_limit_seats) | 按 Instance + PL 维度统计 APF 席位数量的相关指标。包括以下指标： 名义并发限制：不同优先级队列的名义最大并发席位限制。 当前并发限制：不同优先级队列中，在动态调整后实际允许的最大并发席位数量。 在执行：不同优先级队列中当前正在执行的请求数对应的席位数量。 队列中：不同优先级队列中排队中的请求数对应的席位数量。 |
| APF 当前并发限制席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_limit_seats) |  |
| APF 当前在执行的席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_executing_seats) |  |
| APF 当前队列中席位数量 | sum by(instance,priority_level) (apiserver_flowcontrol_current_inqueue_seats) |  |
| APF 请求执行时间 | histogram_quantile($quantile, sum(irate(apiserver_flowcontrol_request_execution_seconds_bucket[$interval])) by (le,instance, flow_schema,priority_level)) | 请求从开始执行到最终完成所花费的时间。 |
| APF 请求等待时间 | histogram_quantile($quantile, sum(irate(apiserver_flowcontrol_request_wait_seconds_bucket[$interval])) by (le,instance, flow_schema,priority_level)) | 请求从进入队列到开始执行之间的等待时间。 |
| APF 成功调度并处理的请求 QPS | sum(irate(apiserver_flowcontrol_dispatched_requests_total[$interval]))by(instance,flow_schema,priority_level) | 成功调度并处理的请求 QPS。 |
| APF 拒绝请求 QPS | sum(irate(apiserver_flowcontrol_rejected_requests_total[$interval]))by(instance,flow_schema,priority_level) | 因超出并发限制或队列容量而被拒绝的请求 QPS。 |
## 准入控制器和Webhook
可观测性展示功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 准入控制器时延[admit] | histogram_quantile($quantile, sum by(operation, name, le, type, rejected) (irate(apiserver_admission_controller_admission_duration_seconds_bucket{type="admit"}[$interval])) ) | 使用到的 admit 类型的 Admission Controller 名称、操作、是否拒绝以及相应的执行时间。 指标 Bucket 的阈值为 {0.005、0.025、0.1、0.5、2.5} 。单位：秒。 |
| 准入控制器时延[validate] | histogram_quantile($quantile, sum by(operation, name, le, type, rejected) (irate(apiserver_admission_controller_admission_duration_seconds_bucket{type="validate"}[$interval])) ) | 使用到的 validate 类型的 Admission Controller 名称、操作、是否拒绝以及相应的执行时间。 指标 Bucket 的阈值为 {0.005、0.025、0.1、0.5、2.5} 。单位：秒。 |
| 准入 Webhook 时延[admit] | histogram_quantile($quantile, sum by(operation, name, le, type, rejected) (irate(apiserver_admission_webhook_admission_duration_seconds_bucket{type="admit"}[$interval])) ) | 使用到的 admit 类型的 Webhook 名称、操作、是否拒绝以及相应的执行时间。 指标 Bucket 的阈值为 {0.005、0.025、0.1、0.5、2.5} ，单位：秒。 |
| 准入 Webhook 时延[validating] | histogram_quantile($quantile, sum by(operation, name, le, type, rejected) (irate(apiserver_admission_webhook_admission_duration_seconds_bucket{type="validating"}[$interval])) ) | 使用到的 admit 类型的 Webhook 名称、操作、是否拒绝以及相应的执行时间。 指标 Bucket 的阈值为 {0.005、0.025、0.1、0.5、2.5} 。单位：秒。 |
| 准入 Webhook 请求 QPS | sum(irate(apiserver_admission_webhook_admission_duration_seconds_count[$interval]))by(name,operation,type,rejected) | 准入 Webhook 的请求 QPS。 |
## 客户端分析
可观测性展示功能解析
| 名称 | PromQL | 说明 |
| --- | --- | --- |
| 按 Client 维度分析 QPS | sum(irate(apiserver_request_total{client!=""}[$interval])) by (client) | 按 Client 维度分析 QPS。用于分析访问 API Server 的客户端以及 QPS。 |
| 按 Verb+Resource+Client 维度分析 QPS | sum(irate(apiserver_request_total{client!="",verb=~"$verb", resource=~"$resource"}[$interval]))by(verb,resource,client) | 按 Verb+Resource+Client 维度分析 QPS。 |
| 按 Verb+Resource+Client 维度分析 LIST 请求 QPS（无 resourceVersion 字段） | sum(irate(apiserver_request_no_resourceversion_list_total[$interval]))by(resource,client) | 按 Verb+Resource+Client 维度分析 LIST 请求的 QPS（无 resourceVersion 字段）。 可以分析对 API Server 的全部 LIST 请求中、到 etcd 的部分 LIST 请求，帮助识别以及优化 API Server 客户端的 LIST 行为。 |
## 常见指标异常
如果组件的常见指标异常，请对照下文的情况说明排查是否为预期内情况。
### 读/写请求成功率
情况说明
| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| 读请求成功率 和 写请求成功率 接近 100%。 | 读请求成功率 和 写请求成功率 维持在较低百分比，例如小于 90%。 | 存在较多非 200 返回值请求。 |
推荐解决方案
查看面板，定位非2xx返回值的读请求QPS和非2xx返回值的写请求 QPS中导致非200返回值请求类型和资源。请评估该类请求是否符合预期，并随之采取措施进行优化。例如，如果有GET/deployment 404，表示存在GET Deployment返回404的请求，会导致读请求成功率降低，请判断是否为预期行为。
### GET/LIST读请求时延和写请求时延
情况说明
| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| GET 读请求时延 、 LIST 读请求时延 、 写请求时延 与访问的集群资源数量和集群规模相关联，没有固定的正常与异常的时间分界，只要不影响业务即在接受范围内。例如，如果访问的某种资源量越大，那么 LIST 请求时间就会越长。一般情况下， GET 读请求时延 、 写请求时延 小于 1s， LIST 读请求时延 小于 5s，为正常现象。 | GET 读请求时延 、 写请求时延 大于 1s。 LIST 读请求时延 大于 5s。 | 请求的响应时延过长时，需要排除集群资源数量多、Webhook 调用慢等因素的影响。 |
推荐解决方案
查看面板，定位GET读请求时延、LIST读请求时延、写请求时延中导致非200返回值的请求类型和资源，并采取解决措施。
请求延时指标apiserver_request_duration_seconds_bucket的最大阈值是60s，超过60s的请求都会统计为60s。而登录Pod的请求POST pod/exec、读取日志的请求会建立长链接，该类请求时间通常会超过60s。问题定位时，您可忽略该类请求。
参见[准入](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)[时延](monitor-kube-apiserver.md)，分析是否由于Webhook执行较慢，导致API Server请求延时长。
### 在处理读/写请求数量和请求限流速率
情况说明
| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| 通常情况下， 在处理读请求数量 和 在处理写请求数量 小于 100， 请求限流速率 为 0，为正常现象。 | 在处理读请求数量 、 在处理写请求数量 大于 100。 请求限流速率 大于 0。 | 当前在处理请求的队列积压时，需要排除短时请求量涌入导致处理延时、Webhook 调用慢等因素的影响。超过队列长度时， API Server 会限流，导致 请求限流速率 大于 0，影响集群稳定性。 |
推荐解决方案
查看[QPS](monitor-kube-apiserver.md)[和时延](monitor-kube-apiserver.md)和[客户端分析](monitor-kube-apiserver.md)，分析请求中占比位于头部的请求，评估是否符合预期。如果请求为实际业务发起，您可以判断是否需降低请求量。
参见[准入](monitor-kube-apiserver.md)[Webhook](monitor-kube-apiserver.md)[时延](monitor-kube-apiserver.md)，分析是否因为Webhook执行慢导致API Server请求处理慢。
### 准入Webhook时延
情况说明
| 正常情况 | 异常情况 | 说明 |
| --- | --- | --- |
| 准入 Webhook 时延 小于 0.5s。 | 持续出现 准入 Webhook 时延 大于 0.5s。 | Webhook 响应慢会影响 API Server 的响应时延。 |
推荐解决方案
排查Webhook日志等信息，判断是否符合预期。如果不需要某个Webhook，请卸载。
## 相关文档
关于其他集群控制面组件监控的指标详情、大盘使用指引和常见指标异常说明，请参见：
[etcd](monitor-etcd.md)[组件监控指标说明](monitor-etcd.md)
[kube-scheduler](monitor-kube-scheduler.md)[组件监控指标说明](monitor-kube-scheduler.md)
[kube-controller-manager](monitor-kube-controller-manager.md)[组件监控指标说明](monitor-kube-controller-manager.md)
[cloud-controller-manager](monitor-cloud-controller-manager.md)[组件监控指标说明](monitor-cloud-controller-manager.md)
关于如何通过控制台或API获取Prometheus监控数据，请参见[通过](use-promql-to-query-prometheus-monitoring-data.md)[PromQL](use-promql-to-query-prometheus-monitoring-data.md)[查询](use-promql-to-query-prometheus-monitoring-data.md)[Prometheus](use-promql-to-query-prometheus-monitoring-data.md)[监控数据](use-promql-to-query-prometheus-monitoring-data.md)。
关于如何通过阿里云Prometheus监控自定义PromQL配置报警规则，请参见[创建](../../../../arms/documents/prometheus-monitoring/create-an-alert-rule-for-a-prometheus-instance.md)[Prometheus](../../../../arms/documents/prometheus-monitoring/create-an-alert-rule-for-a-prometheus-instance.md)[告警规则](../../../../arms/documents/prometheus-monitoring/create-an-alert-rule-for-a-prometheus-instance.md)。
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
