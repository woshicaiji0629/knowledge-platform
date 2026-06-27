## 步骤一：安装LoongCollector
LoongCollector 是阿里云日志服务推出的新一代日志采集 Agent，是 Logtail 的升级版，二者不能同时存在，如需安装Logtail，请参考[安装、运行、升级、卸载](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)。
本文仅介绍LoongCollector的基础安装流程，如需了解详细参数请参考[安装配置](loongcollector-installation-kubernetes-1.md)。若已安装LoongCollector或Logtail，可跳过本步骤，直接[步骤二：创建](collect-kubernetes-cluster-text-logs-daemonset.md)[LogStore](collect-kubernetes-cluster-text-logs-daemonset.md)。
说明
在LoongCollector（Logtail）运行过程中，若宿主机时间发生变化，可能导致日志重复采集或丢失。
