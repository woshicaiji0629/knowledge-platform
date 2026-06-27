# 如何获取Docker容器的Label和环境变量
当您使用Logtail采集容器日志时，可以通过Label和环境变量对待采集的容器进行过滤。Label指运行docker inspect命令时显示的容器元数据中的标签信息，环境变量是在容器启动时设置的运行时环境参数。本文介绍如何获取容器的Label和环境变量。
重要
本文仅适合获取Docker容器的Label和环境变量，采集K8s日志容器过滤推荐使用[K8s Pod](collect-container-text-logs-through-the-daemonset-console.md)[标签白名单](collect-container-text-logs-through-the-daemonset-console.md)和[K8s Pod](collect-container-text-logs-through-the-daemonset-console.md)[标签黑名单](collect-container-text-logs-through-the-daemonset-console.md)。
