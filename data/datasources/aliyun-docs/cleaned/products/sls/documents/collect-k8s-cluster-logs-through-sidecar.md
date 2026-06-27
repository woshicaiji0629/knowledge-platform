# 通过Sidecar方式采集集群日志（阿里云ACK集群和自建Kubernetes集群）-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/collect-k8s-cluster-logs-through-sidecar

# 采集Kubernetes Pod文本日志（Sidecar模式）
在 Kubernetes 环境中，当您需要对特定应用的日志进行精细化管理、实现多租户隔离或确保日志采集与应用生命周期严格绑定时，Sidecar 模式是理想的日志采集方案。该模式通过在业务 Pod 中注入一个独立的 LoongCollector（Logtail） 容器，实现对该 Pod 内日志的专属采集，提供了强大的灵活性和隔离性。
## 工作原理
Sidecar 模式的核心是在您的业务 Pod 内，并排运行一个业务容器和一个 LoongCollector（Logtail） 日志采集容器。它们通过共享卷和生命周期同步机制协同工作。
日志共享：业务容器将其产生的日志文件写入到一个共享卷（通常是emptyDir）。 LoongCollector（Logtail） 容器挂载同个共享卷，从而能实时读取并采集这些日志文件。
配置关联：每个 LoongCollector（Logtail）Sidecar 容器通过设置一个唯一的用户自定义标识来声明自己的身份。在日志服务控制台，您需要创建一个同样使用此标识的机器组。这样，所有使用相同标识的 Sidecar 实例都会自动应用到这个机器组上的采集配置。
生命周期同步：为确保在 Pod 终止时不丢失日志，业务容器和 LoongCollector（Logtail）容器通过共享卷中的信令文件（cornerstone和tombstone）进行通信，配合 Pod 的优雅终止宽限期（terminationGracePeriodSeconds），实现业务容器先停止写入、 LoongCollector（Logtail） 完成日志发送后再一同退出的优雅停机流程。
## 准备工作
在采集日志前，需规划并创建用于管理与存储日志的Project和LogStore。若已有可用资源，可跳过此步骤，直接进入[步骤一：注入](collect-k8s-cluster-logs-through-sidecar.md)[LoongCollector Sidecar](collect-k8s-cluster-logs-through-sidecar.md)[容器](collect-k8s-cluster-logs-through-sidecar.md)。
Project：日志服务的资源管理单元，用于隔离和管理不同项目或业务的日志。
LogStore：日志存储单元，用于存储日志。
创建Project
登录[日志服务控制台](https://sls.console.aliyun.com/)。
单击创建Project，并配置：
所属地域：根据日志来源选择，创建后不可修改。
Project名称：阿里云内全局唯一，创建后不可修改。
其他配置保持默认，单击创建。如需了解其他参数，请参见[创建](manage-a-project.md)[Project](manage-a-project.md)。
创建LogStore
单击Project名称，进入目标Project。
在左侧导航栏，选择日志存储，单击+。
在创建LogStore页面，完成以下核心配置：
Logstore名称：设置一个在Project内唯一的名称，该名称创建后不可修改。
Logstore类型：根据规格对比选择标准型或查询型。
计费模式：
按使用功能计费：按存储、索引、读写次数等各项资源独立计费。适合小规模或功能使用不确定的场景。
按写入数据量计费：仅按原始写入数据量计费，提供30天免费存储，以及免费的数据加工、投递等功能。适合存储周期接近30天或数据处理链路复杂的业务场景。
数据保存时间：设置日志的保留天数（1~3650天，3650为永久保存），默认为30天。
其他配置保持默认，单击确定。如需了解其他配置信息，请参考[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## 步骤一：注入LoongCollector Sidecar容器
在业务应用Pod中注入LoongCollector Sidecar容器，并配置共享卷以实现日志采集。若尚未部署业务应用，或仅用于测试，可直接使用[附录：YAML](collect-k8s-cluster-logs-through-sidecar.md)[示例](collect-k8s-cluster-logs-through-sidecar.md)快速验证流程。
### 1. 修改业务Pod YAML配置
定义共享卷
在spec.template.spec.volumes中添加三个共享卷（与containers同级）：
volumes: # 共享日志目录（业务容器写入，Sidecar 读取） - name: ${shared_volume_name} # <-- 名称需与volumeMounts中的name一致 emptyDir: {} # 容器间通信信令目录（用于优雅启停） - name: tasksite emptyDir: medium: Memory # 使用内存作为介质，性能更高 sizeLimit: "50Mi" # 共享主机时区配置：同步Pod内所有容器的时区 - name: tz-config # <-- 名称需与volumeMounts中的name一致 hostPath: path: /usr/share/zoneinfo/Asia/Shanghai # 请按需修改时区
配置业务容器挂载
在业务容器（如your-business-app-container）的volumeMounts中添加以下挂载项：
确保业务容器将日志写入${shared_volume_path}目录，LoongCollector 才能正确采集。
volumeMounts: # 挂载共享日志卷到业务日志输出目录 - name: ${shared_volume_name} mountPath: ${shared_volume_path} # 例如：/var/log/app # 挂载通信目录 - name: tasksite mountPath: /tasksite # 与 Loongcollector容器通信的共享目录 # 挂载时区文件 - name: tz-config mountPath: /etc/localtime readOnly: true
注入LoongCollector Sidecar容器
在spec.template.spec.containers数组中追加以下 Sidecar 容器定义：
- name: loongcollector image: aliyun-observability-release-registry.cn-shenzhen.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成（通过 tombstone 文件信号） echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done # 留出时间上传剩余日志 echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" sleep 30 # 停止服务 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "2000m" memory: "2048Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "${your_aliyun_user_id}" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "${your_machine_group_user_defined_id}" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/${your_region_config}/ilogtail_config.json" # 启用全量排空，确保 Pod 终止前发送所有日志 - name: enable_full_drain_mode value: "true" # 追加 Pod 环境信息作为日志标签 - name: ALIYUN_LOG_ENV_TAGS value: "_pod_name_|_pod_ip_|_namespace_|_node_name_|_node_ip_" # 自动注入 Pod 和 Node 元数据作为日志标签 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName - name: "_node_ip_" valueFrom: fieldRef: fieldPath: status.hostIP # 卷挂载（与业务容器共享） volumeMounts: # 只读挂载业务日志目录 - name: ${shared_volume_name} # <-- 共享日志目录名 mountPath: ${dir_containing_your_files} # <-- 共享目录在sidercar中的路径 readOnly: true # 挂载通信目录 - name: tasksite mountPath: /tasksite # 挂载时区 - name: tz-config mountPath: /etc/localtime readOnly: true
### 2. 改造业务容器生命周期逻辑
根据工作负载类型，需改造业务容器以支持与Sidecar协同退出：
## 短生命周期任务（Job/CronJob）
# 1. 等待 LoongCollector 准备就绪 echo "[$(date)] Business: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] Business: LoongCollector is ready, starting business logic" # 2. 执行核心业务逻辑（确保日志写入共享目录） echo "Hello, World!" >> /app/logs/business.log # 3. 保存退出码 retcode=$? echo "[$(date)] Business: Task completed with exit code: $retcode" # 4. 通知LoongCollector业务完成 touch /tasksite/tombstone echo "[$(date)] Business: Tombstone created, exiting" exit $retcode
## 长生命周期服务（Deployment / StatefulSet）
# 定义信号处理函数 _term_handler() { echo "[$(date)] [nginx-demo] Caught SIGTERM, starting graceful shutdown..." # 发送QUIT信号给Nginx进行优雅停止 if [ -n "$NGINX_PID" ]; then kill -QUIT "$NGINX_PID" 2>/dev/null || true echo "[$(date)] [nginx-demo] Sent SIGQUIT to Nginx PID: $NGINX_PID" # 等待Nginx优雅停止 wait "$NGINX_PID" EXIT_CODE=$? echo "[$(date)] [nginx-demo] Nginx stopped with exit code: $EXIT_CODE" fi # 通知LoongCollector业务容器已停止 echo "[$(date)] [nginx-demo] Writing tombstone file" touch /tasksite/tombstone exit $EXIT_CODE } # 注册信号处理 trap _term_handler SIGTERM SIGINT SIGQUIT # 等待LoongCollector准备就绪 echo "[$(date)] [nginx-demo]: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] [nginx-demo]: LoongCollector is ready, starting business logic" # 启动Nginx echo "[$(date)] [nginx-demo] Starting Nginx..." nginx -g 'daemon off;' & NGINX_PID=$! echo "[$(date)] [nginx-demo] Nginx started with PID: $NGINX_PID" # 等待Nginx进程 wait $NGINX_PID EXIT_CODE=$? # 非信号导致的退出也要通知LoongCollector if [ ! -f /tasksite/tombstone ]; then echo "[$(date)] [nginx-demo] Unexpected exit, writing tombstone" touch /tasksite/tombstone fi exit $EXIT_CODE
### 3. 设置优雅终止时间
在spec.template.spec中设置足够的终止宽限期，以确保 LoongCollector 有足够时间上传剩余日志。
spec: # ... 您现有的其他 spec 配置 ... template: spec: terminationGracePeriodSeconds: 600 # 10分钟优雅停止时间
### 4. 变量说明
| 变量 | 说明 |
| --- | --- |
| ${your_aliyun_user_id} | 设置为您的阿里云账号（主账号）ID。更多信息，请参见 [配置用户标识](configure-a-user-identifier.md) 。 |
| ${your_machine_group_user_defined_id} | 自定义设置机器组的自定义标识，用于创建自定义机器组。例如 nginx-log-sidecar 。 重要 请确保该标识在您的 Project 所在地域内唯一。 |
| ${your_region_config} | 请根据日志服务 Project 所在地域和访问的网络类型填写。其中，地域信息请参见 [开服地域](sls-supported-regions1.md) 。 示例：若 Project 位于华东 1（杭州），则以阿里云内网访问时为 cn-hangzhou ，公网访问时使用 cn-hangzhou-internet 。 |
| ${shared_volume_name} | 自定义设置卷的名称。 重要 volumeMounts 节点下的 name 参数与 volumes 节点下的 name 参数需设置为一致，即确保 LoongCollector 容器和业务容器挂载相同的卷上。 |
| ${dir_containing_your_files} | 设置挂载路径，即容器待采集文本日志所在目录。 |
### 5. 应用配置并验证
执行以下命令部署变更：
kubectl apply -f <YOUR-YAML>
查看 Pod 状态，确认 LoongCollector 容器已成功注入：
kubectl describe pod <YOUR-POD-NAME>
若看到两个容器（业务容器 +loongcollector），且状态正常，则注入成功。
## 步骤二：创建用户自定义标识机器组
本步骤将Pod中注入的 LoongCollector Sidecar实例注册到日志服务，实现采集配置的统一管理和下发。
操作流程
创建机器组
进入目标Project，在左侧导航栏单击资源>机器组。
在机器组页面，单击>创建机器组。
配置机器组信息
填写以下参数后，单击确定：
名称：机器组名称，创建后不可修改。命名规则如下：
只能包括小写字母、数字、短划线（-）和下划线（_）。
必须以小写字母或者数字开头和结尾。
长度必须在 2~128 字符之间。
机器组标识：选择用户自定义标识。
用户自定义标识：填入您在[步骤一](collect-k8s-cluster-logs-through-sidecar.md)YAML文件中为 LoongCollector 容器设置的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID的值。必须完全一致，否则无法关联成功。
检查机器组心跳状态
创建完成后，单击目标机器组名称，在机器组状态区域，查看心跳状态。
OK：表示LoongCollector 已成功连接到日志服务，机器组注册成功。
FAIL：
可能是配置未生效，配置生效时间大约需要2分钟，请稍后刷新页面重试。
如果2分钟后仍为FAIL，请参考[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组问题排查思路](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行诊断。
每个 Pod 对应一个独立的 LoongCollector 实例，建议为不同业务或环境使用不同的自定义标识，便于精细化管理。
## 步骤三：创建采集配置
定义 LoongCollector 应采集哪些日志文件、如何解析日志结构、如何过滤内容，并将配置绑定到已注册的机器组。
操作流程
在日志库页面，单击目标LogStore名称前的展开。
单击数据接入后的，在快速数据接入弹框中，找到Kubernetes-文件卡片，单击立即接入。
机器组配置，完成后单击下一步：
使用场景：选择K8s场景
部署方式：选择Sidecar
选择机器组：在源机器组列表中勾选[步骤二](collect-k8s-cluster-logs-through-sidecar.md)中创建的用户自定义标识机器组，单击添加至应用机器组列表。
在Logtail配置页面，按照如下步骤配置Logtail采集规则。
### 1. 全局与输入配置
定义采集配置的名称、日志来源及采集范围。
全局配置：
配置名称：自定义采集配置名称，在其所属Project内必须唯一。创建成功后，无法修改。命名规则：
仅支持小写字母、数字、连字符（-）和下划线（_）。
必须以小写字母或者数字作为开头和结尾。
输入配置：
类型：文本日志采集。
Logtail部署模式：选择Sidecar
文件路径类型：
容器内路径：采集容器内的日志文件。
宿主机路径：采集宿主机本地服务日志。
文件路径：日志采集的路径。
Linux：以“/”开头，如/data/mylogs/**/*.log，表示/data/mylogs目录下所有后缀名为.log的文件。
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
添加解析插件：单击添加处理插件，根据实际格式配置[正则解析、分隔符解析、JSON 解析等插件](collect-k8s-cluster-logs-through-sidecar.md)。此处以采集NGINX日志为例，选择原生处理插件>NGINX模式解析。
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
## 容器过滤
基于容器元信息（如环境变量、Pod 标签、命名空间、容器名称等）设置采集条件，精准控制采集哪些容器的日志。
配置步骤：在Logtail配置页面的输入配置区域，启用容器过滤，并单击添加。
多个条件之间为“且”的关系，所有正则匹配均基于 Go 语言的 RE2 正则引擎，功能较 PCRE 等引擎有所限制，请遵循[附录：正则表达式使用限制（容器过滤）](collect-k8s-cluster-logs-through-sidecar.md)编写正则表达式。
环境变量黑/白名单：指定待采集容器的环境变量条件。
K8s Pod标签黑/白名单：指定待采集容器所在Pod 的标签条件。
K8s Pod 名称正则匹配：通过Pod名称指定待采集的容器
K8s Namespace 正则匹配：通过Namespace名称指定待采集的容器。
K8s 容器名称正则匹配：通过容器名称指定待采集的容器。
容器label黑/白名单：采集容器标签符合条件的容器，Docker场景使用，K8s场景不推荐使用。
### 4. 日志分类
在多应用、多实例共用相同日志格式的场景下，日志来源难以区分，导致查询时上下文缺失、分析效率低下。为此，可通过配置日志主题（Topic）和日志打标实现自动化的上下文关联与逻辑分类。
## 配置日志主题（Topic）
当多个应用或实例的日志格式相同但路径不同时（如/apps/app-A/run.log和/apps/app-B/run.log），采集日志难以区分来源。此时可基于机器组、自定义名称或文件路径提取方式生成 Topic，灵活区分不同业务或路径来源的日志。
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
| 多捕获组-命名（使用 (?P<name>.*？) | 需要多个维度区分来源且希望字段含义清晰、便于查询与分析 | 生成 tag 字段 __tag__:{name} | \/logs\/(?P<user>.*?)\/(?P<service>.*?)\/app\.log | /logs/userA/svcA/app.log | __tag__:user:userA ； __tag__:service:svcA |
## 日志打标
启用日志标签富化功能，从容器环境变量或 Kubernetes Pod 标签中提取关键信息并附加为 tag，实现日志的精细化分组。
配置步骤：在Logtail配置页面的输入配置区域，启用日志标签富化，并单击添加。
环境变量相关：配置环境变量名和tag名，环境变量值将存放在tag名中。
环境变量名：指定需要提取的环境变量名称。
tag名：环境变量标签名称。
Pod标签相关：配置Pod标签名和tag名，Pod标签值将存放在tag名中。
Pod标签名：需要提取的 Kubernetes Pod 标签名称。
tag名：标签名称。
### 5. 输出配置
默认采集所有日志发送到当前日志库，压缩方式为lz4。如需将同一来源的日志分发到不同日志库，请参考如下步骤进行配置：
多目标动态分发
重要
多目标发送仅适用于LoongCollector 3.0.0及以上版本，Logtail不支持。
输出目标最多可配置5个。
配置多个输出目标后，该采集配置将不再显示在当前 LogStore 的采集配置列表中。如需查看、修改或删除多目标分发配置，请参考[如何管理多目标分发配置？](collect-k8s-cluster-logs-through-sidecar.md)。
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
## 步骤四：查询与分析配置
在完成日志处理与插件配置后，单击下一步，进入查询分析配置页面：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[字段索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
## 步骤五：查看上报日志
完成采集配置并应用到机器组后，系统将自动下发配置并开始采集增量日志。
确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。
查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。容器文本日志默认字段如下：
| 字段名称 | 说明 |
| --- | --- |
| __tag__:__hostname__ | 容器宿主机的名称。 |
| __tag__:__path__ | 容器内日志文件的路径。 |
| __tag__:_container_ip_ | 容器的 IP 地址。 |
| __tag__:_image_name_ | 容器使用的镜像名称。 说明 若存在多个相同 Hash 但名称或 Tag 不同的镜像，采集配置将根据 Hash 选择其中一个名称进行采集，无法确保所选名称与 YAML 文件中定义的一致。 |
| __tag__:_pod_name_ | Pod 的名称。 |
| __tag__:_namespace_ | Pod 所属的命名空间。 |
| __tag__:_pod_uid_ | Pod 的唯一标识符（UID）。 |
## 影响日志采集完整性的关键配置说明
确保日志采集的完整性是LoongCollector Sidecar部署的核心目标。以下配置参数直接影响日志数据的完整性和可靠性。
LoongCollector 资源配置
在大数据量场景下，合理的资源配置是保证端上采集性能的关键基础。关键配置参数如下：
# 根据日志产生速率配置CPU、内存资源 resources: limits: cpu: "2000m" memory: "2Gi" # 影响采集性能的参数 env: - name: cpu_usage_limit value: "2" - name: mem_usage_limit value: "2048" - name: max_bytes_per_sec value: "209715200" - name: process_thread_count value: "8" - name: send_request_concurrency value: "20"
具体数据量与对应配置关系可以参考[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
服务端 Quota 配置
服务端quota限制或网络异常会导致端上数据发送受阻，从而反压到文件采集侧，影响日志完整性。推荐[使用](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[CloudLens for SLS](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[监控](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[Project](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[资源配额](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)。
首次采集配置优化
Pod启动时的首次文件采集策略直接影响数据完整性，特别是在高速数据写入场景。
通过配置首次采集大小，可以确认首次采集的新文件的内容位置。首次采集大小默认为 1024 KB。
首次采集时，如果文件小于 1024 KB，则从文件内容起始位置开始采集。
首次采集时，如果文件大于 1024 KB，则从距离文件末尾1024 KB 的位置开始采集。
首次采集大小，取值范围为 0~10485760，单位为 KB。
enable_full_drain_mode
这是确保数据完整性的关键参数，保证LoongCollector在收到SIGTERM信号时完成所有数据采集和发送。
# 影响采集完整性的参数 env: - name: enable_full_drain_mode value: "true" # 启用全量排空模式
## 常见问题
### 如何管理多目标分发配置？
由于多目标分发配置关联了多个日志库，这类配置需要通过 Project 级别的管理页面进行维护：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project名称。
在目标Project页面，单击左侧导航栏资源>配置管理。
说明
此页面集中管理Project下的所有采集配置，包括那些因日志库被误删而残留的配置。
## 后续操作
[数据可视化](dashboard-overview.md)：借助可视化仪表盘监控关键指标趋势。
[数据异常自动预警](alarm-settings-quick-start.md)：设置告警策略，实时感知系统的异常情况。
日志服务仅采集增量日志，如需采集历史日志请参见[导入历史日志文件](import-historical-logs.md)。
## 附录：YAML示例
本示例展示了一个完整的 Kubernetes Deployment 配置，包含业务容器（Nginx）和 LoongCollector Sidecar 容器，适用于通过 Sidecar 模式采集容器日志。
使用前请完成以下三项关键替换：
将${your_aliyun_user_id}替换为您的阿里云主账号 UID；
将${your_machine_group_user_defined_id}替换为[步骤三中创建的机器组自定义标识](collect-k8s-cluster-logs-through-sidecar.md)，必须完全一致。
将${your_region_config}替换为与日志服务 Project 所在地域及网络类型匹配的配置名。
示例：Project 位于 华东1（杭州），内网访问——>cn-hangzhou；公网访问——>cn-hangzhou-internet。
## 短生命周期（Job/CronJob）
apiVersion: batch/v1 kind: Job metadata: name: demo-job spec: backoffLimit: 3 activeDeadlineSeconds: 3600 completions: 1 parallelism: 1 template: spec: restartPolicy: Never terminationGracePeriodSeconds: 300 containers: # 业务容器 - name: demo-job image: debian:bookworm-slim command: ["/bin/bash", "-c"] args: - | # 等待LoongCollector准备就绪 echo "[$(date)] Business: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] Business: LoongCollector is ready, starting business logic" # 执行业务逻辑 echo "Hello, World!" >> /app/logs/business.log # 保存退出码 retcode=$? echo "[$(date)] Business: Task completed with exit code: $retcode" # 通知LoongCollector业务完成 touch /tasksite/tombstone echo "[$(date)] Business: Tombstone created, exiting" exit $retcode # 资源限制 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "500" memory: "512Mi" # 卷挂载 volumeMounts: - name: app-logs mountPath: /app/logs - name: tasksite mountPath: /tasksite # LoongCollector Sidecar容器 - name: loongcollector image: aliyun-observability-release-registry.cn-hongkong.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成 echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" # 给足够时间传输剩余日志 sleep 30 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "500m" memory: "512Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "your-user-id" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "your-user-defined-id" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/cn-hongkong/ilogtail_config.json" - name: ALIYUN_LOG_ENV_TAGS value: "_pod_name_|_pod_ip_|_namespace_|_node_name_" # Pod信息注入 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName # 卷挂载 volumeMounts: - name: app-logs mountPath: /app/logs readOnly: true - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # 卷定义 volumes: - name: app-logs emptyDir: {} - name: tasksite emptyDir: medium: Memory sizeLimit: "10Mi" - name: tz-config hostPath: path: /usr/share/zoneinfo/Asia/Shanghai
## 长生命周期（Deployment / StatefulSet）
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-demo namespace: production labels: app: nginx-demo version: v1.0.0 spec: replicas: 3 strategy: type: RollingUpdate rollingUpdate: maxUnavailable: 1 maxSurge: 1 selector: matchLabels: app: nginx-demo template: metadata: labels: app: nginx-demo version: v1.0.0 spec: terminationGracePeriodSeconds: 600 # 10分钟优雅停止时间 containers: # 业务容器 - Web应用 - name: nginx-demo image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 # 启动命令和信号处理 command: ["/bin/sh", "-c"] args: - | # 定义信号处理函数 _term_handler() { echo "[$(date)] [nginx-demo] Caught SIGTERM, starting graceful shutdown..." # 发送QUIT信号给Nginx进行优雅停止 if [ -n "$NGINX_PID" ]; then kill -QUIT "$NGINX_PID" 2>/dev/null || true echo "[$(date)] [nginx-demo] Sent SIGQUIT to Nginx PID: $NGINX_PID" # 等待Nginx优雅停止 wait "$NGINX_PID" EXIT_CODE=$? echo "[$(date)] [nginx-demo] Nginx stopped with exit code: $EXIT_CODE" fi # 通知LoongCollector业务容器已停止 echo "[$(date)] [nginx-demo] Writing tombstone file" touch /tasksite/tombstone exit $EXIT_CODE } # 注册信号处理 trap _term_handler SIGTERM SIGINT SIGQUIT # 等待LoongCollector准备就绪 echo "[$(date)] [nginx-demo]: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] [nginx-demo]: LoongCollector is ready, starting business logic" # 启动Nginx echo "[$(date)] [nginx-demo] Starting Nginx..." nginx -g 'daemon off;' & NGINX_PID=$! echo "[$(date)] [nginx-demo] Nginx started with PID: $NGINX_PID" # 等待Nginx进程 wait $NGINX_PID EXIT_CODE=$? # 非信号导致的退出也要通知LoongCollector if [ ! -f /tasksite/tombstone ]; then echo "[$(date)] [nginx-demo] Unexpected exit, writing tombstone" touch /tasksite/tombstone fi exit $EXIT_CODE # 资源配置 resources: requests: cpu: "200m" memory: "256Mi" limits: cpu: "1000m" memory: "1Gi" # 卷挂载 volumeMounts: - name: nginx-logs mountPath: /var/log/nginx - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # LoongCollector Sidecar容器 - name: loongcollector image: aliyun-observability-release-registry.cn-shenzhen.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成 echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" # 给足够时间传输剩余日志 sleep 30 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "2000m" memory: "2048Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "${your_aliyun_user_id}" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "${your_machine_group_user_defined_id}" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/${your_region_config}/ilogtail_config.json" # 启用全量排空模式，确保Pod停止时发送所有日志 - name: enable_full_drain_mode value: "true" # 追加 Pod 环境信息作为日志标签 - name: "ALIYUN_LOG_ENV_TAGS" value: "_pod_name_|_pod_ip_|_namespace_|_node_name_|_node_ip_" # 获取 Pod 和 Node 的信息 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName - name: "_node_ip_" valueFrom: fieldRef: fieldPath: status.hostIP # 卷挂载 volumeMounts: - name: nginx-logs mountPath: /var/log/nginx readOnly: true - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # 卷定义 volumes: - name: nginx-logs emptyDir: {} - name: tasksite emptyDir: medium: Memory sizeLimit: "50Mi" - name: tz-config hostPath: path: /usr/share/zoneinfo/Asia/Shanghai
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
日志样例区域内显示已粘贴的 Apache Combined 格式访问日志样例（包含客户端 IP、时间戳、请求方法路径、状态码、Referer 及 User-Agent 等字段）。
手动输入：根据日志格式手动输入正则表达式。
配置完成后，单击验证，测试正则表达式是否能够正确解析日志内容。
日志提取字段：为提取的日志内容（Value），设置对应的字段名（Key）。
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
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
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
### 标准JSON解析
将Object类型的JSON日志结构化，解析为键值对形式。
效果示例：
| 未经任何处理的原始日志 | 标准 JSON 键值自动提取 |
| --- | --- |
| {"url": "POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10.200.98.220", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "18204"}, "time": "05/Jan/2025:13:30:28"} | ip: 10.200.98.220 request: {"status": "200", "latency" : "18204" } time: 05/Jan/2025:13:30:28 url: POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek******&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1 user-agent:aliyun-sdk-java |
配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>JSON解析：
原始字段：默认值为content（此字段用于存放待解析的原始日志内容）。
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
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
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
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
日志格式：combined
APACHE配置字段：系统会根据日志格式自动填充配置。
重要
请务必核对自动填充的内容，确保与服务器上 Apache 配置文件（通常位于/etc/apache2/apache2.conf）中定义的 LogFormat 完全一致。
其他参数请参考[场景二：结构化日志](collect-k8s-cluster-logs-through-sidecar.md)中的通用配置参数说明。
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
## 附录：正则表达式使用限制（容器过滤）
容器过滤时所使用的正则表达式基于Go语言的RE2引擎，与PCRE等其他引擎相比存在部分语法限制。请在编写正则表达式时注意以下事项：
1. 命名分组语法差异
Go语言使用(?P<name>...)语法定义命名分组，不支持 PCRE中的(?<name>...)语法。
正确示例：(?P<year>\d{4})
错误写法：(?<year>\d{4})
2. 不支持的正则特性
以下常见但复杂的正则功能在RE2中不可用，请避免使用：
断言：(?=...)、(?!...)、(?<=...)、（?<!...)
条件表达式：(?(condition)true|false)
递归匹配：(?R)、(?0)
子程序引用：(?&name)、(?P>name)
原子组：(?>...)
3. 使用建议
推荐使用[Regex101](https://regex101.com/)等工具调试正则表达式时，选择 Golang (RE2) 模式进行验证，以确保兼容性。若使用了上述不支持的语法，插件将无法正确解析或匹配。
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
