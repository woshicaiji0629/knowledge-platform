## 通过NATS创建
创建event-bus.yaml文件。Event Bus示例代码如下所示：
apiVersion: argoproj.io/v1alpha1 kind: EventBus metadata: name: default spec: nats: native: replicas: 3 auth: token
执行以下命令，创建EventBus。
kubectl apply -f event-bus.yaml
说明
命令执行成功后，会在default命名空间下创建Event Bus Pod。后续操作需在同一命名空间下。
执行以下命令，查看Event Bus Pod是否正常启动。
kubectl get pod
