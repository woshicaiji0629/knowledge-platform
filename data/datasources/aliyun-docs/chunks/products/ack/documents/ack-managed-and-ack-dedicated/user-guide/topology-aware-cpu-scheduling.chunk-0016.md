### 停用CPU拓扑感知调度（CPU核心解绑）
编辑应用YAML，从spec.template.metadata.annotations中移除Annotationcpuset-scheduler: "true"和cpu-policy: "static-burst"（如有）。
在业务低峰期应用修改后的YAML，等待Pod重启后变更生效。
重要
解绑后，Pod 进程不再被绑定到特定物理核心，可能会在节点所有可用 CPU 核心之间切换。潜在影响包括：
因跨核心的上下文切换，CPU 使用率可能微幅上升。
对于计算密集型应用，由于无法独占核心，可能会重新出现因 CPU 资源争抢导致的性能抖动。
当多个高负载 Pod 的进程被调度至同一核心时，可能导致该核心负载瞬时过高，进而触发容器的 CPU 限流（Throttling）。
