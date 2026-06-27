-664cf976d8-whrbc 0/1 pending 0 30s
当前推理任务状态为pending，经确认属于GPU资源不足问题。
创建边缘节点池。具体操作，请参见[创建边缘节点池](../user-guide/edge-node-pool-management.md)。
将GPU实例作为边缘节点，添加到已创建的边缘节点池中。具体操作，请参见[添加](../user-guide/add-a-gpu-node.md)[GPU](../user-guide/add-a-gpu-node.md)[节点](../user-guide/add-a-gpu-node.md)。在创建边缘节点池的配置文件中，将gpuVersion字段设置为实际使用的GPU型号（如Nvidia Tesla A10）。配置文件示例：
{ "enableIptables": true, "quiet": true, "manageRuntime": true, "gpuVersion": "Nvidia Tesla A10", "allowedClusterAddons": [ "kube-proxy", "flannel", "coredns" ] }
查看边缘节点状态。
kubectl get nodes
预期输出：
NAME STATUS ROLES AGE VERSION cn-hangzhou.192.168.XX.XX Ready <none> 9d v1.30.7-aliyun.1 iz2ze21g5pq9jbesubr**** Ready <none> 8d v1.30.7-aliyun.1 izf8z0dko1ivt5kwgl4**** Ready <none> 8d v1.30.7-aliyun.1 izuf65ze9db2kfcethw**** Ready <none> 8d v1.30.7-aliyun.1 # 新添加的GPU边缘节点。
查看推理任务的状态。
kubectl get pods -owide
预期输出：
NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES tensorflow-mnist-664cf976d8-whrbc 1/1 running 0 23m 10.12.XX.XX izuf65ze9db2kfcethw**** <none> <none>
预期输出表明，推理任务已调度到新添加的GPU节点上，并部署成功。
该文章对您有帮助吗？
反馈
