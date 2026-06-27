### 示例二：单地域GPU资源不足时，可跨地域购买GPU实例扩容
准备环境
[创建](../user-guide/create-an-ack-edge-cluster-1.md)[ACK Edge](../user-guide/create-an-ack-edge-cluster-1.md)[集群](../user-guide/create-an-ack-edge-cluster-1.md)
操作步骤
本示例以部署推理任务为例，介绍当集群地域GPU资源不足时，如何通过ACK Edge集群接入跨地域的GPU实例，最终实现任务的调度部署。
部署推理任务并查看任务状态。
创建tensorflow-mnist.yaml文件。
展开查看tensorflow-mnist.yaml文件
apiVersion: apps/v1 kind: Deployment metadata: name: tensorflow-mnist labels: app: tensorflow-mnist spec: replicas: 1 selector: matchLabels: app: tensorflow-mnist template: metadata: name: tensorflow-mnist labels: app: tensorflow-mnist spec: containers: - name: tensorflow-mnist image: registry.cn-beijing.aliyuncs.com/acs/tensorflow-mnist-sample:v1.5 command: - python - tensorflow-sample-code/tfjob/docker/mnist/main.py - --max_steps=100000 - --data_dir=tensorflow-sample-code/data resources: limits: nvidia.com/gpu: "1" requests: nvidia.com/gpu: "1" workingDir: /root
部署推理任务。
kubectl apply -f tensorflow-mnist.yaml
查看推理任务状态。
kubectl get pods
预期输出：
NAME READY STATUS RESTARTS AGE tensorflow-mnist-664cf976d8-whrbc 0/1 pending 0 30s
当前推理任务状态为pending，经确认属于GPU资源不足问题。
创建边缘节点池。具体操作，请参见[创建边缘节点池](../user-guide/edge-node-pool-management.md)。
将GPU实例作为边缘节点，添加到已创建的
