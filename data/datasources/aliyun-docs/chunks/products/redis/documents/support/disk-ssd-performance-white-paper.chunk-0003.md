| 参数 | 说明 |
| --- | --- |
| ip | Tair 实例的 IP 地址。 |
| port | Tair 实例的服务端口。 |
| timeout | 测试命令的超时时间，单位为 ms。 |
| command_group | 测试类型，配置为 String。 |
| recordcount | 数据加载阶段准备的数据量。 |
| run_operationcount | Run 阶段操作的数据量。本测试中： 内存大于数据场景下，配置和 recordcount 参数相同的值。 数据大于内存场景下，配置的值为 recordcount 参数值除以 32。 |
| fieldcount | 字段个数，配置为 1。 |
| fieldlength | 值长度，配置为 100。 |
| threads | YCSB 线程数，根据实例规格配置。 |
