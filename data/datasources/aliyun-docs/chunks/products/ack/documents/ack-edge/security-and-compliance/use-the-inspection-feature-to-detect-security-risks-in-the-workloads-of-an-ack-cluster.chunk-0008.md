ounts 字段实现。 示例： |
| cpuRequestsMissing | 配置运行容器所需的最少 CPU 资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.requests.cpu 字段，可以检查是否未配置运行容器所需的最少 CPU 资源。如果未配置，则 Pod 有被调度到资源紧张的节点上的风险，可能会出现容器内进程运行缓慢的情况。 | 修改 Pod spec，增加 resources.requests.cpu 字段。 示例： |
| cpuLimitsMissing | 限制运行容器可使用的最大 CPU 资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.limits.cpu 字段，检查是否未配置运行容器所需的最大 CPU 资源。如果未配置，则存在被容器内的异常进程消耗大量节点资源，甚至把整个节点或集群的资源消耗殆尽的风险。 | 修改 Pod spec，增加 resources.limits.cpu 字段。 示例： |
| memoryRequestsMissing | 配置运行容器所需的最少内存资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.requests.memory 字段，检查是否未配置运行容器所需的最少内存资源。如果未配置，Pod 有被调度到资源紧张的节点上的风险，可能会出现容器内进程 OOM 的风险。 | 修改 Pod spec，增加 resources.requests.memory 字段。 示例： |
| memoryLimitsMissing | 限制容器可使用的最大内存资源 | 通过检查 Workload 的 Pod spec 中是否未配置 resources.limits.memory 字段，检查是否未配置运行容器所需的最大内存资源。如果未配置，则存在被容器内的异常进程消耗大量节点资源，甚至把整个节点或集群的资源消耗殆尽的风险。 | 修改 Pod spec，增加 resources.limits.memory 字段。 示例： |
| readinessProbeMissing | 配置容器就绪探针 | 通过检查 Workload 的 Pod spec 中是否未配置 readinessProbe 字段，检查是否未配置检测容器内应用能否正常处理请求的探针。如果未配置，则存在容器内应用异常无法处理请求时仍旧有请求发送，继而导致业务异常的风险。 | 修改 Pod spec，增加 readinessProbe 字段。 示例： |
| livenessProbeMissing | 配置容器存活探针 | 通过检查 Workload 的 Pod spec 中是否未配置 livenessProbe ，检查是否未配置
