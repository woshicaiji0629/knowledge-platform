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
