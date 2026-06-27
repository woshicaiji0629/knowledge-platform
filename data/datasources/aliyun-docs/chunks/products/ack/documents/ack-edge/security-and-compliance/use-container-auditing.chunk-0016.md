测试告警规则。
通过kubectl exec -it <pod_name> -- bash命令进入容器，触发Kubernetes进入容器告警的告警规则。告警信息如下图所示。
进入容器后，通过touch a.txt && rm a.txt命令，触发Kubernetes进入容器后执行风险程序告警的告警规则。告警信息如下图所示。
