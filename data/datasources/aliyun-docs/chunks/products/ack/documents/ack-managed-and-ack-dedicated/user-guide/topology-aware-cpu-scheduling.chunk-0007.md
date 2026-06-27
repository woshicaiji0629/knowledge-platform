## 步骤二：启用CPU拓扑感知调度功能
可通过为Pod添加Annotation来启用CPU拓扑感知调度。
[普通绑核策略](topology-aware-cpu-scheduling.md)：通用策略，遵循1:1的绑核原则，为Pod绑定resources.limits.cpu所指定的数量的核心。优先选择同一NUMA节点内的CPU核，以保证良好的内存访问性能。
[自动绑核策略](topology-aware-cpu-scheduling.md)：针对特定硬件优化的策略，优先通过绑定一个完整的物理核心簇（如AMD CPU的CCX/CCD）来最大化CPU局部性并提升并发度。推荐在特定的大规格（如32核及以上）AMD机型上使用。
重要
启用CPU拓扑感知调度时，请勿在Pod上直接指定nodeName，kube-scheduler不参与此类Pod的调度过程。可使用nodeSelector等字段配置亲和性策略来指定节点调度。
