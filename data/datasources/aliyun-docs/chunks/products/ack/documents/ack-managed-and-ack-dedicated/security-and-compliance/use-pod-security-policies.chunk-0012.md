e/customize-the-kubelet-configurations-of-a-node-pool.md)[参数](../user-guide/customize-the-kubelet-configurations-of-a-node-pool.md)。
部署一个使用不安全的sysctl的测试Pod。
可按需调整sysctls参数内容。如果集群中仅有部分节点（例如特定节点池中的节点）的kubelet配置了允许不安全的sysctl，还需为 Pod 添加nodeSelector，以确保Pod可被精确调度到目标节点上。cat <<EOF | kubectl apply -f - apiVersion: v1 kind: Pod metadata: name: sysctl-example spec: # nodeSelector: # alibabacloud.com/nodepool-id: npd912756*** # 替换为目标节点池ID securityContext: sysctls: - name: net.ipv4.tcp_syncookies value: "1" - name: net.core.somaxconn value: "1024" - name: net.ipv4.tcp_max_syn_backlog value: "65536" containers: - name: test image: nginx EOF
预期输出：
如果Pod运行时提示SysctlForbidden事件，表明运行该Pod的节点上的kubelet未配置允许使用不安全的sysctl。请检查并调整 Pod 的nodeSelector，确保被调度到已正确配置kubelet参数的节点。
pod/sysctl-example created
