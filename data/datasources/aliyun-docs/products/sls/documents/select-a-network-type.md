# Logtail参数与配置文件-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/select-a-network-type

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

# Logtail网络类型，启动参数与配置文件

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍使用Logtail采集日志时，如何选择网络来保障采集速度，如何配置启动参数来调整采集性能，以及Logtail运行中依赖的一系列配置文件与信息记录文件。

## 网络类型与选择

在[安装](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)[Logtail](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)时，根据服务器与日志服务之间的关系，选择对应的网络类型有利于日志数据的传输更快速稳定。网络类型选择示例如下：

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

| 网络类型 | 描述 | 适用场景 | 示例 |
| --- | --- | --- | --- |
| 阿里云内网 | 阿里云内网为千兆共享网络，日志数据通过阿里云内网传输比公网传输更快速、稳定，内网包括 VPC 和经典网络。 | ECS 实例和日志服务 Project 属于同一地域。 说明 推荐在 ECS 实例所在地域创建日志服务 Project，日志服务通过阿里云内网采集 ECS 实例的日志，不消耗公网带宽。 | ECS 实例和 Project 属于同一地域 Project：华东 1（杭州） ECS 实例：华东 1（杭州） |
| 公网 | 使用公网传输日志数据，不仅会受到网络带宽的限制，还可能会因网络抖动、延迟、丢包等影响数据采集的速度和稳定性。 | 以下两种情况，可以选择公网传输数据。 ECS 实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 | ECS 实例和 Project 属于不同地域 Project：华东 1（杭州） ECS 实例：华东 2（上海） 自建 IDC Project：华东 5（深圳） 自建 IDC：国内地域 |
| 传输加速 | 利用阿里云 CDN 边缘节点进行日志采集加速，相对公网采集在网络延迟、稳定性上具有很大优势。 | 如果业务服务器、日志服务 Project 分别属于国内地域和国外地域，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，您可以选择传输加速传输数据。更多信息，请参见 [传输加速](products/sls/documents/select-a-network-type.md) 。 | 自建 IDC Project：中国（香港） 自建 IDC：国外地域 说明 如果日志服务 Project 在国内地域，服务器在国外，建议使用传输加速采集服务器日志，相比公网传输的网络稳定性更高、性能更好。 |


### 传输加速

若您选择网络类型为传输加速，需要先为Project开启此项功能。

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)。进入Project的项目概览页面，按下图指示开启传输加速域名。

- 

阅读对话框的提示，然后单击确认修改。

- 

您可以通过如下方式配置Logtail采集加速。

### 采用传输加速方式安装Logtail

如果开启传输加速后再安装Logtail，则您可以选择传输加速方式安装Logtail。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail](products/sls/documents/install-logtail-on-a-linux-server.md)。

### 修改Logtail配置

如果开启传输加速前已安装Logtail，则需要修改Logtail配置。

- 

停止Logtail。

- 

Linux系统

执行sudo /etc/init.d/ilogtaild stop命令。

- 

Windows系统

- 

选择开始>控制面板>管理工具>服务。

- 

在服务对话框中，找到LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），右键单击停止。

- 

修改Logtail启动配置文件ilogtail_config.json。

将data_server_list参数中的endpoint一行替换为log-global.aliyuncs.com。文件路径，请参见[启动参数配置文件（ilogtail_config.json）](products/sls/documents/select-a-network-type.md)。

- 

启动Logtail。

- 

Linux系统

执行sudo /etc/init.d/ilogtaild start命令。

- 

Windows系统

- 

选择开始>控制面板>管理工具>服务。

- 

在服务对话框中，找到LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），右键单击启动。

更多相关操作可参考[管理传输加速](products/sls/documents/transmission-acceleration.md)。

## 设置Logtail启动参数

为防止Logtail消耗过多服务器资源，影响其他服务运行，日志服务对Logtail采集性能做了限制。当您需要提升Logtail采集性能时，可修改Logtail启动参数。

### 使用场景

遇到以下场景时，可修改Logtail启动参数。

- 

需要采集的日志文件数目大（同时采集的文件数超过100个或所监控的目录下的文件数超过5000个），占用大量内存。

- 

日志数据流量大（例如极简模式下超过2 MB/s，正则模式下超过1 MB/s），导致CPU占用率高。

- 

Logtail发送数据到日志服务的速率超过10 MB/s。

### 推荐参数值示例

根据实际经验推荐如下参数配置，适用于普通JSON文件的采集场景。完整正则模式和分隔符模式的性能与JSON模式相近，极简模式性能为JSON模式的5倍。由于数据、规则的复杂度、采集目录和文件的数量都会对CPU和MEM消耗带来影响，请参照下述表格并结合实际情况按需调整。

- 

主机环境

| 参数 | 默认的采集速率 | 采集速率大于 10 MB/s | 采集速率大于 20 MB/s | 采集速率大于 40 MB/s |
| --- | --- | --- | --- | --- |
| cpu_usage_limit | 0.4 | 1 | 2 | 4 |
| mem_usage_limit | 384 | 1024 | 2048 | 4096 |
| max_bytes_per_sec | 20971520 | 209715200 | 209715200 | 209715200 |
| process_thread_count | 1 | 2 | 4 | 8 |
| send_request_concurrency | 15 | 20 | 40 | 80 |


- 

容器或Kubernetes环境

| 环境变量 | 默认的采集速率 | 采集速率大于 10 MB/s | 采集速率大于 20 MB/s | 采集速率大于 40 MB/s |
| --- | --- | --- | --- | --- |
| cpu_usage_limit | 2 | 3 | 5 | 9 |
| mem_usage_limit | 2048 | 2048 | 2048 | 4096 |
| max_bytes_per_sec | 209715200 | 209715200 | 209715200 | 209715200 |
| process_thread_count | 1 | 2 | 4 | 8 |
| send_request_concurrency | 15 | 20 | 40 | 80 |
| resources.limits.cpu | 500M | 1000M | 2000M | 4000M |
| resources.limits.memory | 2 Gi | 2 Gi | 3 Gi | 5 Gi |


容器或Kubernetes环境中的Logtail启动参数修改说明如下：

- 

如果Logtail部署在阿里云Kubernetes集群中，且为Logtail-ds 1.7.3及以上版本，则推荐通过[容器服务管理控制台](https://cs.console.aliyun.com)修改，即在组件管理页面，修改logtail-ds组件中对应的各个参数。

- 

如果Logtail部署在自建容器或Kubernetes环境中，且为Logtail-ds 1.7.3及以上版本，则需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration。

- 

如果Logtail为Logtail-ds 1.7.3之前版本，则需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration。同时还需调整daemonset>kube-system>logtail-ds中的resources.limits.cpu和resources.limits.memory，避免Container资源超限。

按照上述表格中的采集速率大于40 MB/s列配置Logtail启动参数时，Logtail的采集性能接近极限，继续增加线程对性能提升效果不显著。采集端的性能极限说明如下表所示。

说明

因测试环境与生产环境不同，实际采集性能可能存在差异。

| 采集模式 | 性能极限 |
| --- | --- |
| 极简模式 | 440 MB/s |
| 完整正则模式 | 70 MB/s |
| 分隔符模式 | 75 MB/s |
| JSON 模式 | 75 MB/s |


### 启动参数设置

- 

在安装Logtail的服务器上，打开/usr/local/ilogtail/ilogtail_config.json文件。

此步骤适用于主机环境。

在容器或Kubernetes环境下，您需要通过修改daemonset环境变量来修改Logtail启动参数。部分环境引用configmap，configmap路径为configmap>kube-system>alibaba-log-configuration

- 

根据需求设置启动参数。

启动参数示例如下：

{ ... "cpu_usage_limit" : 0.4, "mem_usage_limit" : 384, "max_bytes_per_sec" : 20971520, "process_thread_count" : 1, "send_request_concurrency" : 15, "buffer_file_num" : 25, "buffer_file_size" : 20971520, "buffer_file_path" : "", ... }

说明

- 

下表中只列出您需要关注的常用启动参数，未列出的启动参数，保持默认配置即可。

- 

您可以根据需要新增或修改指定启动参数。

表 1. Logtail启动参数

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

- 

| 参数 | 类型 | 说明 | 示例 |
| --- | --- | --- | --- |
| cpu_usage_limit | double | CPU 使用阈值，以单核计算。取值如下： 取值范围：0.1~当前机器的 CPU 核心数 默认值：0.4 警告 cpu_usage_limit 为软限制，实际 Logtail 占用的 CPU 可能超过限制值，超限 5 分钟后将触发熔断保护，Logtail 自动重启。 例如设置为 0.4 ，表示日志服务将尽可能限制 Logtail 的 CPU 使用为 CPU 单核的 40%，超出后 Logtail 自动重启。 一般情况下，通过极简模式采集日志时，单核处理能力约 100 MB/s；通过完整正则模式采集日志时，单核处理能力约 20 MB/s 。 说明 如果 Logtail 部署在阿里云 Kubernetes 集群中，且为 Logtail-ds 1.7.3 及以上版本，则推荐通过 [容器服务管理控制台](https://cs.console.aliyun.com) 设置 CPU 使用阈值，即在 组件管理 页面，修改 logtail-ds 组件中的 LogtailDSLimitCPU 参数。具体操作，请参见 [管理组件](products/ack/documents/manage-system-components.md) 。 | "cpu_usage_limit" : 0.4 |
| mem_usage_limit | int | 内存使用阈值。取值如下： 取值范围：128 MB ~ 8192 MB 默认值：384 MB（主机），2048 MB（ACK 组件） 警告 mem_usage_limit 为软限制，实际 Logtail 占用的内存可能超过限制值，超限 5 分钟后将触发熔断保护，Logtail 自动重启。 采集速率、监控目录和文件数量、发送阻塞程度与 mem_usage_limit 参数有关。更多信息，请参见 [Logtail](products/sls/documents/logtail-limits.md) [限制说明](products/sls/documents/logtail-limits.md) 。 说明 如果 Logtail 部署在阿里云 Kubernetes 集群中，且为 Logtail-ds 1.7.3 及以上版本，则推荐通过 [容器服务管理控制台](https://cs.console.aliyun.com) 设置内存使用阈值，即在 组件管理 页面，修改 logtail-ds 组件中的 LogtailDSLimitMemory 参数。具体操作，请参见 [管理组件](products/ack/documents/manage-system-components.md) 。 | "mem_usage_limit" : 384 |
| max_bytes_per_sec | int | 每秒钟 Logtail 发送原始数据的流量限制。取值如下： 取值范围：1024 Byte/s ~ 52428800 Byte/s 默认值：20971520 Byte/s 重要 设置的值超过 20971520 Byte/s（20MB/s），表示不限速。 例如设置为 2097152 ，表示 Logtail 发送数据的速率为 2 MB/s。 说明 如果 Logtail 部署在阿里云 Kubernetes 集群中，且为 Logtail-ds 1.7.3 及以上版本，则推荐通过 [容器服务管理控制台](https://cs.console.aliyun.com) 设置流量限制，即在 组件管理 页面，修改 logtail-ds 组件中的 LogtailDSMaxBytePerSec 参数。具体操作，请参见 [管理组件](products/ack/documents/manage-system-components.md) 。 | "max_bytes_per_sec" : 2097152 |
| process_thread_count | int | Logtail 处理数据的线程数。 取值如下： 取值范围：1~64 默认值：1 一般情况下，可以处理极简模式下 24 MB/s 的数据写入或完整正则模式 12 MB/s 的数据写入。默认情况下无需调整该参数取值。 说明 如果 Logtail 部署在阿里云 Kubernetes 集群中，且为 Logtail-ds 1.7.3 及以上版本，则推荐通过 [容器服务管理控制台](https://cs.console.aliyun.com) 设置线程路，即在 组件管理 页面，修改 logtail-ds 组件中的 LogtailDSProcessThreadCount 参数。具体操作，请参见 [管理组件](products/ack/documents/manage-system-components.md) 。 | "process_thread_count" : 1 |
| send_request_concurrency | int | 异步并发的个数。取值如下： 取值范围：15~80 默认值：15 如果写入 TPS 很高，可以设置更高的异步并发个数。可以按照一个并发支持 0.5 MB/s~1 MB/s 网络吞吐来计算，实际根据网络延时而定。 说明 设置异步并发个数过高容易导致网络端口占用过多，需调整 TCP 相关参数。 更多信息，请参见 [调整](https://yq.aliyun.com/articles/52884) [TCP](https://yq.aliyun.com/articles/52884) [相关参数](https://yq.aliyun.com/articles/52884) 。 如果 Logtail 部署在阿里云 Kubernetes 集群中，且为 Logtail-ds 1.7.3 及以上版本，则推荐通过 [容器服务管理控制台](https://cs.console.aliyun.com) 设置异步并发个数，即在 组件管理 页面，修改 logtail-ds 组件中的 LogtailDSSendRequestConcurrency 参数。具体操作，请参见 [管理组件](products/ack/documents/manage-system-components.md) 。 | "send_request_concurrency" : 4 |
| buffer_file_num | int | 限制缓存文件的最大数目。取值如下： 取值范围：1~100 默认值：25 遇到网络异常、写入配额超限等情况时，Logtail 将实时解析后的日志写入本地文件（安装目录下）缓存起来，等待恢复后尝试重新发送。 | "buffer_file_num" : 25 |
| buffer_file_size | int | 单个缓存文件允许的最大字节数。取值如下： 取值范围：1048576 Byte ~ 104857600 Byte 默认值：20971520 Byte buffer_file_size * buffer_file_num 是缓存文件可以实际使用的最大磁盘空间。 | "buffer_file_size" : 20971520 |
| buffer_file_path | String | 缓存文件存放目录。 默认值为空，即缓存文件存放于 logtail 安装目录 /usr/local/ilogtail 下。 当您设置此参数后，需手动将原目录下名为 logtail\_buffer\_file_* 的文件移动到此目录，以保证 Logtail 可以读取到该缓存文件并在发送后进行删除。 | "buffer_file_path" : "" |
| bind_interface | String | 本机绑定的网卡名。默认值为空，自动绑定可用的网卡。 如果设置为指定的网卡（例如 eth1），则表示 Logtail 将强制使用该网卡上传日志。 只支持 Linux 版本。 | "bind_interface" : "" |
| check_point_filename | String | Logtail 的 checkpoint 文件的保存路径， 默认值： /tmp/logtail_check_point 。 建议 Docker/Kubernetes 用户参见 [iLogtail](https://developer.aliyun.com/article/901257) [容器重启数据可靠性探讨](https://developer.aliyun.com/article/901257) 进行配置，避免 Logtail 容器重启时丢失 checkpoint 信息等而造成采集重复或丢失。 | "check_point_filename" : /tmp/logtail_check_point |
| check_point_dump_interval | int | Logtail 更新 Checkpoint 文件的周期，默认值：900，单位：秒。即默认情况下每 15 分钟更新一次 Checkpoint 文件。 仅 Linux Logtail 1.0.19 及以上版本或 Windows Logtail 1.0.19.0 及以上版本支持该参数。 | "check_point_dump_interval" : 900 |
| user_config_file_path | String | Logtail 配置文件的保存路径，默认为进程 binary 所在目录，文件名为 user_log_config.json 。 建议 Docker/Kubernetes 用户参见 [iLogtail](https://developer.aliyun.com/article/901257) [容器重启数据可靠性探讨](https://developer.aliyun.com/article/901257) 进行配置，避免 Logtail 容器重启导致采集重复或丢失。 | "user_config_file_path" : user_log_config.json |
| docker_file_cache_path | String | 该文件记录了容器文件到宿主机文件的路径映射，默认为 /usr/local/ilogtail/docker_path_config.json 。 建议 Docker/Kubernetes 用户参见 [iLogtail](https://developer.aliyun.com/article/901257) [容器重启数据可靠性探讨](https://developer.aliyun.com/article/901257) 进行配置，避免 Logtail 容器重启导致采集重复或丢失。 仅 Linux Logtail 0.16.54 及以上版本或 Windows Logtail 0.16.54.0 及以上版本支持该参数。 | "docker_file_cache_path": /usr/local/ilogtail/docker_path_config.json |
| discard_old_data | Boolean | 是否丢弃历史日志。默认值：true，表示丢弃距离当前时间超过 12 小时的日志。 | "discard_old_data" : true |
| ilogtail_discard_interval | int | 丢弃历史日志距离当前时间的阈值。默认值：43200（12 小时），单位：秒。 | "ilogtail_discard_interval": 43200 |
| working_ip | String | 默认值为空，表示自动从本服务器获取 IP 地址。修改后 Logtail 将以该值作为服务器的 IP 地址上报。 | "working_ip" : "" |
| working_hostname | String | Logtail 上报的本服务器的主机名。默认值为空，表示自动从本服务器获取主机名。 | "working_hostname" : "" |
| max_read_buffer_size | long | 每条日志读取的最大值。默认值：524288（512 KB），最大值：8388608（8 MB）。单位：Byte。 如果您的单条日志超过 524288 Byte，可修改此参数。 | "max_read_buffer_size" : 524288 |
| oas_connect_timeout | long | Logtail 发起获取 Logtail 配置、访问密钥等请求时，连接阶段的超时时间。默认值：5，单位：秒。 网络条件较差，建立连接时间过长时可修改此参数。 | "oas_connect_timeout" : 5 |
| oas_request_timeout | long | Logtail 发起获取 Logtail 配置、访问密钥等请求时，整个请求阶段的超时时间。默认值：10，单位：秒。 网络条件较差，建立连接时间过长时可修改此参数。 | "" : 10 |
| data_server_port | long | 设置 data_server_port 为 443 后，Logtail 将通过 HTTPS 协议传输数据到日志服务。 仅 Linux Logtail 1.0.10 及以上版本或 Windows Logtail 1.0.10.0 及以上版本支持该参数。 | "data_server_port": 443 |
| enable_log_time_auto_adjust | Boolean | 设置 enable_log_time_auto_adjust 为 true 后，日志时间可自适应服务器本地时间。 出于数据安全考虑，日志服务会对请求（包括 Logtail 发起的请求）所携带的时间进行校验，拒绝与日志服务端时间相差超过 15 分钟的请求。Logtail 发起请求时所携带的时间为服务器本地时间，当服务器本地时间被修改后（例如某些测试场景下需要调整本地时间为未来时间），Logtail 请求将被拒绝，导致写入数据失败。您可以使用该参数实现日志时间自适应服务器本地时间。 仅 Linux Logtail 1.0.19 及以上版本或 Windows Logtail 1.0.19.0 及以上版本支持该参数。 重要 开启该功能后，日志时间将被加上日志服务端的时间与服务器本地时间的偏移量。由于偏移量只在请求被日志服务端拒绝时更新，因此可能出现日志服务端所查询到的日志的时间和日志实际的写入时间不一致的情况。 Logtail 的部分逻辑依赖于系统时间的递增，建议在每次机器时间调整后重启 Logtail。 | "enable_log_time_auto_adjust": true |
| accept_multi_config | Boolean | 是否允许多个 Logtail 配置采集同一个文件。默认值：false，表示不允许。 默认情况下，一个文件只能被一个 Logtail 配置采集，您可以通过该参数消除限制。每个 Logtail 配置的处理过程是独立的，当允许多个 Logtail 配置采集同一个文件时，需要消耗多倍的 CPU、内存开销。 仅 Linux Logtail 0.16.26 及以上版本或 Windows Logtail 0.16.26.0 及以上版本支持该参数。 | "accept_multi_config": true |
| enable_checkpoint_sync_write | Boolean | 是否开启 sync 写功能。默认值：false，表示不开启。 sync 写功能主要用于搭配 ExactlyOnce 写入功能。开启 ExactlyOnce 写入功能后，Logtail 会在本地磁盘记录细粒度的 Checkpoint 信息（文件级别）。但出于性能考虑，默认写入 Checkpoint 时不会调用 sync 落盘，所以如果机器重启导致 buffer 数据来不及写入磁盘时，可能导致 Checkpoint 丢失。此时，您可以设置 enable_checkpoint_sync_write 为 true ，开启 sync 写功能。更多信息，请参见 [Logtail](products/sls/documents/developer-reference/logtail-configurations.md) [配置（旧版）](products/sls/documents/developer-reference/logtail-configurations.md) 。 仅 Linux Logtail 1.0.20 及以上版本或 Windows Logtail 1.0.20.0 及以上版本支持该参数。 | "enable_checkpoint_sync_write": false |
| enable_env_ref_in_config | Boolean | 是否启用采集配置环境变量替换功能。默认值：false。 开启该功能后，您可以在控制台的 Logtail 采集配置中使用 ${xxx} 作为环境变量 xxx 的占位符。例如设置采集路径为 /${xxx}/logs ，环境变量为 xxx=user ，则生效的采集路径为 /user/logs 。 如果配置中需要使用 ${ 、 } ，则您可以使用 $${ 、 $} 进行转义。 仅 Linux Logtail 1.0.31 及以上版本或 Windows Logtail 1.0.31.0 及以上版本支持该参数。 | "enable_env_ref_in_config": false |
| docker_config_update_interval | int | 容器路径更新的最小时间间隔。 与 max_docker_config_update_times 配合使用，任意一个参数达到阈值则不再更新容器路径。 如果是 Linux Logtail 1.0.32 及以上版本或 Windows Logtail 1.0.32.0 及以上版本，默认值：3，单位：秒。 如果是 Linux Logtail 1.0.32 之前版本或 Windows Logtail 1.0.32.0 之前版本，默认值：10，单位：秒。 | "docker_config_update_interval": 3 |
| max_docker_config_update_times | int | 3 分钟内更新容器路径最大次数。默认情况下，3 分钟内容器路径更新次数超过 3 次则不再更新容器路径。 如果是 Linux Logtail 1.0.32 及以上版本或 Windows Logtail 1.0.32.0 及以上版本，默认值：10。 如果是 Linux Logtail 1.0.32 之前版本或 Windows Logtail 1.0.32.0 之前版本，默认值：3。 | "max_docker_config_update_times": 10 |
| DOCKER_HOST | String | 与 Docker 通信的 Socket 地址，需通过环境变量进行配置。 默认值：空，表示使用默认地址 unix:///var/run/docker.sock。 | DOCKER_HOST=unix:///var/run/docker.sock |
| CONTAINERD_SOCK_PATH | String | 与 Containerd 通信的 Socket 地址，需通过环境变量进行配置。 默认值：空，表示使用默认地址 unix:///run/containerd/containerd.sock。如果是 K3s 集群，可按照示例修改。 | CONTAINERD_SOCK_PATH=/run/k3s/containerd/containerd.sock |
| logreader_max_rotate_queue_size | Int | 轮转队列最大长度。默认值：20。当日志采集发生阻塞或延时时，待采集的文件会持有文件句柄在队列中等待。 当采集延时时，如果需要控制磁盘最大用量，可考虑减小该值。 警告 当延时的文件数超过该值时，Logtail 将直接跳过新文件的采集。 | "logreader_max_rotate_queue_size" : 10 |
| force_release_deleted_file_fd_timeout | Int | 容器退出或者文件删除将在一定时间内释放句柄，您可以指定对应的时间。默认值：-1，表示关闭功能。值为 0 时，表示立刻释放。单位：秒。 如果您要控制 containerd 容器的最大销毁延时，可考虑将值设置该参数。 警告 当采集发生延时时，延时超过配置的数据会丢失。 | "force_release_deleted_file_fd_timeout" : 0 |
| data_endpoint_policy | string | Logtail 对日志服务访问域名的切换策略。可选值如下： 说明 您可以在 ilogtail_config.json 文件的 data_server_list 参数中，查看是否已配置默认域名。更多信息，请参见 [启动参数配置文件（ilogtail_config.json）](products/sls/documents/select-a-network-type.md) 。 designated_first（默认） 如果已指定某个地域的默认域名且默认域名可用，则系统优先使用默认域名。 如果已指定某个地域的默认域名但默认域名不可用，则系统会自动选择一个可用域名。 如果未指定某个地域的默认域名，则系统会自动选择一个可用域名。 designated_locked 如果已指定某个地域的默认域名，不管其是否可用，系统都将只使用默认域名。 如果未指定某个地域的默认域名，系统会自动选择一个可用域名。 仅 Linux Logtail 1.5.0 及以上版本或 Windows Logtail 1.5.0.0 及以上版本支持该参数。 | "data_endpoint_policy" : "designated_first" |
| inotify_black_list | Array<String> | inotify 监听黑名单，黑名单为完全匹配，此列表中的目录不会启用 inotify 监听。 | "inotify_black_list": ["/tmp"] |
| host_path_blacklist | String | 全局主机路径黑名单，黑名单为子串匹配。 Linux 系统下多个子串以半角冒号（:）分隔。 Windows 系统下多个子串以半角分号（;）分隔。 例如 "host_path_blacklist" : "/volumes/kubernetes.io~csi/nas-" 表示禁止采集 NAS 挂载数据。 仅 Linux Logtail 1.8.0 及以上版本或 Windows Logtail 1.8.0.0 及以上版本支持该参数。 | "host_path_blacklist" : "/volumes/kubernetes.io~csi/nas-" |
| LOGTAIL_LOG_LEVEL | String | 日志打印级别，需通过环境变量进行配置。默认值：空，表示 info，可选值 trace、debug、info、warning、error 和 fatal。 仅 Linux Logtail 1.8.0 及以上版本或 Windows Logtail 1.8.0.0 及以上版本支持该参数。 | LOGTAIL_LOG_LEVEL=info |
| FORCE_RELEASE_STOP_CONTAINER_FILE | Boolean | 配置方式：仅支持通过环境变量方式进行配置。 功能描述：当该参数设置为 true 时，Logtail 会在业务容器退出时立即释放容器文件句柄。此操作可防止因文件句柄未释放而导致容器无法正常退出。 注意事项： 此时无法保证容器内数据采集的完整性。 建议在业务退出前增加几秒的延迟，以确保日志能够完整采集。 支持版本： Linux Logtail 2.1.6 及以上版本 | " FORCE_RELEASE_STOP_CONTAINER_FILE " : "true" |
| default_reader_flush_timeout | int | 最后一行日志完整性判定超时，默认值：60，单位：秒。 仅 Logtail 2.0.0 及以上版本支持该参数。 | " default_reader_flush_timeout " : 1 |


- 

重启Logtail使配置生效。

/etc/init.d/ilogtaild stop && /etc/init.d/ilogtaild start

重启后，您可以执行/etc/init.d/ilogtaild status命令检查Logtail状态。

### 附录：环境变量说明

环境变量与Logtail启动参数的对应关系如下。

表 2. 环境变量与Logtail启动参数对应关系

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

| 参数 | 环境变量 | 优先级 | 支持版本 |
| --- | --- | --- | --- |
| cpu_usage_limit | cpu_usage_limit | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.32 及以上版本 Windows Logtail 0.16.32.0 及以上版本 |
| mem_usage_limit | mem_usage_limit | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.32 及以上版本 Windows Logtail 0.16.32.0 及以上版本 |
| max_bytes_per_sec | max_bytes_per_sec | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.32 及以上版本 Windows Logtail 0.16.32.0 及以上版本 |
| process_thread_count | process_thread_count | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.32 及以上版本 Windows Logtail 0.16.32.0 及以上版本 |
| send_request_concurrency | send_request_concurrency | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.32 及以上版本 Windows Logtail 0.16.32.0 及以上版本 |
| check_point_filename | check_point_filename 或 ALIYUN_LOGTAIL_CHECK_POINT_PATH | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 0.16.36 及以上版本 Windows Logtail 0.16.36.0 及以上版本 |
| docker_file_cache_path | docker_file_cache_path | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.54 及以上版本 Windows Logtail 0.16.54.0 及以上版本 |
| user_config_file_path | user_config_file_path | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| discard_old_data | discard_old_data | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| working_ip | working_ip 或 ALIYUN_LOGTAIL_WORKING_IP | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| working_hostname | working_hostname 或 ALIYUN_LOGTAIL_WORKING_HOSTNAME | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| max_read_buffer_size | max_read_buffer_size | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| oas_connect_timeout | oas_connect_timeout | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| oas_request_timeout | oas_request_timeout | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.56 及以上版本 Windows Logtail 0.16.56.0 及以上版本 |
| data_server_port | data_server_port | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.10 及以上版本 Windows Logtail 1.0.10.0 及以上版本 |
| accept_multi_config | accept_multi_config | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.26 及以上版本 Windows Logtail 0.16.26.0 及以上版本 |
| enable_log_time_auto_adjust | enable_log_time_auto_adjust | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.19 及以上版本 Windows Logtail 1.0.19.0 及以上版本 |
| check_point_dump_interval | check_point_dump_interval | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.19 及以上版本 Windows Logtail 1.0.19.0 及以上版本 |
| enable_checkpoint_sync_write | enable_checkpoint_sync_write | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.20 及以上版本 Windows Logtail 1.0.20.0 及以上版本 |
| docker_config_update_interval | docker_config_update_interval 或 ALIYUN_LOGTAIL_DOCKER_CONFIG_UPDATE_INTERVAL | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.29 及以上版本 Windows Logtail 1.0.29.0 及以上版本 |
| max_docker_config_update_times | max_docker_config_update_times 或 ALIYUN_LOGTAIL_MAX_DOCKER_CONFIG_UPDATE_TIMES | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 1.0.29 及以上版本 Windows Logtail 1.0.29.0 及以上版本 |
| logreader_max_rotate_queue_size | logreader_max_rotate_queue_size | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以配置文件为准。 | Linux Logtail 0.16.54 及以上版本 Windows Logtail 0.16.54.0 及以上版本 |
| force_release_deleted_file_fd_timeout | force_release_deleted_file_fd_timeout | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 1.21.1 及以上版本 Windows Logtail 1.21.1.0 及以上版本 |
| host_path_blacklist | host_path_blacklist | 如果您通过环境变量和配置文件修改了 Logtail 启动参数，以环境变量为准。 | Linux Logtail 1.8.0 及以上版本 Windows Logtail 1.8.0.0 及以上版本 |
| 不支持 | FORCE_RELEASE_STOP_CONTAINER_FILE | 该参数只支持通过环境变量修改。 | Linux Logtail 2.1.6 及以上版本 |


## Logtail配置文件与记录文件

Logtail运行时依赖一系列的配置文件并产生部分信息记录文件，下面将介绍常见文件的基本信息及路径。

### 启动参数配置文件（ilogtail_config.json）

ilogtail_config.json文件用于配置Logtail的启动参数，文件类型为JSON。更多信息，请参见[设置](products/sls/documents/select-a-network-type.md)[Logtail](products/sls/documents/select-a-network-type.md)[启动参数](products/sls/documents/select-a-network-type.md)。

重要

- 

该文件必须为合法JSON，否则无法启动Logtail。

- 

修改该文件后，必须重启Logtail才能生效。具体操作，请参见[启动和停止](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)[Logtail](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)。

- 

Logtail默认使用HTTP协议和服务端进行管控面和数据面的通信，使用HTTPS协议和服务端进行鉴权。

- 

如果出于安全考虑，需要使用HTTPS协议和服务端进行通信，则可以分别将config_server_address和data_server_list.endpoint显式指定为https。

- 

如果使用HTTPS协议传输数据，会增加传输延时，非关键场景不建议使用。

安装Logtail后，您可以在ilogtail_config.json文件进行如下操作。

- 

修改Logtail的运行参数。

- 

检验安装命令是否正确。

ilogtail_config.json文件中的config_server_address参数和data_server_list参数的值取决于安装时选择的安装命令，如果其中的地域和日志服务所在地域不一致或地址无法联通，说明安装时选择了错误的命令。这时Logtail无法正常采集日志，需重新安装。

- 

文件路径

- 

主机环境

| 操作系统 | Logtail | ilogtail_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |


- 

容器环境

ilogtail_config.json文件存储在Logtail容器中，文件路径配置在Logtail容器的环境变量ALIYUN_LOGTAIL_CONFIG中，您可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_CONFIG命令查看。例如：/etc/ilogtail/conf/cn-hangzhou/ilogtail_config.json。

- 

文件示例

$cat /usr/local/ilogtail/ilogtail_config.json { "config_server_address" : "http://logtail.cn-hangzhou-intranet.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "cn-hangzhou", "endpoint" : "cn-hangzhou-intranet.log.aliyuncs.com" } ], "cpu_usage_limit" : 0.4, "mem_usage_limit" : 100, "max_bytes_per_sec" : 2097152, "process_thread_count" : 1, "send_request_concurrency" : 15, "streamlog_open" : false }

### 用户标识配置文件

用户标识配置文件中包含阿里云主账号的ID信息，用于标识这台服务器有权限被该账号访问、采集日志。更多信息，请参见[配置用户标识](products/sls/documents/machine-group-overview.md)。

重要

- 

在采集非本账号ECS、自建IDC、其他云厂商服务器日志时需要配置用户标识。

- 

用户标识配置文件中必须配置阿里云账号（主账号）ID，不支持RAM用户。

- 

用户标识配置文件只需配置文件名，无需配置文件后缀。

- 

一台服务器上可配置多个用户标识，Logtail容器中仅支持配置一个用户标识。

- 

文件路径

- 

主机环境

- 

Linux：/etc/ilogtail/users/。

- 

Windows：C:\LogtailData\users\。

- 

容器环境

用户标识保存在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_ID中，您可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_ID命令查看。

- 

文件示例

$ls /etc/ilogtail/users/

### 用户自定义标识文件（user_defined_id）

user_defined_id文件用于配置用户自定义标识。更多信息，请参见[创建用户自定义标识机器组](products/sls/documents/machine-group-overview.md)。

重要

创建自定义标识机器组时需要配置user_defined_id文件。

- 

文件路径

- 

主机环境

- 

Linux：/etc/ilogtail/user_defined_id。

- 

Windows：C:\LogtailData\user_defined_id。

- 

容器环境

用户自定义标识配置在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID中，可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID命令查看。

- 

文件示例

$cat /etc/ilogtail/user_defined_id aliyun-ecs-rs1e16355

### Logtail采集配置文件（user_log_config.json）

user_log_config.json文件记录Logtail从日志服务获取的Logtail采集配置信息，文件类型为JSON，每次Logtail采集配置更新时会同步更新该文件。可通过user_log_config.json文件确认Logtail采集配置是否已经下发到服务器。Logtail采集配置文件存在，且内容与日志服务上的Logtail采集配置一致，表示Logtail采集配置已下发。

重要

除手动配置AccessKey信息、数据库密码等敏感信息外，不建议修改该文件。

- 

文件路径

- 

主机环境

| 操作系统 | Logtail | user_log_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/user_log_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\user_log_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\user_log_config.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\user_log_config.json |


- 

容器环境

user_log_config.json文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/user_log_config.json。

- 

文件示例

$cat /usr/local/ilogtail/user_log_config.json { "metrics" : { "##1.0##k8s-log-c12ba2028*****939f0b$app-java" : { "aliuid" : "16542189*****50", "category" : "app-java", "create_time" : 1534739165, "defaultEndpoint" : "cn-hangzhou-intranet.log.aliyuncs.com", "delay_alarm_bytes" : 0, "enable" : true, "enable_tag" : true, "filter_keys" : [], "filter_regs" : [], "group_topic" : "", "local_storage" : true, "log_type" : "plugin", "log_tz" : "", "max_send_rate" : -1, "merge_type" : "topic", "plugin" : { "inputs" : [ { "detail" : { "IncludeEnv" : { "aliyun_logs_app-java" : "stdout" }, "IncludeLable" : { "io.kubernetes.container.name" : "java-log-demo-2", "io.kubernetes.pod.namespace" : "default" }, "Stderr" : true, "Stdout" : true }, "type" : "service_docker_stdout" } ] }, "priority" : 0, "project_name" : "k8s-log-c12ba2028c*****ac1286939f0b", "raw_log" : false, "region" : "cn-hangzhou", "send_rate_expire" : 0, "sensitive_keys" : [], "tz_adjust" : false, "version" : 1 } } }

### AppInfo记录文件（app_info.json）

app_info.json文件记录Logtail的启动时间、获取到的IP地址、主机名等信息。

如果已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。如果没有设置主机名绑定，会自动获取本机的第一块网卡的IP地址。

重要

- 

AppInfo记录文件仅用于记录Logtail内部信息。修改该文件不会改变Logtail获取的IP地址。

- 

如果修改了服务器的主机名等网络配置，请重启Logtail，获取新的IP地址。

- 

文件路径

- 

主机环境

| 操作系统 | Logtail | app_info.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/app_info.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\app_info.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |


- 

容器环境

app_info.json文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/app_info.json。

- 

文件示例

$cat /usr/local/ilogtail/app_info.json { "UUID" : "", "hostname" : "logtail-ds-slpn8", "instance_id" : "E5F93BC6-B024-11E8-8831-0A58AC14039E_1**.***.***.***_1536053315", "ip" : "1**.***.***.***", "logtail_version" : "0.16.13", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2018-09-04 09:28:36" }

| 字段 | 说明 |
| --- | --- |
| UUID | 服务器序列号。 |
| hostname | 主机名。 |
| instance_id | 随机生成的 Logtail 唯一标识。 |
| ip | Logtail 获取到的 IP 地址。该字段为空时表示 Logtail 没有获取到 IP 地址，Logtail 无法正常运行，请为服务器设置 IP 地址并重启 Logtail。 说明 如果您创建了 IP 地址机器组，请确保机器组中配置的 IP 与此处显示的 IP 地址一致。若不一致，请确认主机 IP 的正确值，选择在 日志服务 控制台上修改机器组内 IP 地址，或者在 [设置](products/sls/documents/select-a-network-type.md) [Logtail](products/sls/documents/select-a-network-type.md) [启动参数](products/sls/documents/select-a-network-type.md) 中修改参数 working_ip 的值。 |
| logtail_version | Logtail 客户端版本。 |
| os | 操作系统版本。 |
| update_time | Logtail 最近一次启动时间。 |


### Logtail运行日志（ilogtail.LOG）

ilogtail.LOG文件记录了Logtail的运行日志，日志级别从低到高分别为INFO、WARN和ERROR，其中INFO类型的日志无需关注。

如果采集异常，请先诊断采集错误，根据具体的错误类型和Logtail运行日志排查问题。更多信息，请参见[如何查看](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](products/sls/documents/user-guide/how-do-i-view-logtail-collection-errors.md)。

说明

如果因Logtail采集异常提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请同时上传该日志。

- 

文件路径

- 

主机环境

| 操作系统 | Logtail | ilogtail.LOG 件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail.LOG |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail.LOG |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail.LOG 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail.LOG |


- 

容器环境：

ilogtail.LOG文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/ilogtail.LOG。

- 

文件示例

$tail /usr/local/ilogtail/ilogtail.LOG [2018-09-13 01:13:59.024679] [INFO] [3155] [build/release64/sls/ilogtail/elogtail.cpp:123] change working dir:/usr/local/ilogtail/ [2018-09-13 01:13:59.025443] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:175] load logtail config file, path:/etc/ilogtail/conf/ap-southeast-1/ilogtail_config.json [2018-09-13 01:13:59.025460] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:176] load logtail config file, detail:{ "config_server_address" : "http://logtail.ap-southeast-1-intranet.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "ap-southeast-1", "endpoint" : "ap-southeast-1-intranet.log.aliyuncs.com" } ]

### Logtail插件日志（logtail_plugin.LOG）

logtail_plugin.LOG文件记录Logtail插件的运行日志，日志级别从低到高分别为INFO、WARN和ERROR，其中INFO类型的日志无需关注。

如果在诊断采集错误时，提示CANAL_RUNTIME_ALARM等错误，可以通过logtail_plugin.LOG文件排查。

说明

如果因插件异常提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请在工单中上传该文件。

- 

文件路径

- 

主机环境

| 操作系统 | Logtail | logtail_plugin.LOG 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/logtail_plugin.LOG |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\logtail_plugin.LOG |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\logtail_plugin.LOG 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\logtail_plugin.LOG |


- 

容器环境

logtail_plugin.LOG文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/logtail_plugin.LOG。

- 

文件示例

$tail /usr/local/ilogtail/logtail_plugin.LOG 2018-09-13 02:55:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 02:55:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop 2018-09-13 03:00:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 03:00:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop 2018-09-13 03:03:26 [INF] [log_file_reader.go:221] [ReadOpen] [##1.0##sls-zc-test-hz-pub$docker-stdout-config,k8s-stdout] open file for read, file:/logtail_host/var/lib/docker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379573 status:794354-64769-40379963 2018-09-13 03:03:26 [INF] [log_file_reader.go:221] [ReadOpen] [##1.0##k8s-log-c12ba2028cfb444238cd9ac1286939f0b$docker-stdout-config,k8s-stdout] open file for read, file:/logtail_host/var/lib/docker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379573 status:794354-64769-40379963 2018-09-13 03:04:26 [INF] [log_file_reader.go:308] [CloseFile] [##1.0##sls-zc-test-hz-pub$docker-stdout-config,k8s-stdout] close file, reason:no read timeout file:/logtail_host/var/lib/docker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379963 status:794354-64769-40379963 2018-09-13 03:04:27 [INF] [log_file_reader.go:308] [CloseFile] [##1.0##k8s-log-c12ba2028cfb444238cd9ac1286939f0b$docker-stdout-config,k8s-stdout] close file, reason:no read timeout file:/logtail_host/var/lib/docker/containers/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624/7f46afec6a14de39b59ee9cdfbfa8a70c2fa26f1148b2e2f31bd3410f5b2d624-json.log offset:40379963 status:794354-64769-40379963 2018-09-13 03:05:30 [INF] [docker_center.go:525] [func1] docker fetch all:start 2018-09-13 03:05:30 [INF] [docker_center.go:529] [func1] docker fetch all:stop

### 容器路径映射文件（docker_path_config.json）

docker_path_config.json文件只有在采集容器日志时才会创建，用于记录容器文件和宿主机文件的路径映射关系。文件类型为JSON。

如果在诊断采集错误时，如果提示DOCKER_FILE_MAPPING_ALARM错误，表示添加Docker文件映射失败，可以通过docker_path_config.json文件排查。

说明

- 

docker_path_config.json文件为记录文件，任何修改操作均不会生效。删除后会自动创建，不影响业务的正常运行。

- 

因采集容器日志异常而提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请在工单中上传此文件。

- 

文件路径

/usr/local/ilogtail/docker_path_config.json

- 

文件示例

$cat /usr/local/ilogtail/docker_path_config.json { "detail" : [ { "config_name" : "##1.0##k8s-log-c12ba2028cfb444238cd9ac1286939f0b$nginx", "container_id" : "df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330d10", "params" : "{\n \"ID\" : \"df19c06e854a0725ea7fca7e0378b0450f7bd3122f94fe3e754d8483fd330d10\",\n \"Path\" : \"/logtail_host/var/lib/docker/overlay2/947db346695a1f65e63e582ecfd10ae1f57019a1b99260b6c83d00fcd1892874/diff/var/log\",\n \"Tags\" : [\n \"nginx-type\",\n \"access-log\",\n \"_image_name_\",\n \"registry.cn-hangzhou.aliyuncs.com/log-service/docker-log-test:latest\",\n \"_container_name_\",\n \"nginx-log-demo\",\n \"_pod_name_\",\n \"nginx-log-demo-h2lzc\",\n \"_namespace_\",\n \"default\",\n \"_pod_uid_\",\n \"87e56ac3-b65b-11e8-b172-00163f008685\",\n \"_container_ip_\",\n \"172.20.4.224\",\n \"purpose\",\n \"test\"\n ]\n}\n" } ], "version" : "0.1.0" }

[上一篇：安装、运行、升级、卸载Logtail](products/sls/documents/install-run-upgrade-and-uninstall-logtail.md)[下一篇：Logtail发布历史](products/sls/documents/sls-release-notes.md)

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
