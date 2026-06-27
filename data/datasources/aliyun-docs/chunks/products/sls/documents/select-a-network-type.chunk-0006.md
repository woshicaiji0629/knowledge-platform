### 推荐参数值示例
根据实际经验推荐如下参数配置，适用于普通JSON文件的采集场景。完整正则模式和分隔符模式的性能与JSON模式相近，极简模式性能为JSON模式的5倍。由于数据、规则的复杂度、采集目录和文件的数量都会对CPU和MEM消耗带来影响，请参照下述表格并结合实际情况按需调整。
主机环境

| 参数 | 默认的采集速率 | 采集速率大于 10 MB/s | 采集速率大于 20 MB/s | 采集速率大于 40 MB/s |
| --- | --- | --- | --- | --- |
| cpu_usage_limit | 0.4 | 1 | 2 | 4 |
| mem_usage_limit | 384 | 1024 | 2048 | 4096 |
| max_bytes_per_sec | 20971520 | 209715200 | 209715200 | 209715200 |
| process_thread_count | 1 | 2 | 4 | 8 |
| send_request_concurrency | 15 | 20 | 40 | 80 |

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
