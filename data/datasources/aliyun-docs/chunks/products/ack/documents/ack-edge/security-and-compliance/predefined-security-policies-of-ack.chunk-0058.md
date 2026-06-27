### ACKPSPHostNetworkingPorts
规则说明：限制在集群指定范围内部署的Pod使用主机网络和指定端口。
重要等级：high。
参数说明：

| 参数名称 | 参数类型 | 参数说明 |
| --- | --- | --- |
| hostNetwork | boolean | 是否允许 Pod 共享使用主机网络。 |
| min | int | 最小使用的 hostPort 值。 |
| max | int | 最大使用的 hostPort 值。 |

示例：
Constraint：
apiVersion: constraints.gatekeeper.sh/v1beta1 kind: ACKPSPHostNetworkingPorts metadata: name: psp-host-network-ports spec: match: kinds: - apiGroups: [""] kinds: ["Pod"] namespaces: - "test-gatekeeper" parameters: hostNetwork: true min: 80 max: 9000
Allowed：
apiVersion: v1 kind: Pod metadata: name: good-2 namespace: test-gatekeeper spec: hostNetwork: true containers: - image: k8s.gcr.io/test-webserver name: test-container ports: - hostPort: 80 containerPort: 80 initContainers: - image: k8s.gcr.io/test-webserver name: test-container2 ports: - hostPort: 8080 containerPort: 8080
Disallowed：
apiVersion: v1 kind: Pod metadata: name: bad-1 namespace: non-test-gatekeeper spec: hostNetwork: true containers: - image: k8s.gcr.io/test-webserver name: test-container ports: - hostPort: 22 containerPort: 22
