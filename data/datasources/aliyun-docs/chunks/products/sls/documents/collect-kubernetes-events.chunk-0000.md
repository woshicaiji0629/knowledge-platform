# 采集Kubernetes事件
本文档主要介绍如何使用eventer将Kubernetes中的事件采集到日志服务。
Kubernetes的架构设计基于状态机，不同的状态之间进行转换会生成相应的事件，正常的状态之间转换会生成Normal等级的事件，正常状态与异常状态之间的转换会生成Warning等级的事件。
ACK提供开箱即用的容器场景事件监控方案，通过ACK维护的NPD以及包含在NPD中的kube-eventer提供容器事件监控能力。
NPD（node-problem-detector）是Kubernetes节点诊断的工具，可以将节点的异常（例如Docker Engine Hang、Linux Kernel Hang、网络出网异常、文件描述符异常等）转换为节点的事件，结合kube-eventer可以实现节点事件告警的闭环。更多信息，请参见[NPD](https://github.com/AliyunContainerService/node-problem-detector)。
kube-eventer是ACK维护的开源Kubernetes事件离线工具，可以将集群的事件推送至钉钉、SLS、EventBridge等系统，并提供不同等级的过滤条件，实现事件的实时采集、定向告警、异步归档。更多信息，请参见[kube-eventer](https://github.com/AliyunContainerService/kube-eventer)。
NPD（node-problem-detector）是Kubernetes节点诊断的工具，可以将节点的异常（例如Docker Engine Hang、Linux Kernel Hang、网络出网异常、文件描述符异常等）转换为节点的事件，结合kube-eventer可以实现节点事件告警的闭环。更多信息，请参见[NPD](https://github.com/AliyunContainerService/node-problem-detector)。
kube-eventer是ACK维护的开源Kubernetes事件离线工具，可以将集群的事件推送至钉钉、SLS、EventBridge等系统，并提供不同等级的过滤条件，实现事件的实时采集、定向告警、异步归档。更多信息，请参见[kube-eventer](https://github.com/AliyunContainerService/kube-eventer)。
