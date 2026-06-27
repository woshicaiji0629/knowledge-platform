## 工作原理
Sidecar 模式的核心是在您的业务 Pod 内，并排运行一个业务容器和一个 LoongCollector（Logtail） 日志采集容器。它们通过共享卷和生命周期同步机制协同工作。
日志共享：业务容器将其产生的日志文件写入到一个共享卷（通常是emptyDir）。 LoongCollector（Logtail） 容器挂载同个共享卷，从而能实时读取并采集这些日志文件。
配置关联：每个 LoongCollector（Logtail）Sidecar 容器通过设置一个唯一的用户自定义标识来声明自己的身份。在日志服务控制台，您需要创建一个同样使用此标识的机器组。这样，所有使用相同标识的 Sidecar 实例都会自动应用到这个机器组上的采集配置。
生命周期同步：为确保在 Pod 终止时不丢失日志，业务容器和 LoongCollector（Logtail）容器通过共享卷中的信令文件（cornerstone和tombstone）进行通信，配合 Pod 的优雅终止宽限期（terminationGracePeriodSeconds），实现业务容器先停止写入、 LoongCollector（Logtail） 完成日志发送后再一同退出的优雅停机流程。
