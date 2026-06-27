# 如何在容器安装与配置LoongCollector-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/loongcollector-installation-kubernetes-1

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

# 安装配置

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

LoongCollector是阿里云日志服务（SLS）推出的新一代日志采集 Agent，是 Logtail 的升级版。本文档指导您如何在 Kubernetes 集群中安装 LoongCollector，并提供了 DaemonSet 和 Sidecar 两种安装模式。

## 准备工作

在安装前，请在集群节点上验证与日志服务服务端点的网络连通性，确保LoongCollector可以正常上报数据。

- 

获取服务接入点：

- 

登录[日志服务控制台](https://sls.console.aliyun.com/?spm=a2c4g.11186623.0.0.70905a3dccueNa)，在Project列表中，单击目标Project。

- 

单击Project名称右侧的进入项目概览页面。

- 

在基础信息中找到当前Project所在地域的公网和内网Endpoint。

- 

执行连通性测试：登录到将要安装LoongCollector组件的集群节点上，执行以下curl命令。请将${Project名称}和${SLS_ENDPOINT}替换为您的实际信息。

curl https://${Project名称}.${SLS_ENDPOINT}

- 

查看测试结果：

- 

如果命令返回{"Error":{"Code":"OLSInvalidMethod",...}}，表明您的节点与日志服务之间的网络是通畅的。

说明

此测试仅验证网络层连通性。由于请求缺少必要的 API 参数，日志服务返回错误响应是预期结果。

- 

如果命令超时或返回其他网络层错误（如Connection refused），则表示网络不通，请检查节点的网络配置、安全组规则或 DNS 解析。

## 选择合适的安装方式

请根据您的集群类型和需求，选择下表中对应的安装方式：

- 

- 

- 

- 

- 

| 安装方式 | 适用场景 |
| --- | --- |
| [ACK](products/sls/documents/loongcollector-installation-kubernetes-1.md) [集群安装（DaemonSet](products/sls/documents/loongcollector-installation-kubernetes-1.md) [模式）](products/sls/documents/loongcollector-installation-kubernetes-1.md) | 采集 同阿里云账号、同地域 下的 [ACK 托管与专有集群](products/ack/documents/ack-managed-and-ack-dedicated/product-overview/what-is-ack.md) 日志。 |
| [自建集群安装（DaemonSet](products/sls/documents/loongcollector-installation-kubernetes-1.md) [模式）](products/sls/documents/loongcollector-installation-kubernetes-1.md) | 跨阿里云账号或跨地域 采集阿里云 ACK 集群日志。 采集部署在自建 IDC 机房中的 Kubernetes 集群日志。 采集部署在 其他云服务商上 的 Kubernetes 集群日志。 |
| [Sidecar](products/sls/documents/loongcollector-installation-kubernetes-1.md) [模式安装](products/sls/documents/loongcollector-installation-kubernetes-1.md) | 需要对特定业务应用进行日志采集，且有以下需求的场景： 资源隔离 ：避免 DaemonSet 模式影响节点上其他 Pod。 精细化采集 ：为每个应用单独配置采集源、过滤规则、输出目标等。 |


## ACK集群安装（DaemonSet模式）

通过阿里云ACK容器服务控制台一键安装LoongCollector，默认将集群容器日志采集到同账号同地域的Project，如需跨账号或跨地域采集请参考[自建集群安装（DaemonSet](products/sls/documents/loongcollector-installation-kubernetes-1.md)[模式）](products/sls/documents/loongcollector-installation-kubernetes-1.md)。

为已有ACK托管集群安装

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在日志与监控页签中，找到loongcollector，单击安装。

- 

安装完成后，日志服务会自动在ACK所属地域下创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | loongcollector-ds 的机器组，主要用于日志采集场景。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## 新建ACK托管集群时安装

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

单击创建集群，在组件配置页面，勾选使用日志服务。支持创建新Project或使用已有Project。

本文只描述日志服务相关配置，关于更多配置项说明，请参见[创建](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。

- 

当您选择创建新 Project时，日志服务会默认创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | k8s-log-${cluster_id} | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | loongcollector-ds 的机器组，主要用于日志采集场景。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## 自建集群安装（DaemonSet模式）

适用场景

- 

自建 IDC 机房中的 Kubernetes 集群

- 

部署在其他云厂商的 Kubernetes 集群

- 

跨账号或跨地域采集阿里云 ACK 集群容器日志

说明

请确保您的自建集群满足Kubernetes 1.6及以上版本。

操作指南

- 

下载并解压安装包：在安装并配置了kubectl的机器上，根据集群所在地域选择命令下载LoongCollector及其他依赖组件。

#中国地域 wget https://aliyun-observability-release-cn-shanghai.oss-cn-shanghai.aliyuncs.com/loongcollector/k8s-custom-pkg/3.2.6/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh #海外地域 wget https://aliyun-observability-release-ap-southeast-1.oss-ap-southeast-1.aliyuncs.com/loongcollector/k8s-custom-pkg/3.2.6/loongcollector-custom-k8s-package.tgz; tar xvf loongcollector-custom-k8s-package.tgz; chmod 744 ./loongcollector-custom-k8s-package/k8s-custom-install.sh

- 

修改配置文件values.yaml：进入loongcollector-custom-k8s-package目录，修改配置文件./loongcollector/values.yaml。

## 

- 

- 

- 

- 

- 

| 参数说明 | values.yaml # ===================== 必需要补充的内容 ===================== # 本集群要采集的 Project 名，例如 k8s-log-custom-sd89ehdq projectName: "" # Project 所属地域，例如上海：cn-shanghai region: "" # Project 所属主账号 uid，请用引号包围，例如"123456789" aliUid: "" # 使用网络，可选参数：公网 Internet，内网 Intranet，默认使用公网 net: Internet # 主账号或者子账号的 AK，SK accessKeyID: "" accessKeySecret: "" # 自定义集群 ID，命名只支持大小写，数字，短划线(-)。 clusterID: "" # ...省略非必填参数... |
| --- | --- |
| projectName String (必填) Project 名称，LoongCollector 将上传日志到该 Project 中。命名规则如下： 项目名称仅支持小写字母、数字和连字符（-）。 必须以小写字母开头，以小写字母和数字结尾。 名称长度为 3～63 个字符。 |  |
| region String (必填) Project 所属地域 ID，请参考 [地域](products/sls/documents/loongcollector-installation-kubernetes-1.md) 查看 Project 所在地域的 ID。 |  |
| aliUid String (必填) Project 所属的阿里云 主账号 ID 。 |  |
| net String (必填) 日志数据传输使用的 [网络类型](products/sls/documents/loongcollector-installation-kubernetes-1.md) 。 Internet（默认值）：公网。 Intranet：内网。 |  |
| accessKeyID String (必填) Project 所属账号的 AccessKey ID。推荐使用 RAM 用户的 AccessKey，并授予 RAM 用户 AliyunLogFullAccess 系统策略权限。RAM 相关概念请参见 [RAM](products/ram/documents/user-guide/overview-of-ram-users.md) [用户概览](products/ram/documents/user-guide/overview-of-ram-users.md) 。 |  |
| accessKeySecret String (必填) Project 所属账号的 AccessKey Secret。 |  |
| clusterID String (必填) 自定义集群 ID，命名只支持大小写字母、数字、短划线(-)。 重要 不同的 Kubernetes 集群，请勿配置相同的集群 ID。 |  |


- 

执行安装脚本：在loongcollector-custom-k8s-package目录下执行如下命令，安装LoongCollector及其他依赖组件。

bash k8s-custom-install.sh install

- 

验证安装结果：安装完成后，执行如下命令查看组件状态：

# 检查Pod状态 kubectl get po -n kube-system | grep loongcollector-ds

返回结果示例：

loongcollector-ds-gnmnh 1/1 Running 0 63s

若组件未成功启动（非Running）:

- 

检查配置：请确认values.yaml配置项是否正确。

- 

检查镜像：通过如下命令查看Events确认容器镜像是否成功拉取。

kubectl describe pod loongcollector-ds -n kube-system

- 

组件安装成功后，日志服务会自动创建如下资源，您可登录[日志服务控制台](https://sls.console.aliyun.com/)查看。

| 资源类型 | 资源名称 | 作用 |
| --- | --- | --- |
| Project | values.yaml 文件中自定义的 projectName 的值 | 资源管理单元，隔离不同业务日志。 |
| 机器组 | k8s-group-${cluster_id} | 日志采集节点集合。 |
| k8s-group-${cluster_id}-cluster | loongcollector-cluster 的机器组，主要用于指标采集场景。 |  |
| k8s-group-${cluster_id}-singleton | 单实例机器组，主要用于部分单实例采集配置。 |  |


重要

LoongCollector 组件中将不会创建名为config-operation-log的LogStore，若已创建的将不再写入日志。

## Sidecar模式安装

当您需要对特定应用的日志进行精细化管理、实现多租户隔离或确保日志采集与应用生命周期严格绑定时，Sidecar 模式是理想的日志采集方案。该模式通过在业务 Pod 中注入一个独立的 LoongCollector（Logtail） 容器，实现对该 Pod 内日志的专属采集。若尚未部署业务应用，或仅用于测试，可直接使用[附录：YAML](products/sls/documents/loongcollector-installation-kubernetes-1.md)[示例](products/sls/documents/loongcollector-installation-kubernetes-1.md)快速验证流程。

### 1. 修改业务Pod YAML配置

- 

定义共享卷

在spec.template.spec.volumes中添加三个共享卷（与containers同级）：

volumes: # 共享日志目录（业务容器写入，Sidecar 读取） - name: ${shared_volume_name} # <-- 名称需与volumeMounts中的name一致 emptyDir: {} # 容器间通信信令目录（用于优雅启停） - name: tasksite emptyDir: medium: Memory # 使用内存作为介质，性能更高 sizeLimit: "50Mi" # 共享主机时区配置：同步Pod内所有容器的时区 - name: tz-config # <-- 名称需与volumeMounts中的name一致 hostPath: path: /usr/share/zoneinfo/Asia/Shanghai # 请按需修改时区

- 

配置业务容器挂载

在业务容器（如your-business-app-container）的volumeMounts中添加以下挂载项：

确保业务容器将日志写入${shared_volume_path}目录，LoongCollector 才能正确采集。

volumeMounts: # 挂载共享日志卷到业务日志输出目录 - name: ${shared_volume_name} mountPath: ${shared_volume_path} # 例如：/var/log/app # 挂载通信目录 - name: tasksite mountPath: /tasksite # 与 Loongcollector容器通信的共享目录 # 挂载时区文件 - name: tz-config mountPath: /etc/localtime readOnly: true

- 

注入LoongCollector Sidecar容器

在spec.template.spec.containers数组中追加以下 Sidecar 容器定义：

- name: loongcollector image: aliyun-observability-release-registry.cn-shenzhen.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成（通过 tombstone 文件信号） echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done # 留出时间上传剩余日志 echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" sleep 30 # 停止服务 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "2000m" memory: "2048Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "${your_aliyun_user_id}" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "${your_machine_group_user_defined_id}" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/${your_region_config}/ilogtail_config.json" # 启用全量排空，确保 Pod 终止前发送所有日志 - name: enable_full_drain_mode value: "true" # 追加 Pod 环境信息作为日志标签 - name: ALIYUN_LOG_ENV_TAGS value: "_pod_name_|_pod_ip_|_namespace_|_node_name_|_node_ip_" # 自动注入 Pod 和 Node 元数据作为日志标签 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName - name: "_node_ip_" valueFrom: fieldRef: fieldPath: status.hostIP # 卷挂载（与业务容器共享） volumeMounts: # 只读挂载业务日志目录 - name: ${shared_volume_name} # <-- 共享日志目录名 mountPath: ${dir_containing_your_files} # <-- 共享目录在sidercar中的路径 readOnly: true # 挂载通信目录 - name: tasksite mountPath: /tasksite # 挂载时区 - name: tz-config mountPath: /etc/localtime readOnly: true

### 2. 改造业务容器生命周期逻辑

根据工作负载类型，需改造业务容器以支持与Sidecar协同退出：

短生命周期任务（Job/CronJob）# 1. 等待 LoongCollector 准备就绪 echo "[$(date)] Business: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] Business: LoongCollector is ready, starting business logic" # 2. 执行核心业务逻辑（确保日志写入共享目录） echo "Hello, World!" >> /app/logs/business.log # 3. 保存退出码 retcode=$? echo "[$(date)] Business: Task completed with exit code: $retcode" # 4. 通知LoongCollector业务完成 touch /tasksite/tombstone echo "[$(date)] Business: Tombstone created, exiting" exit $retcode

长生命周期服务（Deployment / StatefulSet）# 定义信号处理函数 _term_handler() { echo "[$(date)] [nginx-demo] Caught SIGTERM, starting graceful shutdown..." # 发送QUIT信号给Nginx进行优雅停止 if [ -n "$NGINX_PID" ]; then kill -QUIT "$NGINX_PID" 2>/dev/null || true echo "[$(date)] [nginx-demo] Sent SIGQUIT to Nginx PID: $NGINX_PID" # 等待Nginx优雅停止 wait "$NGINX_PID" EXIT_CODE=$? echo "[$(date)] [nginx-demo] Nginx stopped with exit code: $EXIT_CODE" fi # 通知LoongCollector业务容器已停止 echo "[$(date)] [nginx-demo] Writing tombstone file" touch /tasksite/tombstone exit $EXIT_CODE } # 注册信号处理 trap _term_handler SIGTERM SIGINT SIGQUIT # 等待LoongCollector准备就绪 echo "[$(date)] [nginx-demo]: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] [nginx-demo]: LoongCollector is ready, starting business logic" # 启动Nginx echo "[$(date)] [nginx-demo] Starting Nginx..." nginx -g 'daemon off;' & NGINX_PID=$! echo "[$(date)] [nginx-demo] Nginx started with PID: $NGINX_PID" # 等待Nginx进程 wait $NGINX_PID EXIT_CODE=$? # 非信号导致的退出也要通知LoongCollector if [ ! -f /tasksite/tombstone ]; then echo "[$(date)] [nginx-demo] Unexpected exit, writing tombstone" touch /tasksite/tombstone fi exit $EXIT_CODE

### 3. 设置优雅终止时间

在spec.template.spec中设置足够的终止宽限期，以确保 LoongCollector 有足够时间上传剩余日志。

spec: # ... 您现有的其他 spec 配置 ... template: spec: terminationGracePeriodSeconds: 600 # 10分钟优雅停止时间

### 4. 变量说明

| 变量 | 说明 |
| --- | --- |
| ${your_aliyun_user_id} | 设置为您的阿里云账号（主账号）ID。更多信息，请参见 [配置用户标识](products/sls/documents/configure-a-user-identifier.md) 。 |
| ${your_machine_group_user_defined_id} | 自定义设置机器组的自定义标识，用于创建自定义机器组。例如 nginx-log-sidecar 。 重要 请确保该标识在您的 Project 所在地域内唯一。 |
| ${your_region_config} | 请根据日志服务 Project 所在地域和访问的网络类型填写。其中，地域信息请参见 [开服地域](products/sls/documents/sls-supported-regions1.md) 。 示例：若 Project 位于华东 1（杭州），则以阿里云内网访问时为 cn-hangzhou ，公网访问时使用 cn-hangzhou-internet 。 |
| ${shared_volume_name} | 自定义设置卷的名称。 重要 volumeMounts 节点下的 name 参数与 volumes 节点下的 name 参数需设置为一致，即确保 LoongCollector 容器和业务容器挂载相同的卷上。 |
| ${dir_containing_your_files} | 设置挂载路径，即容器待采集文本日志所在目录。 |


### 5. 应用配置并验证

- 

执行以下命令部署变更：

kubectl apply -f <YOUR-YAML>

- 

查看 Pod 状态，确认 LoongCollector 容器已成功注入：

kubectl describe pod <YOUR-POD-NAME>

若看到两个容器（业务容器 +loongcollector），且状态正常，则注入成功。

### 6. 创建用户自定义标识机器组

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project。

- 

在左侧导航栏中，选择资源>机器组，单击机器组右侧的>创建机器组。

- 

在创建机器组对话框中，配置如下参数，单击确定。

- 

名称：机器组名称，创建后不可修改。命名规则如下：

- 

只能包括小写字母、数字、短划线（-）和下划线（_）。

- 

必须以小写字母或者数字开头和结尾。

- 

长度必须在 2~128 字符之间。

- 

机器组标识：选择用户自定义标识。

- 

用户自定义标识：填入您在[1. 修改业务](products/sls/documents/loongcollector-installation-kubernetes-1.md)[Pod YAML](products/sls/documents/loongcollector-installation-kubernetes-1.md)[配置](products/sls/documents/loongcollector-installation-kubernetes-1.md)YAML文件中为 LoongCollector 容器设置的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID的值。必须完全一致，否则无法关联成功。

- 

检查机器组心跳状态：创建完成后，单击目标机器组名称，在机器组状态区域，查看心跳状态。

- 

OK：表示LoongCollector 已成功连接到日志服务，机器组注册成功。

- 

FAIL：

- 

可能是配置未生效，配置生效时间大约需要2分钟，请稍后刷新页面重试。

- 

如果2分钟后仍为FAIL，请参考[Logtail](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)[机器组问题排查思路](products/sls/documents/troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行诊断。

每个 Pod 对应一个独立的 LoongCollector 实例，建议为不同业务或环境使用不同的自定义标识，便于精细化管理。

## 常见问题

### ACK托管集群如何修改LoongCollector配置以实现跨账号或跨地域采集？

如果您通过阿里云ACK容器服务控制台安装了loongcollector，默认将采集集群容器日志到同账号的日志服务Project下。此时您可以通过以下两种方式实现集群容器日志的跨账号或跨地域采集：

方法一：卸载后重新安装。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。

- 

在日志与监控页签中，找到loongcollector，单击卸载。

- 

参考[自建集群安装（DaemonSet](products/sls/documents/loongcollector-installation-kubernetes-1.md)[模式）](products/sls/documents/loongcollector-installation-kubernetes-1.md)重新安装即可。

方法二：更新Helm配置，重新部署loongcollector。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏，选择应用>Helm。

- 

在Helm应用管理页面，找到loongcollector，单击其右侧操作列中的更新按钮，进入更新发布页面，参考如下表格修改相关配置，其他配置保持不变，单击确定：

| 集群与 Project | 需要修改的配置 |
| --- | --- |
| 同账号，不同地域 | region ：Project 所在地域对应的 [RegionID](products/sls/documents/loongcollector-installation-kubernetes-1.md) 。 |
| net ：Internet，不同地域之间无法通过内网互通，请使用公网传输数据。 |  |
| 不同账号，同地域 | aliUid ：日志服务所属的主账号 ID，多个账号之间使用半角逗号（,）相隔。 |
| net ：Intranet，同地域建议优先使用内网传输数据。 |  |
| 不同账号，不同地域 | aliUid ：日志服务所属的主账号 ID，多个账号之间使用半角逗号（,）相隔。 |
| region ：Project 所在地域的 [RegionID](products/sls/documents/loongcollector-installation-kubernetes-1.md) 。 |  |
| net ：Internet，不同地域之间无法通过内网互通，请使用公网传输数据。 |  |


- 

创建机器组：

- 

登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project。

- 

在左侧导航栏中，选择资源>>>机器组，单击机器组右侧的>>>创建机器组。

- 

在创建机器组对话框中，配置如下参数，然后单击确定。

- 

设置机器组名称。

- 

机器组标识：选择用户自定义标识。

- 

用户自定义标识：k8s-group-${cluster_id}，请将${cluster_id}替换集群实际的clusterID。

- 

创建完成后，在机器组列表，单击新建的机器组，在机器组配置>>>机器组状态区域，查看心跳状态。如果心跳为OK则表示创建成功。若心跳失败，请检查用户标识与用户自定义标识内容是否正确。

- 

修改完成后，单击更新使配置生效。

### 如何采集阿里云ACK Edge、ACK One、ACS、ACK Serverless 集群容器日志？

- 

阿里云[ACK Edge](products/ack/documents/ack-edge/product-overview/ack-edge-overview.md)、[ACK One](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/product-overview/ack-one-overview.md)集群暂不支持安装loongcollector，如需采集日志请参考：

- 

[通过日志服务采集](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md)[ACK Edge](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md)[集群的容器日志](products/ack/documents/ack-edge/user-guide/use-log-service-to-collect-log-data-from-containers-of-ack-edge-clusters.md)

- 

[将日志服务接入](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-log-service-for-an-external-kubernetes-cluster.md)[ACK One](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-log-service-for-an-external-kubernetes-cluster.md)[注册集群](products/ack/documents/distributed-cloud-container-platform-for-kubernetes/user-guide/enable-log-service-for-an-external-kubernetes-cluster.md)

- 

阿里云[ACS](https://help.aliyun.com/zh/cs/product-overview/product-introduction)、[ACK Serverless 集群](products/ack/documents/serverless-kubernetes/product-overview/ask-overview.md)无需安装Loongcollector，需要您部署alibaba-log-controller组件，如需采集日志请参考：

- 

[ACS 集群通过](https://help.aliyun.com/zh/cs/user-guide/use-crd-to-collect-application-logs)[CRD](https://help.aliyun.com/zh/cs/user-guide/use-crd-to-collect-application-logs)[采集应用日志](https://help.aliyun.com/zh/cs/user-guide/use-crd-to-collect-application-logs)

- 

[ACK Serverless 集群通过](products/ack/documents/serverless-kubernetes/user-guide/enable-log-service-for-an-ask-cluster.md)[CRD](products/ack/documents/serverless-kubernetes/user-guide/enable-log-service-for-an-ask-cluster.md)[采集应用日志](products/ack/documents/serverless-kubernetes/user-guide/enable-log-service-for-an-ask-cluster.md)

### 如何修改 loongcollector 组件配置参数 projectName？

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏，选择应用>Helm。

- 

在 Helm 应用管理页面，找到loongcollector，单击其右侧操作列中的更新，进入更新发布页面。

- 

在目标 Helm Chart 的参数配置（Values）区域，修改projectName（根级字段）的值，单击确定。

说明

配置环境变量时，若未显式指定ALICLOUD_LOG_PROJECT，系统将使用安装命令中传入的 Project 参数作为默认值，并自动在该 Project 下创建 LoongCollector 相关配置及集群默认机器组。

## 后续步骤

安装完LoongCollector后，您可以查看[Kubernetes](products/sls/documents/kubernetes-cluster-container-log-collection-instructions.md)[集群容器日志采集须知](products/sls/documents/kubernetes-cluster-container-log-collection-instructions.md)了解Kubernetes容器日志采集的核心原理、关键流程、选型建议和最佳实践，并选择合适的方式创建采集配置：

- 

[Kubernetes-CRD](products/sls/documents/collect-text-logs-of-self-built-k8s-clusters-deploy-logtail-in-daemonset-mode-2.md)

- 

[日志服务控制台](products/sls/documents/container-log-collection-in-a-kubernetes-cluster.md)

## 附录：YAML示例

本示例展示了一个完整的 Kubernetes Deployment 配置，包含业务容器（Nginx）和 LoongCollector Sidecar 容器，适用于通过 Sidecar 模式采集容器日志。

使用前请完成以下三项关键替换：

- 

将${your_aliyun_user_id}替换为您的阿里云主账号 UID；

- 

将${your_machine_group_user_defined_id}替换为[步骤三中创建的机器组自定义标识](products/sls/documents/collect-k8s-cluster-logs-through-sidecar.md)，必须完全一致。

- 

将${your_region_config}替换为与日志服务 Project 所在地域及网络类型匹配的配置名。

示例：Project 位于 华东1（杭州），内网访问——>cn-hangzhou；公网访问——>cn-hangzhou-internet。

### 短生命周期（Job/CronJob）

apiVersion: batch/v1 kind: Job metadata: name: demo-job spec: backoffLimit: 3 activeDeadlineSeconds: 3600 completions: 1 parallelism: 1 template: spec: restartPolicy: Never terminationGracePeriodSeconds: 300 containers: # 业务容器 - name: demo-job image: debian:bookworm-slim command: ["/bin/bash", "-c"] args: - | # 等待LoongCollector准备就绪 echo "[$(date)] Business: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] Business: LoongCollector is ready, starting business logic" # 执行业务逻辑 echo "Hello, World!" >> /app/logs/business.log # 保存退出码 retcode=$? echo "[$(date)] Business: Task completed with exit code: $retcode" # 通知LoongCollector业务完成 touch /tasksite/tombstone echo "[$(date)] Business: Tombstone created, exiting" exit $retcode # 资源限制 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "500" memory: "512Mi" # 卷挂载 volumeMounts: - name: app-logs mountPath: /app/logs - name: tasksite mountPath: /tasksite # LoongCollector Sidecar容器 - name: loongcollector image: aliyun-observability-release-registry.cn-hongkong.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成 echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" # 给足够时间传输剩余日志 sleep 30 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "500m" memory: "512Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "your-user-id" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "your-user-defined-id" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/cn-hongkong/ilogtail_config.json" - name: ALIYUN_LOG_ENV_TAGS value: "_pod_name_|_pod_ip_|_namespace_|_node_name_" # Pod信息注入 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName # 卷挂载 volumeMounts: - name: app-logs mountPath: /app/logs readOnly: true - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # 卷定义 volumes: - name: app-logs emptyDir: {} - name: tasksite emptyDir: medium: Memory sizeLimit: "10Mi" - name: tz-config hostPath: path: /usr/share/zoneinfo/Asia/Shanghai

### 长生命周期（Deployment / StatefulSet）

apiVersion: apps/v1 kind: Deployment metadata: name: nginx-demo namespace: production labels: app: nginx-demo version: v1.0.0 spec: replicas: 3 strategy: type: RollingUpdate rollingUpdate: maxUnavailable: 1 maxSurge: 1 selector: matchLabels: app: nginx-demo template: metadata: labels: app: nginx-demo version: v1.0.0 spec: terminationGracePeriodSeconds: 600 # 10分钟优雅停止时间 containers: # 业务容器 - Web应用 - name: nginx-demo image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 # 启动命令和信号处理 command: ["/bin/sh", "-c"] args: - | # 定义信号处理函数 _term_handler() { echo "[$(date)] [nginx-demo] Caught SIGTERM, starting graceful shutdown..." # 发送QUIT信号给Nginx进行优雅停止 if [ -n "$NGINX_PID" ]; then kill -QUIT "$NGINX_PID" 2>/dev/null || true echo "[$(date)] [nginx-demo] Sent SIGQUIT to Nginx PID: $NGINX_PID" # 等待Nginx优雅停止 wait "$NGINX_PID" EXIT_CODE=$? echo "[$(date)] [nginx-demo] Nginx stopped with exit code: $EXIT_CODE" fi # 通知LoongCollector业务容器已停止 echo "[$(date)] [nginx-demo] Writing tombstone file" touch /tasksite/tombstone exit $EXIT_CODE } # 注册信号处理 trap _term_handler SIGTERM SIGINT SIGQUIT # 等待LoongCollector准备就绪 echo "[$(date)] [nginx-demo]: Waiting for LoongCollector to be ready..." until [[ -f /tasksite/cornerstone ]]; do sleep 1 done echo "[$(date)] [nginx-demo]: LoongCollector is ready, starting business logic" # 启动Nginx echo "[$(date)] [nginx-demo] Starting Nginx..." nginx -g 'daemon off;' & NGINX_PID=$! echo "[$(date)] [nginx-demo] Nginx started with PID: $NGINX_PID" # 等待Nginx进程 wait $NGINX_PID EXIT_CODE=$? # 非信号导致的退出也要通知LoongCollector if [ ! -f /tasksite/tombstone ]; then echo "[$(date)] [nginx-demo] Unexpected exit, writing tombstone" touch /tasksite/tombstone fi exit $EXIT_CODE # 资源配置 resources: requests: cpu: "200m" memory: "256Mi" limits: cpu: "1000m" memory: "1Gi" # 卷挂载 volumeMounts: - name: nginx-logs mountPath: /var/log/nginx - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # LoongCollector Sidecar容器 - name: loongcollector image: aliyun-observability-release-registry.cn-shenzhen.cr.aliyuncs.com/loongcollector/loongcollector:v3.1.1.0-20fa5eb-aliyun command: ["/bin/bash", "-c"] args: - | echo "[$(date)] LoongCollector: Starting initialization" # 启动LoongCollector服务 /etc/init.d/loongcollectord start # 等待配置下载和服务就绪 sleep 15 # 验证服务状态 if /etc/init.d/loongcollectord status; then echo "[$(date)] LoongCollector: Service started successfully" touch /tasksite/cornerstone else echo "[$(date)] LoongCollector: Failed to start service" exit 1 fi # 等待业务容器完成 echo "[$(date)] LoongCollector: Waiting for business container to complete" until [[ -f /tasksite/tombstone ]]; do sleep 2 done echo "[$(date)] LoongCollector: Business completed, waiting for log transmission" # 给足够时间传输剩余日志 sleep 30 echo "[$(date)] LoongCollector: Stopping service" /etc/init.d/loongcollectord stop echo "[$(date)] LoongCollector: Shutdown complete" # 健康检查 livenessProbe: exec: command: ["/etc/init.d/loongcollectord", "status"] initialDelaySeconds: 30 periodSeconds: 10 timeoutSeconds: 5 failureThreshold: 3 # 资源配置 resources: requests: cpu: "100m" memory: "128Mi" limits: cpu: "2000m" memory: "2048Mi" # 环境变量配置 env: - name: ALIYUN_LOGTAIL_USER_ID value: "${your_aliyun_user_id}" - name: ALIYUN_LOGTAIL_USER_DEFINED_ID value: "${your_machine_group_user_defined_id}" - name: ALIYUN_LOGTAIL_CONFIG value: "/etc/ilogtail/conf/${your_region_config}/ilogtail_config.json" # 启用全量排空模式，确保Pod停止时发送所有日志 - name: enable_full_drain_mode value: "true" # 追加 Pod 环境信息作为日志标签 - name: "ALIYUN_LOG_ENV_TAGS" value: "_pod_name_|_pod_ip_|_namespace_|_node_name_|_node_ip_" # 获取 Pod 和 Node 的信息 - name: "_pod_name_" valueFrom: fieldRef: fieldPath: metadata.name - name: "_pod_ip_" valueFrom: fieldRef: fieldPath: status.podIP - name: "_namespace_" valueFrom: fieldRef: fieldPath: metadata.namespace - name: "_node_name_" valueFrom: fieldRef: fieldPath: spec.nodeName - name: "_node_ip_" valueFrom: fieldRef: fieldPath: status.hostIP # 卷挂载 volumeMounts: - name: nginx-logs mountPath: /var/log/nginx readOnly: true - name: tasksite mountPath: /tasksite - name: tz-config mountPath: /etc/localtime readOnly: true # 卷定义 volumes: - name: nginx-logs emptyDir: {} - name: tasksite emptyDir: medium: Memory sizeLimit: "50Mi" - name: tz-config hostPath: path: /usr/share/zoneinfo/Asia/Shanghai

## 相关参考

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


### Loongcollector网络传输类型

服务入口（Endpoint）表示日志服务对外服务的访问域名，是访问一个项目（Project）及其内部日志数据的URL，与Project所在的地域相关。日志服务提供私网域名、公网域名与传输加速域名。可通过如下操作查看域名：

- 

登录[日志服务控制台](https://sls.console.aliyun.com)，在Project列表中，单击目标Project。

- 

单击Project名称右侧的进入项目概览页面。

- 

在访问域名中可查看当前Project的域名信息，不同的网络传输方式对应不同的域名。合适的网络传输方式有利于日志数据的传输更快速稳定。

- 

- 

| 网络类型 | 对应域名类型 | 描述 | 适用场景 |
| --- | --- | --- | --- |
| 阿里云内网 | 私网域名 | 阿里云内网为千兆共享网络，日志数据通过阿里云内网传输比公网传输更快速、稳定，内网包括 VPC 和经典网络。 | ECS 实例和日志服务 Project 属于同一地域或 [自建服务器打通内网](products/ecs/documents/user-guide/manage-servers-that-are-not-provided-by-alibaba-cloud.md) 的情况。 说明 推荐在 ECS 所在地域创建日志服务 Project，通过阿里云内网采集 ECS 中日志，不消耗公网带宽。 |
| 公网 | 公网域名 | 使用公网传输日志数据，不仅会受到网络带宽的限制，还可能会因网络抖动、延迟、丢包等影响数据采集的速度和稳定性。 | 以下两种情况，可以选择公网传输数据。 ECS 实例和日志服务 Project 属于不同地域。 服务器为其他云厂商服务器或自建 IDC。 |
| 传输加速 | 传输加速域名 | 利用阿里云 CDN 边缘节点进行日志采集加速，相对公网采集在网络延迟、稳定性上具有很大优势，但流量需额外计费。 | 如果业务服务器、日志服务 Project 分别属于国内地域和国外地域，使用公网传输数据可能会出现网络延迟高、传输不稳定等问题，您可以选择传输加速传输数据。更多信息，请参见 [传输加速](products/sls/documents/select-a-network-type.md) 。 |


### Loongcollector运行模式

| 特性 | DaemonSet 模式 | Sidecar 模式 |
| --- | --- | --- |
| 部署方式 | 每个节点部署 1 个采集容器 | 每个 Pod 部署 1 个采集容器 |
| 资源消耗 | 低（共享节点资源） | 较高（每个 Pod 单独占用） |
| 适用场景 | 节点级统一日志采集 | 特定应用独立隔离采集 |
| 隔离性 | 节点级共享 | Pod 级独立 |


DaemonSet模式原理

在集群的每个Node节点上部署一个 LoongCollector，负责采集该节点上所有容器的日志；特点：运维简单、资源占用少、配置方式灵活；但是隔离性较弱。

- 

在DaemonSet模式中，Kubernetes集群确保每个节点（Node）只运行一个LoongCollector容器，用于采集当前节点内所有容器（Containers）的日志。

- 

当新节点加入集群时，Kubernetes集群会自动在新节点上创建LoongCollector容器；当节点退出集群时，Kubernetes集群会自动销毁当前节点上的LoongCollector容器。通过DaemonSet的自动扩缩容机制以及标识型机器组，无需手动管理LoongCollector实例。

Sidecar模式原理

每个 Pod 中伴随业务容器注入一个 LoongCollector Sidecar容器，并将业务容器的日志目录通过K8s的Volume机制（如emptyDir、hostPath、PVC等）挂载为共享卷。这样，日志文件会同时出现在业务容器和Sidecar容器的挂载路径下，LoongCollector就能直接读取这些日志文件；特点：多租户隔离性好、性能好；但资源占用较多，配置与维护较复杂。

- 

在Sidecar模式中，每个容器组（Pod）运行一个LoongCollector容器，用于采集当前容器组（Pod）所有容器（Containers）的日志。不同Pod的日志采集相互隔离。

- 

为了采集同一Pod中其他容器的日志文件，需要通过共享存储卷的方式来完成，需要将同一份存储卷分别挂载到业务容器和LoongCollector容器。

- 

当一个节点上的 Pod 数据量异常庞大，远超出 Daemonset 的采集性能上限时，Sidecar模式允许我们为LoongCollector分配特定的资源，从而提升其日志采集的性能和稳定性。

- 

在 Serverless 容器中缺乏节点的概念，传统的 Daemonset 部署模式无法应用。此时，SideCar 模式能够有效地与无服务器架构结合，保证日志采集过程的灵活性和适应性。

[上一篇：Kubernetes 安装与管理](products/sls/documents/loongcollector-installation-and-management-kubernetes.md)[下一篇：运行管理](products/sls/documents/loongcollector-management-kubernetes.md)

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
