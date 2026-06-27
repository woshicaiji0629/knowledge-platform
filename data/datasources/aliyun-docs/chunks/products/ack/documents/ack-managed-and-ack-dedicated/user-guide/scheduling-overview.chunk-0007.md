### 任务调度
适用角色：集群运维人员
说明：调度器能够根据预设的规则决定将Pod放置在哪个节点上运行，但并不适用于批处理任务下Pod的协同调度。在此基础上，ACK为批量计算任务支持了Gang Scheduling、Capacity Scheduling能力。

| 策略 | 策略说明 | 典型场景 | 参考文档 |
| --- | --- | --- | --- |
| Gang Scheduling | 相关 Pod 要么全部被调度，要么都不被调度，防止因部分进程的异常而导致整个关联进程组阻塞的问题。 | 批处理作业：作业中有多个相互依赖的任务组，需要同时处理。 分布式计算：例如机器学习训练任务或其他需要严格协调运行的分布式应用。 高性能计算：作业可能需要整套的资源同时可用才能开始执行。 | [使用](work-with-gang-scheduling.md) [Gang scheduling](work-with-gang-scheduling.md) |
| Capacity Scheduling | 为特定的命名空间或用户组预留一定的资源容量，并在集群资源紧张时，通过资源共享提升整体资源利用率。 | 多租户场景下，不同租户使用资源的周期和方式不同，造成集群的整体资源利用率较低，期望在固定资源分配的基础上允许资源的借用和回收。 | [使用](use-capacity-scheduling.md) [Capacity Scheduling](use-capacity-scheduling.md) |
