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
